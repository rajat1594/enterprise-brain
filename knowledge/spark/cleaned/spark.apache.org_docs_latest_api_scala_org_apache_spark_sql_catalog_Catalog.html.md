Spark 4.1.2 ScalaDoc < Back
 __ __
# Packages
  * [__](https://spark.apache.org/docs/latest/api/scala/index.html "Permalink") package [root](https://spark.apache.org/docs/latest/api/scala/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/index.html "Permalink") package [org](https://spark.apache.org/docs/latest/api/scala/org/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "Permalink") package [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html)

Definition Classes
    [org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink") package [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Core Spark functionality.")
Core Spark functionality.
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html "Permalink") package [catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html "Catalog interface for Spark.")[Catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html "Catalog interface for Spark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "A catalog in Spark, as returned by the listCatalogs method defined in Catalog.")[CatalogMetadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "A catalog in Spark, as returned by the listCatalogs method defined in Catalog.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "A column in Spark, as returned by listColumns method in Catalog.")[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "A column in Spark, as returned by listColumns method in Catalog.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "A database in Spark, as returned by the listDatabases method defined in Catalog.")[Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "A database in Spark, as returned by the listDatabases method defined in Catalog.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "A user-defined function in Spark, as returned by listFunctions method in Catalog.")[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "A user-defined function in Spark, as returned by listFunctions method in Catalog.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "A table in Spark, as returned by the listTables method in Catalog.")[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "A table in Spark, as returned by the listTables method in Catalog.")

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql").[catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html "org.apache.spark.sql.catalog")
# Catalog[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html "Permalink")
####  abstract  class Catalog extends AnyRef
Catalog interface for Spark. To access this, use `SparkSession.catalog`.

Annotations
     @Stable()

Source
    [Catalog.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/catalog/Catalog.scala)

Since

2.0.0
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. Catalog
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#<init>\(\):org.apache.spark.sql.catalog.Catalog "Permalink") new Catalog()

### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#cacheTable\(tableName:String,storageLevel:org.apache.spark.storage.StorageLevel\):Unit "Permalink") abstract  def cacheTable(tableName: String, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): Unit
Caches the specified table with the given storage level.
Caches the specified table with the given storage level.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

storageLevel

storage level to cache table.

Since

2.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#cacheTable\(tableName:String\):Unit "Permalink") abstract  def cacheTable(tableName: String): Unit
Caches the specified table in-memory.
Caches the specified table in-memory.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#clearCache\(\):Unit "Permalink") abstract  def clearCache(): Unit
Removes all cached tables from the in-memory cache.
Removes all cached tables from the in-memory cache.

Since

2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,description:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), description: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options.
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options.
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,description:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, description: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table based on the dataset in a data source and a set of options.
(Scala-specific) Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table based on the dataset in a data source and a set of options.
(Scala-specific) Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,path:String,source:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, path: String, source: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and returns the corresponding DataFrame.
Creates a table from the given path based on a data source and returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,path:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path and returns the corresponding DataFrame.
Creates a table from the given path and returns the corresponding DataFrame. It will use the default data source configured by spark.sql.sources.default.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#currentCatalog\(\):String "Permalink") abstract  def currentCatalog(): String
Returns the current catalog in this session.
Returns the current catalog in this session.

Since

3.4.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#currentDatabase:String "Permalink") abstract  def currentDatabase: String
Returns the current database (namespace) in this session.
Returns the current database (namespace) in this session.

Since

2.0.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#databaseExists\(dbName:String\):Boolean "Permalink") abstract  def databaseExists(dbName: String): Boolean
Check if the database (namespace) with the specified name exists (the name can be qualified with catalog).
Check if the database (namespace) with the specified name exists (the name can be qualified with catalog).

Since

2.1.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#dropGlobalTempView\(viewName:String\):Boolean "Permalink") abstract  def dropGlobalTempView(viewName: String): Boolean
Drops the global temporary view with the given view name in the catalog.
Drops the global temporary view with the given view name in the catalog. If the view has been cached before, then it will also be uncached.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.

viewName

the unqualified name of the temporary view to be dropped.

returns

true if the view is dropped successfully, false otherwise.

Since

2.1.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#dropTempView\(viewName:String\):Boolean "Permalink") abstract  def dropTempView(viewName: String): Boolean
Drops the local temporary view with the given view name in the catalog.
Drops the local temporary view with the given view name in the catalog. If the view has been cached before, then it will also be uncached.
Local temporary view is session-scoped. Its lifetime is the lifetime of the session that created it, i.e. it will be automatically dropped when the session terminates. It's not tied to any databases, i.e. we can't use `db1.view1` to reference a local temporary view.
Note that, the return type of this method was Unit in Spark 2.0, but changed to Boolean in Spark 2.1.

viewName

the name of the temporary view to be dropped.

returns

true if the view is dropped successfully, false otherwise.

Since

2.0.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#functionExists\(functionName:String\):Boolean "Permalink") abstract  def functionExists(functionName: String): Boolean
Check if the function with the specified name exists.
Check if the function with the specified name exists. This can either be a temporary function or a function.

functionName

is either a qualified or unqualified name that designates a function. It follows the same resolution rule with SQL: search for built-in/temp functions first then functions in the current database (namespace).

Since

2.1.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getDatabase\(dbName:String\):org.apache.spark.sql.catalog.Database "Permalink") abstract  def getDatabase(dbName: String): [Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")
Get the database (namespace) with the specified name (can be qualified with catalog).
Get the database (namespace) with the specified name (can be qualified with catalog). This throws an AnalysisException when the database (namespace) cannot be found.

Annotations
     @throws("database does not exist")

Since

2.1.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getFunction\(functionName:String\):org.apache.spark.sql.catalog.Function "Permalink") abstract  def getFunction(functionName: String): [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")
Get the function with the specified name.
Get the function with the specified name. This function can be a temporary function or a function. This throws an AnalysisException when the function cannot be found.

functionName

is either a qualified or unqualified name that designates a function. It follows the same resolution rule with SQL: search for built-in/temp functions first then functions in the current database (namespace).

Annotations
     @throws("function does not exist")

Since

2.1.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getTable\(tableName:String\):org.apache.spark.sql.catalog.Table "Permalink") abstract  def getTable(tableName: String): [Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")
Get the table or view with the specified name.
Get the table or view with the specified name. This table can be a temporary view or a table/view. This throws an AnalysisException when no Table can be found.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Annotations
     @throws("table does not exist")

Since

2.1.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#isCached\(tableName:String\):Boolean "Permalink") abstract  def isCached(tableName: String): Boolean
Returns true if the table is currently cached in-memory.
Returns true if the table is currently cached in-memory.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listCatalogs\(pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.CatalogMetadata\] "Permalink") abstract  def listCatalogs(pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[CatalogMetadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "org.apache.spark.sql.catalog.CatalogMetadata")]
Returns a list of catalogs which name match the specify pattern and available in this session.
Returns a list of catalogs which name match the specify pattern and available in this session.

Since

3.5.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listCatalogs\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.CatalogMetadata\] "Permalink") abstract  def listCatalogs(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[CatalogMetadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "org.apache.spark.sql.catalog.CatalogMetadata")]
Returns a list of catalogs available in this session.
Returns a list of catalogs available in this session.

Since

3.4.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listColumns\(tableName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Column\] "Permalink") abstract  def listColumns(tableName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "org.apache.spark.sql.catalog.Column")]
Returns a list of columns for the given table/view or temporary view.
Returns a list of columns for the given table/view or temporary view.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Annotations
     @throws("table does not exist")

Since

2.0.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listDatabases\(pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Database\] "Permalink") abstract  def listDatabases(pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")]
Returns a list of databases (namespaces) which name match the specify pattern and available within the current catalog.
Returns a list of databases (namespaces) which name match the specify pattern and available within the current catalog.

Since

3.5.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listDatabases\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Database\] "Permalink") abstract  def listDatabases(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")]
Returns a list of databases (namespaces) available within the current catalog.
Returns a list of databases (namespaces) available within the current catalog.

Since

2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(dbName:String,pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(dbName: String, pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog).
Returns a list of functions registered in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog). This includes all built-in and temporary functions.

Annotations
     @throws("database does not exist")

Since

3.5.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(dbName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(dbName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the specified database (namespace) (the name can be qualified with catalog).
Returns a list of functions registered in the specified database (namespace) (the name can be qualified with catalog). This includes all built-in and temporary functions.

Annotations
     @throws("database does not exist")

Since

2.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the current database (namespace).
Returns a list of functions registered in the current database (namespace). This includes all temporary functions.

Since

2.0.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(dbName:String,pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(dbName: String, pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog).
Returns a list of tables/views in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog). This includes all temporary views.

Annotations
     @throws("database does not exist")

Since

3.5.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(dbName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(dbName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the specified database (namespace) (the name can be qualified with catalog).
Returns a list of tables/views in the specified database (namespace) (the name can be qualified with catalog). This includes all temporary views.

Annotations
     @throws("database does not exist")

Since

2.0.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the current database (namespace).
Returns a list of tables/views in the current database (namespace). This includes all temporary views.

Since

2.0.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#recoverPartitions\(tableName:String\):Unit "Permalink") abstract  def recoverPartitions(tableName: String): Unit
Recovers all the partitions in the directory of a table and update the catalog.
Recovers all the partitions in the directory of a table and update the catalog. Only works with a partitioned table, and not a view.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.1.1
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#refreshByPath\(path:String\):Unit "Permalink") abstract  def refreshByPath(path: String): Unit
Invalidates and refreshes all the cached data (and the associated metadata) for any `Dataset` that contains the given data source path.
Invalidates and refreshes all the cached data (and the associated metadata) for any `Dataset` that contains the given data source path. Path matching is by checking for sub-directories, i.e. "/" would invalidate everything that is cached and "/test/parent" would invalidate everything that is a subdirectory of "/test/parent".

Since

2.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#refreshTable\(tableName:String\):Unit "Permalink") abstract  def refreshTable(tableName: String): Unit
Invalidates and refreshes all the cached data and metadata of the given table.
Invalidates and refreshes all the cached data and metadata of the given table. For performance reasons, Spark SQL or the external data source library it uses might cache certain metadata about a table, such as the location of blocks. When those change outside of Spark SQL, users should call this function to invalidate the cache.
If this table is cached as an InMemoryRelation, drop the original cached version and make the new version cached lazily.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#setCurrentCatalog\(catalogName:String\):Unit "Permalink") abstract  def setCurrentCatalog(catalogName: String): Unit
Sets the current catalog in this session.
Sets the current catalog in this session.

Since

3.4.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#setCurrentDatabase\(dbName:String\):Unit "Permalink") abstract  def setCurrentDatabase(dbName: String): Unit
Sets the current database (namespace) in this session.
Sets the current database (namespace) in this session.

Since

2.0.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#tableExists\(tableName:String\):Boolean "Permalink") abstract  def tableExists(tableName: String): Boolean
Check if the table or view with the specified name exists.
Check if the table or view with the specified name exists. This can either be a temporary view or a table/view.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Since

2.1.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#uncacheTable\(tableName:String\):Unit "Permalink") abstract  def uncacheTable(tableName: String): Unit
Removes the specified table from the in-memory cache.
Removes the specified table from the in-memory cache.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#functionExists\(dbName:String,functionName:String\):Boolean "Permalink") abstract  def functionExists(dbName: String, functionName: String): Boolean
Check if the function with the specified name exists in the specified database under the Hive Metastore.
Check if the function with the specified name exists in the specified database under the Hive Metastore.
To check existence of functions in other catalogs, please use `functionExists(functionName)` with qualified function name instead.

dbName

is an unqualified name that designates a database.

functionName

is an unqualified name that designates a function.

Annotations
     @deprecated

Deprecated

_(Since version 4.0.0)_ use functionExists(functionName: String) instead.

Since

2.1.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getFunction\(dbName:String,functionName:String\):org.apache.spark.sql.catalog.Function "Permalink") abstract  def getFunction(dbName: String, functionName: String): [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")
Get the function with the specified name in the specified database under the Hive Metastore.
Get the function with the specified name in the specified database under the Hive Metastore. This throws an AnalysisException when the function cannot be found.
To get functions in other catalogs, please use `getFunction(functionName)` with qualified function name instead.

dbName

is an unqualified name that designates a database.

functionName

is an unqualified name that designates a function in the specified database

Annotations
     @deprecated @throws("database or function does not exist")

Deprecated

_(Since version 4.0.0)_ use getFunction(functionName: String) instead.

Since

2.1.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getTable\(dbName:String,tableName:String\):org.apache.spark.sql.catalog.Table "Permalink") abstract  def getTable(dbName: String, tableName: String): [Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")
Get the table or view with the specified name in the specified database under the Hive Metastore.
Get the table or view with the specified name in the specified database under the Hive Metastore. This throws an AnalysisException when no Table can be found.
To get table/view in other catalogs, please use `getTable(tableName)` with qualified table/view name instead.

Annotations
     @deprecated @throws("database or table does not exist")

Deprecated

_(Since version 4.0.0)_ use getTable(tableName: String) instead.

Since

2.1.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listColumns\(dbName:String,tableName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Column\] "Permalink") abstract  def listColumns(dbName: String, tableName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "org.apache.spark.sql.catalog.Column")]
Returns a list of columns for the given table/view in the specified database under the Hive Metastore.
Returns a list of columns for the given table/view in the specified database under the Hive Metastore.
To list columns for table/view in other catalogs, please use `listColumns(tableName)` with qualified table/view name instead.

dbName

is an unqualified name that designates a database.

tableName

is an unqualified name that designates a table/view.

Annotations
     @deprecated @throws("database or table does not exist")

Deprecated

_(Since version 4.0.0)_ use listColumns(tableName: String) instead.

Since

2.0.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#tableExists\(dbName:String,tableName:String\):Boolean "Permalink") abstract  def tableExists(dbName: String, tableName: String): Boolean
Check if the table or view with the specified name exists in the specified database under the Hive Metastore.
Check if the table or view with the specified name exists in the specified database under the Hive Metastore.
To check existence of table/view in other catalogs, please use `tableExists(tableName)` with qualified table/view name instead.

dbName

is an unqualified name that designates a database.

tableName

is an unqualified name that designates a table.

Annotations
     @deprecated

Deprecated

_(Since version 4.0.0)_ use tableExists(tableName: String) instead.

Since

2.1.0

### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,description:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), description: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table based on the dataset in a data source, a schema and a set of options.
Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table based on the dataset in a data source, a schema and a set of options.
Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,description:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, description: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table based on the dataset in a data source and a set of options.
Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table based on the dataset in a data source and a set of options.
Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table from the given path based on a data source, a schema and a set of options.
(Scala-specific) Create a table from the given path based on a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table from the given path based on a data source, a schema and a set of options.
Create a table from the given path based on a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table from the given path based on a data source and a set of options.
(Scala-specific) Creates a table from the given path based on a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and a set of options.
Creates a table from the given path based on a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,path:String,source:String\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, path: String, source: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and returns the corresponding DataFrame.
Creates a table from the given path based on a data source and returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,path:String\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path and returns the corresponding DataFrame.
Creates a table from the given path and returns the corresponding DataFrame. It will use the default data source configured by spark.sql.sources.default.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Any
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#cacheTable\(tableName:String,storageLevel:org.apache.spark.storage.StorageLevel\):Unit "Permalink") abstract  def cacheTable(tableName: String, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): Unit
Caches the specified table with the given storage level.
Caches the specified table with the given storage level.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

storageLevel

storage level to cache table.

Since

2.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#cacheTable\(tableName:String\):Unit "Permalink") abstract  def cacheTable(tableName: String): Unit
Caches the specified table in-memory.
Caches the specified table in-memory.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#clearCache\(\):Unit "Permalink") abstract  def clearCache(): Unit
Removes all cached tables from the in-memory cache.
Removes all cached tables from the in-memory cache.

Since

2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,description:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), description: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options.
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options.
(Scala-specific) Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,description:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, description: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table based on the dataset in a data source and a set of options.
(Scala-specific) Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, source: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table based on the dataset in a data source and a set of options.
(Scala-specific) Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,path:String,source:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, path: String, source: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and returns the corresponding DataFrame.
Creates a table from the given path based on a data source and returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,path:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def createTable(tableName: String, path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path and returns the corresponding DataFrame.
Creates a table from the given path and returns the corresponding DataFrame. It will use the default data source configured by spark.sql.sources.default.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#currentCatalog\(\):String "Permalink") abstract  def currentCatalog(): String
Returns the current catalog in this session.
Returns the current catalog in this session.

Since

3.4.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#currentDatabase:String "Permalink") abstract  def currentDatabase: String
Returns the current database (namespace) in this session.
Returns the current database (namespace) in this session.

Since

2.0.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#databaseExists\(dbName:String\):Boolean "Permalink") abstract  def databaseExists(dbName: String): Boolean
Check if the database (namespace) with the specified name exists (the name can be qualified with catalog).
Check if the database (namespace) with the specified name exists (the name can be qualified with catalog).

Since

2.1.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#dropGlobalTempView\(viewName:String\):Boolean "Permalink") abstract  def dropGlobalTempView(viewName: String): Boolean
Drops the global temporary view with the given view name in the catalog.
Drops the global temporary view with the given view name in the catalog. If the view has been cached before, then it will also be uncached.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.

viewName

the unqualified name of the temporary view to be dropped.

returns

true if the view is dropped successfully, false otherwise.

Since

2.1.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#dropTempView\(viewName:String\):Boolean "Permalink") abstract  def dropTempView(viewName: String): Boolean
Drops the local temporary view with the given view name in the catalog.
Drops the local temporary view with the given view name in the catalog. If the view has been cached before, then it will also be uncached.
Local temporary view is session-scoped. Its lifetime is the lifetime of the session that created it, i.e. it will be automatically dropped when the session terminates. It's not tied to any databases, i.e. we can't use `db1.view1` to reference a local temporary view.
Note that, the return type of this method was Unit in Spark 2.0, but changed to Boolean in Spark 2.1.

viewName

the name of the temporary view to be dropped.

returns

true if the view is dropped successfully, false otherwise.

Since

2.0.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#functionExists\(functionName:String\):Boolean "Permalink") abstract  def functionExists(functionName: String): Boolean
Check if the function with the specified name exists.
Check if the function with the specified name exists. This can either be a temporary function or a function.

functionName

is either a qualified or unqualified name that designates a function. It follows the same resolution rule with SQL: search for built-in/temp functions first then functions in the current database (namespace).

Since

2.1.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getDatabase\(dbName:String\):org.apache.spark.sql.catalog.Database "Permalink") abstract  def getDatabase(dbName: String): [Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")
Get the database (namespace) with the specified name (can be qualified with catalog).
Get the database (namespace) with the specified name (can be qualified with catalog). This throws an AnalysisException when the database (namespace) cannot be found.

Annotations
     @throws("database does not exist")

Since

2.1.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getFunction\(functionName:String\):org.apache.spark.sql.catalog.Function "Permalink") abstract  def getFunction(functionName: String): [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")
Get the function with the specified name.
Get the function with the specified name. This function can be a temporary function or a function. This throws an AnalysisException when the function cannot be found.

functionName

is either a qualified or unqualified name that designates a function. It follows the same resolution rule with SQL: search for built-in/temp functions first then functions in the current database (namespace).

Annotations
     @throws("function does not exist")

Since

2.1.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getTable\(tableName:String\):org.apache.spark.sql.catalog.Table "Permalink") abstract  def getTable(tableName: String): [Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")
Get the table or view with the specified name.
Get the table or view with the specified name. This table can be a temporary view or a table/view. This throws an AnalysisException when no Table can be found.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Annotations
     @throws("table does not exist")

Since

2.1.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#isCached\(tableName:String\):Boolean "Permalink") abstract  def isCached(tableName: String): Boolean
Returns true if the table is currently cached in-memory.
Returns true if the table is currently cached in-memory.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listCatalogs\(pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.CatalogMetadata\] "Permalink") abstract  def listCatalogs(pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[CatalogMetadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "org.apache.spark.sql.catalog.CatalogMetadata")]
Returns a list of catalogs which name match the specify pattern and available in this session.
Returns a list of catalogs which name match the specify pattern and available in this session.

Since

3.5.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listCatalogs\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.CatalogMetadata\] "Permalink") abstract  def listCatalogs(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[CatalogMetadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/CatalogMetadata.html "org.apache.spark.sql.catalog.CatalogMetadata")]
Returns a list of catalogs available in this session.
Returns a list of catalogs available in this session.

Since

3.4.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listColumns\(tableName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Column\] "Permalink") abstract  def listColumns(tableName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "org.apache.spark.sql.catalog.Column")]
Returns a list of columns for the given table/view or temporary view.
Returns a list of columns for the given table/view or temporary view.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Annotations
     @throws("table does not exist")

Since

2.0.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listDatabases\(pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Database\] "Permalink") abstract  def listDatabases(pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")]
Returns a list of databases (namespaces) which name match the specify pattern and available within the current catalog.
Returns a list of databases (namespaces) which name match the specify pattern and available within the current catalog.

Since

3.5.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listDatabases\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Database\] "Permalink") abstract  def listDatabases(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Database](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Database.html "org.apache.spark.sql.catalog.Database")]
Returns a list of databases (namespaces) available within the current catalog.
Returns a list of databases (namespaces) available within the current catalog.

Since

2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(dbName:String,pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(dbName: String, pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog).
Returns a list of functions registered in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog). This includes all built-in and temporary functions.

Annotations
     @throws("database does not exist")

Since

3.5.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(dbName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(dbName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the specified database (namespace) (the name can be qualified with catalog).
Returns a list of functions registered in the specified database (namespace) (the name can be qualified with catalog). This includes all built-in and temporary functions.

Annotations
     @throws("database does not exist")

Since

2.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listFunctions\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Function\] "Permalink") abstract  def listFunctions(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")]
Returns a list of functions registered in the current database (namespace).
Returns a list of functions registered in the current database (namespace). This includes all temporary functions.

Since

2.0.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(dbName:String,pattern:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(dbName: String, pattern: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog).
Returns a list of tables/views in the specified database (namespace) which name match the specify pattern (the name can be qualified with catalog). This includes all temporary views.

Annotations
     @throws("database does not exist")

Since

3.5.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(dbName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(dbName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the specified database (namespace) (the name can be qualified with catalog).
Returns a list of tables/views in the specified database (namespace) (the name can be qualified with catalog). This includes all temporary views.

Annotations
     @throws("database does not exist")

Since

2.0.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listTables\(\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Table\] "Permalink") abstract  def listTables(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")]
Returns a list of tables/views in the current database (namespace).
Returns a list of tables/views in the current database (namespace). This includes all temporary views.

Since

2.0.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#recoverPartitions\(tableName:String\):Unit "Permalink") abstract  def recoverPartitions(tableName: String): Unit
Recovers all the partitions in the directory of a table and update the catalog.
Recovers all the partitions in the directory of a table and update the catalog. Only works with a partitioned table, and not a view.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.1.1
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#refreshByPath\(path:String\):Unit "Permalink") abstract  def refreshByPath(path: String): Unit
Invalidates and refreshes all the cached data (and the associated metadata) for any `Dataset` that contains the given data source path.
Invalidates and refreshes all the cached data (and the associated metadata) for any `Dataset` that contains the given data source path. Path matching is by checking for sub-directories, i.e. "/" would invalidate everything that is cached and "/test/parent" would invalidate everything that is a subdirectory of "/test/parent".

Since

2.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#refreshTable\(tableName:String\):Unit "Permalink") abstract  def refreshTable(tableName: String): Unit
Invalidates and refreshes all the cached data and metadata of the given table.
Invalidates and refreshes all the cached data and metadata of the given table. For performance reasons, Spark SQL or the external data source library it uses might cache certain metadata about a table, such as the location of blocks. When those change outside of Spark SQL, users should call this function to invalidate the cache.
If this table is cached as an InMemoryRelation, drop the original cached version and make the new version cached lazily.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#setCurrentCatalog\(catalogName:String\):Unit "Permalink") abstract  def setCurrentCatalog(catalogName: String): Unit
Sets the current catalog in this session.
Sets the current catalog in this session.

Since

3.4.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#setCurrentDatabase\(dbName:String\):Unit "Permalink") abstract  def setCurrentDatabase(dbName: String): Unit
Sets the current database (namespace) in this session.
Sets the current database (namespace) in this session.

Since

2.0.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#tableExists\(tableName:String\):Boolean "Permalink") abstract  def tableExists(tableName: String): Boolean
Check if the table or view with the specified name exists.
Check if the table or view with the specified name exists. This can either be a temporary view or a table/view.

tableName

is either a qualified or unqualified name that designates a table/view. It follows the same resolution rule with SQL: search for temp views first then table/views in the current database (namespace).

Since

2.1.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#uncacheTable\(tableName:String\):Unit "Permalink") abstract  def uncacheTable(tableName: String): Unit
Removes the specified table from the in-memory cache.
Removes the specified table from the in-memory cache.

tableName

is either a qualified or unqualified name that designates a table/view. If no database identifier is provided, it refers to a temporary view or a table/view in the current database.

Since

2.0.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#functionExists\(dbName:String,functionName:String\):Boolean "Permalink") abstract  def functionExists(dbName: String, functionName: String): Boolean
Check if the function with the specified name exists in the specified database under the Hive Metastore.
Check if the function with the specified name exists in the specified database under the Hive Metastore.
To check existence of functions in other catalogs, please use `functionExists(functionName)` with qualified function name instead.

dbName

is an unqualified name that designates a database.

functionName

is an unqualified name that designates a function.

Annotations
     @deprecated

Deprecated

_(Since version 4.0.0)_ use functionExists(functionName: String) instead.

Since

2.1.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getFunction\(dbName:String,functionName:String\):org.apache.spark.sql.catalog.Function "Permalink") abstract  def getFunction(dbName: String, functionName: String): [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Function.html "org.apache.spark.sql.catalog.Function")
Get the function with the specified name in the specified database under the Hive Metastore.
Get the function with the specified name in the specified database under the Hive Metastore. This throws an AnalysisException when the function cannot be found.
To get functions in other catalogs, please use `getFunction(functionName)` with qualified function name instead.

dbName

is an unqualified name that designates a database.

functionName

is an unqualified name that designates a function in the specified database

Annotations
     @deprecated @throws("database or function does not exist")

Deprecated

_(Since version 4.0.0)_ use getFunction(functionName: String) instead.

Since

2.1.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getTable\(dbName:String,tableName:String\):org.apache.spark.sql.catalog.Table "Permalink") abstract  def getTable(dbName: String, tableName: String): [Table](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Table.html "org.apache.spark.sql.catalog.Table")
Get the table or view with the specified name in the specified database under the Hive Metastore.
Get the table or view with the specified name in the specified database under the Hive Metastore. This throws an AnalysisException when no Table can be found.
To get table/view in other catalogs, please use `getTable(tableName)` with qualified table/view name instead.

Annotations
     @deprecated @throws("database or table does not exist")

Deprecated

_(Since version 4.0.0)_ use getTable(tableName: String) instead.

Since

2.1.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#listColumns\(dbName:String,tableName:String\):org.apache.spark.sql.Dataset\[org.apache.spark.sql.catalog.Column\] "Permalink") abstract  def listColumns(dbName: String, tableName: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Column.html "org.apache.spark.sql.catalog.Column")]
Returns a list of columns for the given table/view in the specified database under the Hive Metastore.
Returns a list of columns for the given table/view in the specified database under the Hive Metastore.
To list columns for table/view in other catalogs, please use `listColumns(tableName)` with qualified table/view name instead.

dbName

is an unqualified name that designates a database.

tableName

is an unqualified name that designates a table/view.

Annotations
     @deprecated @throws("database or table does not exist")

Deprecated

_(Since version 4.0.0)_ use listColumns(tableName: String) instead.

Since

2.0.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#tableExists\(dbName:String,tableName:String\):Boolean "Permalink") abstract  def tableExists(dbName: String, tableName: String): Boolean
Check if the table or view with the specified name exists in the specified database under the Hive Metastore.
Check if the table or view with the specified name exists in the specified database under the Hive Metastore.
To check existence of table/view in other catalogs, please use `tableExists(tableName)` with qualified table/view name instead.

dbName

is an unqualified name that designates a database.

tableName

is an unqualified name that designates a table.

Annotations
     @deprecated

Deprecated

_(Since version 4.0.0)_ use tableExists(tableName: String) instead.

Since

2.1.0
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,description:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), description: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table based on the dataset in a data source, a schema and a set of options.
Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table based on the dataset in a data source, a schema and a set of options.
Create a table based on the dataset in a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,description:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, description: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table based on the dataset in a data source and a set of options.
Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

3.1.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createTable\(tableName:String,source:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createTable(tableName: String, source: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table based on the dataset in a data source and a set of options.
Creates a table based on the dataset in a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Since

2.2.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Create a table from the given path based on a data source, a schema and a set of options.
(Scala-specific) Create a table from the given path based on a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,schema:org.apache.spark.sql.types.StructType,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType"), options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Create a table from the given path based on a data source, a schema and a set of options.
Create a table from the given path based on a data source, a schema and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,options:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, options: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Creates a table from the given path based on a data source and a set of options.
(Scala-specific) Creates a table from the given path based on a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,source:String,options:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, source: String, options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and a set of options.
Creates a table from the given path based on a data source and a set of options. Then, returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,path:String,source:String\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, path: String, source: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path based on a data source and returns the corresponding DataFrame.
Creates a table from the given path based on a data source and returns the corresponding DataFrame.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(tableName:String,path:String\):org.apache.spark.sql.DataFrame "Permalink") def createExternalTable(tableName: String, path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Creates a table from the given path and returns the corresponding DataFrame.
Creates a table from the given path and returns the corresponding DataFrame. It will use the default data source configured by spark.sql.sources.default.

tableName

is either a qualified or unqualified name that designates a table. If no database identifier is provided, it refers to a table in the current database.

Annotations
     @deprecated

Deprecated

_(Since version 2.2.0)_ use createTable instead.

Since

2.0.0
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/Catalog.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
