[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/mllib/)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/mllib/)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/mllib/)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/mllib/)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/mllib/)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)


  * [ Apache Software Foundation ](https://spark.apache.org/mllib/)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)


# MLlib
**MLlib** is Apache Spark's scalable machine learning library. 
## Ease of use
Usable in Java, Scala, Python, and R. 
MLlib fits into [Spark](https://spark.apache.org/)'s APIs and interoperates with [NumPy](http://www.numpy.org) in Python (as of Spark 0.9) and R libraries (as of Spark 1.5). You can use any Hadoop data source (e.g. HDFS, HBase, or local files), making it easy to plug into Hadoop workflows. 
data = spark.read.format("libsvm")\  
.load("hdfs://...")  
  
model = KMeans(k=10).fit(data) 
Calling MLlib in Python
## Performance
High-quality algorithms, 100x faster than MapReduce. 
Spark excels at iterative computation, enabling MLlib to run fast. At the same time, we care about algorithmic performance: MLlib contains high-quality algorithms that leverage iteration, and can yield better results than the one-pass approximations sometimes used on MapReduce. 
![](https://spark.apache.org/images/logistic-regression.png)
Logistic regression in Hadoop and Spark
## Runs everywhere
Spark runs on Hadoop, Apache Mesos, Kubernetes, standalone, or in the cloud, against diverse data sources. 
You can run Spark using its [standalone cluster mode](https://spark.apache.org/docs/latest/spark-standalone.html), on [EC2](https://github.com/amplab/spark-ec2), on [Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html), on [Mesos](https://mesos.apache.org), or on [Kubernetes](https://kubernetes.io/). Access data in [HDFS](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html), [Apache Cassandra](https://cassandra.apache.org), [Apache HBase](https://hbase.apache.org), [Apache Hive](https://hive.apache.org), and hundreds of other data sources. 
![](https://spark.apache.org/images/hadoop.jpg)
### Algorithms
MLlib contains many algorithms and utilities. 
ML algorithms include: 
  * Classification: logistic regression, naive Bayes,...
  * Regression: generalized linear regression, survival regression,...
  * Decision trees, random forests, and gradient-boosted trees
  * Recommendation: alternating least squares (ALS)
  * Clustering: K-means, Gaussian mixtures (GMMs),...
  * Topic modeling: latent Dirichlet allocation (LDA)
  * Frequent itemsets, association rules, and sequential pattern mining


ML workflow utilities include: 
  * Feature transformations: standardization, normalization, hashing,...
  * ML Pipeline construction
  * Model evaluation and hyper-parameter tuning
  * ML persistence: saving and loading models and Pipelines


Other utilities include: 
  * Distributed linear algebra: SVD, PCA,...
  * Statistics: summary statistics, hypothesis testing,...


Refer to the [MLlib guide](https://spark.apache.org/docs/latest/ml-guide.html) for usage examples.
### Community
MLlib is developed as part of the Apache Spark project. It thus gets tested and updated with each Spark release. 
If you have questions about the library, ask on the [Spark mailing lists](https://spark.apache.org/community.html#mailing-lists). 
MLlib is still a rapidly growing project and welcomes contributions. If you'd like to submit an algorithm to MLlib, read [how to contribute to Spark](https://spark.apache.org/contributing.html) and send us a patch! 
### Getting started
To get started with MLlib: 
  * [Download Spark](https://spark.apache.org/downloads.html). MLlib is included as a module.
  * Read the [MLlib guide](https://spark.apache.org/docs/latest/ml-guide.html), which includes various usage examples.
  * Learn how to [deploy](https://spark.apache.org/docs/latest/#launching-on-a-cluster) Spark on a cluster if you'd like to run in distributed mode. You can also run locally on a multicore machine without any setup. 


[ Download Apache Spark  
Includes MLlib ](https://spark.apache.org/downloads.html)
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
