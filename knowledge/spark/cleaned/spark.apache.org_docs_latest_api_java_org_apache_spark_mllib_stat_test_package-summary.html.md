[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.mllib.stat.test
* * *
package org.apache.spark.mllib.stat.test
  * Related Packages
Package
Description
[org.apache.spark.mllib.stat](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/package-summary.html)
[org.apache.spark.mllib.stat.correlation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/correlation/package-summary.html)
[org.apache.spark.mllib.stat.distribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/distribution/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BinarySample](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/BinarySample.html "class in org.apache.spark.mllib.stat.test")
Class that represents the group and value of a sample.
[ChiSqTest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/ChiSqTest.html "class in org.apache.spark.mllib.stat.test")
Conduct the chi-squared test for the input RDDs using the specified method.
[ChiSqTest.Method](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/ChiSqTest.Method.html "class in org.apache.spark.mllib.stat.test")
param: name String name for the method.
[ChiSqTest.Method$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/ChiSqTest.Method$.html "class in org.apache.spark.mllib.stat.test")
[ChiSqTest.NullHypothesis$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/ChiSqTest.NullHypothesis$.html "class in org.apache.spark.mllib.stat.test")
[ChiSqTestResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/ChiSqTestResult.html "class in org.apache.spark.mllib.stat.test")
Object containing the test results for the chi-squared hypothesis test.
[KolmogorovSmirnovTest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/KolmogorovSmirnovTest.html "class in org.apache.spark.mllib.stat.test")
Conduct the two-sided Kolmogorov Smirnov (KS) test for data sampled from a continuous distribution.
[KolmogorovSmirnovTest.NullHypothesis$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/KolmogorovSmirnovTest.NullHypothesis$.html "class in org.apache.spark.mllib.stat.test")
[KolmogorovSmirnovTestResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/KolmogorovSmirnovTestResult.html "class in org.apache.spark.mllib.stat.test")
Object containing the test results for the Kolmogorov-Smirnov test.
[StreamingTest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/StreamingTest.html "class in org.apache.spark.mllib.stat.test")
Performs online 2-sample significance testing for a stream of (Boolean, Double) pairs.
[StreamingTestMethod](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/StreamingTestMethod.html "interface in org.apache.spark.mllib.stat.test")
Significance testing methods for [`StreamingTest`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/StreamingTest.html "class in org.apache.spark.mllib.stat.test").
[StudentTTest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/StudentTTest.html "class in org.apache.spark.mllib.stat.test")
Performs Students's 2-sample t-test.
[TestResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/TestResult.html "interface in org.apache.spark.mllib.stat.test")<DF>
Trait for hypothesis test results.
[WelchTTest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/stat/test/WelchTTest.html "class in org.apache.spark.mllib.stat.test")
Performs Welch's 2-sample t-test.
