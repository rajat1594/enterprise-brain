[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)

  * [ Apache Software Foundation ](https://spark.apache.org/releases/spark-release-3-5-8.html)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)

# Spark Release 3.5.8
Spark 3.5.8 is the eighth maintenance release containing security and correctness fixes. This release is based on the branch-3.5 maintenance branch of Spark. We strongly recommend all 3.5 users to upgrade to this stable release.
### Notable changes
  * [[SPARK-46485]](https://issues.apache.org/jira/browse/SPARK-46485): V1Write should not add Sort when not needed
  * [[SPARK-49872]](https://issues.apache.org/jira/browse/SPARK-49872): Remove Jackson JSON string length limit in KVStoreScalaSerializer
  * [[SPARK-51831]](https://issues.apache.org/jira/browse/SPARK-51831): Column pruning with existsJoin for Datasource V2
  * [[SPARK-53149]](https://issues.apache.org/jira/browse/SPARK-53149): Fix testing whether BeeLine process run in background
  * [[SPARK-53337]](https://issues.apache.org/jira/browse/SPARK-53337): XSS: Ensure the application name in historypage get escaped
  * [[SPARK-53598]](https://issues.apache.org/jira/browse/SPARK-53598): Check the existence of numParts before reading large table property
  * [[SPARK-53673]](https://issues.apache.org/jira/browse/SPARK-53673): Fix a flaky test failure in `SparkSessionE2ESuite - interrupt tag` caused by the usage of `ForkJoinPool`
  * [[SPARK-53738]](https://issues.apache.org/jira/browse/SPARK-53738): Fix planned write when query output contains foldable orderings
  * [[SPARK-53836]](https://issues.apache.org/jira/browse/SPARK-53836): Update script `free_disk_space_container`
  * [[SPARK-53948]](https://issues.apache.org/jira/browse/SPARK-53948): Fix deadlock in Observation
  * [[SPARK-53955]](https://issues.apache.org/jira/browse/SPARK-53955): Prefer to detect Java Home from env JAVA_HOME on finding jmap for JDK 8
  * [[SPARK-53961]](https://issues.apache.org/jira/browse/SPARK-53961): Fix `FileStreamSinkSuite` flakiness by using `walkFileTree` instead of `walk`
  * [[SPARK-54015]](https://issues.apache.org/jira/browse/SPARK-54015): Relax Py4J requirement to py4j>=0.10.9.7,<0.10.9.10
  * [[SPARK-54034]](https://issues.apache.org/jira/browse/SPARK-54034): Fix `Utils.isBindCollision` to detect port conflict `NativeIoException` correctly
  * [[SPARK-54241]](https://issues.apache.org/jira/browse/SPARK-54241): Enable `NOLINT_ON_COMPILE` for all PySpark GitHub Action jobs
  * [[SPARK-54242]](https://issues.apache.org/jira/browse/SPARK-54242): Skip `Checkstyle` if `NOLINT_ON_COMPILE` is true
  * [[SPARK-54299]](https://issues.apache.org/jira/browse/SPARK-54299): Fix the wrong example query in `WindowGroupLimit`
  * [[SPARK-54336]](https://issues.apache.org/jira/browse/SPARK-54336): Fix `BloomFilterMightContain` input type check with `ScalarSubqueryReference`
  * [[SPARK-54366]](https://issues.apache.org/jira/browse/SPARK-54366): Add `free_disk_space` step to K8s integration test GitHub Action job
  * [[SPARK-54426]](https://issues.apache.org/jira/browse/SPARK-54426): Fix `release-build.sh` to detect `REPO_ID` correctly
  * [[SPARK-54505]](https://issues.apache.org/jira/browse/SPARK-54505): Correct the arguments order of createMetrics call in makeNegative
  * [[SPARK-54600]](https://issues.apache.org/jira/browse/SPARK-54600): Don’t use pickle to save/load models in pyspark.ml.connect
  * [[SPARK-54620]](https://issues.apache.org/jira/browse/SPARK-54620): Add safety check in ObservationManager to avoid Observation blocking
  * [[SPARK-54624]](https://issues.apache.org/jira/browse/SPARK-54624): Ensure user name in historypage get escaped
  * [[SPARK-54625]](https://issues.apache.org/jira/browse/SPARK-54625): UTF8String#reverse should check offset and length on copying
  * [[SPARK-54728]](https://issues.apache.org/jira/browse/SPARK-54728): Remove a wrong note in `dataframe.isEmpty`
  * [[SPARK-54750]](https://issues.apache.org/jira/browse/SPARK-54750): Fix ROUND returning NULL for Decimal values with low runtime precision
  * [[SPARK-54982]](https://issues.apache.org/jira/browse/SPARK-54982): Use ASF_NEXUS_TOKEN to release and drop staging repository when finalizing the RC

### Dependency changes
While being a maintenance release we did still upgrade some dependencies in this release they are:
  * [[SPARK-53953]](https://issues.apache.org/jira/browse/SPARK-53953): Bump Avro 1.11.5
  * [[SPARK-54649]](https://issues.apache.org/jira/browse/SPARK-54649): Upgrade Jersey to 2.47
  * [[SPARK-54900]](https://issues.apache.org/jira/browse/SPARK-54900): Upgrade `ORC` to 1.9.8

You can consult JIRA for the [detailed changes](https://s.apache.org/spark-3.5.8).
We would like to acknowledge all community members for contributing patches to this release.

[Spark News Archive](https://spark.apache.org/news/)
##### Latest News
  * [Spark 4.0.3 released](https://spark.apache.org/news/spark-4-0-3-released.html) (Jun 11, 2026)
  * [Spark 4.1.2 released](https://spark.apache.org/news/spark-4-1-2-released.html) (May 21, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview5-released.html) (May 01, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview4-released.html) (Apr 09, 2026)

[Archive](https://spark.apache.org/news/index.html)
[ ![](https://www.apache.org/events/current-event-234x60.png) ](https://www.apache.org/events/current-event.html)
[ Download Spark ](https://spark.apache.org/downloads.html)
Built-in Libraries:
  * [SQL and DataFrames](https://spark.apache.org/sql/)
  * [Spark Streaming](https://spark.apache.org/streaming/)
  * [MLlib (machine learning)](https://spark.apache.org/mllib/)
  * [GraphX (graph)](https://spark.apache.org/graphx/)

[Third-Party Projects](https://spark.apache.org/third-party-projects.html)
* * *
Apache Spark, Spark, Apache, the Apache feather logo, and the Apache Spark project logo are either registered trademarks or trademarks of The Apache Software Foundation in the United States and other countries. See guidance on use of Apache Spark [trademarks](https://spark.apache.org/trademarks.html). All other marks mentioned may be trademarks or registered trademarks of their respective owners. Copyright © 2018 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/).
