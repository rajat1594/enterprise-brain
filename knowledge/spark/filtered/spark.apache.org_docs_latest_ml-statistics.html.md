[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-statistics.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-statistics.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-statistics.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-statistics.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-statistics.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-statistics.html#mllib-rdd-based-api-guide)
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


# Basic Statistics[](https://spark.apache.org/docs/latest/ml-statistics.html#basic-statistics)
`\[ \newcommand{\R}{\mathbb{R}} \newcommand{\E}{\mathbb{E}} \newcommand{\x}{\mathbf{x}} \newcommand{\y}{\mathbf{y}} \newcommand{\wv}{\mathbf{w}} \newcommand{\av}{\mathbf{\alpha}} \newcommand{\bv}{\mathbf{b}} \newcommand{\N}{\mathbb{N}} \newcommand{\id}{\mathbf{I}} \newcommand{\ind}{\mathbf{1}} \newcommand{\0}{\mathbf{0}} \newcommand{\unit}{\mathbf{e}} \newcommand{\one}{\mathbf{1}} \newcommand{\zero}{\mathbf{0}} \]`
**Table of Contents**
  * [Correlation](https://spark.apache.org/docs/latest/ml-statistics.html#correlation)
  * [Hypothesis testing](https://spark.apache.org/docs/latest/ml-statistics.html#hypothesis-testing)
    * [ChiSquareTest](https://spark.apache.org/docs/latest/ml-statistics.html#chisquaretest)
  * [Summarizer](https://spark.apache.org/docs/latest/ml-statistics.html#summarizer)


## Correlation[](https://spark.apache.org/docs/latest/ml-statistics.html#correlation)
Calculating the correlation between two series of data is a common operation in Statistics. In `spark.ml` we provide the flexibility to calculate pairwise correlations among many series. The supported correlation methods are currently Pearson’s and Spearman’s correlation.
  * **Python**
  * **Scala**
  * **Java**


[`Correlation`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.stat.Correlation.html) computes the correlation matrix for the input Dataset of Vectors using the specified method. The output will be a DataFrame that contains the correlation matrix of the column of vectors.

```
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation

data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
        (Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
        (Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
        (Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]
df = spark.createDataFrame(data, ["features"])

r1 = Correlation.corr(df, "features").head()


print("Pearson correlation matrix:\n" + str(r1[0]))

r2 = Correlation.corr(df, "features", "spearman").head()


print("Spearman correlation matrix:\n" + str(r2[0]))
```

Find full example code at "examples/src/main/python/ml/correlation_example.py" in the Spark repo.
[`Correlation`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/Correlation$.html) computes the correlation matrix for the input Dataset of Vectors using the specified method. The output will be a DataFrame that contains the correlation matrix of the column of vectors.

```
import org.apache.spark.ml.linalg.{Matrix, Vectors}
import org.apache.spark.ml.stat.Correlation
import org.apache.spark.sql.Row

val data = Seq(
  Vectors.sparse(4, Seq((0, 1.0), (3, -2.0))),
  Vectors.dense(4.0, 5.0, 0.0, 3.0),
  Vectors.dense(6.0, 7.0, 0.0, 8.0),
  Vectors.sparse(4, Seq((0, 9.0), (3, 1.0)))
)

val df = data.map(Tuple1.apply).toDF("features")
val Row(coeff1: Matrix) = Correlation.corr(df, "features").head()
println(s"Pearson correlation matrix:\n $coeff1")

val Row(coeff2: Matrix) = Correlation.corr(df, "features", "spearman").head()
println(s"Spearman correlation matrix:\n $coeff2")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/CorrelationExample.scala" in the Spark repo.
[`Correlation`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/stat/Correlation.html) computes the correlation matrix for the input Dataset of Vectors using the specified method. The output will be a DataFrame that contains the correlation matrix of the column of vectors.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.linalg.Vectors;
import org.apache.spark.ml.linalg.VectorUDT;
import org.apache.spark.ml.stat.Correlation;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.types.*;

List<Row> data = Arrays.asList(
  RowFactory.create(Vectors.sparse(4, new int[]{0, 3}, new double[]{1.0, -2.0})),
  RowFactory.create(Vectors.dense(4.0, 5.0, 0.0, 3.0)),
  RowFactory.create(Vectors.dense(6.0, 7.0, 0.0, 8.0)),
  RowFactory.create(Vectors.sparse(4, new int[]{0, 3}, new double[]{9.0, 1.0}))
);

StructType schema = new StructType(new StructField[]{
  new StructField("features", new VectorUDT(), false, Metadata.empty()),
});

Dataset<Row> df = spark.createDataFrame(data, schema);
Row r1 = Correlation.corr(df, "features").head();
System.out.println("Pearson correlation matrix:\n" + r1.get(0).toString());

Row r2 = Correlation.corr(df, "features", "spearman").head();
System.out.println("Spearman correlation matrix:\n" + r2.get(0).toString());
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaCorrelationExample.java" in the Spark repo.
## Hypothesis testing[](https://spark.apache.org/docs/latest/ml-statistics.html#hypothesis-testing)
Hypothesis testing is a powerful tool in statistics to determine whether a result is statistically significant, whether this result occurred by chance or not. `spark.ml` currently supports Pearson’s Chi-squared ( $\chi^2$) tests for independence.
### ChiSquareTest[](https://spark.apache.org/docs/latest/ml-statistics.html#chisquaretest)
`ChiSquareTest` conducts Pearson’s independence test for every feature against the label. For each feature, the (feature, label) pairs are converted into a contingency matrix for which the Chi-squared statistic is computed. All label and feature values must be categorical.
  * **Python**
  * **Scala**
  * **Java**


Refer to the [`ChiSquareTest` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.stat.ChiSquareTest.html) for details on the API.

```
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import ChiSquareTest

data = [(0.0, Vectors.dense(0.5, 10.0)),
        (0.0, Vectors.dense(1.5, 20.0)),
        (1.0, Vectors.dense(1.5, 30.0)),
        (0.0, Vectors.dense(3.5, 30.0)),
        (0.0, Vectors.dense(3.5, 40.0)),
        (1.0, Vectors.dense(3.5, 40.0))]
df = spark.createDataFrame(data, ["label", "features"])

r = ChiSquareTest.test(df, "features", "label").head()



print("pValues: " + str(r.pValues))
print("degreesOfFreedom: " + str(r.degreesOfFreedom))
print("statistics: " + str(r.statistics))
```

Find full example code at "examples/src/main/python/ml/chi_square_test_example.py" in the Spark repo.
Refer to the [`ChiSquareTest` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/ChiSquareTest$.html) for details on the API.

```
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.stat.ChiSquareTest

val data = Seq(
  (0.0, Vectors.dense(0.5, 10.0)),
  (0.0, Vectors.dense(1.5, 20.0)),
  (1.0, Vectors.dense(1.5, 30.0)),
  (0.0, Vectors.dense(3.5, 30.0)),
  (0.0, Vectors.dense(3.5, 40.0)),
  (1.0, Vectors.dense(3.5, 40.0))
)

val df = data.toDF("label", "features")
val chi = ChiSquareTest.test(df, "features", "label").head()
println(s"pValues = ${chi.getAs[Vector](0)}")
println(s"degreesOfFreedom ${chi.getSeq[Int](1).mkString("[", ",", "]")}")
println(s"statistics ${chi.getAs[Vector](2)}")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/ChiSquareTestExample.scala" in the Spark repo.
Refer to the [`ChiSquareTest` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/stat/ChiSquareTest.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.linalg.Vectors;
import org.apache.spark.ml.linalg.VectorUDT;
import org.apache.spark.ml.stat.ChiSquareTest;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.types.*;

List<Row> data = Arrays.asList(
  RowFactory.create(0.0, Vectors.dense(0.5, 10.0)),
  RowFactory.create(0.0, Vectors.dense(1.5, 20.0)),
  RowFactory.create(1.0, Vectors.dense(1.5, 30.0)),
  RowFactory.create(0.0, Vectors.dense(3.5, 30.0)),
  RowFactory.create(0.0, Vectors.dense(3.5, 40.0)),
  RowFactory.create(1.0, Vectors.dense(3.5, 40.0))
);

StructType schema = new StructType(new StructField[]{
  new StructField("label", DataTypes.DoubleType, false, Metadata.empty()),
  new StructField("features", new VectorUDT(), false, Metadata.empty()),
});

Dataset<Row> df = spark.createDataFrame(data, schema);
Row r = ChiSquareTest.test(df, "features", "label").head();
System.out.println("pValues: " + r.get(0).toString());
System.out.println("degreesOfFreedom: " + r.getList(1).toString());
System.out.println("statistics: " + r.get(2).toString());
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaChiSquareTestExample.java" in the Spark repo.
## Summarizer[](https://spark.apache.org/docs/latest/ml-statistics.html#summarizer)
We provide vector column summary statistics for `Dataframe` through `Summarizer`. Available metrics are the column-wise max, min, mean, sum, variance, std, and number of nonzeros, as well as the total count.
  * **Python**
  * **Scala**
  * **Java**


Refer to the [`Summarizer` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.stat.Summarizer.html) for details on the API.

```
from pyspark.ml.stat import Summarizer
from pyspark.sql import Row
from pyspark.ml.linalg import Vectors

df = sc.parallelize([Row(weight=1.0, features=Vectors.dense(1.0, 1.0, 1.0)),
                     Row(weight=0.0, features=Vectors.dense(1.0, 2.0, 3.0))]).toDF()

# create summarizer for multiple metrics "mean" and "count"
summarizer = Summarizer.metrics("mean", "count")

# compute statistics for multiple metrics with weight
df.select(summarizer.summary(df.features, df.weight)).show(truncate=False)

# compute statistics for multiple metrics without weight
df.select(summarizer.summary(df.features)).show(truncate=False)

# compute statistics for single metric "mean" with weight
df.select(Summarizer.mean(df.features, df.weight)).show(truncate=False)

# compute statistics for single metric "mean" without weight
df.select(Summarizer.mean(df.features)).show(truncate=False)
```

Find full example code at "examples/src/main/python/ml/summarizer_example.py" in the Spark repo.
The following example demonstrates using [`Summarizer`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/Summarizer$.html) to compute the mean and variance for a vector column of the input dataframe, with and without a weight column.

```
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.stat.Summarizer

val data = Seq(
  (Vectors.dense(2.0, 3.0, 5.0), 1.0),
  (Vectors.dense(4.0, 6.0, 7.0), 2.0)
)

val df = data.toDF("features", "weight")

val (meanVal, varianceVal) = df.select(metrics("mean", "variance")
  .summary($"features", $"weight").as("summary"))
  .select("summary.mean", "summary.variance")
  .as[(Vector, Vector)].first()

println(s"with weight: mean = ${meanVal}, variance = ${varianceVal}")

val (meanVal2, varianceVal2) = df.select(mean($"features"), variance($"features"))
  .as[(Vector, Vector)].first()

println(s"without weight: mean = ${meanVal2}, sum = ${varianceVal2}")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/SummarizerExample.scala" in the Spark repo.
The following example demonstrates using [`Summarizer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/stat/Summarizer.html) to compute the mean and variance for a vector column of the input dataframe, with and without a weight column.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.ml.linalg.Vectors;
import org.apache.spark.ml.linalg.VectorUDT;
import org.apache.spark.ml.stat.Summarizer;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.Metadata;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

List<Row> data = Arrays.asList(
  RowFactory.create(Vectors.dense(2.0, 3.0, 5.0), 1.0),
  RowFactory.create(Vectors.dense(4.0, 6.0, 7.0), 2.0)
);

StructType schema = new StructType(new StructField[]{
  new StructField("features", new VectorUDT(), false, Metadata.empty()),
  new StructField("weight", DataTypes.DoubleType, false, Metadata.empty())
});

Dataset<Row> df = spark.createDataFrame(data, schema);

Row result1 = df.select(Summarizer.metrics("mean", "variance")
  .summary(new Column("features"), new Column("weight")).as("summary"))
  .select("summary.mean", "summary.variance").first();
System.out.println("with weight: mean = " + result1.<Vector>getAs(0).toString() +
  ", variance = " + result1.<Vector>getAs(1).toString());

Row result2 = df.select(
  Summarizer.mean(new Column("features")),
  Summarizer.variance(new Column("features"))
).first();
System.out.println("without weight: mean = " + result2.<Vector>getAs(0).toString() +
  ", variance = " + result2.<Vector>getAs(1).toString());
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaSummarizerExample.java" in the Spark repo.
