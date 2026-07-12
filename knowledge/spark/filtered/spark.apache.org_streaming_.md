[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/streaming/)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/streaming/)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/streaming/)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/streaming/)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/streaming/)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)


  * [ Apache Software Foundation ](https://spark.apache.org/streaming/)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)


# Spark Structured Streaming
[Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) makes it easy to build streaming applications and pipelines with the same and familiar Spark APIs. 
## Easy to use
Spark Structured Streaming abstracts away complex streaming concepts such as incremental processing, checkpointing, and watermarks so that you can build streaming applications and pipelines without learning any new concepts or tools. 
spark  
.readStream  
.select($"value".cast("string").alias("jsonData"))  
.select(from_json($"jsonData",jsonSchema).alias("payload"))  
.writeStream  
.trigger("1 seconds")  
.start() 
## Unified batch and streaming APIs
Spark Structured Streaming provides the same structured APIs (DataFrames and Datasets) as Spark so that you don’t need to develop on or maintain two different technology stacks for batch and streaming. In addition, unified APIs make it easy to migrate your existing batch Spark jobs to streaming jobs. 
![](https://spark.apache.org/images/spark-unified-batch-and-streaming.png)
## Low latency and cost effective
Spark Structured Streaming uses the same underlying architecture as Spark so that you can take advantage of all the performance and cost optimizations built into the Spark engine. With Spark Structured Streaming, you can build low latency streaming applications and pipelines cost effectively. 
![](https://spark.apache.org/images/spark-structured-streaming-incremental-execution.png)
### Getting started
To get started with Spark Structured Streaming: 
  * [Download Spark](https://spark.apache.org/downloads.html). It includes Structured Streaming as a module.
  * Read the [Spark Structured Streaming programming guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), which includes programming models, tutorials, configurations, etc.


### Community
Spark Structured Streaming is developed as part of Apache Spark. It thus gets tested and updated with each Spark release. 
If you have questions about the system, ask on the [Spark mailing lists](https://spark.apache.org/community.html#mailing-lists). 
The Spark Structured Streaming developers welcome contributions. If you'd like to help out, read [how to contribute to Spark](https://spark.apache.org/contributing.html), and send us a patch! 
[ Download Apache Spark  
Includes Spark Structured Streaming ](https://spark.apache.org/downloads.html)
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
