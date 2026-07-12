[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/faq.html)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/faq.html)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/faq.html)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/faq.html)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/faq.html)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)

  * [ Apache Software Foundation ](https://spark.apache.org/faq.html)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)

# FAQ
How does Spark relate to Apache Hadoop?
Spark is a fast and general processing engine compatible with Hadoop data. It can run in Hadoop clusters through YARN or Spark's standalone mode, and it can process data in HDFS, HBase, Cassandra, Hive, and any Hadoop InputFormat. It is designed to perform both batch processing (similar to MapReduce) and new workloads like streaming, interactive queries, and machine learning.
Who is using Spark in production?
As of 2016, surveys show that more than 1000 organizations are using Spark in production. Some of them are listed on the [Powered By page](https://spark.apache.org/powered-by.html) and at the [Spark Summit](https://spark-summit.org).
How large a cluster can Spark scale to?
Many organizations run Spark on clusters of thousands of nodes. The largest cluster we know has 8000 of them. In terms of data size, Spark has been shown to work well up to petabytes. It has been used to sort 100 TB of data 3X faster than Hadoop MapReduce on 1/10th of the machines, [winning the 2014 Daytona GraySort Benchmark](https://databricks.com/blog/2014/11/05/spark-officially-sets-a-new-record-in-large-scale-sorting.html), as well as to [sort 1 PB](https://databricks.com/blog/2014/10/10/spark-petabyte-sort.html). Several production workloads [use Spark to do ETL and data analysis on PBs of data](https://databricks.com/blog/2014/08/14/mining-graph-data-with-spark-at-alibaba-taobao.html).
Does my data need to fit in memory to use Spark?
No. Spark's operators spill data to disk if it does not fit in memory, allowing it to run well on any sized data. Likewise, cached datasets that do not fit in memory are either spilled to disk or recomputed on the fly when needed, as determined by the RDD's [storage level](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence).
How can I run Spark on a cluster?
You can use either the [standalone deploy mode](https://spark.apache.org/docs/latest/spark-standalone.html), which only needs Java to be installed on each node, or the [Mesos](https://spark.apache.org/docs/latest/running-on-mesos.html) and [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) cluster managers. If you'd like to run on Amazon EC2, AMPLab provides [EC2 scripts](https://github.com/amplab/spark-ec2#readme) to automatically launch a cluster.
Note that you can also run Spark locally (possibly on multiple cores) without any special setup by just passing `local[N]` as the master URL, where `N` is the number of parallel threads you want.
Do I need Hadoop to run Spark?
No, but if you run on a cluster, you will need some form of shared file system (for example, NFS mounted at the same path on each node). If you have this type of filesystem, you can just deploy Spark in standalone mode.
Does Spark require modified versions of Scala or Python?
No. Spark requires no changes to Scala or compiler plugins. The Python API uses the standard CPython implementation, and can call into existing C libraries for Python such as NumPy.
What’s the difference between Spark Streaming and Spark Structured Streaming? What should I use?
Spark Streaming is the previous generation of Spark’s streaming engine. There are no longer updates to Spark Streaming and it’s a legacy project. Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data. Internally, a DStream is represented as a sequence of RDDs.
Spark Structured Streaming is the current generation of Spark’s streaming engine, which is richer in functionality, easier to use, and more scalable. Spark Structured Streaming is built on top of the Spark SQL engine and enables you to express streaming computation the same way you express a batch computation on static data.
You should use Spark Structured Streaming for building streaming applications and pipelines with Spark. If you have legacy applications and pipelines built on Spark Streaming, you should migrate them to Spark Structured Streaming.
Where can I find high-resolution versions of the Spark logo?
We provide versions here: [black logo](https://spark.apache.org/images/spark-logo.eps), [white logo](https://spark.apache.org/images/spark-logo-reverse.eps). Please be aware that Spark, Apache Spark and the Spark logo are trademarks of the Apache Software Foundation, and follow the Foundation's [trademark policy](https://www.apache.org/foundation/marks/) in all uses of these logos.
Can I provide commercial software or services based on Spark?
Yes, as long as you respect the Apache Software Foundation's [software license](https://www.apache.org/licenses/) and [trademark policy](https://www.apache.org/foundation/marks/). In particular, note that there are strong restrictions about how third-party products use the "Spark" name (names based on Spark are generally not allowed). Please also refer to our [trademark policy summary](https://spark.apache.org/trademarks.html).
How can I contribute to Spark?
See the [Contributing to Spark wiki](https://spark.apache.org/contributing.html) for more information.
Where can I get more help?
Please post on StackOverflow's [`apache-spark`](https://stackoverflow.com/questions/tagged/apache-spark) tag or [Spark Users](https://lists.apache.org/list.html?user@spark.apache.org) mailing list. For more information, please refer to [Have Questions?](https://spark.apache.org/community.html#have-questions). We'll be glad to help!
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
