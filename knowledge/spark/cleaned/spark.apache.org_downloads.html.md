[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/downloads.html)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/downloads.html)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/downloads.html)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/downloads.html)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/downloads.html)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)

  * [ Apache Software Foundation ](https://spark.apache.org/downloads.html)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)

# Downloads
  1. Choose a Spark release: 4.1.2 (May 21 2026) 4.0.3 (Jun 11 2026) 3.5.8 (Jan 15 2026)

  2. Choose a package type:  Pre-built for Apache Hadoop 3.4 and later  Pre-built for Apache Hadoop 3.4 and later with Spark Connect enabled  Pre-built with user-provided Apache Hadoop  Source Code

  3. Download Spark: [spark-4.1.2-bin-hadoop3.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz)
  4. Verify this release using the 4.1.2 [signatures](https://downloads.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz.asc), [checksums](https://downloads.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz.sha512) and [project release KEYS](https://downloads.apache.org/spark/KEYS) by following these [procedures](https://www.apache.org/info/verification.html).

Note that Spark 4 is pre-built with Scala 2.13, and support for Scala 2.12 has been officially dropped. Spark 3 is pre-built with Scala 2.12 in general and Spark 3.2+ provides additional pre-built distribution with Scala 2.13.
### Link with Spark
Spark artifacts are [hosted in Maven Central](https://search.maven.org/search?q=g:org.apache.spark). You can add a Maven dependency with the following coordinates:

```
groupId: org.apache.spark
artifactId: spark-core_2.13
version: 4.1.0

```

### Installing with PyPi
[PySpark](https://pypi.org/project/pyspark/) is now available in pypi. To install just run `pip install pyspark`.
### Installing with Docker
Spark docker images are available from Dockerhub under the accounts of both [The Apache Software Foundation](https://hub.docker.com/r/apache/spark/) and [Official Images](https://hub.docker.com/_/spark).
Note that, these images contain non-ASF software and may be subject to different license terms. Please check their [Dockerfiles](https://github.com/apache/spark-docker) to verify whether they are compatible with your deployment.
### Release notes for stable releases
  * [Spark 4.1.2](https://spark.apache.org/releases/spark-release-4-1-2.html) (May 21 2026)
  * [Spark 4.0.3](https://spark.apache.org/releases/spark-release-4-0-3.html) (Jun 11 2026)
  * [Spark 3.5.8](https://spark.apache.org/releases/spark-release-3-5-8.html) (Jan 15 2026)

### Archived releases
As new Spark releases come out for each development stream, previous ones will be archived, but they are still available at [Spark release archives](https://archive.apache.org/dist/spark/).
**NOTE** : Previous releases of Spark may be affected by security issues. Please consult the [Security](https://spark.apache.org/security.html) page for a list of known issues that may affect the version you download before deciding to use it.
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
