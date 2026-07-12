[Skip to main content](https://spark.apache.org/docs/latest/api/python/index.html#main-content)
`⌘`+`K`
[ ![Logo image](https://spark.apache.org/images/spark-logo.png) ![Logo image](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/docs/latest/api/python/index.html)
Site Navigation 
  * [ Overview ](https://spark.apache.org/docs/latest/api/python/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * [ Tutorials ](https://spark.apache.org/docs/latest/api/python/tutorial/index.html)
  * [ User Guide ](https://spark.apache.org/docs/latest/api/python/user_guide/index.html)
  * [ API Reference ](https://spark.apache.org/docs/latest/api/python/reference/index.html)
  * [ Development ](https://spark.apache.org/docs/latest/api/python/development/index.html)
More 
  * [ Migration Guides ](https://spark.apache.org/docs/latest/api/python/migration_guide/index.html)


4.1.2 
  * [ GitHub](https://github.com/apache/spark)
  * [ PyPI](https://pypi.org/project/pyspark)


Site Navigation 
  * [ Overview ](https://spark.apache.org/docs/latest/api/python/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * [ Tutorials ](https://spark.apache.org/docs/latest/api/python/tutorial/index.html)
  * [ User Guide ](https://spark.apache.org/docs/latest/api/python/user_guide/index.html)
  * [ API Reference ](https://spark.apache.org/docs/latest/api/python/reference/index.html)
  * [ Development ](https://spark.apache.org/docs/latest/api/python/development/index.html)
More 
  * [ Migration Guides ](https://spark.apache.org/docs/latest/api/python/migration_guide/index.html)


4.1.2 
  * [ GitHub](https://github.com/apache/spark)
  * [ PyPI](https://pypi.org/project/pyspark)


# PySpark Overview[#](https://spark.apache.org/docs/latest/api/python/index.html#pyspark-overview "Permalink to this headline")
**Date** : May 16, 2026 **Version** : 4.1.2
**Useful links** : [Live Notebook](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_df.ipynb) | [GitHub](https://github.com/apache/spark) | [Issues](https://issues.apache.org/jira/projects/SPARK/issues) | [Examples](https://github.com/apache/spark/tree/f0bb2e6a47d/examples/src/main/python) | [Community](https://spark.apache.org/community.html) | [Stack Overflow](https://stackoverflow.com/questions/tagged/pyspark) | [Dev Mailing List](https://lists.apache.org/list.html?dev@spark.apache.org) | [User Mailing List](https://lists.apache.org/list.html?user@spark.apache.org)
PySpark is the Python API for Apache Spark. It enables you to perform real-time, large-scale data processing in a distributed environment using Python. It also provides a PySpark shell for interactively analyzing your data.
PySpark combines Python’s learnability and ease of use with the power of Apache Spark to enable processing and analysis of data at any size for everyone familiar with Python.
PySpark supports all of Spark’s features such as Spark SQL, DataFrames, Structured Streaming, Machine Learning (MLlib), Pipelines and Spark Core.  
|   |  [![Python Spark Connect Client](https://spark.apache.org/docs/latest/api/python/_images/pyspark-python_spark_connect_client.png)](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)  |   |  
| --- | --- | --- |  
|   |  [![Spark SQL](https://spark.apache.org/docs/latest/api/python/_images/pyspark-spark_sql_and_dataframes.png)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html)  |  [![Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/_images/pyspark-pandas_api_on_spark.png)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/index.html)  |  [![Streaming](https://spark.apache.org/docs/latest/api/python/_images/pyspark-structured_streaming.png)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/index.html)  |  [![Machine Learning](https://spark.apache.org/docs/latest/api/python/_images/pyspark-machine_learning.png)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html)  |   |  
| --- | --- | --- | --- | --- | --- |  
|   |  [![Spark Core and RDDs](https://spark.apache.org/docs/latest/api/python/_images/pyspark-spark_core_and_rdds.png)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.html)  |   |  
| --- | --- | --- |  
**Python Spark Connect Client**
Spark Connect is a client-server architecture within Apache Spark that enables remote connectivity to Spark clusters from any application. PySpark provides the client for the Spark Connect server, allowing Spark to be used as a service.
  * [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)
  * [Live Notebook: Spark Connect](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_connect.ipynb)
  * [Spark Connect Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)


**Spark SQL and DataFrames**
Spark SQL is Apache Spark’s module for working with structured data. It allows you to seamlessly mix SQL queries with Spark programs. With PySpark DataFrames you can efficiently read, write, transform, and analyze data using Python and SQL. Whether you use Python or SQL, the same underlying execution engine is used so you will always leverage the full power of Spark.
  * [Quickstart: DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)
  * [Live Notebook: DataFrame](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_df.ipynb)
  * [Spark SQL API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html)


**Pandas API on Spark**
Pandas API on Spark allows you to scale your pandas workload to any size by running it distributed across multiple nodes. If you are already familiar with pandas and want to leverage Spark for big data, pandas API on Spark makes you immediately productive and lets you migrate your applications without modifying the code. You can have a single codebase that works both with pandas (tests, smaller datasets) and with Spark (production, distributed datasets) and you can switch between the pandas API and the Pandas API on Spark easily and without overhead.
Pandas API on Spark aims to make the transition from pandas to Spark easy but if you are new to Spark or deciding which API to use, we recommend using PySpark (see [Spark SQL and DataFrames](https://spark.apache.org/docs/latest/api/python/index.html#index-page-spark-sql-and-dataframes)).
  * [Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html)
  * [Live Notebook: pandas API on Spark](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_ps.ipynb)
  * [Pandas API on Spark Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/index.html)


**Structured Streaming**
Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. You can express your streaming computation the same way you would express a batch computation on static data. The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.
  * [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
  * [Structured Streaming API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/index.html)


**Machine Learning (MLlib)**
Built on top of Spark, MLlib is a scalable machine learning library that provides a uniform set of high-level APIs that help users create and tune practical machine learning pipelines.
  * [Machine Learning Library (MLlib) Programming Guide](https://spark.apache.org/docs/latest/ml-guide.html)
  * [Machine Learning (MLlib) API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html)


**Declarative Pipelines**
Spark Declarative Pipelines (SDP) is a declarative framework for building reliable, maintainable, and testable data pipelines on Spark. SDP simplifies ETL development by allowing you to focus on the transformations you want to apply to your data, rather than the mechanics of pipeline execution.
  * [Pipelines API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pipelines.html)


**Spark Core and RDDs**
Spark Core is the underlying general execution engine for the Spark platform that all other functionality is built on top of. It provides RDDs (Resilient Distributed Datasets) and in-memory computing capabilities.
Note that the RDD API is a low-level API which can be difficult to use and you do not get the benefit of Spark’s automatic query optimization capabilities. We recommend using DataFrames (see [Spark SQL and DataFrames](https://spark.apache.org/docs/latest/api/python/index.html#index-page-spark-sql-and-dataframes) above) instead of RDDs as it allows you to express what you want more easily and lets Spark automatically construct the most efficient query for you.
  * [Spark Core API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.html)


**Spark Streaming (Legacy)**
Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
Note that Spark Streaming is the previous generation of Spark’s streaming engine. It is a legacy project and it is no longer being updated. There is a newer and easier to use streaming engine in Spark called [Structured Streaming](https://spark.apache.org/docs/latest/api/python/index.html#index-page-structured-streaming) which you should use for your streaming applications and pipelines.
  * [Spark Streaming Programming Guide (Legacy)](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
  * [Spark Streaming API Reference (Legacy)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.streaming.html)


[ next Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html "next page")
[ Show Source ](https://spark.apache.org/docs/latest/api/python/_sources/index.rst.txt)
Copyright @ 2026 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
Created using [Sphinx](https://www.sphinx-doc.org/) 4.5.0.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.13.3. 
