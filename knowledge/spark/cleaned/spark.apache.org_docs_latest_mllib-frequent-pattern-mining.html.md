[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#mllib-main-guide)
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

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
    * [ FP-growth ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#fp-growth)
    * [ association rules ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#association-rules)
    * [ PrefixSpan ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#prefixspan)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)

# Frequent Pattern Mining - RDD-based API[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#frequent-pattern-mining-rdd-based-api)
Mining frequent items, itemsets, subsequences, or other substructures is usually among the first steps to analyze a large-scale dataset, which has been an active research topic in data mining for years. We refer users to Wikipedia’s [association rule learning](http://en.wikipedia.org/wiki/Association_rule_learning) for more information. `spark.mllib` provides a parallel implementation of FP-growth, a popular algorithm to mining frequent itemsets.
## FP-growth[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#fp-growth)
The FP-growth algorithm is described in the paper [Han et al., Mining frequent patterns without candidate generation](https://doi.org/10.1145/335191.335372), where “FP” stands for frequent pattern. Given a dataset of transactions, the first step of FP-growth is to calculate item frequencies and identify frequent items. Different from [Apriori-like](http://en.wikipedia.org/wiki/Apriori_algorithm) algorithms designed for the same purpose, the second step of FP-growth uses a suffix tree (FP-tree) structure to encode transactions without generating candidate sets explicitly, which are usually expensive to generate. After the second step, the frequent itemsets can be extracted from the FP-tree. In `spark.mllib`, we implemented a parallel version of FP-growth called PFP, as described in [Li et al., PFP: Parallel FP-growth for query recommendation](https://doi.org/10.1145/1454008.1454027). PFP distributes the work of growing FP-trees based on the suffixes of transactions, and hence more scalable than a single-machine implementation. We refer users to the papers for more details.
`spark.mllib`’s FP-growth implementation takes the following (hyper-)parameters:
  * `minSupport`: the minimum support for an itemset to be identified as frequent. For example, if an item appears 3 out of 5 transactions, it has a support of 3/5=0.6.
  * `numPartitions`: the number of partitions used to distribute the work.

**Examples**
  * **Python**
  * **Scala**
  * **Java**

[`FPGrowth`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.fpm.FPGrowth.html) implements the FP-growth algorithm. It takes an `RDD` of transactions, where each transaction is a `List` of items of a generic type. Calling `FPGrowth.train` with transactions returns an [`FPGrowthModel`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.fpm.FPGrowthModel.html) that stores the frequent itemsets with their frequencies.
Refer to the [`FPGrowth` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.fpm.FPGrowth.html) for more details on the API.

```
from pyspark.mllib.fpm import FPGrowth

data = sc.textFile("data/mllib/sample_fpgrowth.txt")
transactions = data.map(lambda line: line.strip().split(' '))
model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
result = model.freqItemsets().collect()
for fi in result:
    print(fi)
```

Find full example code at "examples/src/main/python/mllib/fpgrowth_example.py" in the Spark repo.
[`FPGrowth`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/FPGrowth.html) implements the FP-growth algorithm. It takes an `RDD` of transactions, where each transaction is an `Array` of items of a generic type. Calling `FPGrowth.run` with transactions returns an [`FPGrowthModel`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/FPGrowthModel.html) that stores the frequent itemsets with their frequencies. The following example illustrates how to mine frequent itemsets and association rules (see [Association Rules](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#association-rules) for details) from `transactions`.
Refer to the [`FPGrowth` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/FPGrowth.html) for details on the API.

```
import org.apache.spark.mllib.fpm.FPGrowth
import org.apache.spark.rdd.RDD

val data = sc.textFile("data/mllib/sample_fpgrowth.txt")

val transactions: RDD[Array[String]] = data.map(s => s.trim.split(' '))

val fpg = new FPGrowth()
  .setMinSupport(0.2)
  .setNumPartitions(10)
val model = fpg.run(transactions)

model.freqItemsets.collect().foreach { itemset =>
  println(s"${itemset.items.mkString("[", ",", "]")},${itemset.freq}")
}

val minConfidence = 0.8
model.generateAssociationRules(minConfidence).collect().foreach { rule =>
  println(s"${rule.antecedent.mkString("[", ",", "]")}=> " +
    s"${rule.consequent .mkString("[", ",", "]")},${rule.confidence}")
}
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/SimpleFPGrowth.scala" in the Spark repo.
[`FPGrowth`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowth.html) implements the FP-growth algorithm. It takes a `JavaRDD` of transactions, where each transaction is an `Iterable` of items of a generic type. Calling `FPGrowth.run` with transactions returns an [`FPGrowthModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowthModel.html) that stores the frequent itemsets with their frequencies. The following example illustrates how to mine frequent itemsets and association rules (see [Association Rules](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#association-rules) for details) from `transactions`.
Refer to the [`FPGrowth` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowth.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.fpm.AssociationRules;
import org.apache.spark.mllib.fpm.FPGrowth;
import org.apache.spark.mllib.fpm.FPGrowthModel;

JavaRDD<String> data = sc.textFile("data/mllib/sample_fpgrowth.txt");

JavaRDD<List<String>> transactions = data.map(line -> Arrays.asList(line.split(" ")));

FPGrowth fpg = new FPGrowth()
  .setMinSupport(0.2)
  .setNumPartitions(10);
FPGrowthModel<String> model = fpg.run(transactions);

for (FPGrowth.FreqItemset<String> itemset: model.freqItemsets().toJavaRDD().collect()) {
  System.out.println("[" + itemset.javaItems() + "], " + itemset.freq());
}

double minConfidence = 0.8;
for (AssociationRules.Rule<String> rule
  : model.generateAssociationRules(minConfidence).toJavaRDD().collect()) {
  System.out.println(
    rule.javaAntecedent() + " => " + rule.javaConsequent() + ", " + rule.confidence());
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaSimpleFPGrowth.java" in the Spark repo.
## Association Rules[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#association-rules)
  * **Scala**
  * **Java**

[AssociationRules](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/AssociationRules.html) implements a parallel rule generation algorithm for constructing rules that have a single item as the consequent.
Refer to the [`AssociationRules` Scala docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/AssociationRules.html) for details on the API.

```
import org.apache.spark.mllib.fpm.AssociationRules
import org.apache.spark.mllib.fpm.FPGrowth.FreqItemset

val freqItemsets = sc.parallelize(Seq(
  new FreqItemset(Array("a"), 15L),
  new FreqItemset(Array("b"), 35L),
  new FreqItemset(Array("a", "b"), 12L)
))

val ar = new AssociationRules()
  .setMinConfidence(0.8)
val results = ar.run(freqItemsets)

results.collect().foreach { rule =>
println(s"[${rule.antecedent.mkString(",")}=>${rule.consequent.mkString(",")} ]" +
    s" ${rule.confidence}")
}
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/AssociationRulesExample.scala" in the Spark repo.
[AssociationRules](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/AssociationRules.html) implements a parallel rule generation algorithm for constructing rules that have a single item as the consequent.
Refer to the [`AssociationRules` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/AssociationRules.html) for details on the API.

```
import java.util.Arrays;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.fpm.AssociationRules;
import org.apache.spark.mllib.fpm.FPGrowth;
import org.apache.spark.mllib.fpm.FPGrowth.FreqItemset;

JavaRDD<FPGrowth.FreqItemset<String>> freqItemsets = sc.parallelize(Arrays.asList(
  new FreqItemset<>(new String[] {"a"}, 15L),
  new FreqItemset<>(new String[] {"b"}, 35L),
  new FreqItemset<>(new String[] {"a", "b"}, 12L)
));

AssociationRules arules = new AssociationRules()
  .setMinConfidence(0.8);
JavaRDD<AssociationRules.Rule<String>> results = arules.run(freqItemsets);

for (AssociationRules.Rule<String> rule : results.collect()) {
  System.out.println(
    rule.javaAntecedent() + " => " + rule.javaConsequent() + ", " + rule.confidence());
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaAssociationRulesExample.java" in the Spark repo.
## PrefixSpan[](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#prefixspan)
PrefixSpan is a sequential pattern mining algorithm described in [Pei et al., Mining Sequential Patterns by Pattern-Growth: The PrefixSpan Approach](https://doi.org/10.1109%2FTKDE.2004.77). We refer the reader to the referenced paper for formalizing the sequential pattern mining problem.
`spark.mllib`’s PrefixSpan implementation takes the following parameters:
  * `minSupport`: the minimum support required to be considered a frequent sequential pattern.
  * `maxPatternLength`: the maximum length of a frequent sequential pattern. Any frequent pattern exceeding this length will not be included in the results.
  * `maxLocalProjDBSize`: the maximum number of items allowed in a prefix-projected database before local iterative processing of the projected database begins. This parameter should be tuned with respect to the size of your executors.

**Examples**
The following example illustrates PrefixSpan running on the sequences (using same notation as Pei et al):

```
  <(12)3>
  <1(32)(12)>
  <(12)5>
  <6>

```

  * **Scala**
  * **Java**

[`PrefixSpan`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/PrefixSpan.html) implements the PrefixSpan algorithm. Calling `PrefixSpan.run` returns a [`PrefixSpanModel`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/PrefixSpanModel.html) that stores the frequent sequences with their frequencies.
Refer to the [`PrefixSpan` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/PrefixSpan.html) and [`PrefixSpanModel` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/fpm/PrefixSpanModel.html) for details on the API.

```
import org.apache.spark.mllib.fpm.PrefixSpan

val sequences = sc.parallelize(Seq(
  Array(Array(1, 2), Array(3)),
  Array(Array(1), Array(3, 2), Array(1, 2)),
  Array(Array(1, 2), Array(5)),
  Array(Array(6))
), 2).cache()
val prefixSpan = new PrefixSpan()
  .setMinSupport(0.5)
  .setMaxPatternLength(5)
val model = prefixSpan.run(sequences)
model.freqSequences.collect().foreach { freqSequence =>
  println(
    s"${freqSequence.sequence.map(_.mkString("[", ", ", "]")).mkString("[", ", ", "]")}," +
      s" ${freqSequence.freq}")
}
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/PrefixSpanExample.scala" in the Spark repo.
[`PrefixSpan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.html) implements the PrefixSpan algorithm. Calling `PrefixSpan.run` returns a [`PrefixSpanModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpanModel.html) that stores the frequent sequences with their frequencies.
Refer to the [`PrefixSpan` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.html) and [`PrefixSpanModel` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpanModel.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.mllib.fpm.PrefixSpan;
import org.apache.spark.mllib.fpm.PrefixSpanModel;

JavaRDD<List<List<Integer>>> sequences = sc.parallelize(Arrays.asList(
  Arrays.asList(Arrays.asList(1, 2), Arrays.asList(3)),
  Arrays.asList(Arrays.asList(1), Arrays.asList(3, 2), Arrays.asList(1, 2)),
  Arrays.asList(Arrays.asList(1, 2), Arrays.asList(5)),
  Arrays.asList(Arrays.asList(6))
), 2);
PrefixSpan prefixSpan = new PrefixSpan()
  .setMinSupport(0.5)
  .setMaxPatternLength(5);
PrefixSpanModel<Integer> model = prefixSpan.run(sequences);
for (PrefixSpan.FreqSequence<Integer> freqSeq: model.freqSequences().toJavaRDD().collect()) {
  System.out.println(freqSeq.javaSequence() + ", " + freqSeq.freq());
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaPrefixSpanExample.java" in the Spark repo.
