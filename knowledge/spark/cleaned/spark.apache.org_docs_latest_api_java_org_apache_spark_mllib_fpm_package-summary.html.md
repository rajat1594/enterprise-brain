[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.mllib.fpm
* * *
package org.apache.spark.mllib.fpm
  * Related Packages
Package
Description
[org.apache.spark.mllib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/package-summary.html)
RDD-based machine learning APIs (in maintenance mode).
  * Classes
Class
Description
[AssociationRules](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/AssociationRules.html "class in org.apache.spark.mllib.fpm")
Generates association rules from a `RDD[FreqItemset[Item}`.
[AssociationRules.Rule](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/AssociationRules.Rule.html "class in org.apache.spark.mllib.fpm")<Item>
An association rule between sets of items.
[FPGrowth](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowth.html "class in org.apache.spark.mllib.fpm")
A parallel FP-growth algorithm to mine frequent itemsets.
[FPGrowth.FreqItemset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowth.FreqItemset.html "class in org.apache.spark.mllib.fpm")<Item>
Frequent itemset.
[FPGrowthModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowthModel.html "class in org.apache.spark.mllib.fpm")<Item>
Model trained by [`FPGrowth`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowth.html "class in org.apache.spark.mllib.fpm"), which holds frequent itemsets.
[FPGrowthModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/FPGrowthModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.fpm")
[PrefixSpan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.html "class in org.apache.spark.mllib.fpm")
A parallel PrefixSpan algorithm to mine frequent sequential patterns.
[PrefixSpan.FreqSequence](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.FreqSequence.html "class in org.apache.spark.mllib.fpm")<Item>
Represents a frequent sequence.
[PrefixSpan.Postfix$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.Postfix$.html "class in org.apache.spark.mllib.fpm")
[PrefixSpan.Prefix$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.Prefix$.html "class in org.apache.spark.mllib.fpm")
[PrefixSpanModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpanModel.html "class in org.apache.spark.mllib.fpm")<Item>
Model fitted by [`PrefixSpan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpan.html "class in org.apache.spark.mllib.fpm") param: freqSequences frequent sequences
[PrefixSpanModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/fpm/PrefixSpanModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.fpm")
