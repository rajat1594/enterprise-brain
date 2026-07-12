[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.attribute
* * *
package org.apache.spark.ml.attribute
## ML attributes
The ML pipeline API uses [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql")s as ML datasets. Each dataset consists of typed columns, e.g., string, double, vector, etc. However, knowing only the column type may not be sufficient to handle the data properly. For instance, a double column with values 0.0, 1.0, 2.0, ... may represent some label indices, which cannot be treated as numeric values in ML algorithms, and, for another instance, we may want to know the names and types of features stored in a vector column. ML attributes are used to provide additional information to describe columns in a dataset.
### ML columns
A column with ML attributes attached is called an ML column. The data in ML columns are stored as double values, i.e., an ML column is either a scalar column of double values or a vector column. Columns of other types must be encoded into ML columns using transformers. We use [`Attribute`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/Attribute.html "class in org.apache.spark.ml.attribute") to describe a scalar ML column, and [`AttributeGroup`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/AttributeGroup.html "class in org.apache.spark.ml.attribute") to describe a vector ML column. ML attributes are stored in the metadata field of the column schema.
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Attribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/Attribute.html "class in org.apache.spark.ml.attribute")
Abstract class for ML attributes.
[AttributeFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/AttributeFactory.html "interface in org.apache.spark.ml.attribute")
Trait for ML attribute factories.
[AttributeGroup](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/AttributeGroup.html "class in org.apache.spark.ml.attribute")
Attributes that describe a vector ML column.
[AttributeKeys](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/AttributeKeys.html "class in org.apache.spark.ml.attribute")
Keys used to store attributes.
[AttributeType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/AttributeType.html "class in org.apache.spark.ml.attribute")
An enum-like type for attribute types: `AttributeType$.Numeric`, `AttributeType$.Nominal`, and `AttributeType$.Binary`.
[BinaryAttribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/BinaryAttribute.html "class in org.apache.spark.ml.attribute")
A binary attribute.
[NominalAttribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/NominalAttribute.html "class in org.apache.spark.ml.attribute")
A nominal attribute.
[NumericAttribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/NumericAttribute.html "class in org.apache.spark.ml.attribute")
A numeric attribute with optional summary statistics.
[UnresolvedAttribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/UnresolvedAttribute.html "class in org.apache.spark.ml.attribute")
An unresolved attribute.
