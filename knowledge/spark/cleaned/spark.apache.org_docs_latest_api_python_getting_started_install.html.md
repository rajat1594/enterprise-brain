[Skip to main content](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#main-content)
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
[4.0.1](https://spark.apache.org/docs/4.0.1/api/python/getting_started/install.html)[4.0.0](https://spark.apache.org/docs/4.0.0/api/python/getting_started/install.html)[3.5.7](https://spark.apache.org/docs/3.5.7/api/python/getting_started/install.html)[3.5.5](https://spark.apache.org/docs/3.5.5/api/python/getting_started/install.html)[3.5.4](https://spark.apache.org/docs/3.5.4/api/python/getting_started/install.html)[3.5.3](https://spark.apache.org/docs/3.5.3/api/python/getting_started/install.html)[3.5.2](https://archive.apache.org/dist/spark/docs/3.5.2/api/python/getting_started/install.html)[3.5.1](https://archive.apache.org/dist/spark/docs/3.5.1/api/python/getting_started/install.html)[3.5.0](https://archive.apache.org/dist/spark/docs/3.5.0/api/python/getting_started/install.html)[3.4.4](https://archive.apache.org/dist/spark/docs/3.4.4/api/python/getting_started/install.html)[3.4.3](https://archive.apache.org/dist/spark/docs/3.4.3/api/python/getting_started/install.html)[3.4.2](https://archive.apache.org/dist/spark/docs/3.4.2/api/python/getting_started/install.html)[3.4.1](https://archive.apache.org/dist/spark/docs/3.4.1/api/python/getting_started/install.html)[3.4.0](https://archive.apache.org/dist/spark/docs/3.4.0/api/python/getting_started/install.html)[3.3.4](https://archive.apache.org/dist/spark/docs/3.3.4/api/python/getting_started/install.html)[3.3.3](https://archive.apache.org/dist/spark/docs/3.3.3/api/python/getting_started/install.html)[3.3.2](https://archive.apache.org/dist/spark/docs/3.3.2/api/python/getting_started/install.html)[3.3.1](https://archive.apache.org/dist/spark/docs/3.3.1/api/python/getting_started/install.html)[3.3.0](https://archive.apache.org/dist/spark/docs/3.3.0/api/python/getting_started/install.html)
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
  * [Getting Started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * Installation

# Installation[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#installation "Permalink to this headline")
PySpark is included in the official releases of Spark available in the [Apache Spark website](https://spark.apache.org/downloads.html). For Python users, PySpark also provides `pip` installation from PyPI. This is usually for local usage or as a client to connect to a cluster instead of setting up a cluster itself.
This page includes instructions for installing PySpark by using pip, Conda, downloading manually, and building from the source.
## Python Versions Supported[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#python-versions-supported "Permalink to this headline")
Python 3.10 and above.
## Using PyPI[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-pypi "Permalink to this headline")
PySpark installation using [PyPI (pyspark)](https://pypi.org/project/pyspark/) is as follows:

```
pip install pyspark

```
Copy to clipboard
If you want to install extra dependencies for a specific component, you can install it as below:

```
# Spark SQL
pip install pyspark[sql]
# pandas API on Spark
pip install pyspark[pandas_on_spark] plotly  # to plot your data, you can install plotly together.
# Spark Connect
pip install pyspark[connect]

```
Copy to clipboard
See [Optional dependencies](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#optional-dependencies) for more detail about extra dependencies.
For PySpark with/without a specific Hadoop version, you can install it by using `PYSPARK_HADOOP_VERSION` environment variables as below:

```
PYSPARK_HADOOP_VERSION=3 pip install pyspark

```
Copy to clipboard
The default distribution uses Hadoop 3.3 and Hive 2.3. If users specify different versions of Hadoop, the pip installation automatically downloads a different version and uses it in PySpark. Downloading it can take a while depending on the network and the mirror chosen. `PYSPARK_RELEASE_MIRROR` can be set to manually choose the mirror for faster downloading.

```
PYSPARK_RELEASE_MIRROR=http://mirror.apache-kr.org PYSPARK_HADOOP_VERSION=3 pip install

```
Copy to clipboard
It is recommended to use `-v` option in `pip` to track the installation and download status.

```
PYSPARK_HADOOP_VERSION=3 pip install pyspark -v

```
Copy to clipboard
Supported values in `PYSPARK_HADOOP_VERSION` are:
  * `without`: Spark pre-built with user-provided Apache Hadoop
  * `3`: Spark pre-built for Apache Hadoop 3.3 and later (default)

Note that this installation of PySpark with/without a specific Hadoop version is experimental. It can change or be removed between minor releases.
### Making Spark Connect the default[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#making-spark-connect-the-default "Permalink to this headline")
If you want to make Spark Connect the default, you can install an additional library via [PyPI (pyspark-connect)](https://pypi.org/project/pyspark-connect/). Execute the following command:

```
pip install pyspark-connect

```
Copy to clipboard
This will automatically install the `pyspark` library, as well as dependencies that are necessary for Spark Connect. If you want to customize `pyspark`, you need to install `pyspark` with the instructions above in advance.
This package supports both: - `spark.master` (`--master`) with a locally running Spark Connect server - `spark.remote` (`--remote`) including local clusters, e.g., `local[*]` as well as connection URIs such as `sc://localhost`.
See also [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html) for how to use it.
### Python Spark Connect Client[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#python-spark-connect-client "Permalink to this headline")
The Python Spark Connect client is a pure Python library that does not rely on any non-Python dependencies such as jars and JRE in your environment. To install the Python Spark Connect client via [PyPI (pyspark-client)](https://pypi.org/project/pyspark-client/), execute the following command:

```
pip install pyspark-client

```
Copy to clipboard
This package only supports spark.remote with connection URIs, e.g., `sc://localhost`. See also [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html) for how to use it.
## Using Conda[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-conda "Permalink to this headline")
Conda is an open-source package management and environment management system (developed by [Anaconda](https://www.anaconda.com/)), which is best installed through [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniforge](https://github.com/conda-forge/miniforge/). The tool is both cross-platform and language agnostic, and in practice, conda can replace both [pip](https://pip.pypa.io/en/latest/) and [virtualenv](https://virtualenv.pypa.io/en/latest/).
Conda uses so-called channels to distribute packages, and together with the default channels by Anaconda itself, the most important channel is [conda-forge](https://conda-forge.org/), which is the community-driven packaging effort that is the most extensive & the most current (and also serves as the upstream for the Anaconda channels in most cases).
To create a new conda environment from your terminal and activate it, proceed as shown below:

```
conda create -n pyspark_env
conda activate pyspark_env

```
Copy to clipboard
After activating the environment, use the following command to install pyspark, a python version of your choice, as well as other packages you want to use in the same session as pyspark (you can install in several steps too).

```
conda install -c conda-forge pyspark  # can also add "python=3.10 some_package [etc.]" here

```
Copy to clipboard
Note that [PySpark for conda](https://anaconda.org/conda-forge/pyspark) is maintained separately by the community; while new versions generally get packaged quickly, the availability through conda(-forge) is not directly in sync with the PySpark release cycle.
While using pip in a conda environment is technically feasible (with the same command as [above](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-pypi)), this approach is [discouraged](https://www.anaconda.com/blog/using-pip-in-a-conda-environment/), because pip does not interoperate with conda.
For a short summary about useful conda commands, see their [cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).
## Manually Downloading[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading "Permalink to this headline")
PySpark is included in the distributions available at the [Apache Spark website](https://spark.apache.org/downloads.html). You can download a distribution you want from the site. After that, uncompress the tar file into the directory where you want to install Spark, for example, as below:

```
tar xzvf spark-\ |release|\-bin-hadoop3.tgz

```
Copy to clipboard
Ensure the `SPARK_HOME` environment variable points to the directory where the tar file has been extracted. Update `PYTHONPATH` environment variable such that it can find the PySpark and Py4J under `SPARK_HOME/python/lib`. One example of doing this is shown below:

```
cd spark-\ |release|\-bin-hadoop3
export SPARK_HOME=`pwd`
export PYTHONPATH=$(ZIPS=("$SPARK_HOME"/python/lib/*.zip); IFS=:; echo "${ZIPS[*]}"):$PYTHONPATH

```
Copy to clipboard
## Installing from Source[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#installing-from-source "Permalink to this headline")
To install PySpark from source, refer to [Building Spark](https://spark.apache.org/docs/4.1.2/building-spark.html).
## Dependencies[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#dependencies "Permalink to this headline")
### Required dependencies[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#required-dependencies "Permalink to this headline")
PySpark requires the following dependencies.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| py4j  | >=0.10.9.9  | Required to interact with JVM  |
Additional libraries that enhance functionality but are not included in the installation packages:
  * **memory-profiler** : Used for PySpark UDF memory profiling, `spark.profile.show(...)` and `spark.sql.pyspark.udf.profiler`.
  * **plotly** : Used for PySpark plotting, `DataFrame.plot`.

Note that PySpark requires Java 17 or later with `JAVA_HOME` properly set and refer to [Downloading](https://spark.apache.org/docs/4.1.2/#downloading).
### Optional dependencies[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#optional-dependencies "Permalink to this headline")
PySpark has several optional dependencies that enhance its functionality for specific modules. These dependencies are only required for certain features and are not necessary for the basic functionality of PySpark. If these optional dependencies are not installed, PySpark will function correctly for basic operations but will raise an `ImportError` when you try to use features that require these dependencies.
#### Spark Connect[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#spark-connect "Permalink to this headline")
Installable with `pip install "pyspark[connect]"`.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| pandas  | >=2.2.0  | Required for Spark Connect  |
| pyarrow  | >=15.0.0  | Required for Spark Connect  |
| grpcio  | >=1.76.0  | Required for Spark Connect  |
| grpcio-status  | >=1.76.0  | Required for Spark Connect  |
| googleapis-common-protos  | >=1.71.0  | Required for Spark Connect  |
| zstandard  | >=0.25.0  | Required for Spark Connect  |
| graphviz  | >=0.20  | Optional for Spark Connect  |
#### Spark SQL[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#spark-sql "Permalink to this headline")
Installable with `pip install "pyspark[sql]"`.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| pandas  | >=2.2.0  | Required for Spark SQL  |
| pyarrow  | >=15.0.0  | Required for Spark SQL  |
Additional libraries that enhance functionality but are not included in the installation packages:
  * **flameprof** : Provide the default renderer for UDF performance profiling.

#### Pandas API on Spark[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#pandas-api-on-spark "Permalink to this headline")
Installable with `pip install "pyspark[pandas_on_spark]"`.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| pandas  | >=2.2.0  | Required for Pandas API on Spark  |
| pyarrow  | >=15.0.0  | Required for Pandas API on Spark  |
Additional libraries that enhance functionality but are not included in the installation packages:
  * **mlflow** : Required for `pyspark.pandas.mlflow`.
  * **plotly** : Provide plotting for visualization. It is recommended using **plotly** over **matplotlib**.
  * **matplotlib** : Provide plotting for visualization. The default is **plotly**.

#### MLlib DataFrame-based API[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#mllib-dataframe-based-api "Permalink to this headline")
Installable with `pip install "pyspark[ml]"`.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| numpy  | >=1.22  | Required for MLlib DataFrame-based API  |
Additional libraries that enhance functionality but are not included in the installation packages:
  * **scipy** : Required for SciPy integration.
  * **scikit-learn** : Required for implementing machine learning algorithms.
  * **torch** : Required for machine learning model training.
  * **torchvision** : Required for supporting image and video processing.
  * **torcheval** : Required for facilitating model evaluation metrics.
  * **deepspeed** : Required for providing high-performance model training optimizations. Installable on non-Darwin systems.

#### MLlib[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#mllib "Permalink to this headline")
Installable with `pip install "pyspark[mllib]"`.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| numpy  | >=1.22  | Required for MLlib  |
#### Declarative Pipelines[#](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#declarative-pipelines "Permalink to this headline")
Installable with `pip install "pyspark[pipelines]"`. Includes all dependencies for both Spark SQL and Spark Connect, because Declarative Pipelines is built on top of both.
| Package  | Supported version  | Note  |
| --- | --- | --- |
| pandas  | >=2.2.0  | Required for Spark Connect and Spark SQL  |
| pyarrow  | >=15.0.0  | Required for Spark Connect and Spark SQL  |
| grpcio  | >=1.76.0  | Required for Spark Connect  |
| grpcio-status  | >=1.76.0  | Required for Spark Connect  |
| googleapis-common-protos  | >=1.71.0  | Required for Spark Connect  |
| zstandard  | >=0.25.0  | Required for Spark Connect  |
| pyyaml  | >=3.11  | Required for spark-pipelines command line interface  |
| graphviz  | >=0.20  | Optional for Spark Connect  |
[ previous Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html "previous page") [ next Quickstart: DataFrame ](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html "next page")
On this page
  * [Python Versions Supported](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#python-versions-supported)
  * [Using PyPI](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-pypi)
    * [Making Spark Connect the default](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#making-spark-connect-the-default)
    * [Python Spark Connect Client](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#python-spark-connect-client)
  * [Using Conda](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#using-conda)
  * [Manually Downloading](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
  * [Installing from Source](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#installing-from-source)
  * [Dependencies](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#dependencies)
    * [Required dependencies](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#required-dependencies)
    * [Optional dependencies](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#optional-dependencies)
      * [Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#spark-connect)
      * [Spark SQL](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#spark-sql)
      * [Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#pandas-api-on-spark)
      * [MLlib DataFrame-based API](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#mllib-dataframe-based-api)
      * [MLlib](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#mllib)
      * [Declarative Pipelines](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#declarative-pipelines)

[ Show Source ](https://spark.apache.org/docs/latest/api/python/_sources/getting_started/install.rst.txt)
Copyright @ 2026 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Created using [Sphinx](https://www.sphinx-doc.org/) 4.5.0.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.13.3.
