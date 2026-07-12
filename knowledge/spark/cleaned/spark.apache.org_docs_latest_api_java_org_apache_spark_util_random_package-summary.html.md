[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.util.random
* * *
package org.apache.spark.util.random
Utilities for random number generation.
  * Related Packages
Package
Description
[org.apache.spark.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/package-summary.html)
Spark utilities.
[org.apache.spark.util.logging](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/logging/package-summary.html)
[org.apache.spark.util.sketch](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/sketch/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BernoulliCellSampler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/BernoulliCellSampler.html "class in org.apache.spark.util.random")<T>
Developer API A sampler based on Bernoulli trials for partitioning a data sequence.
[BernoulliSampler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/BernoulliSampler.html "class in org.apache.spark.util.random")<T>
Developer API A sampler based on Bernoulli trials.
[BinomialBounds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/BinomialBounds.html "class in org.apache.spark.util.random")
Utility functions that help us determine bounds on adjusted sampling rate to guarantee exact sample size with high confidence when sampling without replacement.
[PoissonBounds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/PoissonBounds.html "class in org.apache.spark.util.random")
Utility functions that help us determine bounds on adjusted sampling rate to guarantee exact sample sizes with high confidence when sampling with replacement.
[PoissonSampler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/PoissonSampler.html "class in org.apache.spark.util.random")<T>
Developer API A sampler for sampling with replacement, based on values drawn from Poisson distribution.
[Pseudorandom](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/Pseudorandom.html "interface in org.apache.spark.util.random")
Developer API A class with pseudorandom behavior.
[RandomSampler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/RandomSampler.html "interface in org.apache.spark.util.random")<T,U>
Developer API A pseudorandom sampler.
[SamplingUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/SamplingUtils.html "class in org.apache.spark.util.random")
[StratifiedSamplingUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/StratifiedSamplingUtils.html "class in org.apache.spark.util.random")
Auxiliary functions and data structures for the sampleByKey method in PairRDDFunctions.
