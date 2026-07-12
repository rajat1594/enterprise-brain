[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#mllib-rdd-based-api-guide)
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


# Frequent Pattern Mining[](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#frequent-pattern-mining)
Mining frequent items, itemsets, subsequences, or other substructures is usually among the first steps to analyze a large-scale dataset, which has been an active research topic in data mining for years. We refer users to Wikipedia’s [association rule learning](http://en.wikipedia.org/wiki/Association_rule_learning) for more information.
**Table of Contents**
  * [FP-Growth](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#fp-growth)
  * [PrefixSpan](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#prefixspan)


## FP-Growth[](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#fp-growth)
The FP-growth algorithm is described in the paper [Han et al., Mining frequent patterns without candidate generation](https://doi.org/10.1145/335191.335372), where “FP” stands for frequent pattern. Given a dataset of transactions, the first step of FP-growth is to calculate item frequencies and identify frequent items. Different from [Apriori-like](http://en.wikipedia.org/wiki/Apriori_algorithm) algorithms designed for the same purpose, the second step of FP-growth uses a suffix tree (FP-tree) structure to encode transactions without generating candidate sets explicitly, which are usually expensive to generate. After the second step, the frequent itemsets can be extracted from the FP-tree. In `spark.mllib`, we implemented a parallel version of FP-growth called PFP, as described in [Li et al., PFP: Parallel FP-growth for query recommendation](https://doi.org/10.1145/1454008.1454027). PFP distributes the work of growing FP-trees based on the suffixes of transactions, and hence is more scalable than a single-machine implementation. We refer users to the papers for more details.
FP-growth operates on _itemsets_. An itemset is an unordered collection of unique items. Spark does not have a _set_ type, so itemsets are represented as arrays.
`spark.ml`’s FP-growth implementation takes the following (hyper-)parameters:
  * `minSupport`: the minimum support for an itemset to be identified as frequent. For example, if an item appears 3 out of 5 transactions, it has a support of 3/5=0.6.
  * `minConfidence`: minimum confidence for generating Association Rule. Confidence is an indication of how often an association rule has been found to be true. For example, if in the transactions itemset `X` appears 4 times, `X` and `Y` co-occur only 2 times, the confidence for the rule `X => Y` is then 2/4 = 0.5. The parameter will not affect the mining for frequent itemsets, but specify the minimum confidence for generating association rules from frequent itemsets.
  * `numPartitions`: the number of partitions used to distribute the work. By default the param is not set, and number of partitions of the input dataset is used.


The `FPGrowthModel` provides:
  * `freqItemsets`: frequent itemsets in the format of a DataFrame with the following columns: 
    * `items: array`: A given itemset.
    * `freq: long`: A count of how many times this itemset was seen, given the configured model parameters.
  * `associationRules`: association rules generated with confidence above `minConfidence`, in the format of a DataFrame with the following columns: 
    * `antecedent: array`: The itemset that is the hypothesis of the association rule.
    * `consequent: array`: An itemset that always contains a single element representing the conclusion of the association rule.
    * `confidence: double`: Refer to `minConfidence` above for a definition of `confidence`.
    * `lift: double`: A measure of how well the antecedent predicts the consequent, calculated as `support(antecedent U consequent) / (support(antecedent) x support(consequent))`
    * `support: double`: Refer to `minSupport` above for a definition of `support`.
  * `transform`: For each transaction in `itemsCol`, the `transform` method will compare its items against the antecedents of each association rule. If the record contains all the antecedents of a specific association rule, the rule will be considered as applicable and its consequents will be added to the prediction result. The transform method will summarize the consequents from all the applicable rules as prediction. The prediction column has the same data type as `itemsCol` and does not contain existing items in the `itemsCol`.


**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.fpm.FPGrowth.html) for more details.

```
from pyspark.ml.fpm import FPGrowth

df = spark.createDataFrame([
    (0, [1, 2, 5]),
    (1, [1, 2, 3, 5]),
    (2, [1, 2])
], ["id", "items"])

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.5, minConfidence=0.6)
model = fpGrowth.fit(df)

# Display frequent itemsets.
model.freqItemsets.show()

# Display generated association rules.
model.associationRules.show()

# transform examines the input items against all the association rules and summarize the
# consequents as prediction
model.transform(df).show()
```

Find full example code at "examples/src/main/python/ml/fpgrowth_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/FPGrowth.html) for more details.

```
import org.apache.spark.ml.fpm.FPGrowth

val dataset = spark.createDataset(Seq(
  "1 2 5",
  "1 2 3 5",
  "1 2")
).map(t => t.split(" ")).toDF("items")

val fpgrowth = new FPGrowth().setItemsCol("items").setMinSupport(0.5).setMinConfidence(0.6)
val model = fpgrowth.fit(dataset)

// Display frequent itemsets.
model.freqItemsets.show()

// Display generated association rules.
model.associationRules.show()

// transform examines the input items against all the association rules and summarize the
// consequents as prediction
model.transform(dataset).show()
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/FPGrowthExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/fpm/FPGrowth.html) for more details.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.fpm.FPGrowth;
import org.apache.spark.ml.fpm.FPGrowthModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.*;

List<Row> data = Arrays.asList(
  RowFactory.create(Arrays.asList("1 2 5".split(" "))),
  RowFactory.create(Arrays.asList("1 2 3 5".split(" "))),
  RowFactory.create(Arrays.asList("1 2".split(" ")))
);
StructType schema = new StructType(new StructField[]{ new StructField(
  "items", new ArrayType(DataTypes.StringType, true), false, Metadata.empty())
});
Dataset<Row> itemsDF = spark.createDataFrame(data, schema);

FPGrowthModel model = new FPGrowth()
  .setItemsCol("items")
  .setMinSupport(0.5)
  .setMinConfidence(0.6)
  .fit(itemsDF);

// Display frequent itemsets.
model.freqItemsets().show();

// Display generated association rules.
model.associationRules().show();

// transform examines the input items against all the association rules and summarize the
// consequents as prediction
model.transform(itemsDF).show();
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaFPGrowthExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html) for more details.

```
# Load training data

df <- selectExpr(createDataFrame(data.frame(rawItems = c(
  "1,2,5", "1,2,3,5", "1,2"
))), "split(rawItems, ',') AS items")

fpm <- spark.fpGrowth(df, itemsCol="items", minSupport=0.5, minConfidence=0.6)

# Extracting frequent itemsets

spark.freqItemsets(fpm)

# Extracting association rules

spark.associationRules(fpm)

# Predict uses association rules to and combines possible consequents

predict(fpm, df)
```

Find full example code at "examples/src/main/r/ml/fpm.R" in the Spark repo.
## PrefixSpan[](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#prefixspan)
PrefixSpan is a sequential pattern mining algorithm described in [Pei et al., Mining Sequential Patterns by Pattern-Growth: The PrefixSpan Approach](https://doi.org/10.1109%2FTKDE.2004.77). We refer the reader to the referenced paper for formalizing the sequential pattern mining problem.
`spark.ml`’s PrefixSpan implementation takes the following parameters:
  * `minSupport`: the minimum support required to be considered a frequent sequential pattern.
  * `maxPatternLength`: the maximum length of a frequent sequential pattern. Any frequent pattern exceeding this length will not be included in the results.
  * `maxLocalProjDBSize`: the maximum number of items allowed in a prefix-projected database before local iterative processing of the projected database begins. This parameter should be tuned with respect to the size of your executors.
  * `sequenceCol`: the name of the sequence column in dataset (default “sequence”), rows with nulls in this column are ignored.


**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.fpm.PrefixSpan) for more details.

```
from pyspark.ml.fpm import PrefixSpan

df = sc.parallelize([Row(sequence=[[1, 2], [3]]),
                     Row(sequence=[[1], [3, 2], [1, 2]]),
                     Row(sequence=[[1, 2], [5]]),
                     Row(sequence=[[6]])]).toDF()

prefixSpan = PrefixSpan(minSupport=0.5, maxPatternLength=5,
                        maxLocalProjDBSize=32000000)

# Find frequent sequential patterns.
prefixSpan.findFrequentSequentialPatterns(df).show()
```

Find full example code at "examples/src/main/python/ml/prefixspan_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/PrefixSpan.html) for more details.

```
import org.apache.spark.ml.fpm.PrefixSpan

val smallTestData = Seq(
  Seq(Seq(1, 2), Seq(3)),
  Seq(Seq(1), Seq(3, 2), Seq(1, 2)),
  Seq(Seq(1, 2), Seq(5)),
  Seq(Seq(6)))

val df = smallTestData.toDF("sequence")
val result = new PrefixSpan()
  .setMinSupport(0.5)
  .setMaxPatternLength(5)
  .setMaxLocalProjDBSize(32000000)
  .findFrequentSequentialPatterns(df)
  .show()
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/PrefixSpanExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/fpm/PrefixSpan.html) for more details.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.fpm.PrefixSpan;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.*;

List<Row> data = Arrays.asList(
  RowFactory.create(Arrays.asList(Arrays.asList(1, 2), Arrays.asList(3))),
  RowFactory.create(Arrays.asList(Arrays.asList(1), Arrays.asList(3, 2), Arrays.asList(1,2))),
  RowFactory.create(Arrays.asList(Arrays.asList(1, 2), Arrays.asList(5))),
  RowFactory.create(Arrays.asList(Arrays.asList(6)))
);
StructType schema = new StructType(new StructField[]{ new StructField(
  "sequence", new ArrayType(new ArrayType(DataTypes.IntegerType, true), true),
  false, Metadata.empty())
});
Dataset<Row> sequenceDF = spark.createDataFrame(data, schema);

PrefixSpan prefixSpan = new PrefixSpan().setMinSupport(0.5).setMaxPatternLength(5);

// Finding frequent sequential patterns
prefixSpan.findFrequentSequentialPatterns(sequenceDF).show();
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaPrefixSpanExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html) for more details.

```
# Load training data

df <- createDataFrame(list(list(list(list(1L, 2L), list(3L))),
                           list(list(list(1L), list(3L, 2L), list(1L, 2L))),
                           list(list(list(1L, 2L), list(5L))),
                           list(list(list(6L)))),
                      schema = c("sequence"))

# Finding frequent sequential patterns
frequency <- spark.findFrequentSequentialPatterns(df, minSupport = 0.5, maxPatternLength = 5L,
                                                  maxLocalProjDBSize = 32000000L)
showDF(frequency)
```

Find full example code at "examples/src/main/r/ml/prefixSpan.R" in the Spark repo.
