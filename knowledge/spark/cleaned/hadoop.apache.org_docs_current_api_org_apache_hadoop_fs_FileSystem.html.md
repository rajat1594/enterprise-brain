[Skip navigation links](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/current/api/index.html)
  * [Package](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/class-use/FileSystem.html)
  * [Tree](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/current/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/current/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/current/api/help-doc.html#class)

  * Summary:
  * [Nested](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#nested-class-summary) |
  * [Field](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#field-summary) |
  * [Constr](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#constructor-summary) |
  * [Method](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#method-summary)

  * Detail:
  * [Field](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#field-detail) |
  * [Constr](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#constructor-detail) |
  * [Method](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#method-detail)

SEARCH:
Package [org.apache.hadoop.fs](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/package-summary.html)
# Class FileSystem
[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
[org.apache.hadoop.conf.Configured](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configured.html "class in org.apache.hadoop.conf")
org.apache.hadoop.fs.FileSystem

All Implemented Interfaces:
     `Closeable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html "class or interface in java.io")`, `AutoCloseable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`, `Configurable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configurable.html "interface in org.apache.hadoop.conf")`, `BulkDeleteSource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDeleteSource.html "interface in org.apache.hadoop.fs")`, `org.apache.hadoop.fs.PathCapabilities`, `org.apache.hadoop.security.token.DelegationTokenIssuer`

Direct Known Subclasses:
     `AdlFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/adl/AdlFileSystem.html "class in org.apache.hadoop.fs.adl")`, `FilterFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FilterFileSystem.html "class in org.apache.hadoop.fs")`, `FTPFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ftp/FTPFileSystem.html "class in org.apache.hadoop.fs.ftp")`, `NativeAzureFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/azure/NativeAzureFileSystem.html "class in org.apache.hadoop.fs.azure")`, `RawLocalFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/RawLocalFileSystem.html "class in org.apache.hadoop.fs")`, `ViewFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/viewfs/ViewFileSystem.html "class in org.apache.hadoop.fs.viewfs")`
* * *
@Public @Stable public abstract class FileSystem extends [Configured](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configured.html "class in org.apache.hadoop.conf") implements [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html "class or interface in java.io"), org.apache.hadoop.security.token.DelegationTokenIssuer, org.apache.hadoop.fs.PathCapabilities, [BulkDeleteSource](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDeleteSource.html "interface in org.apache.hadoop.fs")
An abstract base class for a fairly generic filesystem. It may be implemented as a distributed filesystem, or as a "local" one that reflects the locally-connected disk. The local version exists for small Hadoop instances and for testing.
All user code that may potentially use the Hadoop Distributed File System should be written to use a FileSystem object or its successor, [`FileContext`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html "class in org.apache.hadoop.fs").
The local implementation is [`LocalFileSystem`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocalFileSystem.html "class in org.apache.hadoop.fs") and distributed implementation is DistributedFileSystem. There are other implementations for object stores and (outside the Apache Hadoop codebase), third party filesystems.
Notes
  1. The behaviour of the filesystem is [ specified in the Hadoop documentation. ](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/filesystem/filesystem.html) However, the normative specification of the behavior of this class is actually HDFS: if HDFS does not behave the way these Javadocs or the specification in the Hadoop documentations define, assume that the documentation is incorrect.
  2. The term `FileSystem` refers to an instance of this class.
  3. The acronym "FS" is used as an abbreviation of FileSystem.
  4. The term `filesystem` refers to the distributed/local filesystem itself, rather than the class used to interact with it.
  5. The term "file" refers to a file in the remote filesystem, rather than instances of `java.io.File`.

This is a carefully evolving class. New methods may be marked as Unstable or Evolving for their initial release, as a warning that they are new and may change based on the experience of use in applications.
**Important note for developers**
If you are making changes here to the public API or protected methods, you must review the following subclasses and make sure that they are filtering/passing through new methods as appropriate. [`FilterFileSystem`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FilterFileSystem.html "class in org.apache.hadoop.fs"): methods are passed through. If not, then `TestFilterFileSystem.MustNotImplement` must be updated with the unsupported interface. Furthermore, if the new API's support is probed for via [`hasPathCapability(Path, String)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#hasPathCapability\(org.apache.hadoop.fs.Path,java.lang.String\)) then [`FilterFileSystem.hasPathCapability(Path, String)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FilterFileSystem.html#hasPathCapability\(org.apache.hadoop.fs.Path,java.lang.String\)) must return false, always.
[`ChecksumFileSystem`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ChecksumFileSystem.html "class in org.apache.hadoop.fs"): checksums are created and verified.
`TestHarFileSystem` will need its `MustNotImplement` interface updated.
There are some external places your changes will break things. Do co-ordinate changes here.
HBase: HBoss
Hive: HiveShim23
`shims/0.23/src/main/java/org/apache/hadoop/hive/shims/Hadoop23Shims.java`
  * ## Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class `
`org.apache.hadoop.fs.FileSystem.DirectoryEntries`
Represents a batch of directory entries when iteratively listing a directory.
`protected class `
`org.apache.hadoop.fs.FileSystem.DirListingIterator<T extends FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")>`
Generic iterator for implementing [`listStatusIterator(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatusIterator\(org.apache.hadoop.fs.Path\)).
`static final class `
`org.apache.hadoop.fs.FileSystem.Statistics`
Tracks statistics about how many reads, writes, and so forth have been done in a FileSystem.
  * ## Field Summary
Fields
Modifier and Type
Field
Description
`static final String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`DEFAULT_FS[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#DEFAULT_FS)`
`static final String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`FS_DEFAULT_NAME_KEY[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#FS_DEFAULT_NAME_KEY)`
`static final org.slf4j.Logger`
`LOG`
This log is widely used in the org.apache.hadoop.fs code and tests, so must be considered something to only be changed with care.
`static final int`
`SHUTDOWN_HOOK_PRIORITY[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#SHUTDOWN_HOOK_PRIORITY)`
Priority of the FileSystem shutdown hook: 10.
`protected org.apache.hadoop.fs.FileSystem.Statistics`
`statistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#statistics)`
The statistics for this file system.
`static final String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`TRASH_PREFIX[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#TRASH_PREFIX)`
Prefix for trash directory: ".Trash".
`static final String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`USER_HOME_PREFIX[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#USER_HOME_PREFIX)`
### Fields inherited from interface org.apache.hadoop.security.token.DelegationTokenIssuer
`TOKEN_LOG`
  * ## Constructor Summary
Constructors
Modifier
Constructor
Description
`protected `
`FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#%3Cinit%3E\(\))()`
  * ## Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`access(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  FsAction[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsAction.html "enum class in org.apache.hadoop.fs.permission") mode)`
Checks if the user can access a path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`append[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#append\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Append to an existing file (optional operation).
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`append[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#append\(org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean appendToNewBlock)`
Append to an existing file (optional operation).
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`append[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#append\(org.apache.hadoop.fs.Path,int\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  int bufferSize)`
Append to an existing file (optional operation).
`abstract FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`append[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#append\(org.apache.hadoop.fs.Path,int,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  int bufferSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Append to an existing file (optional operation).
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`append[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#append\(org.apache.hadoop.fs.Path,int,org.apache.hadoop.util.Progressable,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  int bufferSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress,  boolean appendToNewBlock)`
Append to an existing file (optional operation).
`FSDataOutputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs")`
`appendFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#appendFile\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create a Builder to append a file.
`static boolean`
`areSymlinksEnabled[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#areSymlinksEnabled\(\))()`
`boolean`
`cancelDeleteOnExit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#cancelDeleteOnExit\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Cancel the scheduled deletion of the path when the FileSystem is closed.
`protected URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net")`
`canonicalizeUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#canonicalizeUri\(java.net.URI\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri)`
Canonicalize the given URI.
`protected void`
`checkPath[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#checkPath\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Check that a Path belongs to this FileSystem.
`static void`
`clearStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#clearStatistics\(\))()`
Reset all statistics for all file systems.
`void`
`close[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#close\(\))()`
Close this FileSystem instance.
`static void`
`closeAll[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#closeAll\(\))()`
Close all cached FileSystem instances.
`static void`
`closeAllForUGI[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#closeAllForUGI\(org.apache.hadoop.security.UserGroupInformation\))(UserGroupInformation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/UserGroupInformation.html "class in org.apache.hadoop.security") ugi)`
Close all cached FileSystem instances for a given UGI.
`void`
`completeLocalOutput[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#completeLocalOutput\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") fsOutputFile,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") tmpLocalFile)`
Called when we're all done writing to the target.
`void`
`concat[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#concat\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path%5B%5D\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") trg,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] psrcs)`
Concat existing files together.
`void`
`copyFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyFromLocalFile\(boolean,boolean,org.apache.hadoop.fs.Path%5B%5D,org.apache.hadoop.fs.Path\))(boolean delSrc,  boolean overwrite,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] srcs,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src files are on the local disk.
`void`
`copyFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyFromLocalFile\(boolean,boolean,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(boolean delSrc,  boolean overwrite,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src file is on the local disk.
`void`
`copyFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyFromLocalFile\(boolean,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(boolean delSrc,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src file is on the local disk.
`void`
`copyFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyFromLocalFile\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src file is on the local disk.
`void`
`copyToLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyToLocalFile\(boolean,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(boolean delSrc,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
Copy it a file from a remote filesystem to the local one.
`void`
`copyToLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyToLocalFile\(boolean,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path,boolean\))(boolean delSrc,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst,  boolean useRawLocalFileSystem)`
The src file is under this filesystem, and the dst is on the local disk.
`void`
`copyToLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#copyToLocalFile\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
Copy it a file from the remote filesystem to the local one.
`static FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.FileSystem,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))(FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fs,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission)`
Create a file with the provided permission.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Create an FSDataOutputStream at the indicated Path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite)`
Create an FSDataOutputStream at the indicated Path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,boolean,int\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite,  int bufferSize)`
Create an FSDataOutputStream at the indicated Path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,boolean,int,short,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite,  int bufferSize,  short replication,  long blockSize)`
Create an FSDataOutputStream at the indicated Path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,boolean,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an FSDataOutputStream at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,boolean,int,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite,  int bufferSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an [`FSDataOutputStream`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,short\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  short replication)`
Create an FSDataOutputStream at the indicated Path.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,short,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  short replication,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an FSDataOutputStream at the indicated Path with write-progress reporting.
`abstract FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,boolean,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission,  boolean overwrite,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an FSDataOutputStream at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,java.util.EnumSet,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission,  EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<CreateFlag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an FSDataOutputStream at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,java.util.EnumSet,int,short,long,org.apache.hadoop.util.Progressable,org.apache.hadoop.fs.Options.ChecksumOpt\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission,  EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<CreateFlag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress,  org.apache.hadoop.fs.Options.ChecksumOpt checksumOpt)`
Create an FSDataOutputStream at the indicated Path with a custom checksum option.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`create[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.Path,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Create an FSDataOutputStream at the indicated Path with write-progress reporting.
`BulkDelete[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDelete.html "interface in org.apache.hadoop.fs")`
`createBulkDelete[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createBulkDelete\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create a bulk delete operation.
`protected static org.apache.hadoop.fs.FileSystem.FSDataInputStreamBuilder`
`createDataInputStreamBuilder(FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create instance of the standard `FileSystem.FSDataInputStreamBuilder` for the given filesystem and path.
`protected static org.apache.hadoop.fs.FileSystem.FSDataInputStreamBuilder`
`createDataInputStreamBuilder(FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem,  PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle)`
Create instance of the standard `FileSystem.FSDataInputStreamBuilder` for the given filesystem and path handle.
`protected static FSDataOutputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs")`
`createDataOutputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createDataOutputStreamBuilder\(org.apache.hadoop.fs.FileSystem,org.apache.hadoop.fs.Path\))(FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create instance of the standard FSDataOutputStreamBuilder for the given filesystem and path.
`FSDataOutputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs")`
`createFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createFile\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create a new FSDataOutputStreamBuilder for the file with path.
`org.apache.hadoop.fs.MultipartUploaderBuilder`
`createMultipartUploader[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createMultipartUploader\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") basePath)`
Create a multipart uploader.
`boolean`
`createNewFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createNewFile\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Creates the given Path as a brand-new zero-length file.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`createNonRecursive[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createNonRecursive\(org.apache.hadoop.fs.Path,boolean,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean overwrite,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Opens an FSDataOutputStream at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`createNonRecursive[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createNonRecursive\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,boolean,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission,  boolean overwrite,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Opens an FSDataOutputStream at the indicated Path with write-progress reporting.
`FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`createNonRecursive[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createNonRecursive\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,java.util.EnumSet,int,short,long,org.apache.hadoop.util.Progressable\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission,  EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<CreateFlag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress)`
Opens an FSDataOutputStream at the indicated Path with write-progress reporting.
`protected PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs")`
`createPathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createPathHandle\(org.apache.hadoop.fs.FileStatus,org.apache.hadoop.fs.Options.HandleOpt...\))(FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") stat,  org.apache.hadoop.fs.Options.HandleOpt... opt)`
Hook to implement support for [`PathHandle`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") operations.
`final Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`createSnapshot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createSnapshot\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Create a snapshot with a default name.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`createSnapshot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createSnapshot\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotName)`
Create a snapshot.
`void`
`createSymlink[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createSymlink\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") target,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") link,  boolean createParent)`
See [`FileContext.createSymlink(Path, Path, boolean)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#createSymlink\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path,boolean\)).
`boolean`
`delete[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#delete\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Deprecated.
Use [`delete(Path, boolean)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#delete\(org.apache.hadoop.fs.Path,boolean\)) instead.
`abstract boolean`
`delete[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#delete\(org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean recursive)`
Delete a file.
`boolean`
`deleteOnExit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#deleteOnExit\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Mark a path to be deleted when its FileSystem is closed.
`void`
`deleteSnapshot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#deleteSnapshot\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotName)`
Delete a snapshot of a directory.
`static void`
`enableSymlinks[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#enableSymlinks\(\))()`
`boolean`
`exists[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#exists\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Check if a path exists.
`protected Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`fixRelativePart[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#fixRelativePart\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)`
See `FileContext.fixRelativePart(org.apache.hadoop.fs.Path)`.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`get[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#get\(java.net.URI,org.apache.hadoop.conf.Configuration\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Get a FileSystem for this URI's scheme and authority.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`get[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#get\(java.net.URI,org.apache.hadoop.conf.Configuration,java.lang.String\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") user)`
Get a FileSystem instance based on the uri, the passed in configuration and the user.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`get[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#get\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Returns the configured FileSystem implementation.
`AclStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclStatus.html "class in org.apache.hadoop.fs.permission")`
`getAclStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getAclStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Gets the ACL of a file or directory.
`org.apache.hadoop.security.token.DelegationTokenIssuer[]`
`getAdditionalTokenIssuers()`
Issuers may need tokens from additional services.
`static List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<org.apache.hadoop.fs.FileSystem.Statistics>`
`getAllStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getAllStatistics\(\))()`
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
`Collection[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<? extends BlockStoragePolicySpi[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockStoragePolicySpi.html "interface in org.apache.hadoop.fs")>`
`getAllStoragePolicies[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getAllStoragePolicies\(\))()`
Retrieve all the storage policies supported by this file system.
`long`
`getBlockSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getBlockSize\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getCanonicalServiceName[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getCanonicalServiceName\(\))()`
Get a canonical service name for this FileSystem.
`protected URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net")`
`getCanonicalUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getCanonicalUri\(\))()`
Return a canonicalized form of this FileSystem's URI.
`FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")[]`
`getChildFileSystems()`
Get all the immediate child FileSystems embedded in this FileSystem.
`ContentSummary[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ContentSummary.html "class in org.apache.hadoop.fs")`
`getContentSummary[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getContentSummary\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Return the [`ContentSummary`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ContentSummary.html "class in org.apache.hadoop.fs") of a given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").
`long`
`getDefaultBlockSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultBlockSize\(\))()`
Deprecated.
use [`getDefaultBlockSize(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultBlockSize\(org.apache.hadoop.fs.Path\)) instead
`long`
`getDefaultBlockSize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultBlockSize\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Return the number of bytes that large input files should be optimally be split into to minimize I/O time.
`protected int`
`getDefaultPort[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultPort\(\))()`
Get the default port for this FileSystem.
`short`
`getDefaultReplication[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultReplication\(\))()`
Deprecated.
use [`getDefaultReplication(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultReplication\(org.apache.hadoop.fs.Path\)) instead
`short`
`getDefaultReplication[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultReplication\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Get the default replication for a path.
`static URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net")`
`getDefaultUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultUri\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Get the default FileSystem URI from a configuration.
`Token[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/token/Token.html "class in org.apache.hadoop.security.token")<?>`
`getDelegationToken(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") renewer)`
Get a new delegation token for this FileSystem.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getEnclosingRoot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getEnclosingRoot\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Return path of the enclosing root for a given path.
`BlockLocation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockLocation.html "class in org.apache.hadoop.fs")[]`
`getFileBlockLocations[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileBlockLocations\(org.apache.hadoop.fs.FileStatus,long,long\))(FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") file,  long start,  long len)`
Return an array containing hostnames, offset and size of portions of the given file.
`BlockLocation[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockLocation.html "class in org.apache.hadoop.fs")[]`
`getFileBlockLocations[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileBlockLocations\(org.apache.hadoop.fs.Path,long,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p,  long start,  long len)`
Return an array containing hostnames, offset and size of portions of the given file.
`FileChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileChecksum.html "class in org.apache.hadoop.fs")`
`getFileChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileChecksum\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Get the checksum of a file, if the FS supports checksums.
`FileChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileChecksum.html "class in org.apache.hadoop.fs")`
`getFileChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileChecksum\(org.apache.hadoop.fs.Path,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  long length)`
Get the checksum of a file, from the beginning of the file till the specific length.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")`
`getFileLinkStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileLinkStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
See [`FileContext.getFileLinkStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#getFileLinkStatus\(org.apache.hadoop.fs.Path\)).
`abstract FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")`
`getFileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Return a file status object that represents the path.
`static Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")>`
`getFileSystemClass[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileSystemClass\(java.lang.String,org.apache.hadoop.conf.Configuration\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") scheme,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Get the FileSystem implementation class of a filesystem.
`protected static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`getFSofPath[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFSofPath\(org.apache.hadoop.fs.Path,org.apache.hadoop.conf.Configuration\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") absOrFqPath,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
`static GlobalStorageStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/GlobalStorageStatistics.html "enum class in org.apache.hadoop.fs")`
`getGlobalStorageStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))()`
Get the global storage statistics.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getHomeDirectory[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getHomeDirectory\(\))()`
Return the current user's home directory in this FileSystem.
`protected Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getInitialWorkingDirectory[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getInitialWorkingDirectory\(\))()`
Note: with the new FileContext class, getWorkingDirectory() will be removed.
`long`
`getLength[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getLength\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getLinkTarget[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getLinkTarget\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
See [`FileContext.getLinkTarget(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#getLinkTarget\(org.apache.hadoop.fs.Path\)).
`static LocalFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocalFileSystem.html "class in org.apache.hadoop.fs")`
`getLocal[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getLocal\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Get the local FileSystem.
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getName[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getName\(\))()`
Deprecated.
call [`getUri()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getUri\(\)) instead.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`getNamed[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getNamed\(java.lang.String,org.apache.hadoop.conf.Configuration\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Deprecated.
call [`get(URI, Configuration)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#get\(java.net.URI,org.apache.hadoop.conf.Configuration\)) instead.
`final PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs")`
`getPathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getPathHandle\(org.apache.hadoop.fs.FileStatus,org.apache.hadoop.fs.Options.HandleOpt...\))(FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") stat,  org.apache.hadoop.fs.Options.HandleOpt... opt)`
Create a durable, serializable handle to the referent of the given entity.
`QuotaUsage[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/QuotaUsage.html "class in org.apache.hadoop.fs")`
`getQuotaUsage[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getQuotaUsage\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Return the [`QuotaUsage`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/QuotaUsage.html "class in org.apache.hadoop.fs") of a given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").
`short`
`getReplication[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getReplication\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src)`
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
`String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`
`getScheme[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getScheme\(\))()`
Return the protocol scheme for this FileSystem.
`FsServerDefaults[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsServerDefaults.html "class in org.apache.hadoop.fs")`
`getServerDefaults[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getServerDefaults\(\))()`
Deprecated.
use [`getServerDefaults(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getServerDefaults\(org.apache.hadoop.fs.Path\)) instead
`FsServerDefaults[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsServerDefaults.html "class in org.apache.hadoop.fs")`
`getServerDefaults[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getServerDefaults\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)`
Return a set of server default configuration values.
`static Map[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),org.apache.hadoop.fs.FileSystem.Statistics>`
`getStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStatistics\(\))()`
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
`static org.apache.hadoop.fs.FileSystem.Statistics`
`getStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStatistics\(java.lang.String,java.lang.Class\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") scheme,  Class[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")> cls)`
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
`FsStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsStatus.html "class in org.apache.hadoop.fs")`
`getStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStatus\(\))()`
Returns a status object describing the use and capacity of the filesystem.
`FsStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsStatus.html "class in org.apache.hadoop.fs")`
`getStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)`
Returns a status object describing the use and capacity of the filesystem.
`BlockStoragePolicySpi[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockStoragePolicySpi.html "interface in org.apache.hadoop.fs")`
`getStoragePolicy[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStoragePolicy\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src)`
Query the effective storage policy ID for the given file or directory.
`StorageStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/StorageStatistics.html "class in org.apache.hadoop.fs")`
`getStorageStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getStorageStatistics\(\))()`
Get the StorageStatistics for this FileSystem object.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getTrashRoot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getTrashRoot\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Get the root directory of Trash for current user when the path specified is deleted.
`Collection[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")>`
`getTrashRoots[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getTrashRoots\(boolean\))(boolean allUsers)`
Get all the trash roots for current user or all users.
`abstract URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net")`
`getUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getUri\(\))()`
Returns a URI which identifies this FileSystem.
`long`
`getUsed[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getUsed\(\))()`
Return the total size of all files in the filesystem.
`long`
`getUsed[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getUsed\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Return the total size of all files from a specified path.
`abstract Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`getWorkingDirectory[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getWorkingDirectory\(\))()`
Get the current working directory for the given FileSystem
`byte[]`
`getXAttr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getXAttr\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Get an xattr name and value for a file or directory.
`Map[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),byte[]>`
`getXAttrs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getXAttrs\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Get all of the xattr name/value pairs for a file or directory.
`Map[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),byte[]>`
`getXAttrs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getXAttrs\(org.apache.hadoop.fs.Path,java.util.List\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> names)`
Get all of the xattrs name/value pairs for a file or directory.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`globStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#globStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") pathPattern)`
Return all the files that match filePattern and are not checksum files.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`globStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#globStatus\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.PathFilter\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") pathPattern,  PathFilter[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter)`
Return an array of [`FileStatus`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") objects whose path names match `pathPattern` and is accepted by the user-supplied path filter.
`boolean`
`hasPathCapability[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#hasPathCapability\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") capability)`
The base FileSystem implementation generally has no knowledge of the capabilities of actual implementations.
`void`
`initialize[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#initialize\(java.net.URI,org.apache.hadoop.conf.Configuration\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") name,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Initialize a FileSystem.
`boolean`
`isDirectory[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#isDirectory\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
`boolean`
`isFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#isFile\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
`org.apache.hadoop.fs.RemoteIterator<Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")>`
`listCorruptFileBlocks[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listCorruptFileBlocks\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
List corrupted file blocks.
`org.apache.hadoop.fs.RemoteIterator<LocatedFileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")>`
`listFiles[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listFiles\(org.apache.hadoop.fs.Path,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  boolean recursive)`
List the statuses and block locations of the files in the given path.
`org.apache.hadoop.fs.RemoteIterator<LocatedFileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")>`
`listLocatedStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listLocatedStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
List the statuses of the files/directories in the given path if the path is a directory.
`protected org.apache.hadoop.fs.RemoteIterator<LocatedFileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")>`
`listLocatedStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listLocatedStatus\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.PathFilter\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  PathFilter[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter)`
List a directory.
`abstract FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`listStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatus\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
List the statuses of the files/directories in the given path if the path is a directory.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`listStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatus\(org.apache.hadoop.fs.Path%5B%5D\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] files)`
Filter files/directories in the given list of paths using default path filter.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`listStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatus\(org.apache.hadoop.fs.Path%5B%5D,org.apache.hadoop.fs.PathFilter\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] files,  PathFilter[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter)`
Filter files/directories in the given list of paths using user-supplied path filter.
`FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`
`listStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatus\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.PathFilter\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  PathFilter[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter)`
Filter files/directories in the given path using the user-supplied path filter.
`protected org.apache.hadoop.fs.FileSystem.DirectoryEntries`
`listStatusBatch(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  byte[] token)`
Given an opaque iteration token, return the next batch of entries in a directory.
`org.apache.hadoop.fs.RemoteIterator<FileStatus[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")>`
`listStatusIterator[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatusIterator\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)`
Returns a remote iterator so that followup calls are made on demand while consuming the entries.
`List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`listXAttrs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listXAttrs\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Get all of the xattr names for a file or directory.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`makeQualified[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#makeQualified\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Qualify a path to one which uses this FileSystem and, if relative, made absolute.
`static boolean`
`mkdirs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.FileSystem,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))(FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fs,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dir,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission)`
Create a directory with the provided permission.
`boolean`
`mkdirs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Call [`mkdirs(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\)) with default permission.
`abstract boolean`
`mkdirs[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission)`
Make the given file and all non-existent parents into directories.
`void`
`modifyAclEntries[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#modifyAclEntries\(org.apache.hadoop.fs.Path,java.util.List\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<AclEntry[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec)`
Modifies ACL entries of files and directories.
`void`
`moveFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#moveFromLocalFile\(org.apache.hadoop.fs.Path%5B%5D,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] srcs,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src files is on the local disk.
`void`
`moveFromLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#moveFromLocalFile\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
The src file is on the local disk.
`void`
`moveToLocalFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#moveToLocalFile\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
Copy a file to the local filesystem, then delete it from the remote filesystem (if successfully copied).
`void`
`msync[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#msync\(\))()`
Synchronize client metadata state.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`newInstance[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#newInstance\(java.net.URI,org.apache.hadoop.conf.Configuration\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config)`
Returns the FileSystem for this URI's scheme and authority.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`newInstance[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#newInstance\(java.net.URI,org.apache.hadoop.conf.Configuration,java.lang.String\))(URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri,  Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") user)`
Returns the FileSystem for this URI's scheme and authority and the given user.
`static FileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")`
`newInstance[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#newInstance\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Returns a unique configured FileSystem implementation for the default filesystem of the supplied configuration.
`static LocalFileSystem[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocalFileSystem.html "class in org.apache.hadoop.fs")`
`newInstanceLocal[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#newInstanceLocal\(org.apache.hadoop.conf.Configuration\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)`
Get a unique local FileSystem object.
`FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")`
`open[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
Opens an FSDataInputStream at the indicated Path.
`FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")`
`open[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.PathHandle\))(PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") fd)`
Open an FSDataInputStream matching the PathHandle instance.
`FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")`
`open[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.PathHandle,int\))(PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") fd,  int bufferSize)`
Open an FSDataInputStream matching the PathHandle instance.
`abstract FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")`
`open[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path,int\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  int bufferSize)`
Opens an FSDataInputStream at the indicated Path.
`FutureDataInputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FutureDataInputStreamBuilder.html "interface in org.apache.hadoop.fs")`
`openFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#openFile\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Open a file for reading through a builder API.
`FutureDataInputStreamBuilder[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FutureDataInputStreamBuilder.html "interface in org.apache.hadoop.fs")`
`openFile[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#openFile\(org.apache.hadoop.fs.PathHandle\))(PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle)`
Open a file for reading through a builder API.
`protected CompletableFuture[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class or interface in java.util.concurrent")<FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")>`
`openFileWithOptions[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#openFileWithOptions\(org.apache.hadoop.fs.PathHandle,org.apache.hadoop.fs.impl.OpenFileParameters\))(PathHandle[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle,  org.apache.hadoop.fs.impl.OpenFileParameters parameters)`
Execute the actual open file operation.
`protected CompletableFuture[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class or interface in java.util.concurrent")<FSDataInputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")>`
`openFileWithOptions[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#openFileWithOptions\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.impl.OpenFileParameters\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  org.apache.hadoop.fs.impl.OpenFileParameters parameters)`
Execute the actual open file operation.
`protected FSDataOutputStream[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs")`
`primitiveCreate[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#primitiveCreate\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,java.util.EnumSet,int,short,long,org.apache.hadoop.util.Progressable,org.apache.hadoop.fs.Options.ChecksumOpt\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission,  EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<CreateFlag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flag,  int bufferSize,  short replication,  long blockSize,  Progressable[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress,  org.apache.hadoop.fs.Options.ChecksumOpt checksumOpt)`
Deprecated.
`protected boolean`
`primitiveMkdir[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#primitiveMkdir\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission)`
Deprecated.
`protected void`
`primitiveMkdir[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#primitiveMkdir\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission,boolean\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission,  boolean createParent)`
Deprecated.
`static void`
`printStatistics[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#printStatistics\(\))()`
Print all statistics for all file systems to `System.out`
`protected void`
`processDeleteOnExit[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#processDeleteOnExit\(\))()`
Delete all paths that were marked as delete-on-exit.
`void`
`removeAcl[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#removeAcl\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Removes all but the base ACL entries of files and directories.
`void`
`removeAclEntries[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#removeAclEntries\(org.apache.hadoop.fs.Path,java.util.List\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<AclEntry[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec)`
Removes ACL entries from files and directories.
`void`
`removeDefaultAcl[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#removeDefaultAcl\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Removes all default ACL entries from files and directories.
`void`
`removeXAttr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#removeXAttr\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`
Remove an xattr of a file or directory.
`abstract boolean`
`rename[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#rename\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst)`
Renames Path src to Path dst.
`protected void`
`rename[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#rename\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Options.Rename...\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst,  Options.Rename[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Options.Rename.html "enum class in org.apache.hadoop.fs")... options)`
Deprecated.
`void`
`renameSnapshot[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#renameSnapshot\(org.apache.hadoop.fs.Path,java.lang.String,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotOldName,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotNewName)`
Rename a snapshot.
`protected Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`resolveLink[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#resolveLink\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)`
See [`AbstractFileSystem.getLinkTarget(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/AbstractFileSystem.html#getLinkTarget\(org.apache.hadoop.fs.Path\)).
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`resolvePath[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#resolvePath\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)`
Return the fully-qualified path of path, resolving the path through any symlinks or mount point.
`void`
`satisfyStoragePolicy[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#satisfyStoragePolicy\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)`
Set the source path to satisfy storage policy.
`void`
`setAcl[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setAcl\(org.apache.hadoop.fs.Path,java.util.List\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  List[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<AclEntry[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec)`
Fully replaces ACL of files and directories, discarding all existing entries.
`static void`
`setDefaultUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setDefaultUri\(org.apache.hadoop.conf.Configuration,java.lang.String\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") uri)`
Set the default FileSystem URI in a configuration.
`static void`
`setDefaultUri[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setDefaultUri\(org.apache.hadoop.conf.Configuration,java.net.URI\))(Configuration[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf,  URI[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri)`
Set the default FileSystem URI in a configuration.
`void`
`setOwner[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setOwner\(org.apache.hadoop.fs.Path,java.lang.String,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") username,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") groupname)`
Set owner of a path (i.e. a file or a directory).
`void`
`setPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p,  FsPermission[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission)`
Set permission of a path.
`void`
`setQuota[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setQuota\(org.apache.hadoop.fs.Path,long,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  long namespaceQuota,  long storagespaceQuota)`
Set quota for the given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").
`void`
`setQuotaByStorageType[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setQuotaByStorageType\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.StorageType,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  StorageType[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/StorageType.html "enum class in org.apache.hadoop.fs") type,  long quota)`
Set per storage type quota for the given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").
`boolean`
`setReplication[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setReplication\(org.apache.hadoop.fs.Path,short\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  short replication)`
Set the replication for an existing file.
`void`
`setStoragePolicy[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setStoragePolicy\(org.apache.hadoop.fs.Path,java.lang.String\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") policyName)`
Set the storage policy for a given file or directory.
`void`
`setTimes[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setTimes\(org.apache.hadoop.fs.Path,long,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p,  long mtime,  long atime)`
Set access time of a file.
`void`
`setVerifyChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setVerifyChecksum\(boolean\))(boolean verifyChecksum)`
Set the verify checksum flag.
`abstract void`
`setWorkingDirectory[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setWorkingDirectory\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") new_dir)`
Set the current working directory for the given FileSystem.
`void`
`setWriteChecksum[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setWriteChecksum\(boolean\))(boolean writeChecksum)`
Set the write checksum flag.
`void`
`setXAttr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setXAttr\(org.apache.hadoop.fs.Path,java.lang.String,byte%5B%5D\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  byte[] value)`
Set an xattr of a file or directory.
`void`
`setXAttr[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setXAttr\(org.apache.hadoop.fs.Path,java.lang.String,byte%5B%5D,java.util.EnumSet\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path,  String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,  byte[] value,  EnumSet[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<XAttrSetFlag[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/XAttrSetFlag.html "enum class in org.apache.hadoop.fs")> flag)`
Set an xattr of a file or directory.
`Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")`
`startLocalOutput[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#startLocalOutput\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") fsOutputFile,  Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") tmpLocalFile)`
Returns a local file that the user can write output to.
`boolean`
`supportsSymlinks[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#supportsSymlinks\(\))()`
See [`AbstractFileSystem.supportsSymlinks()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/AbstractFileSystem.html#supportsSymlinks\(\)).
`boolean`
`truncate[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#truncate\(org.apache.hadoop.fs.Path,long\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f,  long newLength)`
Truncate the file in the indicated path to the indicated size.
`void`
`unsetStoragePolicy[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#unsetStoragePolicy\(org.apache.hadoop.fs.Path\))(Path[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src)`
Unset the storage policy set for a given file or directory.
### Methods inherited from class org.apache.hadoop.conf.[Configured](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configured.html "class in org.apache.hadoop.conf")
`getConf[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configured.html#getConf\(\)), setConf[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configured.html#setConf\(org.apache.hadoop.conf.Configuration\))`
### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
`clone[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), equals[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), finalize[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), getClass[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), hashCode[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), notify[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), toString[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`
### Methods inherited from interface org.apache.hadoop.security.token.DelegationTokenIssuer
`addDelegationTokens`

  * ## Field Details
    * ### FS_DEFAULT_NAME_KEY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") FS_DEFAULT_NAME_KEY

See Also:

      * [Constant Field Values](https://hadoop.apache.org/docs/current/api/constant-values.html#org.apache.hadoop.fs.FileSystem.FS_DEFAULT_NAME_KEY)
    * ### DEFAULT_FS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") DEFAULT_FS

See Also:

      * [Constant Field Values](https://hadoop.apache.org/docs/current/api/constant-values.html#org.apache.hadoop.fs.FileSystem.DEFAULT_FS)
    * ### LOG
@Private public static final org.slf4j.Logger LOG
This log is widely used in the org.apache.hadoop.fs code and tests, so must be considered something to only be changed with care.
    * ### SHUTDOWN_HOOK_PRIORITY
public static final int SHUTDOWN_HOOK_PRIORITY
Priority of the FileSystem shutdown hook: 10.

See Also:

      * [Constant Field Values](https://hadoop.apache.org/docs/current/api/constant-values.html#org.apache.hadoop.fs.FileSystem.SHUTDOWN_HOOK_PRIORITY)
    * ### TRASH_PREFIX
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") TRASH_PREFIX
Prefix for trash directory: ".Trash".

See Also:

      * [Constant Field Values](https://hadoop.apache.org/docs/current/api/constant-values.html#org.apache.hadoop.fs.FileSystem.TRASH_PREFIX)
    * ### USER_HOME_PREFIX
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") USER_HOME_PREFIX

See Also:

      * [Constant Field Values](https://hadoop.apache.org/docs/current/api/constant-values.html#org.apache.hadoop.fs.FileSystem.USER_HOME_PREFIX)
    * ### statistics
protected org.apache.hadoop.fs.FileSystem.Statistics statistics
The statistics for this file system.
  * ## Constructor Details
    * ### FileSystem
protected FileSystem()
  * ## Method Details
    * ### get
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") get([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") user) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")
Get a FileSystem instance based on the uri, the passed in configuration and the user.

Parameters:
     `uri` - of the filesystem      `conf` - the configuration to use      `user` - to perform the get as

Returns:
    the filesystem instance

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - failure to load      `InterruptedException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")` - If the `UGI.doAs()` call was somehow interrupted.
    * ### get
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") get([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns the configured FileSystem implementation.

Parameters:
     `conf` - the configuration to use

Returns:
    FileSystem.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.
    * ### getDefaultUri
public static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") getDefaultUri([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf)
Get the default FileSystem URI from a configuration.

Parameters:
     `conf` - the configuration to use

Returns:
    the uri of the default filesystem
    * ### setDefaultUri
public static void setDefaultUri([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf, [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri)
Set the default FileSystem URI in a configuration.

Parameters:
     `conf` - the configuration to alter      `uri` - the new default filesystem uri
    * ### setDefaultUri
public static void setDefaultUri([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") uri)
Set the default FileSystem URI in a configuration.

Parameters:
     `conf` - the configuration to alter      `uri` - the new default filesystem uri
    * ### initialize
public void initialize([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") name, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Initialize a FileSystem. Called after the new FileSystem instance is constructed, and before it is ready for use. FileSystem implementations overriding this method MUST forward it to their superclass, though the order in which it is done, and whether to alter the configuration before the invocation are options of the subclass.

Parameters:
     `name` - a URI whose authority section names the host, port, etc. for this FileSystem      `conf` - the configuration

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - on any failure to initialize this instance.      `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - if the URI is considered invalid.
    * ### getScheme
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getScheme()
Return the protocol scheme for this FileSystem.
This implementation throws an `UnsupportedOperationException`.

Returns:
    the protocol scheme for this FileSystem.

Throws:
     `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### getUri
public abstract [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") getUri()
Returns a URI which identifies this FileSystem.

Returns:
    the URI of this filesystem.
    * ### getCanonicalUri
protected [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") getCanonicalUri()
Return a canonicalized form of this FileSystem's URI. The default implementation simply calls [`canonicalizeUri(URI)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#canonicalizeUri\(java.net.URI\)) on the filesystem's own URI, so subclasses typically only need to implement that method.

Returns:
    the URI of this filesystem.

See Also:

      * [`canonicalizeUri(URI)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#canonicalizeUri\(java.net.URI\))
    * ### canonicalizeUri
protected [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") canonicalizeUri([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri)
Canonicalize the given URI. This is implementation-dependent, and may for example consist of canonicalizing the hostname using DNS and adding the default port if not specified. The default implementation simply fills in the default port if not specified and if [`getDefaultPort()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultPort\(\)) returns a default port.

Parameters:
     `uri` - url.

Returns:
    URI

See Also:

      * `NetUtils.getCanonicalUri(URI, int)`
    * ### getDefaultPort
protected int getDefaultPort()
Get the default port for this FileSystem.

Returns:
    the default port or 0 if there isn't one
    * ### getFSofPath
protected static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") getFSofPath([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") absOrFqPath, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [UnsupportedFileSystemException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")

Throws:
    `UnsupportedFileSystemException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs")`     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")`
    * ### getCanonicalServiceName
@Public @Evolving public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getCanonicalServiceName()
Get a canonical service name for this FileSystem. The token cache is the only user of the canonical service name, and uses it to lookup this FileSystem's service tokens. If the file system provides a token of its own then it must have a canonical name, otherwise the canonical name can be null. Default implementation: If the FileSystem has child file systems (such as an embedded file system) then it is assumed that the FS has no tokens of its own and hence returns a null name; otherwise a service name is built using Uri and port.

Specified by:
     `getCanonicalServiceName` in interface `org.apache.hadoop.security.token.DelegationTokenIssuer`

Returns:
    a service string that uniquely identifies this file system, null if the filesystem does not implement tokens

See Also:

      * [`SecurityUtil.buildDTServiceName(URI, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/SecurityUtil.html#buildDTServiceName\(java.net.URI,int\))
    * ### getName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getName()
Deprecated.
call [`getUri()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getUri\(\)) instead.

Returns:
    uri to string.
    * ### getNamed
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") getNamed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
call [`get(URI, Configuration)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#get\(java.net.URI,org.apache.hadoop.conf.Configuration\)) instead.

Parameters:
     `name` - name.      `conf` - configuration.

Returns:
    file system.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.
    * ### getLocal
public static [LocalFileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocalFileSystem.html "class in org.apache.hadoop.fs") getLocal([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get the local FileSystem.

Parameters:
     `conf` - the configuration to configure the FileSystem with if it is newly instantiated.

Returns:
    a LocalFileSystem

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if somehow the local FS cannot be instantiated.
    * ### get
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") get([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get a FileSystem for this URI's scheme and authority.
      1. If the configuration has the property `"fs.$SCHEME.impl.disable.cache"` set to true, a new instance will be created, initialized with the supplied URI and configuration, then returned without being cached.
      2. If the there is a cached FS instance matching the same URI, it will be returned.
      3. Otherwise: a new FS instance will be created, initialized with the configuration and URI, cached and returned to the caller.

Parameters:
     `uri` - uri of the filesystem.      `conf` - configrution.

Returns:
    filesystem instance.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if the FileSystem cannot be instantiated.
    * ### newInstance
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") newInstance([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") user) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")
Returns the FileSystem for this URI's scheme and authority and the given user. Internally invokes [`newInstance(URI, Configuration)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#newInstance\(java.net.URI,org.apache.hadoop.conf.Configuration\))

Parameters:
     `uri` - uri of the filesystem.      `conf` - the configuration to use      `user` - to perform the get as

Returns:
    filesystem instance

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if the FileSystem cannot be instantiated.      `InterruptedException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")` - If the `UGI.doAs()` call was somehow interrupted.
    * ### newInstance
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") newInstance([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html "class or interface in java.net") uri, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") config) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns the FileSystem for this URI's scheme and authority. The entire URI is passed to the FileSystem instance's initialize method. This always returns a new FileSystem object.

Parameters:
     `uri` - FS URI      `config` - configuration to use

Returns:
    the new FS instance

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - FS creation or initialization failure.
    * ### newInstance
public static [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") newInstance([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns a unique configured FileSystem implementation for the default filesystem of the supplied configuration. This always returns a new FileSystem object.

Parameters:
     `conf` - the configuration to use

Returns:
    the new FS instance

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - FS creation or initialization failure.
    * ### newInstanceLocal
public static [LocalFileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocalFileSystem.html "class in org.apache.hadoop.fs") newInstanceLocal([Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get a unique local FileSystem object.

Parameters:
     `conf` - the configuration to configure the FileSystem with

Returns:
    a new LocalFileSystem object.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - FS creation or initialization failure.
    * ### closeAll
public static void closeAll() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Close all cached FileSystem instances. After this operation, they may not be used in any operations.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - a problem arose closing one or more filesystem.
    * ### closeAllForUGI
public static void closeAllForUGI([UserGroupInformation](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/UserGroupInformation.html "class in org.apache.hadoop.security") ugi) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Close all cached FileSystem instances for a given UGI. Be sure those filesystems are not used anymore.

Parameters:
     `ugi` - user group info to close

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - a problem arose closing one or more filesystem.
    * ### makeQualified
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") makeQualified([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Qualify a path to one which uses this FileSystem and, if relative, made absolute.

Parameters:
     `path` - to qualify.

Returns:
    this path if it contains a scheme and authority and is absolute, or a new path that includes a path and authority and is fully qualified

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - if the path has a schema/URI different from this FileSystem.

See Also:

      * `Path.makeQualified(URI, Path)`
    * ### getDelegationToken
@Private public [Token](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/token/Token.html "class in org.apache.hadoop.security.token")<?> getDelegationToken([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") renewer) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get a new delegation token for this FileSystem. This is an internal method that should have been declared protected but wasn't historically. Callers should use `DelegationTokenIssuer.addDelegationTokens(String, Credentials)`

Specified by:
     `getDelegationToken` in interface `org.apache.hadoop.security.token.DelegationTokenIssuer`

Parameters:
     `renewer` - the account name that is allowed to renew the token.

Returns:
    a new delegation token or null if the FS does not support tokens.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - on any problem obtaining a token
    * ### getChildFileSystems
@LimitedPrivate("HDFS") @VisibleForTesting public [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")[] getChildFileSystems()
Get all the immediate child FileSystems embedded in this FileSystem. It does not recurse and get grand children. If a FileSystem has multiple child FileSystems, then it must return a unique list of those FileSystems. Default is to return null to signify no children.

Returns:
    FileSystems that are direct children of this FileSystem, or null for "no children"
    * ### getAdditionalTokenIssuers
@Private public org.apache.hadoop.security.token.DelegationTokenIssuer[] getAdditionalTokenIssuers() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Description copied from interface: `org.apache.hadoop.security.token.DelegationTokenIssuer`
Issuers may need tokens from additional services.

Specified by:
     `getAdditionalTokenIssuers` in interface `org.apache.hadoop.security.token.DelegationTokenIssuer`

Returns:
    delegation token issuer.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### create
public static [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fs, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") file, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a file with the provided permission. The permission of the file is set to be the provided permission as in setPermission, not permission&~umask The HDFS implementation is implemented using two RPCs. It is understood that it is inefficient, but the implementation is thread-safe. The other option is to change the value of umask in configuration to be 0, but it is not thread-safe.

Parameters:
     `fs` - FileSystem      `file` - the name of the file to be created      `permission` - the permission of the file

Returns:
    an output stream

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### mkdirs
public static boolean mkdirs([FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fs, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dir, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a directory with the provided permission. The permission of the directory is set to be the provided permission as in setPermission, not permission&~umask

Parameters:
     `fs` - FileSystem handle      `dir` - the name of the directory to be created      `permission` - the permission of the directory

Returns:
    true if the directory creation succeeds; false otherwise

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - A problem creating the directories.

See Also:

      * [`create(FileSystem, Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#create\(org.apache.hadoop.fs.FileSystem,org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### checkPath
protected void checkPath([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Check that a Path belongs to this FileSystem. The base implementation performs case insensitive equality checks of the URIs' schemes and authorities. Subclasses may implement slightly different checks.

Parameters:
     `path` - to check

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - if the path is not considered to be part of this FileSystem.
    * ### getFileBlockLocations
public [BlockLocation](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockLocation.html "class in org.apache.hadoop.fs")[] getFileBlockLocations([FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") file, long start, long len) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return an array containing hostnames, offset and size of portions of the given file. For nonexistent file or regions, `null` is returned.
```
   if f == null :
     result = null
   elif f.getLen() <= start:
     result = []
   else result = [ locations(FS, b) for b in blocks(FS, p, s, s+l)]

```
This call is most helpful with and distributed filesystem where the hostnames of machines that contain blocks of the given file can be determined. The default implementation returns an array containing one element:
```
 BlockLocation( { "localhost:9866" },  { "localhost" }, 0, file.getLen())

```
In HDFS, if file is three-replicated, the returned array contains elements like:
```
 BlockLocation(offset: 0, length: BLOCK_SIZE,
   hosts: {"host1:9866", "host2:9866, host3:9866"})
 BlockLocation(offset: BLOCK_SIZE, length: BLOCK_SIZE,
   hosts: {"host2:9866", "host3:9866, host4:9866"})

```
And if a file is erasure-coded, the returned BlockLocation are logical block groups. Suppose we have a RS_3_2 coded file (3 data units and 2 parity units). 1. If the file size is less than one stripe size, say 2 * CELL_SIZE, then there will be one BlockLocation returned, with 0 offset, actual file size and 4 hosts (2 data blocks and 2 parity blocks) hosting the actual blocks. 3. If the file size is less than one group size but greater than one stripe size, then there will be one BlockLocation returned, with 0 offset, actual file size with 5 hosts (3 data blocks and 2 parity blocks) hosting the actual blocks. 4. If the file size is greater than one group size, 3 * BLOCK_SIZE + 123 for example, then the result will be like:
```
 BlockLocation(offset: 0, length: 3 * BLOCK_SIZE, hosts: {"host1:9866",
   "host2:9866","host3:9866","host4:9866","host5:9866"})
 BlockLocation(offset: 3 * BLOCK_SIZE, length: 123, hosts: {"host1:9866",
   "host4:9866", "host5:9866"})

```

Parameters:
     `file` - FilesStatus to get data from      `start` - offset into the given file      `len` - length for which to get locations for

Returns:
    block location array.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getFileBlockLocations
public [BlockLocation](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockLocation.html "class in org.apache.hadoop.fs")[] getFileBlockLocations([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p, long start, long len) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return an array containing hostnames, offset and size of portions of the given file. For a nonexistent file or regions, `null` is returned. This call is most helpful with location-aware distributed filesystems, where it returns hostnames of machines that contain the given file. A FileSystem will normally return the equivalent result of passing the `FileStatus` of the path to [`getFileBlockLocations(FileStatus, long, long)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileBlockLocations\(org.apache.hadoop.fs.FileStatus,long,long\))

Parameters:
     `p` - path is used to identify an FS since an FS could have another FS that it could be delegating the call to      `start` - offset into the given file      `len` - length for which to get locations for

Returns:
    block location array.

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getServerDefaults
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public [FsServerDefaults](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsServerDefaults.html "class in org.apache.hadoop.fs") getServerDefaults() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
use [`getServerDefaults(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getServerDefaults\(org.apache.hadoop.fs.Path\)) instead
Return a set of server default configuration values.

Returns:
    server default configuration values

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getServerDefaults
public [FsServerDefaults](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsServerDefaults.html "class in org.apache.hadoop.fs") getServerDefaults([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return a set of server default configuration values.

Parameters:
     `p` - path is used to identify an FS since an FS could have another FS that it could be delegating the call to

Returns:
    server default configuration values

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### resolvePath
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") resolvePath([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return the fully-qualified path of path, resolving the path through any symlinks or mount point.

Parameters:
     `p` - path to be resolved

Returns:
    fully qualified path

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path is not present      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - for any other error
    * ### open
public abstract [FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs") open([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, int bufferSize) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Opens an FSDataInputStream at the indicated Path.

Parameters:
     `f` - the file name to open      `bufferSize` - the size of the buffer to be used.

Returns:
    input stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### open
public [FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs") open([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Opens an FSDataInputStream at the indicated Path.

Parameters:
     `f` - the file to open

Returns:
    input stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### open
public [FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs") open([PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") fd) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Open an FSDataInputStream matching the PathHandle instance. The implementation may encode metadata in PathHandle to address the resource directly and verify that the resource referenced satisfies constraints specified at its construciton.

Parameters:
     `fd` - PathHandle object returned by the FS authority.

Returns:
    input stream.

Throws:
     `InvalidPathHandleException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/InvalidPathHandleException.html "class in org.apache.hadoop.fs")` - If [`PathHandle`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") constraints are not satisfied      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - If [`open(PathHandle, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.PathHandle,int\)) not overridden by subclass
    * ### open
public [FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs") open([PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") fd, int bufferSize) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Open an FSDataInputStream matching the PathHandle instance. The implementation may encode metadata in PathHandle to address the resource directly and verify that the resource referenced satisfies constraints specified at its construciton.

Parameters:
     `fd` - PathHandle object returned by the FS authority.      `bufferSize` - the size of the buffer to use

Returns:
    input stream.

Throws:
     `InvalidPathHandleException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/InvalidPathHandleException.html "class in org.apache.hadoop.fs")` - If [`PathHandle`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") constraints are not satisfied      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - If not overridden by subclass
    * ### getPathHandle
public final [PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") getPathHandle([FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") stat, org.apache.hadoop.fs.Options.HandleOpt... opt)
Create a durable, serializable handle to the referent of the given entity.

Parameters:
     `stat` - Referent in the target FileSystem      `opt` - If absent, assume `Options.HandleOpt.path()`.

Returns:
    path handle.

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - If the FileStatus does not belong to this FileSystem      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - If [`createPathHandle(org.apache.hadoop.fs.FileStatus, org.apache.hadoop.fs.Options.HandleOpt...)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#createPathHandle\(org.apache.hadoop.fs.FileStatus,org.apache.hadoop.fs.Options.HandleOpt...\)) not overridden by subclass.      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - If this FileSystem cannot enforce the specified constraints.
    * ### createPathHandle
protected [PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") createPathHandle([FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") stat, org.apache.hadoop.fs.Options.HandleOpt... opt)
Hook to implement support for [`PathHandle`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") operations.

Parameters:
     `stat` - Referent in the target FileSystem      `opt` - Constraints that determine the validity of the [`PathHandle`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") reference.

Returns:
    path handle.
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path. Files are overwritten by default.

Parameters:
     `f` - the file to create

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path.

Parameters:
     `f` - the file to create      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an exception will be thrown.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with write-progress reporting. Files are overwritten by default.

Parameters:
     `f` - the file to create      `progress` - to report progress

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, short replication) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path. Files are overwritten by default.

Parameters:
     `f` - the file to create      `replication` - the replication factor

Returns:
    output stream1

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, short replication, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with write-progress reporting. Files are overwritten by default.

Parameters:
     `f` - the file to create      `replication` - the replication factor      `progress` - to report progress

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite, int bufferSize) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path.

Parameters:
     `f` - the file to create      `overwrite` - if a path with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite, int bufferSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an [`FSDataOutputStream`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") at the indicated Path with write-progress reporting. The frequency of callbacks is implementation-specific; it may be "none".

Parameters:
     `f` - the path of the file to open      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `progress` - to report progress.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite, int bufferSize, short replication, long blockSize) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path.

Parameters:
     `f` - the file name to open      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - the size of the buffer to be used.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with write-progress reporting.

Parameters:
     `f` - the file name to open      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - the size of the buffer to be used.      `progress` - to report progress.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### create
public abstract [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission, boolean overwrite, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with write-progress reporting.

Parameters:
     `f` - the file name to open      `permission` - file permission      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission, [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<[CreateFlag](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with write-progress reporting.

Parameters:
     `f` - the file name to open      `permission` - file permission      `flags` - [`CreateFlag`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")s to use for this stream.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### create
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") create([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission, [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<[CreateFlag](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress, org.apache.hadoop.fs.Options.ChecksumOpt checksumOpt) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create an FSDataOutputStream at the indicated Path with a custom checksum option.

Parameters:
     `f` - the file name to open      `permission` - file permission      `flags` - [`CreateFlag`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")s to use for this stream.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter      `checksumOpt` - checksum parameter. If null, the values found in conf will be used.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### primitiveCreate
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") protected [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") primitiveCreate([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission, [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<[CreateFlag](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flag, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress, org.apache.hadoop.fs.Options.ChecksumOpt checksumOpt) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
This create has been added to support the FileContext that processes the permission with umask before calling this method. This a temporary method added to support the transition from FileSystem to FileContext for user applications.

Parameters:
     `f` - path.      `absolutePermission` - permission.      `flag` - create flag.      `bufferSize` - buffer size.      `replication` - replication.      `blockSize` - block size.      `progress` - progress.      `checksumOpt` - check sum opt.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### primitiveMkdir
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") protected boolean primitiveMkdir([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
This version of the mkdirs method assumes that the permission is absolute. It has been added to support the FileContext that processes the permission with umask before calling this method. This a temporary method added to support the transition from FileSystem to FileContext for user applications.

Parameters:
     `f` - path      `absolutePermission` - permissions

Returns:
    true if the directory was actually created.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`mkdirs(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### primitiveMkdir
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") protected void primitiveMkdir([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") absolutePermission, boolean createParent) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
This version of the mkdirs method assumes that the permission is absolute. It has been added to support the FileContext that processes the permission with umask before calling this method. This a temporary method added to support the transition from FileSystem to FileContext for user applications.

Parameters:
     `f` - the path.      `absolutePermission` - permission.      `createParent` - create parent.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure.
    * ### createNonRecursive
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") createNonRecursive([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean overwrite, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Opens an FSDataOutputStream at the indicated Path with write-progress reporting. Same as create(), except fails if parent directory doesn't already exist.

Parameters:
     `f` - the file name to open      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### createNonRecursive
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") createNonRecursive([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission, boolean overwrite, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Opens an FSDataOutputStream at the indicated Path with write-progress reporting. Same as create(), except fails if parent directory doesn't already exist.

Parameters:
     `f` - the file name to open      `permission` - file permission      `overwrite` - if a file with this name already exists, then if true, the file will be overwritten, and if false an error will be thrown.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### createNonRecursive
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") createNonRecursive([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission, [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<[CreateFlag](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")> flags, int bufferSize, short replication, long blockSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Opens an FSDataOutputStream at the indicated Path with write-progress reporting. Same as create(), except fails if parent directory doesn't already exist.

Parameters:
     `f` - the file name to open      `permission` - file permission      `flags` - [`CreateFlag`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/CreateFlag.html "enum class in org.apache.hadoop.fs")s to use for this stream.      `bufferSize` - the size of the buffer to be used.      `replication` - required block replication for the file.      `blockSize` - block size      `progress` - the progress reporter

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure

See Also:

      * [`setPermission(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#setPermission\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\))
    * ### createNewFile
public boolean createNewFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Creates the given Path as a brand-new zero-length file. If create fails, or if it already existed, return false. _Important: the default implementation is not atomic_

Parameters:
     `f` - path to use for create

Returns:
    if create new file success true,not false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### append
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") append([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Append to an existing file (optional operation). Same as `append(f, getConf().getInt(IO_FILE_BUFFER_SIZE_KEY,      IO_FILE_BUFFER_SIZE_DEFAULT), null)`

Parameters:
     `f` - the existing file to be appended.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### append
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") append([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, int bufferSize) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Append to an existing file (optional operation). Same as append(f, bufferSize, null).

Parameters:
     `f` - the existing file to be appended.      `bufferSize` - the size of the buffer to be used.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### append
public abstract [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") append([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, int bufferSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Append to an existing file (optional operation).

Parameters:
     `f` - the existing file to be appended.      `bufferSize` - the size of the buffer to be used.      `progress` - for reporting progress if it is not null.

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### append
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") append([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean appendToNewBlock) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Append to an existing file (optional operation).

Parameters:
     `f` - the existing file to be appended.      `appendToNewBlock` - whether to append data to a new block instead of the end of the last partial block

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### append
public [FSDataOutputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStream.html "class in org.apache.hadoop.fs") append([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, int bufferSize, [Progressable](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/util/Progressable.html "interface in org.apache.hadoop.util") progress, boolean appendToNewBlock) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Append to an existing file (optional operation). This function is used for being overridden by some FileSystem like DistributedFileSystem

Parameters:
     `f` - the existing file to be appended.      `bufferSize` - the size of the buffer to be used.      `progress` - for reporting progress if it is not null.      `appendToNewBlock` - whether to append data to a new block instead of the end of the last partial block

Returns:
    output stream.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### concat
public void concat([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") trg, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] psrcs) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Concat existing files together.

Parameters:
     `trg` - the path to the target destination.      `psrcs` - the paths to the sources to use for the concatenation.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### getReplication
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public short getReplication([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
Get the replication factor.

Parameters:
     `src` - file name

Returns:
    file replication

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path does not resolve.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - an IO failure
    * ### setReplication
public boolean setReplication([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, short replication) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set the replication for an existing file. If a filesystem does not support replication, it will always return true: the check for a file existing may be bypassed. This is the default behavior.

Parameters:
     `src` - file name      `replication` - new replication

Returns:
    true if successful, or the feature in unsupported; false if replication is supported but the file does not exist, or is a directory

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - an IO failure.
    * ### rename
public abstract boolean rename([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Renames Path src to Path dst.

Parameters:
     `src` - path to be renamed      `dst` - new path after rename

Returns:
    true if rename is successful

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - on failure
    * ### rename
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") protected void rename([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst, [Options.Rename](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Options.Rename.html "enum class in org.apache.hadoop.fs")... options) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Renames Path src to Path dst
      * Fails if src is a file and dst is a directory.
      * Fails if src is a directory and dst is a file.
      * Fails if the parent of dst does not exist or is a file.
If OVERWRITE option is not passed as an argument, rename fails if the dst already exists.
If OVERWRITE option is passed as an argument, rename overwrites the dst if it is a file or an empty directory. Rename fails if dst is a non-empty directory.
Note that atomicity of rename is dependent on the file system implementation. Please refer to the file system documentation for details. This default implementation is non atomic.
This method is deprecated since it is a temporary method added to support the transition from FileSystem to FileContext for user applications.

Parameters:
     `src` - path to be renamed      `dst` - new path after rename      `options` - rename options.

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - src path does not exist, or the parent path of dst does not exist.      `FileAlreadyExistsException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileAlreadyExistsException.html "class in org.apache.hadoop.fs")` - dest path exists and is a file      `ParentNotDirectoryException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ParentNotDirectoryException.html "class in org.apache.hadoop.fs")` - if the parent path of dest is not a directory      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - on failure
    * ### truncate
public boolean truncate([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, long newLength) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Truncate the file in the indicated path to the indicated size.
      * Fails if path is a directory.
      * Fails if path does not exist.
      * Fails if path is not closed.
      * Fails if new size is greater than current size.

Parameters:
     `f` - The path to the file to be truncated      `newLength` - The size the file is to be truncated to

Returns:
     `true` if the file has been truncated to the desired `newLength` and is immediately available to be reused for write operations such as `append`, or `false` if a background process of adjusting the length of the last block has been started, and clients should wait for it to complete before proceeding with further file updates.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).
    * ### delete
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public boolean delete([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`delete(Path, boolean)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#delete\(org.apache.hadoop.fs.Path,boolean\)) instead.
Delete a file/directory.

Parameters:
     `f` - the path.

Returns:
    if delete success true, not false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure.
    * ### delete
public abstract boolean delete([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean recursive) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Delete a file.

Parameters:
     `f` - the path to delete.      `recursive` - if path is a directory and set to true, the directory is deleted else throws an exception. In case of a file the recursive can be set to either true or false.

Returns:
    true if delete is successful else false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### deleteOnExit
public boolean deleteOnExit([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Mark a path to be deleted when its FileSystem is closed. When the JVM shuts down cleanly, all cached FileSystem objects will be closed automatically. These the marked paths will be deleted as a result. If a FileSystem instance is not cached, i.e. has been created with `createFileSystem(URI, Configuration)`, then the paths will be deleted in when [`close()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#close\(\)) is called on that instance. The path must exist in the filesystem at the time of the method call; it does not have to exist at the time of JVM shutdown. Notes
      1. Clean shutdown of the JVM cannot be guaranteed.
      2. The time to shut down a FileSystem will depends on the number of files to delete. For filesystems where the cost of checking for the existence of a file/directory and the actual delete operation (for example: object stores) is high, the time to shutdown the JVM can be significantly extended by over-use of this feature.
      3. Connectivity problems with a remote filesystem may delay shutdown further, and may cause the files to not be deleted.

Parameters:
     `f` - the path to delete.

Returns:
    true if deleteOnExit is successful, otherwise false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### cancelDeleteOnExit
public boolean cancelDeleteOnExit([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)
Cancel the scheduled deletion of the path when the FileSystem is closed.

Parameters:
     `f` - the path to cancel deletion

Returns:
    true if the path was found in the delete-on-exit list.
    * ### processDeleteOnExit
protected void processDeleteOnExit()
Delete all paths that were marked as delete-on-exit. This recursively deletes all files and directories in the specified paths. The time to process this operation is `O(paths)`, with the actual time dependent on the time for existence and deletion operations to complete, successfully or not.
    * ### exists
public boolean exists([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Check if a path exists. It is highly discouraged to call this method back to back with other [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) calls, as this will involve multiple redundant RPC calls in HDFS.

Parameters:
     `f` - source path

Returns:
    true if the path exists

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### isDirectory
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public boolean isDirectory([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
True iff the named path is a directory. Note: Avoid using this method. Instead reuse the FileStatus returned by getFileStatus() or listStatus() methods.

Parameters:
     `f` - path to check

Returns:
    if f is directory true, not false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### isFile
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public boolean isFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
True iff the named path is a regular file. Note: Avoid using this method. Instead reuse the FileStatus returned by [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) or listStatus() methods.

Parameters:
     `f` - path to check

Returns:
    if f is file true, not false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getLength
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public long getLength([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead.
The number of bytes in a file.

Parameters:
     `f` - the path.

Returns:
    the number of bytes; 0 for a directory

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path does not resolve      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getContentSummary
public [ContentSummary](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ContentSummary.html "class in org.apache.hadoop.fs") getContentSummary([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return the [`ContentSummary`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ContentSummary.html "class in org.apache.hadoop.fs") of a given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").

Parameters:
     `f` - path to use

Returns:
    content summary.

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path does not resolve      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getQuotaUsage
public [QuotaUsage](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/QuotaUsage.html "class in org.apache.hadoop.fs") getQuotaUsage([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return the [`QuotaUsage`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/QuotaUsage.html "class in org.apache.hadoop.fs") of a given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").

Parameters:
     `f` - path to use

Returns:
    the quota usage

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### setQuota
public void setQuota([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, long namespaceQuota, long storagespaceQuota) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set quota for the given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").

Parameters:
     `src` - the target path to set quota for      `namespaceQuota` - the namespace quota (i.e., # of files/directories) to set      `storagespaceQuota` - the storage space quota to set

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### setQuotaByStorageType
public void setQuotaByStorageType([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [StorageType](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/StorageType.html "enum class in org.apache.hadoop.fs") type, long quota) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set per storage type quota for the given [`Path`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs").

Parameters:
     `src` - the target path to set storage type quota for      `type` - the storage type to set      `quota` - the quota to set for the given storage type

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### listStatus
public abstract [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] listStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
List the statuses of the files/directories in the given path if the path is a directory.
Does not guarantee to return the List of files/directories status in a sorted order.
Will not return null. Expect IOException upon access error.

Parameters:
     `f` - given path

Returns:
    the statuses of the files/directories in the given patch

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### listStatusBatch
@Private protected org.apache.hadoop.fs.FileSystem.DirectoryEntries listStatusBatch([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, byte[] token) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Given an opaque iteration token, return the next batch of entries in a directory. This is a private API not meant for use by end users.
This method should be overridden by FileSystem subclasses that want to use the generic [`listStatusIterator(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#listStatusIterator\(org.apache.hadoop.fs.Path\)) implementation.

Parameters:
     `f` - Path to list      `token` - opaque iteration token returned by previous call, or null if this is the first call.

Returns:
    directory entries.

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.
    * ### listCorruptFileBlocks
public org.apache.hadoop.fs.RemoteIterator<[Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")> listCorruptFileBlocks([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
List corrupted file blocks.

Parameters:
     `path` - the path.

Returns:
    an iterator over the corrupt files under the given path (may contain duplicates if a file has more than one corrupt block)

Throws:
     `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default).      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### listStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] listStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [PathFilter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Filter files/directories in the given path using the user-supplied path filter.
Does not guarantee to return the List of files/directories status in a sorted order.

Parameters:
     `f` - a path name      `filter` - the user-supplied path filter

Returns:
    an array of FileStatus objects for the files under the given path after applying the filter

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### listStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] listStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] files) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Filter files/directories in the given list of paths using default path filter.
Does not guarantee to return the List of files/directories status in a sorted order.

Parameters:
     `files` - a list of paths

Returns:
    a list of statuses for the files under the given paths after applying the filter default Path filter

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### listStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] listStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] files, [PathFilter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Filter files/directories in the given list of paths using user-supplied path filter.
Does not guarantee to return the List of files/directories status in a sorted order.

Parameters:
     `files` - a list of paths      `filter` - the user-supplied path filter

Returns:
    a list of statuses for the files under the given paths after applying the filter

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### globStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] globStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") pathPattern) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return all the files that match filePattern and are not checksum files. Results are sorted by their names.
A filename pattern is composed of _regular_ characters and _special pattern matching_ characters, which are:

` ? `
     Matches any single character.

` * `
     Matches zero or more characters.

` [_abc_] `
     Matches a single character from character set `{_a,b,c_}`.

` [_a_-_b_] `
     Matches a single character from the character range `{_a...b_}`. Note that character` _a_`must be lexicographically less than or equal to character` _b_`.

` [^_a_] `
     Matches a single character that is not from character set or range `{_a_}`. Note that the`^` character must occur immediately to the right of the opening bracket.

` \_c_ `
     Removes (escapes) any special meaning of character _c_.

` {ab,cd} `
     Matches a string from the string set `{_ab, cd_} `

` {ab,c{de,fh}} `
     Matches a string from the string set `{_ab, cde, cfh_}`

Parameters:
     `pathPattern` - a glob specifying a path pattern

Returns:
    an array of paths that match the path pattern

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### globStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] globStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") pathPattern, [PathFilter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return an array of [`FileStatus`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") objects whose path names match `pathPattern` and is accepted by the user-supplied path filter. Results are sorted by their path names.

Parameters:
     `pathPattern` - a glob specifying the path pattern      `filter` - a user-supplied path filter

Returns:
    null if `pathPattern` has no glob and the path does not exist an empty array if `pathPattern` has a glob and no path matches it else an array of [`FileStatus`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") objects matching the pattern

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if any I/O error occurs when fetching file status
    * ### listLocatedStatus
public org.apache.hadoop.fs.RemoteIterator<[LocatedFileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")> listLocatedStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
List the statuses of the files/directories in the given path if the path is a directory. Return the file's status and block locations If the path is a file. If a returned status is a file, it contains the file's block locations.

Parameters:
     `f` - is the path

Returns:
    an iterator that traverses statuses of the files/directories in the given path

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - If `f` does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred
    * ### listLocatedStatus
protected org.apache.hadoop.fs.RemoteIterator<[LocatedFileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")> listLocatedStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [PathFilter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathFilter.html "interface in org.apache.hadoop.fs") filter) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
List a directory. The returned results include its block location if it is a file The results are filtered by the given path filter

Parameters:
     `f` - a path      `filter` - a path filter

Returns:
    an iterator that traverses statuses of the files/directories in the given path

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if `f` does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if any I/O error occurred
    * ### listStatusIterator
public org.apache.hadoop.fs.RemoteIterator<[FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")> listStatusIterator([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns a remote iterator so that followup calls are made on demand while consuming the entries. Each FileSystem implementation should override this method and provide a more efficient implementation, if possible. Does not guarantee to return the iterator that traverses statuses of the files in a sorted order.

Parameters:
     `p` - target path

Returns:
    remote iterator

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if `p` does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if any I/O error occurred
    * ### listFiles
public org.apache.hadoop.fs.RemoteIterator<[LocatedFileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs")> listFiles([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, boolean recursive) throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
List the statuses and block locations of the files in the given path. Does not guarantee to return the iterator that traverses statuses of the files in a sorted order.
```
 If the path is a directory,
   if recursive is false, returns files in the directory;
   if recursive is true, return files in the subtree rooted at the path.
 If the path is a file, return the file's status and block locations.

```

Parameters:
     `f` - is the path      `recursive` - if the subdirectories need to be traversed recursively

Returns:
    an iterator that traverses statuses of the files

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist;      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### getHomeDirectory
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getHomeDirectory()
Return the current user's home directory in this FileSystem. The default implementation returns `"/user/$USER/"`.

Returns:
    the path.
    * ### setWorkingDirectory
public abstract void setWorkingDirectory([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") new_dir)
Set the current working directory for the given FileSystem. All relative paths will be resolved relative to it.

Parameters:
     `new_dir` - Path of new working directory
    * ### getWorkingDirectory
public abstract [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getWorkingDirectory()
Get the current working directory for the given FileSystem

Returns:
    the directory pathname
    * ### getInitialWorkingDirectory
protected [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getInitialWorkingDirectory()
Note: with the new FileContext class, getWorkingDirectory() will be removed. The working directory is implemented in FileContext. Some FileSystems like LocalFileSystem have an initial workingDir that we use as the starting workingDir. For other file systems like HDFS there is no built in notion of an initial workingDir.

Returns:
    if there is built in notion of workingDir then it is returned; else a null is returned.
    * ### mkdirs
public boolean mkdirs([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Call [`mkdirs(Path, FsPermission)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#mkdirs\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.permission.FsPermission\)) with default permission.

Parameters:
     `f` - path

Returns:
    true if the directory was created

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### mkdirs
public abstract boolean mkdirs([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Make the given file and all non-existent parents into directories. Has roughly the semantics of Unix @{code mkdir -p}. Existence of the directory hierarchy is not an error.

Parameters:
     `f` - path to create      `permission` - to apply to f

Returns:
    if mkdir success true, not false.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyFromLocalFile
public void copyFromLocalFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src file is on the local disk. Add it to filesystem at the given dst name and the source is kept intact afterwards

Parameters:
     `src` - path      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### moveFromLocalFile
public void moveFromLocalFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] srcs, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src files is on the local disk. Add it to filesystem at the given dst name, removing the source afterwards.

Parameters:
     `srcs` - source paths      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### moveFromLocalFile
public void moveFromLocalFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src file is on the local disk. Add it to the filesystem at the given dst name, removing the source afterwards.

Parameters:
     `src` - local path      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyFromLocalFile
public void copyFromLocalFile(boolean delSrc, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src file is on the local disk. Add it to the filesystem at the given dst name. delSrc indicates if the source should be removed

Parameters:
     `delSrc` - whether to delete the src      `src` - path      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure.
    * ### copyFromLocalFile
public void copyFromLocalFile(boolean delSrc, boolean overwrite, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs")[] srcs, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src files are on the local disk. Add it to the filesystem at the given dst name. delSrc indicates if the source should be removed

Parameters:
     `delSrc` - whether to delete the src      `overwrite` - whether to overwrite an existing file      `srcs` - array of paths which are source      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyFromLocalFile
public void copyFromLocalFile(boolean delSrc, boolean overwrite, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src file is on the local disk. Add it to the filesystem at the given dst name. delSrc indicates if the source should be removed

Parameters:
     `delSrc` - whether to delete the src      `overwrite` - whether to overwrite an existing file      `src` - path      `dst` - path

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyToLocalFile
public void copyToLocalFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Copy it a file from the remote filesystem to the local one.

Parameters:
     `src` - path src file in the remote filesystem      `dst` - path local destination

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### moveToLocalFile
public void moveToLocalFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Copy a file to the local filesystem, then delete it from the remote filesystem (if successfully copied).

Parameters:
     `src` - path src file in the remote filesystem      `dst` - path local destination

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyToLocalFile
public void copyToLocalFile(boolean delSrc, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Copy it a file from a remote filesystem to the local one. delSrc indicates if the src will be removed or not.

Parameters:
     `delSrc` - whether to delete the src      `src` - path src file in the remote filesystem      `dst` - path local destination

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### copyToLocalFile
public void copyToLocalFile(boolean delSrc, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") dst, boolean useRawLocalFileSystem) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The src file is under this filesystem, and the dst is on the local disk. Copy it from the remote filesystem to the local dst name. delSrc indicates if the src will be removed or not. useRawLocalFileSystem indicates whether to use RawLocalFileSystem as the local file system or not. RawLocalFileSystem is non checksumming, So, It will not create any crc files at local.

Parameters:
     `delSrc` - whether to delete the src      `src` - path      `dst` - path      `useRawLocalFileSystem` - whether to use RawLocalFileSystem as local file system or not.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - for any IO error
    * ### startLocalOutput
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") startLocalOutput([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") fsOutputFile, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") tmpLocalFile) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns a local file that the user can write output to. The caller provides both the eventual target name in this FileSystem and the local working file path. If this FileSystem is local, we write directly into the target. If the FileSystem is not local, we write into the tmp local area.

Parameters:
     `fsOutputFile` - path of output file      `tmpLocalFile` - path of local tmp file

Returns:
    the path.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### completeLocalOutput
public void completeLocalOutput([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") fsOutputFile, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") tmpLocalFile) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Called when we're all done writing to the target. A local FS will do nothing, because we've written to exactly the right place. A remote FS will copy the contents of tmpLocalFile to the correct target at fsOutputFile.

Parameters:
     `fsOutputFile` - path of output file      `tmpLocalFile` - path to local tmp file

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### close
public void close() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Close this FileSystem instance. Will release any held locks, delete all files queued for deletion through calls to [`deleteOnExit(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#deleteOnExit\(org.apache.hadoop.fs.Path\)), and remove this FS instance from the cache, if cached. After this operation, the outcome of any method call on this FileSystem instance, or any input/output stream created by it is _undefined_.

Specified by:
     `close[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `AutoCloseable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

Specified by:
     `close[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#close\(\) "class or interface in java.io")` in interface `Closeable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html "class or interface in java.io")`

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getUsed
public long getUsed() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return the total size of all files in the filesystem.

Returns:
    the number of path used.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getUsed
public long getUsed([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return the total size of all files from a specified path.

Parameters:
     `path` - the path.

Returns:
    the number of path content summary.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getBlockSize
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public long getBlockSize([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Deprecated.
Use [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) instead
Get the block size for a particular file.

Parameters:
     `f` - the filename

Returns:
    the number of bytes in a block

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path is not present      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getDefaultBlockSize
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public long getDefaultBlockSize()
Deprecated.
use [`getDefaultBlockSize(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultBlockSize\(org.apache.hadoop.fs.Path\)) instead
Return the number of bytes that large input files should be optimally be split into to minimize I/O time.

Returns:
    default block size.
    * ### getDefaultBlockSize
public long getDefaultBlockSize([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f)
Return the number of bytes that large input files should be optimally be split into to minimize I/O time. The given path will be used to locate the actual filesystem. The full path does not have to exist.

Parameters:
     `f` - path of file

Returns:
    the default block size for the path's filesystem
    * ### getDefaultReplication
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public short getDefaultReplication()
Deprecated.
use [`getDefaultReplication(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getDefaultReplication\(org.apache.hadoop.fs.Path\)) instead
Get the default replication.

Returns:
    the replication; the default value is "1".
    * ### getDefaultReplication
public short getDefaultReplication([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Get the default replication for a path. The given path will be used to locate the actual FileSystem to query. The full path does not have to exist.

Parameters:
     `path` - of the file

Returns:
    default replication for the path's filesystem
    * ### getFileStatus
public abstract [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") getFileStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return a file status object that represents the path.

Parameters:
     `f` - The path we want information from

Returns:
    a FileStatus object

Throws:
     `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### msync
public void msync() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [UnsupportedOperationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")
Synchronize client metadata state.
In some FileSystem implementations such as HDFS metadata synchronization is essential to guarantee consistency of read requests particularly in HA setting.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported.
    * ### access
@LimitedPrivate({"HDFS","Hive"}) public void access([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [FsAction](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsAction.html "enum class in org.apache.hadoop.fs.permission") mode) throws [AccessControlException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security"), [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Checks if the user can access a path. The mode specifies which access checks to perform. If the requested permissions are granted, then the method returns normally. If access is denied, then the method throws an [`AccessControlException`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security").
The default implementation calls [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) and checks the returned permissions against the requested permissions. Note that the [`getFileStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getFileStatus\(org.apache.hadoop.fs.Path\)) call will be subject to authorization checks. Typically, this requires search (execute) permissions on each directory in the path's prefix, but this is implementation-defined. Any file system that provides a richer authorization model (such as ACLs) may override the default implementation so that it checks against that model instead.
In general, applications should avoid using this method, due to the risk of time-of-check/time-of-use race conditions. The permissions on a file may change immediately after the access call returns. Most applications should prefer running specific file system actions as the desired user represented by a [`UserGroupInformation`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/UserGroupInformation.html "class in org.apache.hadoop.security").

Parameters:
     `path` - Path to check      `mode` - type of access to check

Throws:
     `AccessControlException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security")` - if access is denied      `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - if the path does not exist      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### fixRelativePart
protected [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") fixRelativePart([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p)
See `FileContext.fixRelativePart(org.apache.hadoop.fs.Path)`.

Parameters:
     `p` - the path.

Returns:
    relative part.
    * ### createSymlink
public void createSymlink([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") target, [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") link, boolean createParent) throws [AccessControlException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security"), [FileAlreadyExistsException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileAlreadyExistsException.html "class in org.apache.hadoop.fs"), [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [ParentNotDirectoryException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ParentNotDirectoryException.html "class in org.apache.hadoop.fs"), [UnsupportedFileSystemException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
See [`FileContext.createSymlink(Path, Path, boolean)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#createSymlink\(org.apache.hadoop.fs.Path,org.apache.hadoop.fs.Path,boolean\)).

Parameters:
     `target` - target path.      `link` - link.      `createParent` - create parent.

Throws:
     `AccessControlException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security")` - if access is denied.      `FileAlreadyExistsException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileAlreadyExistsException.html "class in org.apache.hadoop.fs")` - when the path does not exist.      `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist.      `ParentNotDirectoryException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/ParentNotDirectoryException.html "class in org.apache.hadoop.fs")` - if the parent path of dest is not a directory.      `UnsupportedFileSystemException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs")` - if there was no known implementation for the scheme.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.
    * ### getFileLinkStatus
public [FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs") getFileLinkStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [AccessControlException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security"), [FileNotFoundException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io"), [UnsupportedFileSystemException](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
See [`FileContext.getFileLinkStatus(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#getFileLinkStatus\(org.apache.hadoop.fs.Path\)).

Parameters:
     `f` - the path.

Returns:
    file status

Throws:
     `AccessControlException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/security/AccessControlException.html "class in org.apache.hadoop.security")` - if access is denied.      `FileNotFoundException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FileNotFoundException.html "class or interface in java.io")` - when the path does not exist.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - raised on errors performing I/O.      `UnsupportedFileSystemException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs")` - if there was no known implementation for the scheme.
    * ### supportsSymlinks
public boolean supportsSymlinks()
See [`AbstractFileSystem.supportsSymlinks()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/AbstractFileSystem.html#supportsSymlinks\(\)).

Returns:
    if support symlinkls true, not false.
    * ### getLinkTarget
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getLinkTarget([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
See [`FileContext.getLinkTarget(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileContext.html#getLinkTarget\(org.apache.hadoop.fs.Path\)).

Parameters:
     `f` - the path.

Returns:
    the path.

Throws:
     `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure.
    * ### resolveLink
protected [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") resolveLink([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
See [`AbstractFileSystem.getLinkTarget(Path)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/AbstractFileSystem.html#getLinkTarget\(org.apache.hadoop.fs.Path\)).

Parameters:
     `f` - the path.

Returns:
    the path.

Throws:
     `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure.
    * ### getFileChecksum
public [FileChecksum](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileChecksum.html "class in org.apache.hadoop.fs") getFileChecksum([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get the checksum of a file, if the FS supports checksums.

Parameters:
     `f` - The file path

Returns:
    The file checksum. The default return value is null, which indicates that no checksum algorithm is implemented in the corresponding FileSystem.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### getFileChecksum
public [FileChecksum](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileChecksum.html "class in org.apache.hadoop.fs") getFileChecksum([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") f, long length) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get the checksum of a file, from the beginning of the file till the specific length.

Parameters:
     `f` - The file path      `length` - The length of the file range for checksum calculation

Returns:
    The file checksum or null if checksums are not supported.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### setVerifyChecksum
public void setVerifyChecksum(boolean verifyChecksum)
Set the verify checksum flag. This is only applicable if the corresponding filesystem supports checksums. By default doesn't do anything.

Parameters:
     `verifyChecksum` - Verify checksum flag
    * ### setWriteChecksum
public void setWriteChecksum(boolean writeChecksum)
Set the write checksum flag. This is only applicable if the corresponding filesystem supports checksums. By default doesn't do anything.

Parameters:
     `writeChecksum` - Write checksum flag
    * ### getStatus
public [FsStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsStatus.html "class in org.apache.hadoop.fs") getStatus() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns a status object describing the use and capacity of the filesystem. If the filesystem has multiple partitions, the use and capacity of the root partition is reflected.

Returns:
    a FsStatus object

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### getStatus
public [FsStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FsStatus.html "class in org.apache.hadoop.fs") getStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Returns a status object describing the use and capacity of the filesystem. If the filesystem has multiple partitions, the use and capacity of the partition pointed to by the specified path is reflected.

Parameters:
     `p` - Path for which status should be obtained. null means the default partition.

Returns:
    a FsStatus object

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - see specific implementation
    * ### setPermission
public void setPermission([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p, [FsPermission](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission") permission) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set permission of a path.

Parameters:
     `p` - The path      `permission` - permission

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### setOwner
public void setOwner([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") username, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") groupname) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set owner of a path (i.e. a file or a directory). The parameters username and groupname cannot both be null.

Parameters:
     `p` - The path      `username` - If it is null, the original username remains unchanged.      `groupname` - If it is null, the original groupname remains unchanged.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### setTimes
public void setTimes([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") p, long mtime, long atime) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set access time of a file.

Parameters:
     `p` - The path      `mtime` - Set the modification time of this file. The number of milliseconds since Jan 1, 1970. A value of -1 means that this call should not set modification time.      `atime` - Set the access time of this file. The number of milliseconds since Jan 1, 1970. A value of -1 means that this call should not set access time.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure
    * ### createSnapshot
public final [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") createSnapshot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a snapshot with a default name.

Parameters:
     `path` - The directory where snapshots will be taken.

Returns:
    the snapshot path.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported
    * ### createSnapshot
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") createSnapshot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotName) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a snapshot.

Parameters:
     `path` - The directory where snapshots will be taken.      `snapshotName` - The name of the snapshot

Returns:
    the snapshot path.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported
    * ### renameSnapshot
public void renameSnapshot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotOldName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotNewName) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Rename a snapshot.

Parameters:
     `path` - The directory path where the snapshot was taken      `snapshotOldName` - Old name of the snapshot      `snapshotNewName` - New name of the snapshot

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### deleteSnapshot
public void deleteSnapshot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") snapshotName) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Delete a snapshot of a directory.

Parameters:
     `path` - The directory that the to-be-deleted snapshot belongs to      `snapshotName` - The name of the snapshot

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### modifyAclEntries
public void modifyAclEntries([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[AclEntry](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Modifies ACL entries of files and directories. This method can add new ACL entries or modify the permissions on existing ACL entries. All existing ACL entries that are not specified in this call are retained without changes. (Modifications are merged into the current ACL.)

Parameters:
     `path` - Path to modify      `aclSpec` - List<AclEntry> describing modifications

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be modified      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### removeAclEntries
public void removeAclEntries([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[AclEntry](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Removes ACL entries from files and directories. Other ACL entries are retained.

Parameters:
     `path` - Path to modify      `aclSpec` - List describing entries to remove

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be modified      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### removeDefaultAcl
public void removeDefaultAcl([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Removes all default ACL entries from files and directories.

Parameters:
     `path` - Path to modify

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be modified      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### removeAcl
public void removeAcl([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Removes all but the base ACL entries of files and directories. The entries for user, group, and others are retained for compatibility with permission bits.

Parameters:
     `path` - Path to modify

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be removed      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### setAcl
public void setAcl([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[AclEntry](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclEntry.html "class in org.apache.hadoop.fs.permission")> aclSpec) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Fully replaces ACL of files and directories, discarding all existing entries.

Parameters:
     `path` - Path to modify      `aclSpec` - List describing modifications, which must include entries for user, group, and others for compatibility with permission bits.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be modified      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getAclStatus
public [AclStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/permission/AclStatus.html "class in org.apache.hadoop.fs.permission") getAclStatus([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Gets the ACL of a file or directory.

Parameters:
     `path` - Path to get

Returns:
    AclStatus describing the ACL of the file or directory

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if an ACL could not be read      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### setXAttr
public void setXAttr([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, byte[] value) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set an xattr of a file or directory. The name must be prefixed with the namespace followed by ".". For example, "user.attr".
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to modify      `name` - xattr name.      `value` - xattr value.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### setXAttr
public void setXAttr([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, byte[] value, [EnumSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html "class or interface in java.util")<[XAttrSetFlag](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/XAttrSetFlag.html "enum class in org.apache.hadoop.fs")> flag) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set an xattr of a file or directory. The name must be prefixed with the namespace followed by ".". For example, "user.attr".
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to modify      `name` - xattr name.      `value` - xattr value.      `flag` - xattr set flag

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getXAttr
public byte[] getXAttr([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get an xattr name and value for a file or directory. The name must be prefixed with the namespace followed by ".". For example, "user.attr".
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to get extended attribute      `name` - xattr name.

Returns:
    byte[] xattr value.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getXAttrs
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),byte[]> getXAttrs([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get all of the xattr name/value pairs for a file or directory. Only those xattrs which the logged-in user has permissions to view are returned.
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to get extended attributes

Returns:
    Map describing the XAttrs of the file or directory

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getXAttrs
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),byte[]> getXAttrs([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> names) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get all of the xattrs name/value pairs for a file or directory. Only those xattrs which the logged-in user has permissions to view are returned.
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to get extended attributes      `names` - XAttr names.

Returns:
    Map describing the XAttrs of the file or directory

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### listXAttrs
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listXAttrs([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get all of the xattr names for a file or directory. Only those xattr names which the logged-in user has permissions to view are returned.
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to get extended attributes

Returns:
    List<String> of the XAttr names of the file or directory

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### removeXAttr
public void removeXAttr([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Remove an xattr of a file or directory. The name must be prefixed with the namespace followed by ".". For example, "user.attr".
Refer to the HDFS extended attributes user documentation for details.

Parameters:
     `path` - Path to remove extended attribute      `name` - xattr name

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### satisfyStoragePolicy
public void satisfyStoragePolicy([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set the source path to satisfy storage policy.

Parameters:
     `path` - The source path referring to either a directory or a file.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.
    * ### setStoragePolicy
public void setStoragePolicy([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") policyName) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Set the storage policy for a given file or directory.

Parameters:
     `src` - file or directory path.      `policyName` - the name of the target storage policy. The list of supported Storage policies can be retrieved via [`getAllStoragePolicies()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getAllStoragePolicies\(\)).

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### unsetStoragePolicy
public void unsetStoragePolicy([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Unset the storage policy set for a given file or directory.

Parameters:
     `src` - file or directory path.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getStoragePolicy
public [BlockStoragePolicySpi](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockStoragePolicySpi.html "interface in org.apache.hadoop.fs") getStoragePolicy([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") src) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Query the effective storage policy ID for the given file or directory.

Parameters:
     `src` - file or directory path.

Returns:
    storage policy for give file.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getAllStoragePolicies
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<? extends [BlockStoragePolicySpi](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BlockStoragePolicySpi.html "interface in org.apache.hadoop.fs")> getAllStoragePolicies() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Retrieve all the storage policies supported by this file system.

Returns:
    all storage policies supported by this filesystem.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - IO failure      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if the operation is unsupported (default outcome).
    * ### getTrashRoot
public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getTrashRoot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Get the root directory of Trash for current user when the path specified is deleted.

Parameters:
     `path` - the trash root of the path to be determined.

Returns:
    the default implementation returns `/user/$USER/.Trash`
    * ### getTrashRoots
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<[FileStatus](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")> getTrashRoots(boolean allUsers)
Get all the trash roots for current user or all users.

Parameters:
     `allUsers` - return trash roots for all users if true.

Returns:
    all the trash root directories. Default FileSystem returns .Trash under users' home directories if `/user/$USER/.Trash` exists.
    * ### hasPathCapability
public boolean hasPathCapability([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") capability) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
The base FileSystem implementation generally has no knowledge of the capabilities of actual implementations. Unless it has a way to explicitly determine the capabilities, this method returns false. Probe for a specific capability under the given path. If the function returns `true`, this instance is explicitly declaring that the capability is available. If the function returns `false`, it can mean one of:
      * The capability is not known.
      * The capability is known but it is not supported.
      * The capability is known but the filesystem does not know if it is supported under the supplied path.
The core guarantee which a caller can rely on is: if the predicate returns true, then the specific operation/behavior can be expected to be supported. However a specific call may be rejected for permission reasons, the actual file/directory not being present, or some other failure during the attempted execution of the operation.
Implementors: `PathCapabilitiesSupport` can be used to help implement this method.

Specified by:
     `hasPathCapability` in interface `org.apache.hadoop.fs.PathCapabilities`

Parameters:
     `path` - path to query the capability of.      `capability` - non-null, non-empty string to query the path for support.

Returns:
    true if the capability is supported under that part of the FS.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - this should not be raised, except on problems resolving paths or relaying the call.
    * ### getFileSystemClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")> getFileSystemClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") scheme, [Configuration](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf") conf) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Get the FileSystem implementation class of a filesystem. This triggers a scan and load of all FileSystem implementations listed as services and discovered via the [`ServiceLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ServiceLoader.html "class or interface in java.util")

Parameters:
     `scheme` - URL scheme of FS      `conf` - configuration: can be null, in which case the check for a filesystem binding declaration in the configuration is skipped.

Returns:
    the filesystem

Throws:
     `UnsupportedFileSystemException[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/UnsupportedFileSystemException.html "class in org.apache.hadoop.fs")` - if there was no known implementation for the scheme.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if the filesystem could not be loaded
    * ### getStatistics
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),org.apache.hadoop.fs.FileSystem.Statistics> getStatistics()
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
Get the Map of Statistics object indexed by URI Scheme.

Returns:
    a Map having a key as URI scheme and value as Statistics object
    * ### getAllStatistics
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<org.apache.hadoop.fs.FileSystem.Statistics> getAllStatistics()
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
Return the FileSystem classes that have Statistics.

Returns:
    statistics lists.
    * ### getStatistics
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public static org.apache.hadoop.fs.FileSystem.Statistics getStatistics([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") scheme, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs")> cls)
Deprecated.
use [`getGlobalStorageStatistics()`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#getGlobalStorageStatistics\(\))
Get the statistics for a particular file system.

Parameters:
     `scheme` - scheme.      `cls` - the class to lookup

Returns:
    a statistics object
    * ### clearStatistics
public static void clearStatistics()
Reset all statistics for all file systems.
    * ### printStatistics
public static void printStatistics() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Print all statistics for all file systems to `System.out`

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - If an I/O error occurred.
    * ### areSymlinksEnabled
@VisibleForTesting public static boolean areSymlinksEnabled()
    * ### enableSymlinks
@VisibleForTesting public static void enableSymlinks()
    * ### getStorageStatistics
public [StorageStatistics](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/StorageStatistics.html "class in org.apache.hadoop.fs") getStorageStatistics()
Get the StorageStatistics for this FileSystem object. These statistics are per-instance. They are not shared with any other FileSystem object.
This is a default method which is intended to be overridden by subclasses. The default implementation returns an empty storage statistics object.

Returns:
    The StorageStatistics for this FileSystem instance. Will never be null.
    * ### getGlobalStorageStatistics
public static [GlobalStorageStatistics](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/GlobalStorageStatistics.html "enum class in org.apache.hadoop.fs") getGlobalStorageStatistics()
Get the global storage statistics.

Returns:
    global storage statistics.
    * ### createDataOutputStreamBuilder
@Unstable protected static [FSDataOutputStreamBuilder](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs") createDataOutputStreamBuilder(@Nonnull [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem, @Nonnull [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Create instance of the standard FSDataOutputStreamBuilder for the given filesystem and path.

Parameters:
     `fileSystem` - owner      `path` - path to create

Returns:
    a builder.
    * ### createFile
public [FSDataOutputStreamBuilder](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs") createFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Create a new FSDataOutputStreamBuilder for the file with path. Files are overwritten by default.

Parameters:
     `path` - file path

Returns:
    a FSDataOutputStreamBuilder object to build the file HADOOP-14384. Temporarily reduce the visibility of method before the builder interface becomes stable.
    * ### appendFile
public [FSDataOutputStreamBuilder](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs") appendFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Create a Builder to append a file.

Parameters:
     `path` - file path.

Returns:
    a [`FSDataOutputStreamBuilder`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataOutputStreamBuilder.html "class in org.apache.hadoop.fs") to build file append request.
    * ### openFile
@Unstable public [FutureDataInputStreamBuilder](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FutureDataInputStreamBuilder.html "interface in org.apache.hadoop.fs") openFile([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [UnsupportedOperationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")
Open a file for reading through a builder API. Ultimately calls [`open(Path, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path,int\)) unless a subclass executes the open command differently. The semantics of this call are therefore the same as that of [`open(Path, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path,int\)) with one special point: it is in `FSDataInputStreamBuilder.build()` in which the open operation takes place -it is there where all preconditions to the operation are checked.

Parameters:
     `path` - file path

Returns:
    a FSDataInputStreamBuilder object to build the input stream

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if some early checks cause IO failures.      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if support is checked early.
    * ### openFile
@Unstable public [FutureDataInputStreamBuilder](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FutureDataInputStreamBuilder.html "interface in org.apache.hadoop.fs") openFile([PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [UnsupportedOperationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")
Open a file for reading through a builder API. Ultimately calls [`open(PathHandle, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.PathHandle,int\)) unless a subclass executes the open command differently. If PathHandles are unsupported, this may fail in the `FSDataInputStreamBuilder.build()` command, rather than in this `openFile()` operation.

Parameters:
     `pathHandle` - path handle.

Returns:
    a FSDataInputStreamBuilder object to build the input stream

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if some early checks cause IO failures.      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if support is checked early.
    * ### openFileWithOptions
protected [CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class or interface in java.util.concurrent")<[FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")> openFileWithOptions([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path, org.apache.hadoop.fs.impl.OpenFileParameters parameters) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Execute the actual open file operation. This is invoked from `FSDataInputStreamBuilder.build()` and from `DelegateToFileSystem` and is where the action of opening the file should begin. The base implementation performs a blocking call to [`open(Path, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path,int\)) in this call; the actual outcome is in the returned `CompletableFuture`. This avoids having to create some thread pool, while still setting up the expectation that the `get()` call is needed to evaluate the result.

Parameters:
     `path` - path to the file      `parameters` - open file parameters from the builder.

Returns:
    a future which will evaluate to the opened file.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - failure to resolve the link.      `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - unknown mandatory key
    * ### openFileWithOptions
protected [CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class or interface in java.util.concurrent")<[FSDataInputStream](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FSDataInputStream.html "class in org.apache.hadoop.fs")> openFileWithOptions([PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle, org.apache.hadoop.fs.impl.OpenFileParameters parameters) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Execute the actual open file operation. The base implementation performs a blocking call to [`open(Path, int)`](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html#open\(org.apache.hadoop.fs.Path,int\)) in this call; the actual outcome is in the returned `CompletableFuture`. This avoids having to create some thread pool, while still setting up the expectation that the `get()` call is needed to evaluate the result.

Parameters:
     `pathHandle` - path to the file      `parameters` - open file parameters from the builder.

Returns:
    a future which will evaluate to the opened file.

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - failure to resolve the link.      `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - unknown mandatory key      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - PathHandles are not supported. This may be deferred until the future is evaluated.
    * ### createDataInputStreamBuilder
@LimitedPrivate("Filesystems") @Unstable protected static org.apache.hadoop.fs.FileSystem.FSDataInputStreamBuilder createDataInputStreamBuilder(@Nonnull [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem, @Nonnull [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path)
Create instance of the standard `FileSystem.FSDataInputStreamBuilder` for the given filesystem and path.

Parameters:
     `fileSystem` - owner      `path` - path to read

Returns:
    a builder.
    * ### createDataInputStreamBuilder
@LimitedPrivate("Filesystems") @Unstable protected static org.apache.hadoop.fs.FileSystem.FSDataInputStreamBuilder createDataInputStreamBuilder(@Nonnull [FileSystem](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") fileSystem, @Nonnull [PathHandle](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/PathHandle.html "interface in org.apache.hadoop.fs") pathHandle)
Create instance of the standard `FileSystem.FSDataInputStreamBuilder` for the given filesystem and path handle.

Parameters:
     `fileSystem` - owner      `pathHandle` - path handle of file to open.

Returns:
    a builder.
    * ### getEnclosingRoot
@Public @Unstable public [Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") getEnclosingRoot([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Return path of the enclosing root for a given path. The enclosing root path is a common ancestor that should be used for temp and staging dirs as well as within encryption zones and other restricted directories. Call makeQualified on the param path to ensure its part of the correct filesystem.

Parameters:
     `path` - file path to find the enclosing root path for

Returns:
    a path to the enclosing root

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - early checks like failure to resolve path cause IO failures
    * ### createMultipartUploader
@Unstable public org.apache.hadoop.fs.MultipartUploaderBuilder createMultipartUploader([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") basePath) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a multipart uploader.

Parameters:
     `basePath` - file path under which all files are uploaded

Returns:
    a MultipartUploaderBuilder object to build the uploader

Throws:
     `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if some early checks cause IO failures.      `UnsupportedOperationException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html "class or interface in java.lang")` - if support is checked early.
    * ### createBulkDelete
public [BulkDelete](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDelete.html "interface in org.apache.hadoop.fs") createBulkDelete([Path](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/Path.html "class in org.apache.hadoop.fs") path) throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang"), [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")
Create a bulk delete operation. The default implementation returns an instance of `DefaultBulkDeleteOperation`.

Specified by:
     `createBulkDelete[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDeleteSource.html#createBulkDelete\(org.apache.hadoop.fs.Path\))` in interface `BulkDeleteSource[](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/BulkDeleteSource.html "interface in org.apache.hadoop.fs")`

Parameters:
     `path` - base path for the operation.

Returns:
    an instance of the bulk delete.

Throws:
     `IllegalArgumentException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` - any argument is invalid.      `IOException[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` - if there is an IO problem.

* * *
Copyright © 2026 [Apache Software Foundation](https://www.apache.org). All rights reserved.
