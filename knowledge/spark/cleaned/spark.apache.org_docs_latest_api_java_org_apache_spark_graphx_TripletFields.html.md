[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * [Package](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html)
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#class)

  * Summary:
  * Nested |
  * [Field](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#field-summary) |
  * [Constr](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#constructor-summary) |
  * [Method](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#method-summary)

  * Detail:
  * [Field](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#field-detail) |
  * [Constr](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#constructor-detail) |
  * Method

SEARCH:
Package [org.apache.spark.graphx](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html)
# Class TripletFields
[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
org.apache.spark.graphx.TripletFields

All Implemented Interfaces:
    `Serializable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")`
* * *
public class TripletFields extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")
Represents a subset of the fields of an [[EdgeTriplet]] or [[EdgeContext]]. This allows the system to populate only those fields for efficiency.

See Also:

  * [Serialized Form](https://spark.apache.org/docs/latest/api/java/serialized-form.html#org.apache.spark.graphx.TripletFields)

  * ## Field Summary
Fields
Modifier and Type
Field
Description
`static final TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")`
`All[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#All)`
Expose all the fields (source, edge, and destination).
`static final TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")`
`Dst[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#Dst)`
Expose the destination and edge fields but not the source field.
`static final TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")`
`EdgeOnly[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#EdgeOnly)`
Expose only the edge field and not the source or destination field.
`static final TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")`
`None[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#None)`
None of the triplet fields are exposed.
`static final TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")`
`Src[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#Src)`
Expose the source and edge fields but not the destination field.
`final boolean`
`useDst[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#useDst)`
Indicates whether the destination vertex attribute is included.
`final boolean`
`useEdge[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#useEdge)`
Indicates whether the edge attribute is included.
`final boolean`
`useSrc[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#useSrc)`
Indicates whether the source vertex attribute is included.
  * ## Constructor Summary
Constructors
Constructor
Description
`TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#%3Cinit%3E\(\))()`
Constructs a default TripletFields in which all fields are included.
`TripletFields[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html#%3Cinit%3E\(boolean,boolean,boolean\))(boolean useSrc,  boolean useDst,  boolean useEdge)`
  * ## Method Summary
### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
`equals[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), getClass[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), hashCode[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), notify[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), toString[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

  * ## Field Details
    * ### useSrc
public final boolean useSrc
Indicates whether the source vertex attribute is included.
    * ### useDst
public final boolean useDst
Indicates whether the destination vertex attribute is included.
    * ### useEdge
public final boolean useEdge
Indicates whether the edge attribute is included.
    * ### None
public static final [TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx") None
None of the triplet fields are exposed.
    * ### EdgeOnly
public static final [TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx") EdgeOnly
Expose only the edge field and not the source or destination field.
    * ### Src
public static final [TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx") Src
Expose the source and edge fields but not the destination field. (Same as Src)
    * ### Dst
public static final [TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx") Dst
Expose the destination and edge fields but not the source field. (Same as Dst)
    * ### All
public static final [TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx") All
Expose all the fields (source, edge, and destination).
  * ## Constructor Details
    * ### TripletFields
public TripletFields()
Constructs a default TripletFields in which all fields are included.
    * ### TripletFields
public TripletFields(boolean useSrc, boolean useDst, boolean useEdge)
