[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.sources
* * *
package org.apache.spark.sql.sources
  * Related Packages
Package
Description
[org.apache.spark.sql](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AlwaysFalse](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/AlwaysFalse.html "class in org.apache.spark.sql.sources")
A filter that always evaluates to `false`.
[AlwaysTrue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/AlwaysTrue.html "class in org.apache.spark.sql.sources")
A filter that always evaluates to `true`.
[And](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/And.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff both `left` or `right` evaluate to `true`.
[BaseRelation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/BaseRelation.html "class in org.apache.spark.sql.sources")
Represents a collection of tuples with a known schema.
[CatalystScan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CatalystScan.html "interface in org.apache.spark.sql.sources")
::Experimental:: An interface for experimenting with a more direct connection to the query planner.
[CollatedEqualNullSafe](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedEqualNullSafe.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`EqualNullSafe`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/EqualNullSafe.html "class in org.apache.spark.sql.sources").
[CollatedEqualTo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedEqualTo.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`EqualTo`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/EqualTo.html "class in org.apache.spark.sql.sources").
[CollatedFilter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedFilter.html "class in org.apache.spark.sql.sources")
Base class for collation aware string filters.
[CollatedGreaterThan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedGreaterThan.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`GreaterThan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/GreaterThan.html "class in org.apache.spark.sql.sources").
[CollatedGreaterThanOrEqual](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedGreaterThanOrEqual.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`GreaterThanOrEqual`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/GreaterThanOrEqual.html "class in org.apache.spark.sql.sources").
[CollatedIn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedIn.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`In`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/In.html "class in org.apache.spark.sql.sources").
[CollatedLessThan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedLessThan.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`LessThan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/LessThan.html "class in org.apache.spark.sql.sources").
[CollatedLessThanOrEqual](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedLessThanOrEqual.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`LessThanOrEqual`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/LessThanOrEqual.html "class in org.apache.spark.sql.sources").
[CollatedStringContains](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedStringContains.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`StringContains`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringContains.html "class in org.apache.spark.sql.sources").
[CollatedStringEndsWith](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedStringEndsWith.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`StringEndsWith`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringEndsWith.html "class in org.apache.spark.sql.sources").
[CollatedStringStartsWith](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CollatedStringStartsWith.html "class in org.apache.spark.sql.sources")
Collation aware equivalent of [`StringStartsWith`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringStartsWith.html "class in org.apache.spark.sql.sources").
[CreatableRelationProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/CreatableRelationProvider.html "interface in org.apache.spark.sql.sources")
[DataSourceRegister](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/DataSourceRegister.html "interface in org.apache.spark.sql.sources")
Data sources should implement this trait so that they can register an alias to their data source.
[EqualNullSafe](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/EqualNullSafe.html "class in org.apache.spark.sql.sources")
Performs equality comparison, similar to [`EqualTo`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/EqualTo.html "class in org.apache.spark.sql.sources").
[EqualTo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/EqualTo.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the column evaluates to a value equal to `value`.
[Filter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/Filter.html "class in org.apache.spark.sql.sources")
A filter predicate for data sources.
[GreaterThan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/GreaterThan.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a value greater than `value`.
[GreaterThanOrEqual](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/GreaterThanOrEqual.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a value greater than or equal to `value`.
[In](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/In.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to one of the values in the array.
[InsertableRelation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/InsertableRelation.html "interface in org.apache.spark.sql.sources")
A BaseRelation that can be used to insert data into it through the insert method.
[IsNotNull](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/IsNotNull.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a non-null value.
[IsNull](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/IsNull.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to null.
[LessThan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/LessThan.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a value less than `value`.
[LessThanOrEqual](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/LessThanOrEqual.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a value less than or equal to `value`.
[Not](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/Not.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff `child` is evaluated to `false`.
[Or](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/Or.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff at least one of `left` or `right` evaluates to `true`.
[PrunedFilteredScan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/PrunedFilteredScan.html "interface in org.apache.spark.sql.sources")
A BaseRelation that can eliminate unneeded columns and filter using selected predicates before producing an RDD containing all matching tuples as Row objects.
[PrunedScan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/PrunedScan.html "interface in org.apache.spark.sql.sources")
A BaseRelation that can eliminate unneeded columns before producing an RDD containing all of its tuples as Row objects.
[RelationProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/RelationProvider.html "interface in org.apache.spark.sql.sources")
Implemented by objects that produce relations for a specific kind of data source.
[SchemaRelationProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/SchemaRelationProvider.html "interface in org.apache.spark.sql.sources")
Implemented by objects that produce relations for a specific kind of data source with a given schema.
[StreamSinkProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StreamSinkProvider.html "interface in org.apache.spark.sql.sources")
::Experimental:: Implemented by objects that can produce a streaming `Sink` for a specific format or system.
[StreamSourceProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StreamSourceProvider.html "interface in org.apache.spark.sql.sources")
::Experimental:: Implemented by objects that can produce a streaming `Source` for a specific format or system.
[StringContains](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringContains.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a string that contains the string `value`.
[StringEndsWith](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringEndsWith.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a string that ends with `value`.
[StringStartsWith](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/StringStartsWith.html "class in org.apache.spark.sql.sources")
A filter that evaluates to `true` iff the attribute evaluates to a string that starts with `value`.
[SupportsStreamSourceMetadataColumns](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/SupportsStreamSourceMetadataColumns.html "interface in org.apache.spark.sql.sources")
Implemented by StreamSourceProvider objects that can generate file metadata columns.
[TableScan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/TableScan.html "interface in org.apache.spark.sql.sources")
A BaseRelation that can produce all of its tuples as an RDD of Row objects.


