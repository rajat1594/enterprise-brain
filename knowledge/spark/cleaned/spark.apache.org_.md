[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (deprecated)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
    * [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
  * [ Developers ](https://spark.apache.org/)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)

  * [ Apache Software Foundation ](https://spark.apache.org/)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)

# Unified engine for large-scale data analytics
[Get Started](https://spark.apache.org/docs/latest/quick-start.html)
## What is Apache Spark™?
Apache Spark™ is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.
Simple.
Fast.
Scalable.
Unified.
Key features
![Batch/streaming data](https://spark.apache.org/images/batch-sstreaming-data-icon.svg)
Batch/streaming data
Unify the processing of your data in batches and real-time streaming, using your preferred language: Python, SQL, Scala, Java or R.
![SQL analytics](https://spark.apache.org/images/sql-analytics-icon.svg)
SQL analytics
Execute fast, distributed ANSI SQL queries for dashboarding and ad-hoc reporting. Runs faster than most data warehouses.
![Data science at scale](https://spark.apache.org/images/data-science-scale-icon.svg)
Data science at scale
Perform Exploratory Data Analysis (EDA) on petabyte-scale data without having to resort to downsampling
![Machine Learning](https://spark.apache.org/images/machine-learning-icon.svg)
Machine learning
Train machine learning algorithms on a laptop and use the same code to scale to fault-tolerant clusters of thousands of machines.
Python  SQL  Scala  Java  R
Run now
Install with 'pip'
$ pip install pyspark
$ pyspark
Use the official Docker image
$ docker run -it --rm spark:python3 /opt/spark/bin/pyspark
QuickStart  Machine Learning  Analytics & Data Science

```
df = spark.read.json("logs.json")
df.where("age > 21").select("name.first").show()
```

```
# Every record contains a label and feature vector
df = spark.createDataFrame(data, ["label", "features"])

# Split the data into train/test datasets
train_df, test_df = df.randomSplit([.80, .20], seed=42)

# Set hyperparameters for the algorithm
rf = RandomForestRegressor(numTrees=100)

# Fit the model to the training data
model = rf.fit(train_df)

# Generate predictions on the test dataset.
model.transform(test_df).show()
```

```
df = spark.read.csv("accounts.csv", header=True)

# Select subset of features and filter for balance > 0
filtered_df = df.select("AccountBalance", "CountOfDependents").filter("AccountBalance > 0")

# Generate summary statistics
filtered_df.summary().show()
```

Run now
$ docker run -it --rm spark /opt/spark/bin/spark-sql
spark-sql>

```
SELECT
  name.first AS first_name,
  name.last AS last_name,
  age
FROM json.`logs.json`
  WHERE age > 21;
```

Run now
$ docker run -it --rm spark /opt/spark/bin/spark-shell
scala>

```
val df = spark.read.json("logs.json")
df.where("age > 21")
  .select("name.first").show()
```

Run now
$ docker run -it --rm spark /opt/spark/bin/spark-shell
scala>

```
Dataset df = spark.read().json("logs.json");
df.where("age > 21")
  .select("name.first").show();
```

Run now
$ docker run -it --rm spark:r /opt/spark/bin/sparkR
>

```
df <- read.json(path = "logs.json")
df <- filter(df, df$age > 21)
head(select(df, df$name.first))
```

The most widely-used engine for scalable computing
Thousands of companies, including 80% of the Fortune 500, use Apache Spark™.
Over 2,000 contributors to the open source project from industry and academia.
Ecosystem
Apache Spark™ integrates with your favorite frameworks, helping to scale them to thousands of machines.
Data science and Machine learning
![scikit learn](https://spark.apache.org/images/scikit-learn.png)
![pandas](https://spark.apache.org/images/pandas.png)
![TensorFlow](https://spark.apache.org/images/tf_logo_social.png)
![PyTorch](https://spark.apache.org/images/pytorch.png)
![mlflow](https://spark.apache.org/images/mlflow-logo.png)
![R](https://spark.apache.org/images/r_logo.png)
![NumPy](https://spark.apache.org/images/numpy.png)
SQL analytics and BI
![Apache Superset](https://spark.apache.org/images/superset.png)
![PowerBI](https://spark.apache.org/images/PowerBI-Logo-Square-Insight-Platforms.png)
![Looker](https://spark.apache.org/images/looker_logo.png)
![Redash](https://spark.apache.org/images/redash.png)
![Tableau](https://spark.apache.org/images/tableau-logo-tableau-software.png)
![dbt](https://spark.apache.org/images/dbt.png)
Storage and Infrastructure
![Elasticsearch](https://spark.apache.org/images/Elasticsearch.png)
![mongoDB](https://spark.apache.org/images/mongo.png)
![Apache Kafka](https://spark.apache.org/images/kafka.png)
![Delta Lake](https://spark.apache.org/images/delta-lake-logo.png)
![Kubernetes](https://spark.apache.org/images/kubernetes-horizontal-color.png)
![Apache Airflow](https://spark.apache.org/images/AirflowLogo.png)
![Parquet](https://spark.apache.org/images/Apache_Parquet_logo.png)
![SQL Server](https://spark.apache.org/images/sqlserver.png)
![Cassandra](https://spark.apache.org/images/1280px-Cassandra_logo.png)
![Apache Iceberg](https://spark.apache.org/images/Apache_Iceberg_logo.png)
![Apache Orc](https://spark.apache.org/images/Apache_Orc_logo.png)
Spark SQL engine: under the hood
Apache Spark™ is built on an advanced distributed SQL engine for large-scale data
[Adaptive Query Execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution)
Spark SQL adapts the execution plan at runtime, such as automatically setting the number of reducers and join algorithms.
[Support for ANSI SQL](https://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html)
Use the same SQL you’re already comfortable with.
[Structured and unstructured data](https://spark.apache.org/docs/latest/sql-data-sources-json.html)
Spark SQL works on structured tables and unstructured data such as JSON or images.
TPC-DS 1TB No-Stats With vs. Without Adaptive Query Execution
![](https://spark.apache.org/images/AQE-compersion.png)
Accelerates TPC-DS queries up to 8x
Join the community
Spark has a thriving open source community, with contributors from around the globe building features, documentation and assisting other users.
[ ![Mailing list](https://spark.apache.org/images/icon-orange-mailing-list.svg) Mailing list  ](https://spark.apache.org/community.html)
[ ![Source code](https://spark.apache.org/images/icon-orange-built-in-functions.svg) Source code  ](https://github.com/apache/spark)
[ ![News and events](https://spark.apache.org/images/icon-orange-Delta-Table.svg) News and events  ](https://spark.apache.org/news/)
[ ![How to contribute](https://spark.apache.org/images/icon-orange-Collaborative.svg) How to contribute  ](https://spark.apache.org/contributing.html)
[ ![Issue tracking](https://spark.apache.org/images/icon-orange-Scheduled-Jobs.svg) Issue tracking  ](https://issues.apache.org/jira/projects/SPARK/issues)
[ ![Committers](https://spark.apache.org/images/icon-orange-data-engineer-persona.svg) Committers  ](https://spark.apache.org/committers.html)
* * *
Apache Spark, Spark, Apache, the Apache feather logo, and the Apache Spark project logo are either registered trademarks or trademarks of The Apache Software Foundation in the United States and other countries. See guidance on use of Apache Spark [trademarks](https://spark.apache.org/trademarks.html). All other marks mentioned may be trademarks or registered trademarks of their respective owners. Copyright © 2018 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/).
