[Fork me on GitHub](https://github.com/apache/maven-shade-plugin)
# [![](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
# [![](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
* * *
  * [Apache](https://www.apache.org/)/
  * [Maven](https://maven.apache.org/index.html)/
  * [Plugins](https://maven.apache.org/plugins/index.html)/
  * [Apache Maven Shade Plugin](https://maven.apache.org/plugins/maven-shade-plugin/index.html)/
  * Introduction [![Edit](https://maven.apache.org/plugins/maven-shade-plugin/images/accessories-text-editor.png)](https://github.com/apache/maven-shade-plugin/tree/maven-shade-plugin-3.6.2/src/site/apt/index.apt.vm)
  * | Last Published: 2026-03-02
  * Version: 3.6.2

  * Overview
  * Introduction
  * [Plugin Documentation](https://maven.apache.org/plugins/maven-shade-plugin/plugin-info.html)
    * [shade:shade](https://maven.apache.org/plugins/maven-shade-plugin/shade-mojo.html)
    * [shade:help](https://maven.apache.org/plugins/maven-shade-plugin/help-mojo.html)
  * [Usage](https://maven.apache.org/plugins/maven-shade-plugin/usage.html)
  * [FAQ](https://maven.apache.org/plugins/maven-shade-plugin/faq.html)
  * [License](https://www.apache.org/licenses/)
  * [Download](https://maven.apache.org/plugins/maven-shade-plugin/download.html)
  * Examples
  * [Selecting Contents for Uber JAR](https://maven.apache.org/plugins/maven-shade-plugin/examples/includes-excludes.html)
  * [Relocating Classes](https://maven.apache.org/plugins/maven-shade-plugin/examples/class-relocation.html)
  * [Attaching the Shaded Artifact](https://maven.apache.org/plugins/maven-shade-plugin/examples/attached-artifact.html)
  * [Executable JAR](https://maven.apache.org/plugins/maven-shade-plugin/examples/executable-jar.html)
  * [Resource Transformers](https://maven.apache.org/plugins/maven-shade-plugin/examples/resource-transformers.html)
  * [Using another Shader implementation](https://maven.apache.org/plugins/maven-shade-plugin/examples/use-shader-other-impl.html)
  * Project Documentation
  * [Project Information](https://maven.apache.org/plugins/maven-shade-plugin/project-info.html)
    * About
    * [Summary](https://maven.apache.org/plugins/maven-shade-plugin/summary.html)
    * [Maven Coordinates](https://maven.apache.org/plugins/maven-shade-plugin/dependency-info.html)
    * [Team](https://maven.apache.org/plugins/maven-shade-plugin/team.html)
    * [Source Code Management](https://maven.apache.org/plugins/maven-shade-plugin/scm.html)
    * [Issue Management](https://maven.apache.org/plugins/maven-shade-plugin/issue-management.html)
    * [Mailing Lists](https://maven.apache.org/plugins/maven-shade-plugin/mailing-lists.html)
    * [Dependency Management](https://maven.apache.org/plugins/maven-shade-plugin/dependency-management.html)
    * [Dependencies](https://maven.apache.org/plugins/maven-shade-plugin/dependencies.html)
    * [Dependency Convergence](https://maven.apache.org/plugins/maven-shade-plugin/dependency-convergence.html)
    * [CI Management](https://maven.apache.org/plugins/maven-shade-plugin/ci-management.html)
    * [Plugin Management](https://maven.apache.org/plugins/maven-shade-plugin/plugin-management.html)
    * [Plugins](https://maven.apache.org/plugins/maven-shade-plugin/plugins.html)
    * [Distribution Management](https://maven.apache.org/plugins/maven-shade-plugin/distribution-management.html)
  * [Project Reports](https://maven.apache.org/plugins/maven-shade-plugin/project-reports.html)
  * Maven Projects
  * [Maven](https://maven.apache.org/ref/current)
  * [Archetypes](https://maven.apache.org/archetypes/index.html)
  * [Extensions](https://maven.apache.org/extensions/index.html)
  * [Parent POMs](https://maven.apache.org/pom/index.html)
  * [Plugins](https://maven.apache.org/plugins/index.html)
  * [Skins](https://maven.apache.org/skins/index.html)
  * Components
    * [Archetype](https://maven.apache.org/archetype/index.html)
    * [Artifact Resolver](https://maven.apache.org/resolver/index.html)
    * [Doxia](https://maven.apache.org/doxia/index.html)
    * [Indexer](https://maven.apache.org/maven-indexer/index.html)
    * [JXR](https://maven.apache.org/jxr/index.html)
    * [Plugin Testing](https://maven.apache.org/plugin-testing/index.html)
    * [Plugin Tools](https://maven.apache.org/plugin-tools/index.html)
    * [Resource Bundles](https://maven.apache.org/apache-resource-bundles/index.html)
    * [SCM](https://maven.apache.org/scm/index.html)
    * [Shared Components](https://maven.apache.org/shared/index.html)
    * [Surefire](https://maven.apache.org/surefire/index.html)
    * [Wagon](https://maven.apache.org/wagon/index.html)
  * ASF
  * [How Apache Works](https://www.apache.org/foundation/how-it-works.html)
  * [Foundation](https://www.apache.org/foundation/)
  * [Data Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
  * [Sponsoring Apache](https://www.apache.org/foundation/sponsorship.html)
  * [Thanks](https://www.apache.org/foundation/thanks.html)

[![Built by Maven](https://maven.apache.org/plugins/maven-shade-plugin/images/logos/maven-feather.png)](https://maven.apache.org/)
# Apache Maven Shade Plugin
This plugin provides the capability to package the artifact in an uber-jar, including its dependencies and to _shade_ - i.e. rename - the packages of some of the dependencies.
## Goals Overview[](https://maven.apache.org/plugins/maven-shade-plugin/#goals-overview)
The Shade Plugin has a single goal:
  * [shade:shade](https://maven.apache.org/plugins/maven-shade-plugin/shade-mojo.html) is bound to the `package` phase and is used to create a shaded jar.

## Usage[](https://maven.apache.org/plugins/maven-shade-plugin/#usage)
General instructions on how to use the Shade Plugin can be found on the [usage page](https://maven.apache.org/plugins/maven-shade-plugin/usage.html). Some more specific use cases are described in the examples given below.
In case you still have questions regarding the plugin's usage, please feel free to contact the [user mailing list](https://maven.apache.org/plugins/maven-shade-plugin/mailing-lists.html). The posts to the mailing list are archived and could already contain the answer to your question as part of an older thread. Hence, it is also worth browsing/searching the [mail archive](https://maven.apache.org/plugins/maven-shade-plugin/mail-lists.html).
If you feel like the plugin is missing a feature or has a defect, you can fill a feature request or bug report in our [issue tracker](https://maven.apache.org/plugins/maven-shade-plugin/issue-management.html). When creating a new issue, please provide a comprehensive description of your concern. Especially for fixing bugs it is crucial that the developers can reproduce your problem. For this reason, entire debug logs, POMs or most preferably little demo projects attached to the issue are very much appreciated. Of course, patches are welcome, too. Contributors can check out the project from our [source repository](https://maven.apache.org/plugins/maven-shade-plugin/scm.html) and will find supplementary information in the [guide to helping with Maven](http://maven.apache.org/guides/development/guide-helping.html).
## Examples[](https://maven.apache.org/plugins/maven-shade-plugin/#examples)
To provide you with better understanding on some usages of the Shade Plugin, you can take a look into the following examples:
  * [Selecting Contents for Uber JAR](https://maven.apache.org/plugins/maven-shade-plugin/examples/includes-excludes.html)
  * [Relocating Classes](https://maven.apache.org/plugins/maven-shade-plugin/examples/class-relocation.html)
  * [Attaching the Shaded Artifact](https://maven.apache.org/plugins/maven-shade-plugin/examples/attached-artifact.html)
  * [Executable JAR](https://maven.apache.org/plugins/maven-shade-plugin/examples/executable-jar.html)
  * [Resource Transformers](https://maven.apache.org/plugins/maven-shade-plugin/examples/resource-transformers.html)
  * [Using another Shader implementation](https://maven.apache.org/plugins/maven-shade-plugin/examples/use-shader-other-impl.html)

* * *
© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
