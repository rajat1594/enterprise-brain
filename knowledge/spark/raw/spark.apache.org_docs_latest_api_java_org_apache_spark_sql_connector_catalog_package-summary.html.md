[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.catalog
* * *
package org.apache.spark.sql.connector.catalog
  * Related Packages
Package
Description
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
[org.apache.spark.sql.connector.catalog.constraints](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/constraints/package-summary.html)
[org.apache.spark.sql.connector.catalog.functions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/package-summary.html)
[org.apache.spark.sql.connector.catalog.index](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/index/package-summary.html)
[org.apache.spark.sql.connector.catalog.procedures](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/procedures/package-summary.html)
  * All Classes and InterfacesInterfacesClassesEnum ClassesExceptions
Class
Description
[CatalogExtension](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogExtension.html "interface in org.apache.spark.sql.connector.catalog")
An API to extend the Spark built-in session catalog.
[CatalogNotFoundException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogNotFoundException.html "class in org.apache.spark.sql.connector.catalog")
[CatalogPlugin](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogPlugin.html "interface in org.apache.spark.sql.connector.catalog")
A marker interface to provide a catalog implementation for Spark.
[Catalogs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Catalogs.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.html "class in org.apache.spark.sql.connector.catalog")
Conversion helpers for working with v2 [`CatalogPlugin`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogPlugin.html "interface in org.apache.spark.sql.connector.catalog").
[CatalogV2Implicits.BucketSpecHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.BucketSpecHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.CatalogHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.CatalogHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.ClusterByHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.ClusterByHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.ColumnsHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.ColumnsHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.FunctionIdentifierHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.FunctionIdentifierHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.IdentifierHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.IdentifierHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.MultipartIdentifierHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.MultipartIdentifierHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.NamespaceHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.NamespaceHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.PartitionTypeHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.PartitionTypeHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.TableIdentifierHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.TableIdentifierHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Implicits.TransformHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Implicits.TransformHelper.html "class in org.apache.spark.sql.connector.catalog")
[CatalogV2Util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogV2Util.html "class in org.apache.spark.sql.connector.catalog")
[Column](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Column.html "interface in org.apache.spark.sql.connector.catalog")
An interface representing a column of a [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog").
[ColumnDefaultValue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ColumnDefaultValue.html "class in org.apache.spark.sql.connector.catalog")
A class representing the default value of a column.
[DefaultValue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/DefaultValue.html "class in org.apache.spark.sql.connector.catalog")
A class that represents default values.
[DelegatingCatalogExtension](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/DelegatingCatalogExtension.html "class in org.apache.spark.sql.connector.catalog")
A simple implementation of [`CatalogExtension`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/CatalogExtension.html "interface in org.apache.spark.sql.connector.catalog"), which implements all the catalog functions by calling the built-in session catalog directly.
[FunctionCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/FunctionCatalog.html "interface in org.apache.spark.sql.connector.catalog")
Catalog methods for working with Functions.
[Identifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Identifier.html "interface in org.apache.spark.sql.connector.catalog")
Identifies an object in a catalog.
[IdentityColumnSpec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/IdentityColumnSpec.html "class in org.apache.spark.sql.connector.catalog")
Identity column specification.
[LookupCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.html "interface in org.apache.spark.sql.connector.catalog")
A trait to encapsulate catalog lookup function and helpful extractors.
[LookupCatalog.AsTableIdentifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.AsTableIdentifier.html "class in org.apache.spark.sql.connector.catalog")
Extract legacy table identifier from a multi-part identifier.
[LookupCatalog.AsTableIdentifier$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.AsTableIdentifier$.html "class in org.apache.spark.sql.connector.catalog")
Extract legacy table identifier from a multi-part identifier.
[LookupCatalog.CatalogAndIdentifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.CatalogAndIdentifier.html "class in org.apache.spark.sql.connector.catalog")
Extract catalog and identifier from a multi-part name with the current catalog if needed.
[LookupCatalog.CatalogAndIdentifier$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.CatalogAndIdentifier$.html "class in org.apache.spark.sql.connector.catalog")
Extract catalog and identifier from a multi-part name with the current catalog if needed.
[LookupCatalog.CatalogAndNamespace](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.CatalogAndNamespace.html "class in org.apache.spark.sql.connector.catalog")
Extract catalog and namespace from a multi-part name with the current catalog if needed.
[LookupCatalog.CatalogAndNamespace$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.CatalogAndNamespace$.html "class in org.apache.spark.sql.connector.catalog")
Extract catalog and namespace from a multi-part name with the current catalog if needed.
[LookupCatalog.NonSessionCatalogAndIdentifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.NonSessionCatalogAndIdentifier.html "class in org.apache.spark.sql.connector.catalog")
Extract non-session catalog and identifier from a multi-part identifier.
[LookupCatalog.NonSessionCatalogAndIdentifier$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.NonSessionCatalogAndIdentifier$.html "class in org.apache.spark.sql.connector.catalog")
Extract non-session catalog and identifier from a multi-part identifier.
[LookupCatalog.SessionCatalogAndIdentifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.SessionCatalogAndIdentifier.html "class in org.apache.spark.sql.connector.catalog")
Extract session catalog and identifier from a multi-part identifier.
[LookupCatalog.SessionCatalogAndIdentifier$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/LookupCatalog.SessionCatalogAndIdentifier$.html "class in org.apache.spark.sql.connector.catalog")
Extract session catalog and identifier from a multi-part identifier.
[MetadataColumn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/MetadataColumn.html "interface in org.apache.spark.sql.connector.catalog")
Interface for a metadata column.
[NamespaceChange](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/NamespaceChange.html "interface in org.apache.spark.sql.connector.catalog")
NamespaceChange subclasses represent requested changes to a namespace.
[NamespaceChange.RemoveProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/NamespaceChange.RemoveProperty.html "class in org.apache.spark.sql.connector.catalog")
A NamespaceChange to remove a namespace property.
[NamespaceChange.SetProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/NamespaceChange.SetProperty.html "class in org.apache.spark.sql.connector.catalog")
A NamespaceChange to set a namespace property.
[ProcedureCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ProcedureCatalog.html "interface in org.apache.spark.sql.connector.catalog")
A catalog API for working with procedures.
[SessionConfigSupport](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SessionConfigSupport.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface for [`TableProvider`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableProvider.html "interface in org.apache.spark.sql.connector.catalog").
[StagedTable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagedTable.html "interface in org.apache.spark.sql.connector.catalog")
Represents a table which is staged for being committed to the metastore.
[StagingTableCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html "interface in org.apache.spark.sql.connector.catalog")
An optional mix-in for implementations of [`TableCatalog`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html "interface in org.apache.spark.sql.connector.catalog") that support staging creation of a table before committing the table's metadata along with its contents in CREATE TABLE AS SELECT or REPLACE TABLE AS SELECT operations.
[SupportsAtomicPartitionManagement](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsAtomicPartitionManagement.html "interface in org.apache.spark.sql.connector.catalog")
An atomic partition interface of [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog") to operate multiple partitions atomically.
[SupportsCatalogOptions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsCatalogOptions.html "interface in org.apache.spark.sql.connector.catalog")
An interface, which TableProviders can implement, to support table existence checks and creation through a catalog, without having to use table identifiers.
[SupportsDelete](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsDelete.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface for [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog") delete support.
[SupportsDeleteV2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsDeleteV2.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface for [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog") delete support.
[SupportsMetadataColumns](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsMetadataColumns.html "interface in org.apache.spark.sql.connector.catalog")
An interface for exposing data columns for a table that are not in the table schema.
[SupportsNamespaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsNamespaces.html "interface in org.apache.spark.sql.connector.catalog")
Catalog methods for working with namespaces.
[SupportsPartitionManagement](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsPartitionManagement.html "interface in org.apache.spark.sql.connector.catalog")
A partition interface of [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog").
[SupportsRead](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsRead.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface of [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog"), to indicate that it's readable.
[SupportsRowLevelOperations](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsRowLevelOperations.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface for [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog") row-level operations support.
[SupportsV1OverwriteWithSaveAsTable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsV1OverwriteWithSaveAsTable.html "interface in org.apache.spark.sql.connector.catalog")
A marker interface that can be mixed into a [`TableProvider`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableProvider.html "interface in org.apache.spark.sql.connector.catalog") to indicate that the data source needs to distinguish between DataFrameWriter V1 `saveAsTable` operations and DataFrameWriter V2 `createOrReplace`/`replace` operations.
[SupportsWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/SupportsWrite.html "interface in org.apache.spark.sql.connector.catalog")
A mix-in interface of [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog"), to indicate that it's writable.
[Table](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog")
An interface representing a logical structured data set of a data source.
[TableCapability](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCapability.html "enum class in org.apache.spark.sql.connector.catalog")
Capabilities that can be provided by a [`Table`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html "interface in org.apache.spark.sql.connector.catalog") implementation.
[TableCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html "interface in org.apache.spark.sql.connector.catalog")
Catalog methods for working with Tables.
[TableCatalogCapability](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalogCapability.html "enum class in org.apache.spark.sql.connector.catalog")
Capabilities that can be provided by a [`TableCatalog`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html "interface in org.apache.spark.sql.connector.catalog") implementation.
[TableChange](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.html "interface in org.apache.spark.sql.connector.catalog")
TableChange subclasses represent requested changes to a table.
[TableChange.AddColumn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.AddColumn.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to add a field.
[TableChange.AddConstraint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.AddConstraint.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to alter table and add a constraint.
[TableChange.After](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.After.html "class in org.apache.spark.sql.connector.catalog")
Column position AFTER means the specified column should be put after the given `column`.
[TableChange.ClusterBy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.ClusterBy.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to alter clustering columns for a table.
[TableChange.ColumnChange](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.ColumnChange.html "interface in org.apache.spark.sql.connector.catalog")
[TableChange.ColumnPosition](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.ColumnPosition.html "interface in org.apache.spark.sql.connector.catalog")
[TableChange.DeleteColumn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.DeleteColumn.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to delete a field.
[TableChange.DropConstraint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.DropConstraint.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to alter table and drop a constraint.
[TableChange.DropConstraint.Mode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.DropConstraint.Mode.html "enum class in org.apache.spark.sql.connector.catalog")
Defines modes for dropping a constraint.
[TableChange.First](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.First.html "class in org.apache.spark.sql.connector.catalog")
Column position FIRST means the specified column should be the first column.
[TableChange.RemoveProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.RemoveProperty.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to remove a table property.
[TableChange.RenameColumn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.RenameColumn.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to rename a field.
[TableChange.SetProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.SetProperty.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to set a table property.
[TableChange.UpdateColumnComment](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnComment.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to update the comment of a field.
[TableChange.UpdateColumnDefaultValue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnDefaultValue.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to update the default value of a field.
[TableChange.UpdateColumnNullability](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnNullability.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to update the nullability of a field.
[TableChange.UpdateColumnPosition](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnPosition.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to update the position of a field.
[TableChange.UpdateColumnType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnType.html "class in org.apache.spark.sql.connector.catalog")
A TableChange to update the type of a field.
[TableInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableInfo.html "class in org.apache.spark.sql.connector.catalog")
[TableInfo.Builder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableInfo.Builder.html "class in org.apache.spark.sql.connector.catalog")
[TableProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableProvider.html "interface in org.apache.spark.sql.connector.catalog")
The base interface for v2 data sources which don't have a real catalog.
[TableSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableSummary.html "interface in org.apache.spark.sql.connector.catalog")
[TableWritePrivilege](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableWritePrivilege.html "enum class in org.apache.spark.sql.connector.catalog")
The table write privileges that will be provided when loading a table.
[TruncatableTable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TruncatableTable.html "interface in org.apache.spark.sql.connector.catalog")
Represents a table which can be atomically truncated.
[V2TableUtil](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/V2TableUtil.html "class in org.apache.spark.sql.connector.catalog")
[V2TableWithV1Fallback](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/V2TableWithV1Fallback.html "interface in org.apache.spark.sql.connector.catalog")
A V2 table with V1 fallback support.
[View](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/View.html "interface in org.apache.spark.sql.connector.catalog")
An interface representing a persisted view.
[ViewCatalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ViewCatalog.html "interface in org.apache.spark.sql.connector.catalog")
Catalog methods for working with views.
[ViewChange](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ViewChange.html "interface in org.apache.spark.sql.connector.catalog")
ViewChange subclasses represent requested changes to a view.
[ViewChange.RemoveProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ViewChange.RemoveProperty.html "class in org.apache.spark.sql.connector.catalog")
[ViewChange.SetProperty](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ViewChange.SetProperty.html "class in org.apache.spark.sql.connector.catalog")
[ViewInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/ViewInfo.html "class in org.apache.spark.sql.connector.catalog")
A class that holds view information.


