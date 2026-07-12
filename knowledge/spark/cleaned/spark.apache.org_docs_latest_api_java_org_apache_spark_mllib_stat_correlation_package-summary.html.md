[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.mllib.stat.correlation
* * *
package org.apache.spark.mllib.stat.correlation
  * Related Packages
Package
Description
[org.apache.spark.mllib.stat](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/package-summary.html)
[org.apache.spark.mllib.stat.distribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/distribution/package-summary.html)
[org.apache.spark.mllib.stat.test](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Correlation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/Correlation.html "interface in org.apache.spark.mllib.stat.correlation")
Trait for correlation algorithms.
[CorrelationNames](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/CorrelationNames.html "class in org.apache.spark.mllib.stat.correlation")
Maintains supported and default correlation names.
[Correlations](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/Correlations.html "class in org.apache.spark.mllib.stat.correlation")
Delegates computation to the specific correlation object based on the input method name.
[PearsonCorrelation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/PearsonCorrelation.html "class in org.apache.spark.mllib.stat.correlation")
Compute Pearson correlation for two RDDs of the type RDD[Double] or the correlation matrix for an RDD of the type RDD[Vector].
[SpearmanCorrelation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/SpearmanCorrelation.html "class in org.apache.spark.mllib.stat.correlation")
Compute Spearman's correlation for two RDDs of the type RDD[Double] or the correlation matrix for an RDD of the type RDD[Vector].
