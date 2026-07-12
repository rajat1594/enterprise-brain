[Skip navigation links](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/current/api/index.html)
  * [Package](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/class-use/Configuration.html)
  * [Tree](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/current/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/current/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/current/api/help-doc.html#class)


  * Summary: 
  * [Nested](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#nested-class-summary) | 
  * Field | 
  * [Constr](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#constructor-summary) | 
  * [Method](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#method-summary)


  * Detail: 
  * Field | 
  * [Constr](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#constructor-detail) | 
  * [Method](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#method-detail)


SEARCH:
Package [org.apache.hadoop.conf](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/package-summary.html)
# Class Configuration
[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
org.apache.hadoop.conf.Configuration 

All Implemented Interfaces:
     `Iterable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<Map.Entry[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`, `Writable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")` 

Direct Known Subclasses:
     `JobConf[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred")`, `YarnConfiguration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/yarn/conf/YarnConfiguration.html "class in org.apache.hadoop.yarn.conf")`
* * *
@Public @Stable public class Configuration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>, [Writable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")
Provides access to configuration parameters. 
## Resources
Configurations are specified by resources. A resource contains a set of name/value pairs as XML data. Each resource is named by either a `String` or by a [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs"). If named by a `String`, then the classpath is examined for a file with that name. If named by a `Path`, then the local filesystem is examined directly, without referring to the classpath. 
Unless explicitly turned off, Hadoop by default specifies two resources, loaded in-order from the classpath: 
  1. `    core-default.xml[](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/core-default.xml)`: Read-only defaults for hadoop.
  2. `core-site.xml`: Site-specific configuration for a given hadoop installation.

Applications may add additional resources, which are loaded subsequent to these resources in the order they are added. 
### Final Parameters
Configuration parameters may be declared _final_. Once a resource declares a value final, no subsequently-loaded resource can alter that value. For example, one might define a final parameter with: 

```

  <property>
    <name>dfs.hosts.include</name>
    <value>/etc/hadoop/conf/hosts.include</value>
    **<final>true</final>**
  </property>
```
Administrators typically define parameters as final in`core-site.xml` for values that user applications may not alter. 
### Variable Expansion
Value strings are first processed for _variable expansion_. The available properties are:
  1. Other properties defined in this Configuration; and, if a name is undefined here,
  2. Environment variables in [`System.getenv()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/System.html#getenv\(\) "class or interface in java.lang") if a name starts with "env.", or
  3. Properties in [`System.getProperties()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/System.html#getProperties\(\) "class or interface in java.lang").


For example, if a configuration resource contains the following property definitions: 

```

  <property>
    <name>basedir</name>
    <value>/user/${_user.name_}</value>
  </property>
  
  <property>
    <name>tempdir</name>
    <value>${_basedir_}/tmp</value>
  </property>

  <property>
    <name>otherdir</name>
    <value>${_env.BASE_DIR_}/other</value>
  </property>
  
```

When `conf.get("tempdir")` is called, then `${_basedir_}`will be resolved to another property in this Configuration, while`${ _user.name_}`would then ordinarily be resolved to the value of the System property with that name.
When `conf.get("otherdir")` is called, then `${_env.BASE_DIR_}`will be resolved to the value of the`${ _BASE_DIR_}`environment variable. It supports`${ _env.NAME:-default_}`and`${ _env.NAME-default_}`notations. The former is resolved to "default" if`${ _NAME_}`environment variable is undefined or its value is empty. The latter behaves the same way only if`${ _NAME_}`is undefined.
By default, warnings will be given to any deprecated configuration parameters and these are suppressible by configuring `log4j.logger.org.apache.hadoop.conf.Configuration.deprecation` in log4j.properties file. 
### Tags
Optionally we can tag related properties together by using tag attributes. System tags are defined by hadoop.tags.system property. Users can define there own custom tags in hadoop.tags.custom property. 
For example, we can tag existing property as: 

```

  <property>
    <name>dfs.replication</name>
    <value>3</value>
    <tag>HDFS,REQUIRED</tag>
  </property>

  <property>
    <name>dfs.data.transfer.protection</name>
    <value>3</value>
    <tag>HDFS,SECURITY</tag>
  </property>
 
```

Properties marked with tags can be retrieved with `conf  .getAllPropertiesByTag("HDFS")` or `conf.getAllPropertiesByTags  (Arrays.asList("YARN","SECURITY"))`.
  * ## Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class `
`org.apache.hadoop.conf.Configuration.DeprecationDelta`
A pending addition to the global set of deprecated keys.
`static class `
`org.apache.hadoop.conf.Configuration.IntegerRanges`
A class that represents a set of positive integer ranges.
  * ## Constructor Summary
Constructors
Constructor
Description
`Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#%3Cinit%3E\(\))()`
A new configuration.
`Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#%3Cinit%3E\(boolean\))(boolean loadDefaults)`
A new configuration where the behavior of reading from the default resources can be turned off.
`Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#%3Cinit%3E\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") other)`
A new configuration with the same settings cloned from another.
  * ## Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`addDefaultResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDefaultResource\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Add a default resource.
`static void`
`addDeprecation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newKey)`
Adds the deprecated key to the global deprecation map when no custom message is provided.
`static void`
`addDeprecation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String%5B%5D\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] newKeys)`
Deprecated.
use [`addDeprecation(String key, String newKey)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String\)) instead
`static void`
`addDeprecation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String%5B%5D,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] newKeys,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") customMessage)`
Deprecated.
use [`addDeprecation(String key, String newKey, String customMessage)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String,java.lang.String\)) instead
`static void`
`addDeprecation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newKey,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") customMessage)`
Adds the deprecated key to the global deprecation map.
`static void`
`addDeprecations[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecations\(org.apache.hadoop.conf.Configuration.DeprecationDelta%5B%5D\))(org.apache.hadoop.conf.Configuration.DeprecationDelta[] deltas)`
Adds a set of deprecated keys to the global deprecations.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.io.InputStream\))(InputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.io.InputStream,boolean\))(InputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in,  boolean restrictedParser)`
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.io.InputStream,java.lang.String\))(InputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.io.InputStream,java.lang.String,boolean\))(InputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  boolean restrictedParser)`
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.lang.String,boolean\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  boolean restrictedParser)`
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.net.URL\))(URL[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") url)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(java.net.URL,boolean\))(URL[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") url,  boolean restrictedParser)`
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file)`
Add a configuration resource.
`void`
`addResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addResource\(org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file,  boolean restrictedParser)`
`void`
`addTags[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addTags\(java.util.Properties\))(Properties[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util") prop)`
Add tags defined in HADOOP_TAGS_SYSTEM, HADOOP_TAGS_CUSTOM.
`void`
`clear[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#clear\(\))()`
Clears all keys from the configuration.
`static void`
`dumpConfiguration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#dumpConfiguration\(org.apache.hadoop.conf.Configuration,java.io.Writer\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config,  Writer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out)`
Writes out all properties and their attributes (final and resource) to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"), the format of the output would be,
`static void`
`dumpConfiguration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#dumpConfiguration\(org.apache.hadoop.conf.Configuration,java.lang.String,java.io.Writer\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName,  Writer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out)`
Writes properties and their attributes (final and resource) to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io").
`static void`
`dumpDeprecatedKeys[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#dumpDeprecatedKeys\(\))()`
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`get[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#get\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the value of the `name` property, `null` if no such property exists.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`get[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#get\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)`
Get the value of the `name`.
`Properties[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util")`
`getAllPropertiesByTag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getAllPropertiesByTag\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tag)`
Get all properties belonging to tag.
`Properties[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util")`
`getAllPropertiesByTags[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getAllPropertiesByTags\(java.util.List\))(List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> tagList)`
Get all properties belonging to list of input tags.
`boolean`
`getBoolean[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getBoolean\(java.lang.String,boolean\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  boolean defaultValue)`
Get the value of the `name` property as a `boolean`.
`Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>`
`getClass[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClass\(java.lang.String,java.lang.Class\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> defaultValue)`
Get the value of the `name` property as a `Class`.
`<U> Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends U>`
`getClass[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClass\(java.lang.String,java.lang.Class,java.lang.Class\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends U> defaultValue,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<U> xface)`
Get the value of the `name` property as a `Class` implementing the interface specified by `xface`.
`Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>`
`getClassByName[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClassByName\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Load a class by name.
`Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>`
`getClassByNameOrNull[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClassByNameOrNull\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Load a class by name, returning null rather than throwing an exception if it couldn't be loaded.
`Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>[]`
`getClasses[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClasses\(java.lang.String,java.lang.Class...\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>... defaultValue)`
Get the value of the `name` property as an array of `Class`.
`ClassLoader[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang")`
`getClassLoader[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getClassLoader\(\))()`
Get the [`ClassLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang") for this job.
`InputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io")`
`getConfResourceAsInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getConfResourceAsInputStream\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get an input stream attached to the configuration resource with the given `name`.
`Reader[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Reader.html "class or interface in java.io")`
`getConfResourceAsReader[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getConfResourceAsReader\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get a [`Reader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Reader.html "class or interface in java.io") attached to the configuration resource with the given `name`.
`double`
`getDouble[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getDouble\(java.lang.String,double\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  double defaultValue)`
Get the value of the `name` property as a `double`.
`<T extends Enum[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T>>  
T`
`getEnum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getEnum\(java.lang.String,T\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  T defaultValue)`
Return value matching this enumerated type.
`<E extends Enum[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<E>>  
EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<E>`
`getEnumSet[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getEnumSet\(java.lang.String,java.lang.Class,boolean\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<E> enumClass,  boolean ignoreUnknown)`
Build an enumset from a comma separated list of values.
`File[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html "class or interface in java.io")`
`getFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getFile\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dirsProp,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path)`
Get a local file name under a directory named in _dirsProp_ with the given _path_.
`Set[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`getFinalParameters[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getFinalParameters\(\))()`
Get the set of parameters marked final.
`float`
`getFloat[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getFloat\(java.lang.String,float\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  float defaultValue)`
Get the value of the `name` property as a `float`.
`<U> List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<U>`
`getInstances[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getInstances\(java.lang.String,java.lang.Class\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<U> xface)`
Get the value of the `name` property as a `List` of objects implementing the interface specified by `xface`.
`int`
`getInt[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getInt\(java.lang.String,int\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  int defaultValue)`
Get the value of the `name` property as an `int`.
`int[]`
`getInts[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getInts\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the value of the `name` property as a set of comma-delimited `int` values.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getLocalPath[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getLocalPath\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dirsProp,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path)`
Get a local file under a directory named by _dirsProp_ with the given _path_.
`long`
`getLong[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getLong\(java.lang.String,long\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long defaultValue)`
Get the value of the `name` property as a `long`.
`long`
`getLongBytes[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getLongBytes\(java.lang.String,long\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long defaultValue)`
Get the value of the `name` property as a `long` or human readable format.
`char[]`
`getPassword[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPassword\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the value for a known password configuration element.
`protected char[]`
`getPasswordFromConfig[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPasswordFromConfig\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Fallback to clear text passwords in configuration.
`char[]`
`getPasswordFromCredentialProviders[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPasswordFromCredentialProviders\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Try and resolve the provided element name as a credential provider alias.
`Pattern[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex")`
`getPattern[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPattern\(java.lang.String,java.util.regex.Pattern\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Pattern[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex") defaultValue)`
Get the value of the `name` property as a `Pattern`.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[]`
`getPropertySources[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPropertySources\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Gets information about why a property was set.
`protected Properties[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util")`
`getProps[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getProps\(\))()`
`Map[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`getPropsWithPrefix[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getPropsWithPrefix\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") confPrefix)`
Constructs a mapping of configuration and includes all properties that start with the specified configuration prefix.
`org.apache.hadoop.conf.Configuration.IntegerRanges`
`getRange[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getRange\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)`
Parse the given attribute as a set of integer ranges.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getRaw[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getRaw\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the value of the `name` property, without doing [variable expansion](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#VariableExpansion).If the key is deprecated, it returns the value of the first key which replaces the deprecated key and is not null.
`URL[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net")`
`getResource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getResource\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the [`URL`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") for the named resource.
`InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net")`
`getSocketAddr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getSocketAddr\(java.lang.String,java.lang.String,int\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddress,  int defaultPort)`
Get the socket address for `name` property as a `InetSocketAddress`.
`InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net")`
`getSocketAddr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getSocketAddr\(java.lang.String,java.lang.String,java.lang.String,int\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hostProperty,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") addressProperty,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddressValue,  int defaultPort)`
Get the socket address for `hostProperty` as a `InetSocketAddress`.
`double`
`getStorageSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStorageSize\(java.lang.String,double,org.apache.hadoop.conf.StorageUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  double defaultValue,  StorageUnit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") targetUnit)`
Gets storage size from a config file.
`double`
`getStorageSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStorageSize\(java.lang.String,java.lang.String,org.apache.hadoop.conf.StorageUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue,  StorageUnit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") targetUnit)`
Gets the Storage Size from the config, or returns the defaultValue.
`Collection[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`getStringCollection[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStringCollection\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the comma delimited values of the `name` property as a collection of `String`s.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[]`
`getStrings[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStrings\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the comma delimited values of the `name` property as an array of `String`s.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[]`
`getStrings[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStrings\(java.lang.String,java.lang.String...\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... defaultValue)`
Get the comma delimited values of the `name` property as an array of `String`s.
`long`
`getTimeDuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDuration\(java.lang.String,long,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long defaultValue,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)`
Return time duration in the given time unit.
`long`
`getTimeDuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDuration\(java.lang.String,long,java.util.concurrent.TimeUnit,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long defaultValue,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") defaultUnit,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") returnUnit)`
Return time duration in the given time unit.
`long`
`getTimeDuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDuration\(java.lang.String,java.lang.String,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)`
`long`
`getTimeDuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDuration\(java.lang.String,java.lang.String,java.util.concurrent.TimeUnit,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") defaultUnit,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") returnUnit)`
`long`
`getTimeDurationHelper[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDurationHelper\(java.lang.String,java.lang.String,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") vStr,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)`
Return time duration in the given time unit.
`long[]`
`getTimeDurations[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTimeDurations\(java.lang.String,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)`
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getTrimmed[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTrimmed\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the value of the `name` property as a trimmed `String`, `null` if no such property exists.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getTrimmed[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTrimmed\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)`
Get the value of the `name` property as a trimmed `String`, `defaultValue` if no such property exists.
`Collection[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`getTrimmedStringCollection[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTrimmedStringCollection\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the comma delimited values of the `name` property as a collection of `String`s, trimmed of the leading and trailing whitespace.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[]`
`getTrimmedStrings[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTrimmedStrings\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get the comma delimited values of the `name` property as an array of `String`s, trimmed of the leading and trailing whitespace.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[]`
`getTrimmedStrings[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getTrimmedStrings\(java.lang.String,java.lang.String...\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... defaultValue)`
Get the comma delimited values of the `name` property as an array of `String`s, trimmed of the leading and trailing whitespace.
`Map[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`getValByRegex[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getValByRegex\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") regex)`
get keys matching the the regex.
`static boolean`
`hasWarnedDeprecation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#hasWarnedDeprecation\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Returns whether or not a deprecated name has been warned.
`static boolean`
`isDeprecated[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#isDeprecated\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key)`
checks whether the given `key` is deprecated.
`boolean`
`isPropertyTag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#isPropertyTag\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tagStr)`
Get Property tag Enum corresponding to given source.
`Iterator[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<Map.Entry[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`
`iterator[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#iterator\(\))()`
Get an [`Iterator`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util") to go through the list of `String` key-value pairs in the configuration.
`static void`
`main[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#main\(java.lang.String%5B%5D\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] args)`
For debugging.
`boolean`
`onlyKeyExists[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#onlyKeyExists\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Return existence of the `name` property, but only for names which have no valid value, usually non-existent or commented out in XML.
`void`
`readFields[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#readFields\(java.io.DataInput\))(DataInput[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/DataInput.html "class or interface in java.io") in)`
Deserialize the fields of this object from `in`.
`void`
`reloadConfiguration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#reloadConfiguration\(\))()`
Reload configuration from previously added resources.
`static void`
`reloadExistingConfigurations[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#reloadExistingConfigurations\(\))()`
Reload existing configuration instances.
`void`
`set[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#set\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`
Set the `value` of the `name` property.
`void`
`set[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#set\(java.lang.String,java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") source)`
Set the `value` of the `name` property.
`void`
`setAllowNullValueProperties[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setAllowNullValueProperties\(boolean\))(boolean val)`
Set Configuration to allow keys without values during setup.
`void`
`setBoolean[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setBoolean\(java.lang.String,boolean\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  boolean value)`
Set the value of the `name` property to a `boolean`.
`void`
`setBooleanIfUnset[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setBooleanIfUnset\(java.lang.String,boolean\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  boolean value)`
Set the given property, if it is currently unset.
`void`
`setClass[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setClass\(java.lang.String,java.lang.Class,java.lang.Class\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> theClass,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> xface)`
Set the value of the `name` property to the name of a `theClass` implementing the given interface `xface`.
`void`
`setClassLoader[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setClassLoader\(java.lang.ClassLoader\))(ClassLoader[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang") classLoader)`
Set the class loader that will be used to load the various objects.
`void`
`setDeprecatedProperties[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setDeprecatedProperties\(\))()`
Sets all deprecated properties that are not currently set but have a corresponding new property that is set.
`void`
`setDouble[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setDouble\(java.lang.String,double\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  double value)`
Set the value of the `name` property to a `double`.
`<T extends Enum[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T>>  
void`
`setEnum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setEnum\(java.lang.String,T\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  T value)`
Set the value of the `name` property to the given type.
`void`
`setFloat[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setFloat\(java.lang.String,float\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  float value)`
Set the value of the `name` property to a `float`.
`void`
`setIfUnset[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setIfUnset\(java.lang.String,java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`
Sets a property if it is currently unset.
`void`
`setInt[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setInt\(java.lang.String,int\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  int value)`
Set the value of the `name` property to an `int`.
`void`
`setLong[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setLong\(java.lang.String,long\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long value)`
Set the value of the `name` property to a `long`.
`void`
`setPattern[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setPattern\(java.lang.String,java.util.regex.Pattern\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Pattern[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex") pattern)`
Set the given property to `Pattern`.
`void`
`setQuietMode[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setQuietMode\(boolean\))(boolean quietmode)`
Set the quietness-mode.
`void`
`setRestrictSystemProperties[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setRestrictSystemProperties\(boolean\))(boolean val)`
`static void`
`setRestrictSystemPropertiesDefault[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setRestrictSystemPropertiesDefault\(boolean\))(boolean val)`
`void`
`setRestrictSystemProps[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setRestrictSystemProps\(boolean\))(boolean val)`
`void`
`setSocketAddr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setSocketAddr\(java.lang.String,java.net.InetSocketAddress\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)`
Set the socket address for the `name` property as a `host:port`.
`void`
`setStorageSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setStorageSize\(java.lang.String,double,org.apache.hadoop.conf.StorageUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  double value,  StorageUnit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") unit)`
Sets Storage Size for the specified key.
`void`
`setStrings[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setStrings\(java.lang.String,java.lang.String...\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... values)`
Set the array of string values for the `name` property as as comma delimited values.
`void`
`setTimeDuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#setTimeDuration\(java.lang.String,long,java.util.concurrent.TimeUnit\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  long value,  TimeUnit[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)`
Set the value of `name` to the given time duration.
`int`
`size[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#size\(\))()`
Return the number of keys in the configuration.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`substituteCommonVariables[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#substituteCommonVariables\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") expr)`
Provides a public wrapper over substituteVars in order to avoid compatibility issues.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`toString[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#toString\(\))()`
`void`
`unset[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#unset\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Unset a previously set property.
`InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net")`
`updateConnectAddr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#updateConnectAddr\(java.lang.String,java.lang.String,java.lang.String,java.net.InetSocketAddress\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hostProperty,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") addressProperty,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddressValue,  InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)`
Set the socket address a client can use to connect for the `name` property as a `host:port`.
`InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net")`
`updateConnectAddr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#updateConnectAddr\(java.lang.String,java.net.InetSocketAddress\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  InetSocketAddress[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)`
Set the socket address a client can use to connect for the `name` property as a `host:port`.
`void`
`write[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#write\(java.io.DataOutput\))(DataOutput[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/DataOutput.html "class or interface in java.io") out)`
Serialize the fields of this object to `out`.
`void`
`writeXml[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#writeXml\(java.io.OutputStream\))(OutputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html "class or interface in java.io") out)`
Write out the non-default properties in this configuration to the given [`OutputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html "class or interface in java.io") using UTF-8 encoding.
`void`
`writeXml[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#writeXml\(java.io.Writer\))(Writer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out)`
`void`
`writeXml[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#writeXml\(java.lang.String,java.io.Writer\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName,  Writer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out)`
`void`
`writeXml[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#writeXml\(java.lang.String,java.io.Writer,org.apache.hadoop.conf.Configuration\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName,  Writer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config)`
Write out the non-default properties in this configuration to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io").
### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
`clone[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), equals[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), finalize[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), getClass[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), hashCode[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), notify[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`
### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")
`forEach[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach\(java.util.function.Consumer\) "class or interface in java.lang"), spliterator[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#spliterator\(\) "class or interface in java.lang")`


  * ## Constructor Details
    * ### Configuration
public Configuration()
A new configuration.
    * ### Configuration
public Configuration(boolean loadDefaults)
A new configuration where the behavior of reading from the default resources can be turned off. If the parameter `loadDefaults` is false, the new instance will not load resources from the default files. 

Parameters:
     `loadDefaults` - specifies whether to load from the default files
    * ### Configuration
public Configuration([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") other)
A new configuration with the same settings cloned from another. 

Parameters:
     `other` - the configuration from which to clone settings.
  * ## Method Details
    * ### addDeprecations
public static void addDeprecations(org.apache.hadoop.conf.Configuration.DeprecationDelta[] deltas)
Adds a set of deprecated keys to the global deprecations. This method is lockless. It works by means of creating a new DeprecationContext based on the old one, and then atomically swapping in the new context. If someone else updated the context in between us reading the old context and swapping in the new one, we try again until we win the race. 

Parameters:
     `deltas` - The deprecations to add.
    * ### addDeprecation
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static void addDeprecation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] newKeys, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") customMessage)
Deprecated.
use [`addDeprecation(String key, String newKey, String customMessage)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String,java.lang.String\)) instead
Adds the deprecated key to the global deprecation map. It does not override any existing entries in the deprecation map. This is to be used only by the developers in order to add deprecation of keys, and attempts to call this method after loading resources once, would lead to `UnsupportedOperationException` If a key is deprecated in favor of multiple keys, they are all treated as aliases of each other, and setting any one of them resets all the others to the new value. If you have multiple deprecation entries to add, it is more efficient to use #addDeprecations(DeprecationDelta[] deltas) instead. 

Parameters:
     `key` - to be deprecated      `newKeys` - list of keys that take up the values of deprecated key      `customMessage` - depcrication message
    * ### addDeprecation
public static void addDeprecation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") customMessage)
Adds the deprecated key to the global deprecation map. It does not override any existing entries in the deprecation map. This is to be used only by the developers in order to add deprecation of keys, and attempts to call this method after loading resources once, would lead to `UnsupportedOperationException` If you have multiple deprecation entries to add, it is more efficient to use #addDeprecations(DeprecationDelta[] deltas) instead. 

Parameters:
     `key` - to be deprecated      `newKey` - key that take up the values of deprecated key      `customMessage` - deprecation message
    * ### addDeprecation
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static void addDeprecation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] newKeys)
Deprecated.
use [`addDeprecation(String key, String newKey)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#addDeprecation\(java.lang.String,java.lang.String\)) instead
Adds the deprecated key to the global deprecation map when no custom message is provided. It does not override any existing entries in the deprecation map. This is to be used only by the developers in order to add deprecation of keys, and attempts to call this method after loading resources once, would lead to `UnsupportedOperationException` If a key is deprecated in favor of multiple keys, they are all treated as aliases of each other, and setting any one of them resets all the others to the new value. If you have multiple deprecation entries to add, it is more efficient to use #addDeprecations(DeprecationDelta[] deltas) instead. 

Parameters:
     `key` - Key that is to be deprecated      `newKeys` - list of keys that take up the values of deprecated key
    * ### addDeprecation
public static void addDeprecation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newKey)
Adds the deprecated key to the global deprecation map when no custom message is provided. It does not override any existing entries in the deprecation map. This is to be used only by the developers in order to add deprecation of keys, and attempts to call this method after loading resources once, would lead to `UnsupportedOperationException` If you have multiple deprecation entries to add, it is more efficient to use #addDeprecations(DeprecationDelta[] deltas) instead. 

Parameters:
     `key` - Key that is to be deprecated      `newKey` - key that takes up the value of deprecated key
    * ### isDeprecated
public static boolean isDeprecated([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key)
checks whether the given `key` is deprecated. 

Parameters:
     `key` - the parameter which is to be checked for deprecation 

Returns:
     `true` if the key is deprecated and `false` otherwise.
    * ### setDeprecatedProperties
public void setDeprecatedProperties()
Sets all deprecated properties that are not currently set but have a corresponding new property that is set. Useful for iterating the properties when all deprecated properties for currently set properties need to be present.
    * ### reloadExistingConfigurations
public static void reloadExistingConfigurations()
Reload existing configuration instances.
    * ### addDefaultResource
public static void addDefaultResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Add a default resource. Resources are loaded in the order of the resources added. 

Parameters:
     `name` - file name. File should be present in the classpath.
    * ### setRestrictSystemPropertiesDefault
public static void setRestrictSystemPropertiesDefault(boolean val)
    * ### setRestrictSystemProperties
public void setRestrictSystemProperties(boolean val)
    * ### addResource
public void addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). 

Parameters:
     `name` - resource to be added, the classpath is examined for a file with that name.
    * ### addResource
public void addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, boolean restrictedParser)
    * ### addResource
public void addResource([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") url)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). 

Parameters:
     `url` - url of the resource to be added, the local filesystem is examined directly to find the resource, without referring to the classpath.
    * ### addResource
public void addResource([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") url, boolean restrictedParser)
    * ### addResource
public void addResource([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). 

Parameters:
     `file` - file-path of resource to be added, the local filesystem is examined directly to find the resource, without referring to the classpath.
    * ### addResource
public void addResource([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file, boolean restrictedParser)
    * ### addResource
public void addResource([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). WARNING: The contents of the InputStream will be cached, by this method. So use this sparingly because it does increase the memory consumption. 

Parameters:
     `in` - InputStream to deserialize the object from. In will be read from when a get or set is called next. After it is read the stream will be closed.
    * ### addResource
public void addResource([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in, boolean restrictedParser)
    * ### addResource
public void addResource([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). 

Parameters:
     `in` - InputStream to deserialize the object from.      `name` - the name of the resource because InputStream.toString is not very descriptive some times.
    * ### addResource
public void addResource([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") in, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, boolean restrictedParser)
    * ### addResource
public void addResource([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)
Add a configuration resource. The properties of this resource will override properties of previously added resources, unless they were marked [final](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#Final). 

Parameters:
     `conf` - Configuration object from which to load properties
    * ### reloadConfiguration
public void reloadConfiguration()
Reload configuration from previously added resources. This method will clear all the configuration read from the added resources, and final parameters. This will make the resources to be read again before accessing the values. Values that are added via set methods will overlay values read from the resources.
    * ### substituteCommonVariables
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") substituteCommonVariables([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") expr)
Provides a public wrapper over substituteVars in order to avoid compatibility issues. See HADOOP-18021 for further details. 

Parameters:
     `expr` - the literal value of a config key 

Returns:
    null if expr is null, otherwise the value resulting from expanding expr using the algorithm above. 

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - when more than `MAX_SUBST` replacements are required
    * ### get
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the value of the `name` property, `null` if no such property exists. If the key is deprecated, it returns the value of the first key which replaces the deprecated key and is not null. Values are processed for [variable expansion](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#VariableExpansion) before being returned. As a side effect get loads the properties from the sources if called for the first time as a lazy init. 

Parameters:
     `name` - the property name, will be trimmed before get value. 

Returns:
    the value of the `name` or its replacing property, or null if no such property exists.
    * ### setAllowNullValueProperties
@VisibleForTesting public void setAllowNullValueProperties(boolean val)
Set Configuration to allow keys without values during setup. Intended for use during testing. 

Parameters:
     `val` - If true, will allow Configuration to store keys without values
    * ### setRestrictSystemProps
public void setRestrictSystemProps(boolean val)
    * ### onlyKeyExists
@VisibleForTesting public boolean onlyKeyExists([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Return existence of the `name` property, but only for names which have no valid value, usually non-existent or commented out in XML. 

Parameters:
     `name` - the property name 

Returns:
    true if the property `name` exists without value
    * ### getTrimmed
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getTrimmed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the value of the `name` property as a trimmed `String`, `null` if no such property exists. If the key is deprecated, it returns the value of the first key which replaces the deprecated key and is not null Values are processed for [variable expansion](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#VariableExpansion) before being returned. 

Parameters:
     `name` - the property name. 

Returns:
    the value of the `name` or its replacing property, or null if no such property exists.
    * ### getTrimmed
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getTrimmed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)
Get the value of the `name` property as a trimmed `String`, `defaultValue` if no such property exists. See @{Configuration#getTrimmed} for more details. 

Parameters:
     `name` - the property name.      `defaultValue` - the property default value. 

Returns:
    the value of the `name` or defaultValue if it is not set.
    * ### getRaw
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getRaw([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the value of the `name` property, without doing [variable expansion](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#VariableExpansion).If the key is deprecated, it returns the value of the first key which replaces the deprecated key and is not null. 

Parameters:
     `name` - the property name. 

Returns:
    the value of the `name` property or its replacing property and null if no such property exists.
    * ### set
public void set([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)
Set the `value` of the `name` property. If `name` is deprecated or there is a deprecated name associated to it, it sets the value to both names. Name will be trimmed before put into configuration. 

Parameters:
     `name` - property name.      `value` - property value.
    * ### set
public void set([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") source)
Set the `value` of the `name` property. If `name` is deprecated, it also sets the `value` to the keys that replace the deprecated key. Name will be trimmed before put into configuration. 

Parameters:
     `name` - property name.      `value` - property value.      `source` - the place that this configuration value came from (For debugging). 

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - when the value or name is null.
    * ### unset
public void unset([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Unset a previously set property. 

Parameters:
     `name` - the property name
    * ### setIfUnset
public void setIfUnset([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)
Sets a property if it is currently unset. 

Parameters:
     `name` - the property name      `value` - the new value
    * ### get
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)
Get the value of the `name`. If the key is deprecated, it returns the value of the first key which replaces the deprecated key and is not null. If no such property exists, then `defaultValue` is returned. 

Parameters:
     `name` - property name, will be trimmed before get value.      `defaultValue` - default value. 

Returns:
    property value, or `defaultValue` if the property doesn't exist.
    * ### getInt
public int getInt([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, int defaultValue)
Get the value of the `name` property as an `int`. If no such property exists, the provided default value is returned, or if the specified value is not a valid `int`, then an error is thrown. 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as an `int`, or `defaultValue`. 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - when the value is invalid
    * ### getInts
public int[] getInts([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the value of the `name` property as a set of comma-delimited `int` values. If no such property exists, an empty array is returned. 

Parameters:
     `name` - property name 

Returns:
    property value interpreted as an array of comma-delimited `int` values
    * ### setInt
public void setInt([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, int value)
Set the value of the `name` property to an `int`. 

Parameters:
     `name` - property name.      `value` - `int` value of the property.
    * ### getLong
public long getLong([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long defaultValue)
Get the value of the `name` property as a `long`. If no such property exists, the provided default value is returned, or if the specified value is not a valid `long`, then an error is thrown. 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as a `long`, or `defaultValue`. 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - when the value is invalid
    * ### getLongBytes
public long getLongBytes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long defaultValue)
Get the value of the `name` property as a `long` or human readable format. If no such property exists, the provided default value is returned, or if the specified value is not a valid `long` or human readable format, then an error is thrown. You can use the following suffix (case insensitive): k(kilo), m(mega), g(giga), t(tera), p(peta), e(exa) 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as a `long`, or `defaultValue`. 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - when the value is invalid
    * ### setLong
public void setLong([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long value)
Set the value of the `name` property to a `long`. 

Parameters:
     `name` - property name.      `value` - `long` value of the property.
    * ### getFloat
public float getFloat([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, float defaultValue)
Get the value of the `name` property as a `float`. If no such property exists, the provided default value is returned, or if the specified value is not a valid `float`, then an error is thrown. 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as a `float`, or `defaultValue`. 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - when the value is invalid
    * ### setFloat
public void setFloat([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, float value)
Set the value of the `name` property to a `float`. 

Parameters:
     `name` - property name.      `value` - property value.
    * ### getDouble
public double getDouble([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, double defaultValue)
Get the value of the `name` property as a `double`. If no such property exists, the provided default value is returned, or if the specified value is not a valid `double`, then an error is thrown. 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as a `double`, or `defaultValue`. 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - when the value is invalid
    * ### setDouble
public void setDouble([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, double value)
Set the value of the `name` property to a `double`. 

Parameters:
     `name` - property name.      `value` - property value.
    * ### getBoolean
public boolean getBoolean([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, boolean defaultValue)
Get the value of the `name` property as a `boolean`. If no such property is specified, or if the specified value is not a valid `boolean`, then `defaultValue` is returned. 

Parameters:
     `name` - property name.      `defaultValue` - default value. 

Returns:
    property value as a `boolean`, or `defaultValue`.
    * ### setBoolean
public void setBoolean([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, boolean value)
Set the value of the `name` property to a `boolean`. 

Parameters:
     `name` - property name.      `value` - `boolean` value of the property.
    * ### setBooleanIfUnset
public void setBooleanIfUnset([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, boolean value)
Set the given property, if it is currently unset. 

Parameters:
     `name` - property name      `value` - new value
    * ### setEnum
public <T extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T>> void setEnum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, T value)
Set the value of the `name` property to the given type. This is equivalent to `set(<name>, value.toString())`. 

Type Parameters:
     `T` - enumeration type 

Parameters:
     `name` - property name      `value` - new value
    * ### getEnum
public <T extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T>> T getEnum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, T defaultValue)
Return value matching this enumerated type. Note that the returned value is trimmed by this method. 

Type Parameters:
     `T` - enumeration type 

Parameters:
     `name` - Property name      `defaultValue` - Value returned if no mapping exists 

Returns:
    enumeration type 

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - If mapping is illegal for the type provided
    * ### getEnumSet
public <E extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<E>> [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<E> getEnumSet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<E> enumClass, boolean ignoreUnknown) throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")
Build an enumset from a comma separated list of values. Case independent. Special handling of "*" meaning: all values. 

Type Parameters:
     `E` - enumeration type 

Parameters:
     `key` - key to look for      `enumClass` - class of enum      `ignoreUnknown` - should unknown values raise an exception? 

Returns:
    a mutable set of the identified enum values declared in the configuration 

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - if one of the entries was unknown and ignoreUnknown is false, or there are two entries in the enum which differ only by case.
    * ### setTimeDuration
public void setTimeDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long value, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)
Set the value of `name` to the given time duration. This is equivalent to `set(<name>, value + <time suffix>)`. 

Parameters:
     `name` - Property name      `value` - Time duration      `unit` - Unit of time
    * ### getTimeDuration
public long getTimeDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long defaultValue, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)
Return time duration in the given time unit. Valid units are encoded in properties as suffixes: nanoseconds (ns), microseconds (us), milliseconds (ms), seconds (s), minutes (m), hours (h), and days (d). 

Parameters:
     `name` - Property name      `defaultValue` - Value returned if no mapping exists.      `unit` - Unit to convert the stored property, if it exists. 

Returns:
    time duration in given time unit 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - If the property stripped of its unit is not a number
    * ### getTimeDuration
public long getTimeDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)
    * ### getTimeDuration
public long getTimeDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, long defaultValue, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") defaultUnit, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") returnUnit)
Return time duration in the given time unit. Valid units are encoded in properties as suffixes: nanoseconds (ns), microseconds (us), milliseconds (ms), seconds (s), minutes (m), hours (h), and days (d). If no unit is provided, the default unit is applied. 

Parameters:
     `name` - Property name      `defaultValue` - Value returned if no mapping exists.      `defaultUnit` - Default time unit if no valid suffix is provided.      `returnUnit` - The unit used for the returned value. 

Returns:
    time duration in given time unit 

Throws:
     `NumberFormatException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html "class or interface in java.lang")` - If the property stripped of its unit is not a number
    * ### getTimeDuration
public long getTimeDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") defaultUnit, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") returnUnit)
    * ### getTimeDurationHelper
public long getTimeDurationHelper([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") vStr, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)
Return time duration in the given time unit. Valid units are encoded in properties as suffixes: nanoseconds (ns), microseconds (us), milliseconds (ms), seconds (s), minutes (m), hours (h), and days (d). 

Parameters:
     `name` - Property name      `vStr` - The string value with time unit suffix to be converted.      `unit` - Unit to convert the stored property, if it exists. 

Returns:
    time duration in given time unit.
    * ### getTimeDurations
public long[] getTimeDurations([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [TimeUnit](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/TimeUnit.html "class or interface in java.util.concurrent") unit)
    * ### getStorageSize
public double getStorageSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue, [StorageUnit](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") targetUnit)
Gets the Storage Size from the config, or returns the defaultValue. The unit of return value is specified in target unit. 

Parameters:
     `name` - - Key Name      `defaultValue` - - Default Value -- e.g. 100MB      `targetUnit` - - The units that we want result to be in. 

Returns:
    double -- formatted in target Units
    * ### getStorageSize
public double getStorageSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, double defaultValue, [StorageUnit](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") targetUnit)
Gets storage size from a config file. 

Parameters:
     `name` - - Key to read.      `defaultValue` - - The default value to return in case the key is not present.      `targetUnit` - - The Storage unit that should be used for the return value. 

Returns:
    - double value in the Storage Unit specified.
    * ### setStorageSize
public void setStorageSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, double value, [StorageUnit](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/StorageUnit.html "enum class in org.apache.hadoop.conf") unit)
Sets Storage Size for the specified key. 

Parameters:
     `name` - - Key to set.      `value` - - The numeric value to set.      `unit` - - Storage Unit to be used.
    * ### getPattern
public [Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex") getPattern([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex") defaultValue)
Get the value of the `name` property as a `Pattern`. If no such property is specified, or if the specified value is not a valid `Pattern`, then `DefaultValue` is returned. Note that the returned value is NOT trimmed by this method. 

Parameters:
     `name` - property name      `defaultValue` - default value 

Returns:
    property value as a compiled Pattern, or defaultValue
    * ### setPattern
public void setPattern([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "class or interface in java.util.regex") pattern)
Set the given property to `Pattern`. If the pattern is passed as null, sets the empty pattern which results in further calls to getPattern(...) returning the default value. 

Parameters:
     `name` - property name      `pattern` - new value
    * ### getPropertySources
@Unstable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] getPropertySources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Gets information about why a property was set. Typically this is the path to the resource objects (file, URL, etc.) the property came from, but it can also indicate that it was set programmatically, or because of the command line. 

Parameters:
     `name` - - The property name to get the source of. 

Returns:
    null - If the property or its source wasn't found. Otherwise, returns a list of the sources of the resource. The older sources are the first ones in the list. So for example if a configuration is set from the command line, and then written out to a file that is read back in the first entry would indicate that it was set from the command line, while the second one would indicate the file that the new configuration was read in from.
    * ### getRange
public org.apache.hadoop.conf.Configuration.IntegerRanges getRange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultValue)
Parse the given attribute as a set of integer ranges. 

Parameters:
     `name` - the attribute name      `defaultValue` - the default value if it is not set 

Returns:
    a new set of ranges from the configured value
    * ### getStringCollection
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getStringCollection([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the comma delimited values of the `name` property as a collection of `String`s. If no such property is specified then empty collection is returned. 
This is an optimized version of [`getStrings(String)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#getStrings\(java.lang.String\)) 

Parameters:
     `name` - property name. 

Returns:
    property value as a collection of `String`s.
    * ### getStrings
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] getStrings([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the comma delimited values of the `name` property as an array of `String`s. If no such property is specified then `null` is returned. 

Parameters:
     `name` - property name. 

Returns:
    property value as an array of `String`s, or `null`.
    * ### getStrings
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] getStrings([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... defaultValue)
Get the comma delimited values of the `name` property as an array of `String`s. If no such property is specified then default value is returned. 

Parameters:
     `name` - property name.      `defaultValue` - The default value 

Returns:
    property value as an array of `String`s, or default value.
    * ### getTrimmedStringCollection
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getTrimmedStringCollection([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the comma delimited values of the `name` property as a collection of `String`s, trimmed of the leading and trailing whitespace. If no such property is specified then empty `Collection` is returned. 

Parameters:
     `name` - property name. 

Returns:
    property value as a collection of `String`s, or empty `Collection`
    * ### getTrimmedStrings
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] getTrimmedStrings([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the comma delimited values of the `name` property as an array of `String`s, trimmed of the leading and trailing whitespace. If no such property is specified then an empty array is returned. 

Parameters:
     `name` - property name. 

Returns:
    property value as an array of trimmed `String`s, or empty array.
    * ### getTrimmedStrings
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] getTrimmedStrings([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... defaultValue)
Get the comma delimited values of the `name` property as an array of `String`s, trimmed of the leading and trailing whitespace. If no such property is specified then default value is returned. 

Parameters:
     `name` - property name.      `defaultValue` - The default value 

Returns:
    property value as an array of trimmed `String`s, or default value.
    * ### setStrings
public void setStrings([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")... values)
Set the array of string values for the `name` property as as comma delimited values. 

Parameters:
     `name` - property name.      `values` - The values
    * ### getPassword
public char[] getPassword([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get the value for a known password configuration element. In order to enable the elimination of clear text passwords in config, this method attempts to resolve the property name as an alias through the CredentialProvider API and conditionally fallsback to config. 

Parameters:
     `name` - property name 

Returns:
    password 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - when error in fetching password
    * ### getPasswordFromCredentialProviders
public char[] getPasswordFromCredentialProviders([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Try and resolve the provided element name as a credential provider alias. 

Parameters:
     `name` - alias of the provisioned credential 

Returns:
    password or null if not found 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - when error in fetching password
    * ### getPasswordFromConfig
protected char[] getPasswordFromConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Fallback to clear text passwords in configuration. 

Parameters:
     `name` - the property name. 

Returns:
    clear text password or null
    * ### getSocketAddr
public [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") getSocketAddr([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hostProperty, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") addressProperty, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddressValue, int defaultPort)
Get the socket address for `hostProperty` as a `InetSocketAddress`. If `hostProperty` is `null`, `addressProperty` will be used. This is useful for cases where we want to differentiate between host bind address and address clients should use to establish connection. 

Parameters:
     `hostProperty` - bind host property name.      `addressProperty` - address property name.      `defaultAddressValue` - the default value      `defaultPort` - the default port 

Returns:
    InetSocketAddress
    * ### getSocketAddr
public [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") getSocketAddr([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddress, int defaultPort)
Get the socket address for `name` property as a `InetSocketAddress`. 

Parameters:
     `name` - property name.      `defaultAddress` - the default value      `defaultPort` - the default port 

Returns:
    InetSocketAddress
    * ### setSocketAddr
public void setSocketAddr([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)
Set the socket address for the `name` property as a `host:port`. 

Parameters:
     `name` - property name.      `addr` - inetSocketAddress addr.
    * ### updateConnectAddr
public [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") updateConnectAddr([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hostProperty, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") addressProperty, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") defaultAddressValue, [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)
Set the socket address a client can use to connect for the `name` property as a `host:port`. The wildcard address is replaced with the local host's address. If the host and address properties are configured the host component of the address will be combined with the port component of the addr to generate the address. This is to allow optional control over which host name is used in multi-home bind-host cases where a host can have multiple names 

Parameters:
     `hostProperty` - the bind-host configuration name      `addressProperty` - the service address configuration name      `defaultAddressValue` - the service default address configuration value      `addr` - InetSocketAddress of the service listener 

Returns:
    InetSocketAddress for clients to connect
    * ### updateConnectAddr
public [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") updateConnectAddr([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [InetSocketAddress](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetSocketAddress.html "class or interface in java.net") addr)
Set the socket address a client can use to connect for the `name` property as a `host:port`. The wildcard address is replaced with the local host's address. 

Parameters:
     `name` - property name.      `addr` - InetSocketAddress of a listener to store in the given property 

Returns:
    InetSocketAddress for clients to connect
    * ### getClassByName
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> getClassByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name) throws [ClassNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassNotFoundException.html "class or interface in java.lang")
Load a class by name. 

Parameters:
     `name` - the class name. 

Returns:
    the class object. 

Throws:
     `ClassNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassNotFoundException.html "class or interface in java.lang")` - if the class is not found.
    * ### getClassByNameOrNull
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> getClassByNameOrNull([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Load a class by name, returning null rather than throwing an exception if it couldn't be loaded. This is to avoid the overhead of creating an exception. 

Parameters:
     `name` - the class name 

Returns:
    the class object, or null if it could not be found.
    * ### getClasses
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>[] getClasses([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?>... defaultValue)
Get the value of the `name` property as an array of `Class`. The value of the property specifies a list of comma separated class names. If no such property is specified, then `defaultValue` is returned. 

Parameters:
     `name` - the property name.      `defaultValue` - default value. 

Returns:
    property value as a `Class[]`, or `defaultValue`.
    * ### getClass
public [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> getClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> defaultValue)
Get the value of the `name` property as a `Class`. If no such property is specified, then `defaultValue` is returned. 

Parameters:
     `name` - the conf key name.      `defaultValue` - default value. 

Returns:
    property value as a `Class`, or `defaultValue`.
    * ### getClass
public <U> [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends U> getClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends U> defaultValue, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<U> xface)
Get the value of the `name` property as a `Class` implementing the interface specified by `xface`. If no such property is specified, then `defaultValue` is returned. An exception is thrown if the returned class does not implement the named interface. 

Type Parameters:
     `U` - Interface class type. 

Parameters:
     `name` - the conf key name.      `defaultValue` - default value.      `xface` - the interface implemented by the named class. 

Returns:
    property value as a `Class`, or `defaultValue`.
    * ### getInstances
public <U> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<U> getInstances([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<U> xface)
Get the value of the `name` property as a `List` of objects implementing the interface specified by `xface`. An exception is thrown if any of the classes does not exist, or if it does not implement the named interface. 

Type Parameters:
     `U` - Interface class type. 

Parameters:
     `name` - the property name.      `xface` - the interface implemented by the classes named by `name`. 

Returns:
    a `List` of objects implementing `xface`.
    * ### setClass
public void setClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> theClass, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> xface)
Set the value of the `name` property to the name of a `theClass` implementing the given interface `xface`. An exception is thrown if `theClass` does not implement the interface `xface`. 

Parameters:
     `name` - property name.      `theClass` - property value.      `xface` - the interface implemented by the named class.
    * ### getLocalPath
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getLocalPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dirsProp, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get a local file under a directory named by _dirsProp_ with the given _path_. If _dirsProp_ contains multiple directories, then one is chosen based on _path_ 's hash code. If the selected directory does not exist, an attempt is made to create it. 

Parameters:
     `dirsProp` - directory in which to locate the file.      `path` - file-path. 

Returns:
    local file under the directory with the given path. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### getFile
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html "class or interface in java.io") getFile([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dirsProp, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get a local file name under a directory named in _dirsProp_ with the given _path_. If _dirsProp_ contains multiple directories, then one is chosen based on _path_ 's hash code. If the selected directory does not exist, an attempt is made to create it. 

Parameters:
     `dirsProp` - directory in which to locate the file.      `path` - file-path. 

Returns:
    local file under the directory with the given path. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### getResource
public [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") getResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get the [`URL`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html "class or interface in java.net") for the named resource. 

Parameters:
     `name` - resource name. 

Returns:
    the url for the named resource.
    * ### getConfResourceAsInputStream
public [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") getConfResourceAsInputStream([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get an input stream attached to the configuration resource with the given `name`. 

Parameters:
     `name` - configuration resource name. 

Returns:
    an input stream attached to the resource.
    * ### getConfResourceAsReader
public [Reader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Reader.html "class or interface in java.io") getConfResourceAsReader([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Get a [`Reader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Reader.html "class or interface in java.io") attached to the configuration resource with the given `name`. 

Parameters:
     `name` - configuration resource name. 

Returns:
    a reader attached to the resource.
    * ### getFinalParameters
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getFinalParameters()
Get the set of parameters marked final. 

Returns:
    final parameter set.
    * ### getProps
protected [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util") getProps()
    * ### size
public int size()
Return the number of keys in the configuration. 

Returns:
    number of keys in the configuration.
    * ### clear
public void clear()
Clears all keys from the configuration.
    * ### iterator
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> iterator()
Get an [`Iterator`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util") to go through the list of `String` key-value pairs in the configuration. 

Specified by:
     `iterator[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#iterator\(\) "class or interface in java.lang")` in interface `Iterable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<Map.Entry[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>` 

Returns:
    an iterator over the entries.
    * ### getPropsWithPrefix
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getPropsWithPrefix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") confPrefix)
Constructs a mapping of configuration and includes all properties that start with the specified configuration prefix. Property names in the mapping are trimmed to remove the configuration prefix. 

Parameters:
     `confPrefix` - configuration prefix 

Returns:
    mapping of configuration properties with prefix stripped
    * ### addTags
public void addTags([Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util") prop)
Add tags defined in HADOOP_TAGS_SYSTEM, HADOOP_TAGS_CUSTOM. 

Parameters:
     `prop` - properties.
    * ### writeXml
public void writeXml([OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Write out the non-default properties in this configuration to the given [`OutputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html "class or interface in java.io") using UTF-8 encoding. 

Parameters:
     `out` - the output stream to write to. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### writeXml
public void writeXml([Writer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io") 

Throws:
    `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")`
    * ### writeXml
public void writeXml(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName, [Writer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")
Write out the non-default properties in this configuration to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"). 
      * When property name is not empty and the property exists in the configuration, this method writes the property and its attributes to the [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"). 
      * When property name is null or empty, this method writes all the configuration properties and their attributes to the [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"). 
      * When property name is not empty but the property doesn't exist in the configuration, this method throws an [`IllegalArgumentException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang").  

Parameters:
     `propertyName` - xml property name.      `out` - the writer to write to.      `config` - configuration. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")`
    * ### writeXml
public void writeXml(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName, [Writer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang") 

Throws:
    `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")`     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")`
    * ### dumpConfiguration
public static void dumpConfiguration([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") propertyName, [Writer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Writes properties and their attributes (final and resource) to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"). 
      * When propertyName is not empty, and the property exists in the configuration, the format of the output would be, 
```
  {
    "property": {
      "key" : "key1",
      "value" : "value1",
      "isFinal" : "key1.isFinal",
      "resource" : "key1.resource"
    }
  }
  
```

      * When propertyName is null or empty, it behaves same as [`dumpConfiguration(Configuration, Writer)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html#dumpConfiguration\(org.apache.hadoop.conf.Configuration,java.io.Writer\)), the output would be, 
```
  { "properties" :
      [ { key : "key1",
          value : "value1",
          isFinal : "key1.isFinal",
          resource : "key1.resource" },
        { key : "key2",
          value : "value2",
          isFinal : "ke2.isFinal",
          resource : "key2.resource" }
       ]
   }
  
```

      * When propertyName is not empty, and the property is not found in the configuration, this method will throw an [`IllegalArgumentException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang").  

Parameters:
     `config` - the configuration      `propertyName` - property name      `out` - the Writer to write to 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.      `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - when property name is not empty and the property is not found in configuration
    * ### dumpConfiguration
public static void dumpConfiguration([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config, [Writer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Writes out all properties and their attributes (final and resource) to the given [`Writer`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Writer.html "class or interface in java.io"), the format of the output would be, 
```
  { "properties" :
      [ { key : "key1",
          value : "value1",
          isFinal : "key1.isFinal",
          resource : "key1.resource" },
        { key : "key2",
          value : "value2",
          isFinal : "ke2.isFinal",
          resource : "key2.resource" }
       ]
   }
  
```
It does not output the properties of the configuration object which is loaded from an input stream.  

Parameters:
     `config` - the configuration      `out` - the Writer to write to 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### getClassLoader
public [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang") getClassLoader()
Get the [`ClassLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang") for this job. 

Returns:
    the correct class loader.
    * ### setClassLoader
public void setClassLoader([ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class or interface in java.lang") classLoader)
Set the class loader that will be used to load the various objects. 

Parameters:
     `classLoader` - the new class loader.
    * ### toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString() 

Overrides:
     `toString[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang")` in class `Object[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`
    * ### setQuietMode
public void setQuietMode(boolean quietmode)
Set the quietness-mode. In the quiet-mode, error and informational messages might not be logged. 

Parameters:
     `quietmode` - `true` to set quiet-mode on, `false` to turn it off.
    * ### main
public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] args) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")
For debugging. List non-default properties to the terminal and exit. 

Parameters:
     `args` - the argument to be parsed. 

Throws:
     `Exception[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")` - exception.
    * ### readFields
public void readFields([DataInput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/DataInput.html "class or interface in java.io") in) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Description copied from interface: `Writable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html#readFields\(java.io.DataInput\))`
Deserialize the fields of this object from `in`. 
For efficiency, implementations should attempt to re-use storage in the existing object where possible. 

Specified by:
     `readFields[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html#readFields\(java.io.DataInput\))` in interface `Writable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")` 

Parameters:
     `in` - `DataInput` to deseriablize this object from. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - any other problem for readFields.
    * ### write
public void write([DataOutput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/DataOutput.html "class or interface in java.io") out) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Description copied from interface: `Writable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html#write\(java.io.DataOutput\))`
Serialize the fields of this object to `out`. 

Specified by:
     `write[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html#write\(java.io.DataOutput\))` in interface `Writable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")` 

Parameters:
     `out` - `DataOuput` to serialize this object into. 

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - any other problem for write.
    * ### getValByRegex
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getValByRegex([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") regex)
get keys matching the the regex. 

Parameters:
     `regex` - the regex to match against. 

Returns:
    Map<String,String> with matching keys
    * ### dumpDeprecatedKeys
public static void dumpDeprecatedKeys()
    * ### hasWarnedDeprecation
public static boolean hasWarnedDeprecation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)
Returns whether or not a deprecated name has been warned. If the name is not deprecated then always return false 

Parameters:
     `name` - proprties. 

Returns:
    true if name is a warned deprecation.
    * ### getAllPropertiesByTag
public [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util") getAllPropertiesByTag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tag)
Get all properties belonging to tag. 

Parameters:
     `tag` - tag 

Returns:
    Properties with matching tag
    * ### getAllPropertiesByTags
public [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html "class or interface in java.util") getAllPropertiesByTags([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> tagList)
Get all properties belonging to list of input tags. Calls getAllPropertiesByTag internally. 

Parameters:
     `tagList` - list of input tags 

Returns:
    Properties with matching tags
    * ### isPropertyTag
public boolean isPropertyTag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tagStr)
Get Property tag Enum corresponding to given source. 

Parameters:
     `tagStr` - String representation of Enum 

Returns:
    true if tagStr is a valid tag


* * *
Copyright © 2026 [Apache Software Foundation](https://www.apache.org). All rights reserved.
