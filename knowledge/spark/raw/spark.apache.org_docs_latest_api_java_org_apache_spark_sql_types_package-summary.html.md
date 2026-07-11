[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.types
* * *
package org.apache.spark.sql.types
  * Related Packages
Package
Description
[org.apache.spark.sql](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html)
  * All Classes and InterfacesInterfacesClassesAnnotation Interfaces
Class
Description
[AnyDataType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/AnyDataType.html "class in org.apache.spark.sql.types")
An `AbstractDataType` that matches any concrete data types.
[AnyTimestampType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/AnyTimestampType.html "class in org.apache.spark.sql.types")
[AnyTimestampTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/AnyTimestampTypeExpression.html "class in org.apache.spark.sql.types")
[ArrayType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ArrayType.html "class in org.apache.spark.sql.types")
[BinaryType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/BinaryType.html "class in org.apache.spark.sql.types")
The data type representing `Array[Byte]` values.
[BooleanType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/BooleanType.html "class in org.apache.spark.sql.types")
The data type representing `Boolean` values.
[BooleanTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/BooleanTypeExpression.html "class in org.apache.spark.sql.types")
[ByteExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ByteExactNumeric.html "class in org.apache.spark.sql.types")
[ByteType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ByteType.html "class in org.apache.spark.sql.types")
The data type representing `Byte` values.
[ByteTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ByteTypeExpression.html "class in org.apache.spark.sql.types")
[CalendarIntervalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/CalendarIntervalType.html "class in org.apache.spark.sql.types")
The data type representing calendar intervals.
[CharType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/CharType.html "class in org.apache.spark.sql.types")
[DataType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DataType.html "class in org.apache.spark.sql.types")
The base type of all Spark SQL data types.
[DataTypes](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DataTypes.html "class in org.apache.spark.sql.types")
To get/create specific data type, users should use singleton objects and factory methods provided by this class.
[DateType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DateType.html "class in org.apache.spark.sql.types")
The date type represents a valid date in the proleptic Gregorian calendar.
[DateTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DateTypeExpression.html "class in org.apache.spark.sql.types")
[DayTimeIntervalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DayTimeIntervalType.html "class in org.apache.spark.sql.types")
The type represents day-time intervals of the SQL standard.
[Decimal](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Decimal.html "class in org.apache.spark.sql.types")
A mutable implementation of BigDecimal that can hold a Long if values are small enough.
[Decimal.DecimalAsIfIntegral$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Decimal.DecimalAsIfIntegral$.html "class in org.apache.spark.sql.types")
A `Integral` evidence parameter for Decimals.
[Decimal.DecimalIsConflicted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Decimal.DecimalIsConflicted.html "interface in org.apache.spark.sql.types")
Common methods for Decimal evidence parameters
[Decimal.DecimalIsFractional$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Decimal.DecimalIsFractional$.html "class in org.apache.spark.sql.types")
A `Fractional` evidence parameter for Decimals.
[DecimalExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DecimalExactNumeric.html "class in org.apache.spark.sql.types")
[DecimalExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DecimalExpression.html "class in org.apache.spark.sql.types")
[DecimalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DecimalType.html "class in org.apache.spark.sql.types")
The data type representing `java.math.BigDecimal` values.
[DecimalType.Fixed$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DecimalType.Fixed$.html "class in org.apache.spark.sql.types")
[DoubleExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleExactNumeric.html "class in org.apache.spark.sql.types")
[DoubleType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleType.html "class in org.apache.spark.sql.types")
The data type representing `Double` values.
[DoubleType.DoubleAsIfIntegral](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleType.DoubleAsIfIntegral.html "interface in org.apache.spark.sql.types")
[DoubleType.DoubleAsIfIntegral$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleType.DoubleAsIfIntegral$.html "class in org.apache.spark.sql.types")
[DoubleType.DoubleIsConflicted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleType.DoubleIsConflicted.html "interface in org.apache.spark.sql.types")
[DoubleTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/DoubleTypeExpression.html "class in org.apache.spark.sql.types")
[EdgeInterpolationAlgorithm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/EdgeInterpolationAlgorithm.html "class in org.apache.spark.sql.types")
Edge interpolation algorithm for Geography logical type.
[EdgeInterpolationAlgorithm.SPHERICAL$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/EdgeInterpolationAlgorithm.SPHERICAL$.html "class in org.apache.spark.sql.types")
[FixedLength](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FixedLength.html "class in org.apache.spark.sql.types")
[FloatExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatExactNumeric.html "class in org.apache.spark.sql.types")
[FloatType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatType.html "class in org.apache.spark.sql.types")
The data type representing `Float` values.
[FloatType.FloatAsIfIntegral](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatType.FloatAsIfIntegral.html "interface in org.apache.spark.sql.types")
[FloatType.FloatAsIfIntegral$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatType.FloatAsIfIntegral$.html "class in org.apache.spark.sql.types")
[FloatType.FloatIsConflicted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatType.FloatIsConflicted.html "interface in org.apache.spark.sql.types")
[FloatTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/FloatTypeExpression.html "class in org.apache.spark.sql.types")
[Geography](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Geography.html "class in org.apache.spark.sql.types")
[GeographyType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/GeographyType.html "class in org.apache.spark.sql.types")
The data type representing GEOGRAPHY values which are spatial objects, as defined in the Open Geospatial Consortium (OGC) Simple Feature Access specification (https://portal.ogc.org/files/?artifact_id=25355), with a geographic coordinate system.
[Geometry](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Geometry.html "class in org.apache.spark.sql.types")
[GeometryType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/GeometryType.html "class in org.apache.spark.sql.types")
The data type representing GEOMETRY values which are spatial objects, as defined in the Open Geospatial Consortium (OGC) Simple Feature Access specification (https://portal.ogc.org/files/?artifact_id=25355), with a Cartesian coordinate system.
[IndeterminateStringType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/IndeterminateStringType.html "class in org.apache.spark.sql.types")
String type that was the result of coercing two different non-explicit collations.
[IntegerExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/IntegerExactNumeric.html "class in org.apache.spark.sql.types")
[IntegerType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/IntegerType.html "class in org.apache.spark.sql.types")
The data type representing `Int` values.
[IntegerTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/IntegerTypeExpression.html "class in org.apache.spark.sql.types")
[IntegralTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/IntegralTypeExpression.html "class in org.apache.spark.sql.types")
[LongExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/LongExactNumeric.html "class in org.apache.spark.sql.types")
[LongType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/LongType.html "class in org.apache.spark.sql.types")
The data type representing `Long` values.
[LongTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/LongTypeExpression.html "class in org.apache.spark.sql.types")
[MapType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/MapType.html "class in org.apache.spark.sql.types")
The data type for Maps.
[MaxLength](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/MaxLength.html "class in org.apache.spark.sql.types")
[Metadata](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Metadata.html "class in org.apache.spark.sql.types")
Metadata is a wrapper over Map[String, Any] that limits the value type to simple ones: Boolean, Long, Double, String, Metadata, Array[Boolean], Array[Long], Array[Double], Array[String], and Array[Metadata].
[MetadataBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/MetadataBuilder.html "class in org.apache.spark.sql.types")
Builder for [`Metadata`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/Metadata.html "class in org.apache.spark.sql.types").
[NoConstraint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/NoConstraint.html "class in org.apache.spark.sql.types")
[NullType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/NullType.html "class in org.apache.spark.sql.types")
The data type representing `NULL` values.
[NumericType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/NumericType.html "class in org.apache.spark.sql.types")
Numeric data types.
[NumericTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/NumericTypeExpression.html "class in org.apache.spark.sql.types")
[ObjectType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ObjectType.html "class in org.apache.spark.sql.types")
[ShortExactNumeric](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ShortExactNumeric.html "class in org.apache.spark.sql.types")
[ShortType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ShortType.html "class in org.apache.spark.sql.types")
The data type representing `Short` values.
[ShortTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/ShortTypeExpression.html "class in org.apache.spark.sql.types")
[SpatialType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/SpatialType.html "interface in org.apache.spark.sql.types")
[SQLUserDefinedType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/SQLUserDefinedType.html "annotation interface in org.apache.spark.sql.types")
::DeveloperApi:: A user-defined type which can be automatically recognized by a SQLContext and registered.
[StringConstraint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StringConstraint.html "interface in org.apache.spark.sql.types")
[StringHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StringHelper.html "class in org.apache.spark.sql.types")
[StringType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StringType.html "class in org.apache.spark.sql.types")
The data type representing `String` values.
[StringTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StringTypeExpression.html "class in org.apache.spark.sql.types")
[StructField](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StructField.html "class in org.apache.spark.sql.types")
A field inside a StructType.
[StructType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StructType.html "class in org.apache.spark.sql.types")
A [`StructType`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/StructType.html "class in org.apache.spark.sql.types") object can be constructed by
[TimestampNTZType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/TimestampNTZType.html "class in org.apache.spark.sql.types")
The timestamp without time zone type represents a local time in microsecond precision, which is independent of time zone.
[TimestampType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/TimestampType.html "class in org.apache.spark.sql.types")
The timestamp type represents a time instant in microsecond precision.
[TimestampTypeExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/TimestampTypeExpression.html "class in org.apache.spark.sql.types")
[TimeType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/TimeType.html "class in org.apache.spark.sql.types")
The time type represents a time value with fields hour, minute, second, up to microseconds.
[UDTRegistration](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/UDTRegistration.html "class in org.apache.spark.sql.types")
This object keeps the mappings between user classes and their User Defined Types (UDTs).
[UpCastRule](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/UpCastRule.html "class in org.apache.spark.sql.types")
Rule that defines which upcasts are allow in Spark.
[UserDefinedType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/UserDefinedType.html "class in org.apache.spark.sql.types")<UserType>
The data type for User Defined Types (UDTs).
[VarcharType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/VarcharType.html "class in org.apache.spark.sql.types")
[VariantType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/VariantType.html "class in org.apache.spark.sql.types")
The data type representing semi-structured values with arbitrary hierarchical data structures.
[YearMonthIntervalType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/YearMonthIntervalType.html "class in org.apache.spark.sql.types")
The type represents year-month intervals of the SQL standard.


