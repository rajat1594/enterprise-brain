[Skip to main content](https://spark.apache.org/docs/latest/api/python/getting_started/index.html#main-content)
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

Section Navigation
  * [Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
  * [Quickstart: DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)
  * [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)
  * [Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html)
  * [Testing PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html)

  * [ ](https://spark.apache.org/docs/latest/api/python/index.html)
  * Getting Started

# Getting Started[#](https://spark.apache.org/docs/latest/api/python/getting_started/index.html#getting-started "Permalink to this headline")
This page summarizes the basic steps required to setup and get started with PySpark. There are more guides shared with other languages such as [Quick Start](https://spark.apache.org/docs/latest/quick-start.html) in Programming Guides at [the Spark documentation](https://spark.apache.org/docs/latest/index.html#where-to-go-from-here).
There are live notebooks where you can try PySpark out without any other step:
  * [Live Notebook: DataFrame](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_df.ipynb)
  * [Live Notebook: Spark Connect](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_connect.ipynb)
  * [Live Notebook: pandas API on Spark](https://mybinder.org/v2/gh/apache/spark/f0bb2e6a47d?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_ps.ipynb)

The list below is the contents of this quickstart page:
  * [Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
    * [Python Versions Supported](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#python-versions-supported)
    * [Using PyPI](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-pypi)
    * [Using Conda](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-conda)
    * [Manually Downloading](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
    * [Installing from Source](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#installing-from-source)
    * [Dependencies](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#dependencies)
  * [Quickstart: DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)
    * [DataFrame Creation](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#DataFrame-Creation)
    * [Viewing Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Viewing-Data)
    * [Selecting and Accessing Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Selecting-and-Accessing-Data)
    * [Applying a Function](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Applying-a-Function)
    * [Grouping Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Grouping-Data)
    * [Getting Data In/Out](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Getting-Data-In/Out)
    * [Working with SQL](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Working-with-SQL)
  * [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)
    * [Launch Spark server with Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html#Launch-Spark-server-with-Spark-Connect)
    * [Connect to Spark Connect server](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html#Connect-to-Spark-Connect-server)
    * [Create DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html#Create-DataFrame)
  * [Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html)
    * [Object Creation](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Object-Creation)
    * [Missing Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Missing-Data)
    * [Operations](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Operations)
    * [Grouping](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Grouping)
    * [Plotting](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Plotting)
    * [Getting data in/out](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html#Getting-data-in/out)
  * [Testing PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html)
    * [Build a PySpark Application](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html#Build-a-PySpark-Application)
    * [Testing your PySpark Application](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html#Testing-your-PySpark-Application)
    * [Putting It All Together!](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html#Putting-It-All-Together!)

[ previous PySpark Overview ](https://spark.apache.org/docs/latest/api/python/index.html "previous page") [ next Installation ](https://spark.apache.org/docs/latest/api/python/getting_started/install.html "next page")
[ Show Source ](https://spark.apache.org/docs/latest/api/python/_sources/getting_started/index.rst.txt)
Copyright @ 2026 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Created using [Sphinx](https://www.sphinx-doc.org/) 4.5.0.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.13.3.
