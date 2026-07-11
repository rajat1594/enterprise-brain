[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/graphx/)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/graphx/)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/graphx/)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/graphx/)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/graphx/)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)


  * [ Apache Software Foundation ](https://spark.apache.org/graphx/)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)


# GraphX
**GraphX** is Apache Spark's API for graphs and graph-parallel computation. 
## Flexibility
Seamlessly work with both graphs and collections. 
GraphX unifies ETL, exploratory analysis, and iterative graph computation within a single system. You can [view](https://spark.apache.org/docs/latest/graphx-programming-guide.html#the-property-graph) the same data as both graphs and collections, [transform](https://spark.apache.org/docs/latest/graphx-programming-guide.html#property-operators) and [join](https://spark.apache.org/docs/latest/graphx-programming-guide.html#join-operators) graphs with RDDs efficiently, and write custom iterative graph algorithms using the [Pregel API](https://spark.apache.org/docs/latest/graphx-programming-guide.html#pregel-api). 
graph = Graph(vertices, edges)  
messages = spark.textFile("hdfs://...")  
graph2 = graph.joinVertices(messages) {  
(id, vertex, msg) => ...  
} 
Using GraphX in Scala
## Speed
Comparable performance to the fastest specialized graph processing systems. 
GraphX competes on performance with the fastest graph systems while retaining Spark's flexibility, fault tolerance, and ease of use. 
![](https://spark.apache.org/images/graphx-perf-comparison.png)
End-to-end PageRank performance (20 iterations, 3.7B edges)
## Algorithms
Choose from a growing library of graph algorithms. 
In addition to a [highly flexible API](https://spark.apache.org/docs/latest/graphx-programming-guide.html#graph-operators), GraphX comes with a variety of graph algorithms, many of which were contributed by our users.
  * PageRank
  * Connected components
  * Label propagation
  * SVD++
  * Strongly connected components
  * Triangle count


### Community
GraphX is developed as part of the Apache Spark project. It thus gets tested and updated with each Spark release. 
If you have questions about the library, ask on the [Spark mailing lists](https://spark.apache.org/community.html#mailing-lists). 
GraphX is in the alpha stage and welcomes contributions. If you'd like to submit a change to GraphX, read [how to contribute to Spark](https://spark.apache.org/contributing.html) and send us a patch! 
### Getting started
To get started with GraphX: 
  * [Download Spark](https://spark.apache.org/downloads.html). GraphX is included as a module.
  * Read the [GraphX guide](https://spark.apache.org/docs/latest/graphx-programming-guide.html), which includes usage examples.
  * Learn how to [deploy](https://spark.apache.org/docs/latest/#launching-on-a-cluster) Spark on a cluster if you'd like to run in distributed mode. You can also run locally on a multicore machine without any setup. 


[ Download Apache Spark  
Includes GraphX ](https://spark.apache.org/downloads.html)
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
