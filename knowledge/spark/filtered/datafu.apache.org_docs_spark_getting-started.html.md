  * [Blog](https://datafu.apache.org/blog)


### [Apache DataFu™](https://datafu.apache.org/)
#### Getting Started
  * [Download](https://datafu.apache.org/docs/download.html)
  * [DataFu Spark](https://datafu.apache.org/docs/spark/getting-started.html)
  * [DataFu Pig](https://datafu.apache.org/docs/datafu/getting-started.html)
  * [DataFu Hourglass](https://datafu.apache.org/docs/hourglass/getting-started.html)


#### DataFu Spark Docs
  * [Guide](https://datafu.apache.org/docs/spark/guide.html)
  * [Scaladocs](https://datafu.apache.org/docs/spark/2.1.0/)


#### DataFu Pig Docs
  * [Guide](https://datafu.apache.org/docs/datafu/guide.html)
  * [Javadocs](https://datafu.apache.org/docs/datafu/1.6.1/)


#### DataFu Hourglass Docs
  * [Concepts](https://datafu.apache.org/docs/hourglass/concepts.html)
  * [Javadocs](https://datafu.apache.org/docs/hourglass/1.6.1/)


#### Community
  * [Mailing Lists](https://datafu.apache.org/community/mailing-lists.html)
  * [Contributing](https://datafu.apache.org/community/contributing.html)
  * [Issues](https://datafu.apache.org/community/issues.html)
  * [Wiki](https://cwiki.apache.org/confluence/display/DATAFU/DataFu+Home)


#### Apache Software Foundation
  * [Homepage](https://www.apache.org/)
  * [License](https://www.apache.org/licenses/)
  * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
  * [Security](https://www.apache.org/security/)
  * [Thanks](https://www.apache.org/foundation/thanks.html)


#### Getting Started
# DataFu Spark
Apache DataFu Spark is a collection of utils and user-defined functions for working with large scale data in [Apache Spark](http://spark.apache.org/).   
  

## Compatibility Matrix
This matrix represents versions of Spark that DataFu has been compiled and tested on. Some/many methods work on unsupported versions as well.   
  
  
| _DataFu_  | _Spark_  |  
| --- | --- |  
| 1.7.0  | 2.2.0 to 2.2.2, 2.3.0 to 2.3.2 and 2.4.0 to 2.4.3  |  
| 1.8.0  | 2.2.3, 2.3.3, and 2.4.4 to 2.4.5  |  
| 2.0.0  | 3.0.x - 3.1.x  |  
| 2.1.0  | 3.0.x - 3.4.2  |  
  

## Examples
A list of some of the things you can do with DataFu Spark is given below:
  * ["Dedup" a table](https://github.com/apache/datafu/blob/main/datafu-spark/src/main/scala/datafu/spark/SparkDFUtils.scala#L139) - remove duplicates based on a key and ordering (typically a date updated field, to get only the mostly recently updated record).
  * [Join a table with a numeric field with a table with a range](https://github.com/apache/datafu/blob/main/datafu-spark/src/main/scala/datafu/spark/SparkDFUtils.scala#L361)
  * [Do a skewed join between tables](https://github.com/apache/datafu/blob/main/datafu-spark/src/main/scala/datafu/spark/SparkDFUtils.scala#L274) (where the small table is still too big to fit in memory)
  * [Count distinct up to](https://github.com/apache/datafu/blob/main/datafu-spark/src/main/scala/datafu/spark/Aggregators.scala#L187) - an efficient implementation when you just want to verify that a certain minimum of distinct rows appear in a table
  * Call Python code from Spark Scala, or Scala code from PySpark


If you'd like to read more details about these functions, check out the [Guide](https://datafu.apache.org/docs/spark/guide.html). Otherwise if you are ready to get started using DataFu Spark, keep reading.
The rest of this page assumes you already have a built JAR available. If this is not the case, please see the [Download](https://datafu.apache.org/docs/download.html) page.
This jar should be loaded to the Spark class path. You can verify that you've done this correctly by trying to import one of our DataFu classes, for example, _DataFrameOps_.
## Basic Example: Finding the most recent update of a given record
A common scenario in data sent to the HDFS — the Hadoop Distributed File System — is multiple rows representing updates for the same logical data. For example, in a table representing accounts, a record might be written every time customer data is updated, with each update receiving a newer timestamp. Let’s consider the following simplified example.
  

Raw customers’ data, with more than one row per customer   

We can see that though most of the customers only appear once, _julia_ and _quentin_ have 2 and 3 rows, respectively. How can we get just the most recent record for each customer? We can use DataFu's _dedupWithOrder_ method.

```
import datafu.spark.DataFrameOps._

val customers = spark.read.format("csv").option("header", "true").load("customers.csv")

csv.dedupWithOrder($"id", $"date_updated".desc).show

```

Our result will be as expected — each customer only appears once, as you can see below:
  

“Deduplicated” data, with only the most recent record for each customer (though not in order)   

There are two additional variants of _dedupWithOrder_ in datafu-spark. The _dedupWithCombiner_ method has similar functionality to _dedupWithOrder_ , but uses a UDAF to utilize map side aggregation. _dedupTopN_ allows retaining more than one record for each key.
## Next Steps
Check out the [Guide](https://datafu.apache.org/docs/spark/guide.html) for more information on what you can do with DataFu Spark.
[![Apache Feather](https://datafu.apache.org/images/feather.png)](http://www.apache.org/)
Copyright © 2011-2025 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  
Apache DataFu, DataFu, Apache Pig, Apache Hadoop, Hadoop, Apache, and the Apache feather logo are either registered trademarks or trademarks of the [Apache Software Foundation](http://www.apache.org/) in the United States and other countries. 
