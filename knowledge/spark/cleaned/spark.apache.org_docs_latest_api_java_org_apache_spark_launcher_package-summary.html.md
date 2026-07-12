[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.launcher
* * *
package org.apache.spark.launcher
Library for launching Spark applications programmatically.
There are two ways to start applications with this library: as a child process, using [`SparkLauncher`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkLauncher.html "class in org.apache.spark.launcher"), or in-process, using [`InProcessLauncher`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/InProcessLauncher.html "class in org.apache.spark.launcher").
The [`AbstractLauncher.startApplication(org.apache.spark.launcher.SparkAppHandle.Listener...)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/AbstractLauncher.html#startApplication\(org.apache.spark.launcher.SparkAppHandle.Listener...\)) method can be used to start Spark and provide a handle to monitor and control the running application:

```

   import org.apache.spark.launcher.SparkAppHandle;
   import org.apache.spark.launcher.SparkLauncher;

   public class MyLauncher {
     public static void main(String[] args) throws Exception {
       SparkAppHandle handle = new SparkLauncher()
         .setAppResource("/my/app.jar")
         .setMainClass("my.spark.app.Main")
         .setMaster("local")
         .setConf(SparkLauncher.DRIVER_MEMORY, "2g")
         .startApplication();
       // Use handle API to monitor / control application.
     }
   }

```

Launching applications as a child process requires a full Spark installation. The installation directory can be provided to the launcher explicitly in the launcher's configuration, or by setting the _SPARK_HOME_ environment variable.
Launching applications in-process is only recommended in cluster mode, since Spark cannot run multiple client-mode applications concurrently in the same process. The in-process launcher requires the necessary Spark dependencies (such as spark-core and cluster manager-specific modules) to be present in the caller thread's class loader.
It's also possible to launch a raw child process, without the extra monitoring, using the [`SparkLauncher.launch()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkLauncher.html#launch\(\)) method:

```

   import org.apache.spark.launcher.SparkLauncher;

   public class MyLauncher {
     public static void main(String[] args) throws Exception {
       Process spark = new SparkLauncher()
         .setAppResource("/my/app.jar")
         .setMainClass("my.spark.app.Main")
         .setMaster("local")
         .setConf(SparkLauncher.DRIVER_MEMORY, "2g")
         .launch();
       spark.waitFor();
     }
   }

```

This method requires the calling code to manually manage the child process, including its output streams (to avoid possible deadlocks). It's recommended that [`SparkLauncher.startApplication(org.apache.spark.launcher.SparkAppHandle.Listener...)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkLauncher.html#startApplication\(org.apache.spark.launcher.SparkAppHandle.Listener...\)) be used instead.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
  * All Classes and InterfacesInterfacesClassesEnum Classes
Class
Description
[AbstractLauncher](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/AbstractLauncher.html "class in org.apache.spark.launcher")<T extends [AbstractLauncher](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/AbstractLauncher.html "class in org.apache.spark.launcher")<T>>
Base class for launcher implementations.
[InProcessLauncher](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/InProcessLauncher.html "class in org.apache.spark.launcher")
In-process launcher for Spark applications.
[JavaModuleOptions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/JavaModuleOptions.html "class in org.apache.spark.launcher")
This helper class is used to place some JVM runtime options(eg: `--add-opens`) required by Spark when using Java 17.
[SparkAppHandle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkAppHandle.html "interface in org.apache.spark.launcher")
A handle to a running Spark application.
[SparkAppHandle.Listener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkAppHandle.Listener.html "interface in org.apache.spark.launcher")
Listener for updates to a handle's state.
[SparkAppHandle.State](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkAppHandle.State.html "enum class in org.apache.spark.launcher")
Represents the application's state.
[SparkLauncher](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkLauncher.html "class in org.apache.spark.launcher")
Launcher for Spark applications.
