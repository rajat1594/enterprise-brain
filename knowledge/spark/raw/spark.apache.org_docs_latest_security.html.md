[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/security.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/security.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/security.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/security.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

# Spark Security[](https://spark.apache.org/docs/latest/security.html#spark-security)
  * [Spark Security: Things You Need To Know](https://spark.apache.org/docs/latest/security.html#spark-security-things-you-need-to-know)
  * [Spark RPC (Communication protocol between Spark processes)](https://spark.apache.org/docs/latest/security.html#spark-rpc-communication-protocol-between-spark-processes)
    * [Authentication](https://spark.apache.org/docs/latest/security.html#authentication)
      * [YARN](https://spark.apache.org/docs/latest/security.html#yarn)
      * [Kubernetes](https://spark.apache.org/docs/latest/security.html#kubernetes)
  * [Network Encryption](https://spark.apache.org/docs/latest/security.html#network-encryption)
    * [SSL Encryption (Preferred)](https://spark.apache.org/docs/latest/security.html#ssl-encryption-preferred)
    * [AES-based Encryption (Legacy)](https://spark.apache.org/docs/latest/security.html#aes-based-encryption-legacy)
  * [Local Storage Encryption](https://spark.apache.org/docs/latest/security.html#local-storage-encryption)
  * [Web UI](https://spark.apache.org/docs/latest/security.html#web-ui)
    * [Authentication and Authorization](https://spark.apache.org/docs/latest/security.html#authentication-and-authorization)
    * [Spark History Server ACLs](https://spark.apache.org/docs/latest/security.html#spark-history-server-acls)
    * [SSL Configuration](https://spark.apache.org/docs/latest/security.html#ssl-configuration)
    * [Preparing the key stores](https://spark.apache.org/docs/latest/security.html#preparing-the-key-stores)
      * [YARN mode](https://spark.apache.org/docs/latest/security.html#yarn-mode)
      * [Standalone mode](https://spark.apache.org/docs/latest/security.html#standalone-mode)
    * [HTTP Security Headers](https://spark.apache.org/docs/latest/security.html#http-security-headers)
  * [Configuring Ports for Network Security](https://spark.apache.org/docs/latest/security.html#configuring-ports-for-network-security)
    * [Standalone mode only](https://spark.apache.org/docs/latest/security.html#standalone-mode-only)
    * [All cluster managers](https://spark.apache.org/docs/latest/security.html#all-cluster-managers)
  * [Kerberos](https://spark.apache.org/docs/latest/security.html#kerberos)
    * [Long-Running Applications](https://spark.apache.org/docs/latest/security.html#long-running-applications)
      * [Using a Keytab](https://spark.apache.org/docs/latest/security.html#using-a-keytab)
      * [Using a ticket cache](https://spark.apache.org/docs/latest/security.html#using-a-ticket-cache)
    * [Proxy User](https://spark.apache.org/docs/latest/security.html#proxy-user)
    * [Secure Interaction with Kubernetes](https://spark.apache.org/docs/latest/security.html#secure-interaction-with-kubernetes)
  * [Event Logging](https://spark.apache.org/docs/latest/security.html#event-logging)
  * [Persisting driver logs in client mode](https://spark.apache.org/docs/latest/security.html#persisting-driver-logs-in-client-mode)


# Spark Security: Things You Need To Know[](https://spark.apache.org/docs/latest/security.html#spark-security-things-you-need-to-know)
Security features like authentication are not enabled by default. When deploying a cluster that is open to the internet or an untrusted network, it’s important to secure access to the cluster to prevent unauthorized applications from running on the cluster.
Spark supports multiple deployments types and each one supports different levels of security. Not all deployment types will be secure in all environments and none are secure by default. Be sure to evaluate your environment, what Spark supports, and take the appropriate measure to secure your Spark deployment.
There are many different types of security concerns. Spark does not necessarily protect against all things. Listed below are some of the things Spark supports. Also check the deployment documentation for the type of deployment you are using for deployment specific settings. Anything not documented, Spark does not support.
# Spark RPC (Communication protocol between Spark processes)[](https://spark.apache.org/docs/latest/security.html#spark-rpc-communication-protocol-between-spark-processes)
## Authentication[](https://spark.apache.org/docs/latest/security.html#authentication)
Spark currently supports authentication for RPC channels using a shared secret. Authentication can be turned on by setting the `spark.authenticate` configuration parameter.
The exact mechanism used to generate and distribute the shared secret is deployment-specific. Unless specified below, the secret must be defined by setting the `spark.authenticate.secret` config option. The same secret is shared by all Spark applications and daemons in that case, which limits the security of these deployments, especially on multi-tenant clusters.
The REST Submission Server supports HTTP `Authorization` header with a cryptographically signed JSON Web Token via `JWSFilter`. To enable authorization, Spark Master should have `spark.master.rest.filters=org.apache.spark.ui.JWSFilter` and `spark.org.apache.spark.ui.JWSFilter.param.secretKey=BASE64URL-ENCODED-KEY` configurations, and client should provide HTTP `Authorization` header which contains JSON Web Token signed by the shared secret key.
### YARN[](https://spark.apache.org/docs/latest/security.html#yarn)
For Spark on [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html), Spark will automatically handle generating and distributing the shared secret. Each application will use a unique shared secret. In the case of YARN, this feature relies on YARN RPC encryption being enabled for the distribution of secrets to be secure.  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.yarn.shuffle.server.recovery.disabled`  | false  |  Set to true for applications that have higher security requirements and prefer that their secret is not saved in the db. The shuffle data of such applications will not be recovered after the External Shuffle Service restarts.   | 3.5.0  |  
### Kubernetes[](https://spark.apache.org/docs/latest/security.html#kubernetes)
On Kubernetes, Spark will also automatically generate an authentication secret unique to each application. The secret is propagated to executor pods using environment variables. This means that any user that can list pods in the namespace where the Spark application is running can also see their authentication secret. Access control rules should be properly set up by the Kubernetes admin to ensure that Spark authentication is secure.  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.authenticate`  | false  | Whether Spark authenticates its internal connections.  | 1.0.0  |  
| `spark.authenticate.secret`  | None  |  The secret key used authentication. See above for when this configuration should be set.   | 1.0.0  |  
Alternatively, one can mount authentication secrets using files and Kubernetes secrets that the user mounts into their pods.  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.authenticate.secret.file`  | None  |  Path pointing to the secret key to use for securing connections. Ensure that the contents of the file have been securely generated. This file is loaded on both the driver and the executors unless other settings override this (see below).   | 3.0.0  |  
| `spark.authenticate.secret.driver.file`  | The value of `spark.authenticate.secret.file`  |  When specified, overrides the location that the Spark driver reads to load the secret. Useful when in client mode, when the location of the secret file may differ in the pod versus the node the driver is running in. When this is specified, `spark.authenticate.secret.executor.file` must be specified so that the driver and the executors can both use files to load the secret key. Ensure that the contents of the file on the driver is identical to the contents of the file on the executors.   | 3.0.0  |  
| `spark.authenticate.secret.executor.file`  | The value of `spark.authenticate.secret.file`  |  When specified, overrides the location that the Spark executors read to load the secret. Useful in client mode, when the location of the secret file may differ in the pod versus the node the driver is running in. When this is specified, `spark.authenticate.secret.driver.file` must be specified so that the driver and the executors can both use files to load the secret key. Ensure that the contents of the file on the driver is identical to the contents of the file on the executors.   | 3.0.0  |  
Note that when using files, Spark will not mount these files into the containers for you. It is up you to ensure that the secret files are deployed securely into your containers and that the driver’s secret file agrees with the executors’ secret file.
# Network Encryption[](https://spark.apache.org/docs/latest/security.html#network-encryption)
Spark supports two mutually exclusive forms of encryption for RPC connections:
The **preferred method** uses TLS (aka SSL) encryption via Netty’s support for SSL. Enabling SSL requires keys and certificates to be properly configured. SSL is standardized and considered more secure.
The legacy method is an AES-based encryption mechanism relying on a shared secret. This requires RPC authentication to also be enabled. This method uses a bespoke protocol and it is recommended to use SSL instead.
One may prefer to use the SSL based encryption in scenarios where compliance mandates the usage of specific protocols; or to leverage the security of a more standard encryption library. However, the AES based encryption is simpler to configure and may be preferred if the only requirement is that data be encrypted in transit.
If both options are enabled in the configuration, the SSL based RPC encryption takes precedence and the AES based encryption will not be used (and a warning message will be emitted).
## SSL Encryption (Preferred)[](https://spark.apache.org/docs/latest/security.html#ssl-encryption-preferred)
Spark supports SSL based encryption for RPC connections. Please refer to the SSL Configuration section below to understand how to configure it. The SSL settings are mostly similar across the UI and RPC, however there are a few additional settings which are specific to the RPC implementation. The RPC implementation uses Netty under the hood (while the UI uses Jetty), which supports a different set of options.
Unlike the other SSL settings for the UI, the RPC SSL is _not_ automatically enabled if `spark.ssl.enabled` is set. It must be explicitly enabled, to ensure a safe migration path for users upgrading Spark versions.
## AES-based Encryption (Legacy)[](https://spark.apache.org/docs/latest/security.html#aes-based-encryption-legacy)
Spark supports AES-based encryption for RPC connections. For encryption to be enabled, RPC authentication must also be enabled and properly configured. AES encryption uses the [Apache Commons Crypto](https://commons.apache.org/proper/commons-crypto/) library, and Spark’s configuration system allows access to that library’s configuration for advanced users.
This legacy protocol has two mutually incompatible versions. Version 1 omits applying key derivation function (KDF) to the key exchange protocol’s output, while version 2 applies a KDF to ensure that the derived session key is uniformly distributed. Version 1 is default for backward compatibility. It is **recommended to use version 2** for better security properties. The version can be configured by setting `spark.network.crypto.authEngineVersion` to 1 or 2 respectively.
There is also support for SASL-based encryption, although it should be considered deprecated. It is still required when talking to shuffle services from Spark versions older than 2.2.0.
The following table describes the different options available for configuring this feature.  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.network.crypto.enabled`  | false  |  Enable AES-based RPC encryption, including the new authentication protocol added in 2.2.0.   | 2.2.0  |  
| `spark.network.crypto.cipher`  | AES/CTR/NoPadding  |  Cipher mode to use. Defaults "AES/CTR/NoPadding" for backward compatibility, which is not authenticated. Recommended to use "AES/GCM/NoPadding", which is an authenticated encryption mode.   | 4.0.0, 3.5.2, 3.4.4  |  
| `spark.network.crypto.authEngineVersion`  | 1  | Version of AES-based RPC encryption to use. Valid versions are 1 or 2. Version 2 is recommended.  | 4.0.0  |  
| `spark.network.crypto.config.*`  | None  |  Configuration values for the commons-crypto library, such as which cipher implementations to use. The config name should be the name of commons-crypto configuration without the `commons.crypto` prefix.   | 2.2.0  |  
| `spark.network.crypto.saslFallback`  | true  |  Whether to fall back to SASL authentication if authentication fails using Spark's internal mechanism. This is useful when the application is connecting to old shuffle services that do not support the internal Spark authentication protocol. On the shuffle service side, disabling this feature will block older clients from authenticating.   | 2.2.0  |  
| `spark.authenticate.enableSaslEncryption`  | false  |  Enable SASL-based encrypted communication.   | 2.2.0  |  
| `spark.network.sasl.serverAlwaysEncrypt`  | false  |  Disable unencrypted connections for ports using SASL authentication. This will deny connections from clients that have authentication enabled, but do not request SASL-based encryption.   | 1.4.0  |  
# Local Storage Encryption[](https://spark.apache.org/docs/latest/security.html#local-storage-encryption)
Spark supports encrypting temporary data written to local disks. This covers shuffle files, shuffle spills and data blocks stored on disk (for both caching and broadcast variables). It does not cover encrypting output data generated by applications with APIs such as `saveAsHadoopFile` or `saveAsTable`. It also may not cover temporary files created explicitly by the user.
The following settings cover enabling encryption for data written to disk:  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.io.encryption.enabled`  | false  |  Enable local disk I/O encryption. Currently supported by all modes. It's strongly recommended that RPC encryption be enabled when using this feature.   | 2.1.0  |  
| `spark.io.encryption.keySizeBits`  | 128  |  IO encryption key size in bits. Supported values are 128, 192 and 256.   | 2.1.0  |  
| `spark.io.encryption.keygen.algorithm`  | HmacSHA1  |  The algorithm to use when generating the IO encryption key. The supported algorithms are described in the KeyGenerator section of the Java Cryptography Architecture Standard Algorithm Name Documentation.   | 2.1.0  |  
| `spark.io.encryption.commons.config.*`  | None  |  Configuration values for the commons-crypto library, such as which cipher implementations to use. The config name should be the name of commons-crypto configuration without the `commons.crypto` prefix.   | 2.1.0  |  
# Web UI[](https://spark.apache.org/docs/latest/security.html#web-ui)
## Authentication and Authorization[](https://spark.apache.org/docs/latest/security.html#authentication-and-authorization)
Enabling authentication for the Web UIs is done using [jakarta servlet filters](https://jakarta.ee/specifications/servlet/5.0/apidocs/jakarta/servlet/filter). You will need a filter that implements the authentication method you want to deploy. Spark does not provide any built-in authentication filters.
Spark also supports access control to the UI when an authentication filter is present. Each application can be configured with its own separate access control lists (ACLs). Spark differentiates between “view” permissions (who is allowed to see the application’s UI), and “modify” permissions (who can do things like kill jobs in a running application).
ACLs can be configured for either users or groups. Configuration entries accept comma-separated lists as input, meaning multiple users or groups can be given the desired privileges. This can be used if you run on a shared cluster and have a set of administrators or developers who need to monitor applications they may not have started themselves. A wildcard (`*`) added to specific ACL means that all users will have the respective privilege. By default, only the user submitting the application is added to the ACLs.
Group membership is established by using a configurable group mapping provider. The mapper is configured using the `spark.user.groups.mapping` config option, described in the table below.
The following options control the authentication of Web UIs:  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.ui.allowFramingFrom`  | `SAMEORIGIN`  | Allow framing for a specific named URI via `X-Frame-Options`. By default, allow only from the same origin.  | 1.6.0  |  
| `spark.ui.filters`  | None  |  Spark supports HTTP `Authorization` header with a cryptographically signed JSON Web Token via `org.apache.spark.ui.JWSFilter`.   
See the [Spark UI](https://spark.apache.org/docs/latest/configuration.html#spark-ui) configuration for how to configure filters.   | 1.0.0  |  
| `spark.acls.enable`  | false  |  Whether UI ACLs should be enabled. If enabled, this checks to see if the user has access permissions to view or modify the application. Note this requires the user to be authenticated, so if no authentication filter is installed, this option does not do anything.   | 1.1.0  |  
| `spark.admin.acls`  | None  |  Comma-separated list of users that have view and modify access to the Spark application.   | 1.1.0  |  
| `spark.admin.acls.groups`  | None  |  Comma-separated list of groups that have view and modify access to the Spark application.   | 2.0.0  |  
| `spark.modify.acls`  | None  |  Comma-separated list of users that have modify access to the Spark application.   | 1.1.0  |  
| `spark.modify.acls.groups`  | None  |  Comma-separated list of groups that have modify access to the Spark application.   | 2.0.0  |  
| `spark.ui.view.acls`  | None  |  Comma-separated list of users that have view access to the Spark application.   | 1.0.0  |  
| `spark.ui.view.acls.groups`  | None  |  Comma-separated list of groups that have view access to the Spark application.   | 2.0.0  |  
| `spark.user.groups.mapping`  | `org.apache.spark.security.ShellBasedGroupsMappingProvider`  |  The list of groups for a user is determined by a group mapping service defined by the trait `org.apache.spark.security.GroupMappingServiceProvider`, which can be configured by this property.   
By default, a Unix shell-based implementation is used, which collects this information from the host OS.   
_Note:_ This implementation supports only Unix/Linux-based environments. Windows environment is currently **not** supported. However, a new platform/protocol can be supported by implementing the trait mentioned above.   | 2.0.0  |  
On YARN, the view and modify ACLs are provided to the YARN service when submitting applications, and control who has the respective privileges via YARN interfaces.
## Spark History Server ACLs[](https://spark.apache.org/docs/latest/security.html#spark-history-server-acls)
Authentication for the SHS Web UI is enabled the same way as for regular applications, using servlet filters.
To enable authorization in the SHS, a few extra options are used:  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.history.ui.acls.enable`  | false  |  Specifies whether ACLs should be checked to authorize users viewing the applications in the history server. If enabled, access control checks are performed regardless of what the individual applications had set for `spark.ui.acls.enable`. The application owner will always have authorization to view their own application and any users specified via `spark.ui.view.acls` and groups specified via `spark.ui.view.acls.groups` when the application was run will also have authorization to view that application. If disabled, no access control checks are made for any application UIs available through the history server.   | 1.0.1  |  
| `spark.history.ui.admin.acls`  | None  |  Comma separated list of users that have view access to all the Spark applications in history server.   | 2.1.1  |  
| `spark.history.ui.admin.acls.groups`  | None  |  Comma separated list of groups that have view access to all the Spark applications in history server.   | 2.1.1  |  
The SHS uses the same options to configure the group mapping provider as regular applications. In this case, the group mapping provider will apply to all UIs server by the SHS, and individual application configurations will be ignored.
## SSL Configuration[](https://spark.apache.org/docs/latest/security.html#ssl-configuration)
Configuration for SSL is organized hierarchically. The user can configure the default SSL settings which will be used for all the supported communication protocols unless they are overwritten by protocol-specific settings. This way the user can easily provide the common settings for all the protocols without disabling the ability to configure each one individually. Note that all settings are inherited this way, _except_ for `spark.ssl.rpc.enabled` which must be explicitly set.
The following table describes the SSL configuration namespaces:  
| Config Namespace  | Component  |  
| --- | --- |  
| `spark.ssl`  |  The default SSL configuration. These values will apply to all namespaces below, unless explicitly overridden at the namespace level.   |  
| `spark.ssl.ui`  | Spark application Web UI  |  
| `spark.ssl.standalone`  | Standalone Master / Worker Web UI  |  
| `spark.ssl.historyServer`  | History Server Web UI  |  
| `spark.ssl.rpc`  | Spark RPC communication  |  
The full breakdown of available SSL options can be found below. The `${ns}` placeholder should be replaced with one of the above namespaces.  
| Property Name  | Default  | Meaning  | Supported Namespaces  |  
| --- | --- | --- | --- |  
| `${ns}.enabled`  | false  | Enables SSL. When enabled, `${ns}.ssl.protocol` is required.  | ui,standalone,historyServer,rpc  |  
| `${ns}.port`  | None  |  The port where the SSL service will listen on.   
The port must be defined within a specific namespace configuration. The default namespace is ignored when reading this configuration.   
When not set, the SSL port will be derived from the non-SSL port for the same service. A value of "0" will make the service bind to an ephemeral port.   | ui,standalone,historyServer  |  
| `${ns}.enabledAlgorithms`  | None  |  A comma-separated list of ciphers. The specified ciphers must be supported by JVM.   
The reference list of protocols can be found in the "JSSE Cipher Suite Names" section of the Java security guide. The list for Java 17 can be found at [this](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names) page.   
Note: If not set, the default cipher suite for the JRE will be used.   | ui,standalone,historyServer,rpc  |  
| `${ns}.keyPassword`  | None  |  The password to the private key in the key store.   | ui,standalone,historyServer,rpc  |  
| `${ns}.keyStore`  | None  |  Path to the key store file. The path can be absolute or relative to the directory in which the process is started.   | ui,standalone,historyServer,rpc  |  
| `${ns}.keyStorePassword`  | None  | Password to the key store.  | ui,standalone,historyServer,rpc  |  
| `${ns}.keyStoreType`  | JKS  | The type of the key store.  | ui,standalone,historyServer  |  
| `${ns}.protocol`  | None  |  TLS protocol to use. The protocol must be supported by JVM.   
The reference list of protocols can be found in the "Additional JSSE Standard Names" section of the Java security guide. For Java 17, the list can be found at [this](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#additional-jsse-standard-names) page.   | ui,standalone,historyServer,rpc  |  
| `${ns}.needClientAuth`  | false  |  Whether to require client authentication.   | ui,standalone,historyServer  |  
| `${ns}.trustStore`  | None  |  Path to the trust store file. The path can be absolute or relative to the directory in which the process is started.   | ui,standalone,historyServer,rpc  |  
| `${ns}.trustStorePassword`  | None  | Password for the trust store.  | ui,standalone,historyServer,rpc  |  
| `${ns}.trustStoreType`  | JKS  | The type of the trust store.  | ui,standalone,historyServer  |  
| `${ns}.openSSLEnabled`  | false  |  Whether to use OpenSSL for cryptographic operations instead of the JDK SSL provider. This setting requires the `certChain` and `privateKey` settings to be set. This takes precedence over the `keyStore` and `trustStore` settings if both are specified. If the OpenSSL library is not available at runtime, we will fall back to the JDK provider.   | rpc  |  
| `${ns}.privateKey`  | None  |  Path to the private key file in PEM format. The path can be absolute or relative to the directory in which the process is started. This setting is required when using the OpenSSL implementation.   | rpc  |  
| `${ns}.privateKeyPassword`  | None  |  The password to the above private key file in PEM format.   | rpc  |  
| `${ns}.certChain`  | None  |  Path to the certificate chain file in PEM format. The path can be absolute or relative to the directory in which the process is started. This setting is required when using the OpenSSL implementation.   | rpc  |  
| `${ns}.trustStoreReloadingEnabled`  | false  |  Whether the trust store should be reloaded periodically. This setting is mostly only useful in standalone deployments, not k8s or yarn deployments.   | rpc  |  
| `${ns}.trustStoreReloadIntervalMs`  | 10000  |  The interval at which the trust store should be reloaded (in milliseconds). This setting is mostly only useful in standalone deployments, not k8s or yarn deployments.   | rpc  |  
Spark also supports retrieving `${ns}.keyPassword`, `${ns}.keyStorePassword` and `${ns}.trustStorePassword` from [Hadoop Credential Providers](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/CredentialProviderAPI.html). User could store password into credential file and make it accessible by different components, like:

```
hadoop credential create spark.ssl.keyPassword -value password \
    -provider jceks://hdfs@nn1.example.com:9001/user/backup/ssl.jceks

```

To configure the location of the credential provider, set the `hadoop.security.credential.provider.path` config option in the Hadoop configuration used by Spark, like:

```
  <property>
    <name>hadoop.security.credential.provider.path</name>
    <value>jceks://hdfs@nn1.example.com:9001/user/backup/ssl.jceks</value>
  </property>

```

Or via SparkConf “spark.hadoop.hadoop.security.credential.provider.path=jceks://hdfs@nn1.example.com:9001/user/backup/ssl.jceks”.
## Preparing the key stores[](https://spark.apache.org/docs/latest/security.html#preparing-the-key-stores)
Key stores can be generated by `keytool` program. The reference documentation for this tool for Java 17 is [here](https://docs.oracle.com/en/java/javase/17/docs/specs/man/keytool.html). The most basic steps to configure the key stores and the trust store for a Spark Standalone deployment mode is as follows:
  * Generate a key pair for each node
  * Export the public key of the key pair to a file on each node
  * Import all exported public keys into a single trust store
  * Distribute the trust store to the cluster nodes


### YARN mode[](https://spark.apache.org/docs/latest/security.html#yarn-mode)
To provide a local trust store or key store file to drivers running in cluster mode, they can be distributed with the application using the `--files` command line argument (or the equivalent `spark.files` configuration). The files will be placed on the driver’s working directory, so the TLS configuration should just reference the file name with no absolute path.
Distributing local key stores this way may require the files to be staged in HDFS (or other similar distributed file system used by the cluster), so it’s recommended that the underlying file system be configured with security in mind (e.g. by enabling authentication and wire encryption).
### Standalone mode[](https://spark.apache.org/docs/latest/security.html#standalone-mode)
The user needs to provide key stores and configuration options for master and workers. They have to be set by attaching appropriate Java system properties in `SPARK_MASTER_OPTS` and in `SPARK_WORKER_OPTS` environment variables, or just in `SPARK_DAEMON_JAVA_OPTS`.
The user may allow the executors to use the SSL settings inherited from the worker process. That can be accomplished by setting `spark.ssl.useNodeLocalConf` to `true`. In that case, the settings provided by the user on the client side are not used.
## HTTP Security Headers[](https://spark.apache.org/docs/latest/security.html#http-security-headers)
Apache Spark can be configured to include HTTP headers to aid in preventing Cross Site Scripting (XSS), Cross-Frame Scripting (XFS), MIME-Sniffing, and also to enforce HTTP Strict Transport Security.  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.ui.xXssProtection`  | `1; mode=block`  |  Value for HTTP X-XSS-Protection response header. You can choose appropriate value from below: 
  * `0` (Disables XSS filtering)
  * `1` (Enables XSS filtering. If a cross-site scripting attack is detected, the browser will sanitize the page.)
  * `1; mode=block` (Enables XSS filtering. The browser will prevent rendering of the page if an attack is detected.)

 | 2.3.0  |  
| `spark.ui.xContentTypeOptions.enabled`  | `true`  |  When enabled, X-Content-Type-Options HTTP response header will be set to "nosniff".   | 2.3.0  |  
| `spark.ui.strictTransportSecurity`  | None  |  Value for HTTP Strict Transport Security (HSTS) Response Header. You can choose appropriate value from below and set `expire-time` accordingly. This option is only used when SSL/TLS is enabled. 
  * `max-age=<expire-time>`
  * `max-age=<expire-time>; includeSubDomains`
  * `max-age=<expire-time>; preload`

 | 2.3.0  |  
# Configuring Ports for Network Security[](https://spark.apache.org/docs/latest/security.html#configuring-ports-for-network-security)
Generally speaking, a Spark cluster and its services are not deployed on the public internet. They are generally private services, and should only be accessible within the network of the organization that deploys Spark. Access to the hosts and ports used by Spark services should be limited to origin hosts that need to access the services.
However, like the REST Submission port, Spark also supports HTTP `Authorization` header with a cryptographically signed JSON Web Token (JWT) for all UI ports. To use it, a user needs to configure `spark.ui.filters=org.apache.spark.ui.JWSFilter` and `spark.org.apache.spark.ui.JWSFilter.param.secretKey=BASE64URL-ENCODED-KEY`.
Below are the primary ports that Spark uses for its communication and how to configure those ports.
## Standalone mode only[](https://spark.apache.org/docs/latest/security.html#standalone-mode-only)  
| From  | To  | Default Port  | Purpose  | Configuration Setting  | Notes  |  
| --- | --- | --- | --- | --- | --- |  
| Browser  | Standalone Master  | 8080  | Web UI  | `spark.master.ui.port /  
 SPARK_MASTER_WEBUI_PORT`  | Jetty-based. Standalone mode only.  |  
| Browser  | Standalone Worker  | 8081  | Web UI  | `spark.worker.ui.port /  
 SPARK_WORKER_WEBUI_PORT`  | Jetty-based. Standalone mode only.  |  
| Driver /  
Standalone Worker  | Standalone Master  | 7077  | Submit job to cluster /  
Join cluster  | `SPARK_MASTER_PORT`  | Set to "0" to choose a port randomly. Standalone mode only.  |  
| External Service  | Standalone Master  | 6066  | Submit job to cluster via REST API  | `spark.master.rest.port`  | Use `spark.master.rest.enabled` to enable/disable this service. Standalone mode only.  |  
| Standalone Master  | Standalone Worker  | (random)  | Schedule executors  | `SPARK_WORKER_PORT`  | Set to "0" to choose a port randomly. Standalone mode only.  |  
## All cluster managers[](https://spark.apache.org/docs/latest/security.html#all-cluster-managers)  
| From  | To  | Default Port  | Purpose  | Configuration Setting  | Notes  |  
| --- | --- | --- | --- | --- | --- |  
| Browser  | Application  | 4040  | Web UI  | `spark.ui.port`  | Jetty-based  |  
| Browser  | History Server  | 18080  | Web UI  | `spark.history.ui.port`  | Jetty-based  |  
| Executor /  
Standalone Master  | Driver  | (random)  | Connect to application /  
Notify executor state changes  | `spark.driver.port`  | Set to "0" to choose a port randomly.  |  
| Executor / Driver  | Executor / Driver  | (random)  | Block Manager port  | `spark.blockManager.port`  | Raw socket via ServerSocketChannel  |  
# Kerberos[](https://spark.apache.org/docs/latest/security.html#kerberos)
Spark supports submitting applications in environments that use Kerberos for authentication. In most cases, Spark relies on the credentials of the current logged in user when authenticating to Kerberos-aware services. Such credentials can be obtained by logging in to the configured KDC with tools like `kinit`.
When talking to Hadoop-based services, Spark needs to obtain delegation tokens so that non-local processes can authenticate. Spark ships with support for HDFS and other Hadoop file systems, Hive and HBase.
When using a Hadoop filesystem (such HDFS or WebHDFS), Spark will acquire the relevant tokens for the service hosting the user’s home directory.
An HBase token will be obtained if HBase is in the application’s classpath, and the HBase configuration has Kerberos authentication turned (`hbase.security.authentication=kerberos`).
Similarly, a Hive token will be obtained if Hive is in the classpath, and the configuration includes URIs for remote metastore services (`hive.metastore.uris` is not empty).
If an application needs to interact with other secure Hadoop filesystems, their URIs need to be explicitly provided to Spark at launch time. This is done by listing them in the `spark.kerberos.access.hadoopFileSystems` property, described in the configuration section below.
Spark also supports custom delegation token providers using the Java Services mechanism (see `java.util.ServiceLoader`). Implementations of `org.apache.spark.security.HadoopDelegationTokenProvider` can be made available to Spark by listing their names in the corresponding file in the jar’s `META-INF/services` directory.
Delegation token support is currently only supported in YARN and Kubernetes mode. Consult the deployment-specific page for more information.
The following options provides finer-grained control for this feature:  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.security.credentials.${service}.enabled`  | `true`  |  Controls whether to obtain credentials for services when security is enabled. By default, credentials for all supported services are retrieved when those services are configured, but it's possible to disable that behavior if it somehow conflicts with the application being run.   | 2.3.0  |  
| `spark.kerberos.access.hadoopFileSystems`  | (none)  |  A comma-separated list of secure Hadoop filesystems your Spark application is going to access. For example, `spark.kerberos.access.hadoopFileSystems=hdfs://nn1.com:8032,hdfs://nn2.com:8032,     webhdfs://nn3.com:50070`. The Spark application must have access to the filesystems listed and Kerberos must be properly configured to be able to access them (either in the same realm or in a trusted realm). Spark acquires security tokens for each of the filesystems so that the Spark application can access those remote Hadoop filesystems.   | 3.0.0  |  
Users can exclude Kerberos delegation token renewal at resource scheduler. Currently it is only supported on YARN. The configuration is covered in the [Running Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html#yarn-specific-kerberos-configuration) page.
## Long-Running Applications[](https://spark.apache.org/docs/latest/security.html#long-running-applications)
Long-running applications may run into issues if their run time exceeds the maximum delegation token lifetime configured in services it needs to access.
This feature is not available everywhere. In particular, it’s only implemented on YARN and Kubernetes (both client and cluster modes).
Spark supports automatically creating new tokens for these applications. There are two ways to enable this functionality.
### Using a Keytab[](https://spark.apache.org/docs/latest/security.html#using-a-keytab)
By providing Spark with a principal and keytab (e.g. using `spark-submit` with `--principal` and `--keytab` parameters), the application will maintain a valid Kerberos login that can be used to retrieve delegation tokens indefinitely.
Note that when using a keytab in cluster mode, it will be copied over to the machine running the Spark driver. In the case of YARN, this means using HDFS as a staging area for the keytab, so it’s strongly recommended that both YARN and HDFS be secured with encryption, at least.
### Using a ticket cache[](https://spark.apache.org/docs/latest/security.html#using-a-ticket-cache)
By setting `spark.kerberos.renewal.credentials` to `ccache` in Spark’s configuration, the local Kerberos ticket cache will be used for authentication. Spark will keep the ticket renewed during its renewable life, but after it expires a new ticket needs to be acquired (e.g. by running `kinit`).
It’s up to the user to maintain an updated ticket cache that Spark can use.
The location of the ticket cache can be customized by setting the `KRB5CCNAME` environment variable.
## Proxy User[](https://spark.apache.org/docs/latest/security.html#proxy-user)
Spark also provides `--proxy-user` parameter for `spark-submit` to enable Hadoop’s [Proxy user](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/Superusers.html) feature.
If the target cluster, e.g., YARN, HDFS, is running in Secure Mode, the superuser must have a valid Kerberos ticket to log in. The impersonated user (proxy-user) does not need to have a Kerberos ticket. In addition, the superuser must be configured in the cluster to be allowed to impersonate the proxy user.
The authentication happens on the target cluster side, and once the authentication is successful, the cluster will do resource allocation and file system access on behalf of the proxy user.
Note that, depending on Spark’s deployment mode, the proxy user might behave differently. For cluster mode, the JVM running the driver will be started by the proxy user, while for client mode, it will be started by the superuser instead. This is due to the Driver being initialized inside the progress of `SparkSubmit` client. This makes a difference in file system access for local file permissions. This is not considered a CVE issue, but users should be aware of this difference.
Nowadays, many projects, such as Apache Kyuubi, provide a multi-tenant Spark service with impersonation. To prevent server-side local files from reading and leaking by superuser to other tenants, it is recommended to refer to their documentation to find out instructions on how to ensure cluster mode is used for a more secure purpose.
## Secure Interaction with Kubernetes[](https://spark.apache.org/docs/latest/security.html#secure-interaction-with-kubernetes)
When talking to Hadoop-based services behind Kerberos, it was noted that Spark needs to obtain delegation tokens so that non-local processes can authenticate. These delegation tokens in Kubernetes are stored in Secrets that are shared by the Driver and its Executors. As such, there are three ways of submitting a Kerberos job:
In all cases you must define the environment variable: `HADOOP_CONF_DIR` or `spark.kubernetes.hadoop.configMapName.`
It also important to note that the KDC needs to be visible from inside the containers.
If a user wishes to use a remote HADOOP_CONF directory, that contains the Hadoop configuration files, this could be achieved by setting `spark.kubernetes.hadoop.configMapName` to a pre-existing ConfigMap.
  1. Submitting with a $kinit that stores a TGT in the Local Ticket Cache: 

```
/usr/bin/kinit -kt <keytab_file> <username>/<krb5 realm>
/opt/spark/bin/spark-submit \
 --deploy-mode cluster \
 --class org.apache.spark.examples.HdfsTest \
 --master k8s://<KUBERNETES_MASTER_ENDPOINT> \
 --conf spark.executor.instances=1 \
 --conf spark.app.name=spark-hdfs \
 --conf spark.kubernetes.container.image=spark:latest \
 --conf spark.kubernetes.kerberos.krb5.path=/etc/krb5.conf \
 local:///opt/spark/examples/jars/spark-examples_<VERSION>.jar \
 <HDFS_FILE_LOCATION>

```

  2. Submitting with a local Keytab and Principal 

```
/opt/spark/bin/spark-submit \
 --deploy-mode cluster \
 --class org.apache.spark.examples.HdfsTest \
 --master k8s://<KUBERNETES_MASTER_ENDPOINT> \
 --conf spark.executor.instances=1 \
 --conf spark.app.name=spark-hdfs \
 --conf spark.kubernetes.container.image=spark:latest \
 --conf spark.kerberos.keytab=<KEYTAB_FILE> \
 --conf spark.kerberos.principal=<PRINCIPAL> \
 --conf spark.kubernetes.kerberos.krb5.path=/etc/krb5.conf \
 local:///opt/spark/examples/jars/spark-examples_<VERSION>.jar \
 <HDFS_FILE_LOCATION>

```

  3. Submitting with pre-populated secrets, that contain the Delegation Token, already existing within the namespace 

```
/opt/spark/bin/spark-submit \
 --deploy-mode cluster \
 --class org.apache.spark.examples.HdfsTest \
 --master k8s://<KUBERNETES_MASTER_ENDPOINT> \
 --conf spark.executor.instances=1 \
 --conf spark.app.name=spark-hdfs \
 --conf spark.kubernetes.container.image=spark:latest \
 --conf spark.kubernetes.kerberos.tokenSecret.name=<SECRET_TOKEN_NAME> \
 --conf spark.kubernetes.kerberos.tokenSecret.itemKey=<SECRET_ITEM_KEY> \
 --conf spark.kubernetes.kerberos.krb5.path=/etc/krb5.conf \
 local:///opt/spark/examples/jars/spark-examples_<VERSION>.jar \
 <HDFS_FILE_LOCATION>

```



3b. Submitting like in (3) however specifying a pre-created krb5 ConfigMap and pre-created `HADOOP_CONF_DIR` ConfigMap

```
/opt/spark/bin/spark-submit \
    --deploy-mode cluster \
    --class org.apache.spark.examples.HdfsTest \
    --master k8s://<KUBERNETES_MASTER_ENDPOINT> \
    --conf spark.executor.instances=1 \
    --conf spark.app.name=spark-hdfs \
    --conf spark.kubernetes.container.image=spark:latest \
    --conf spark.kubernetes.kerberos.tokenSecret.name=<SECRET_TOKEN_NAME> \
    --conf spark.kubernetes.kerberos.tokenSecret.itemKey=<SECRET_ITEM_KEY> \
    --conf spark.kubernetes.hadoop.configMapName=<HCONF_CONFIG_MAP_NAME> \
    --conf spark.kubernetes.kerberos.krb5.configMapName=<KRB_CONFIG_MAP_NAME> \
    local:///opt/spark/examples/jars/spark-examples_<VERSION>.jar \
    <HDFS_FILE_LOCATION>

```

# Event Logging[](https://spark.apache.org/docs/latest/security.html#event-logging)
If your applications are using event logging, the directory where the event logs go (`spark.eventLog.dir`) should be manually created with proper permissions. To secure the log files, the directory permissions should be set to `drwxrwxrwxt`. The owner and group of the directory should correspond to the super user who is running the Spark History Server.
This will allow all users to write to the directory but will prevent unprivileged users from reading, removing or renaming a file unless they own it. The event log files will be created by Spark with permissions such that only the user and group have read and write access.
# Persisting driver logs in client mode[](https://spark.apache.org/docs/latest/security.html#persisting-driver-logs-in-client-mode)
If your applications persist driver logs in client mode by enabling `spark.driver.log.persistToDfs.enabled`, the directory where the driver logs go (`spark.driver.log.dfsDir`) should be manually created with proper permissions. To secure the log files, the directory permissions should be set to `drwxrwxrwxt`. The owner and group of the directory should correspond to the super user who is running the Spark History Server.
This will allow all users to write to the directory but will prevent unprivileged users from reading, removing or renaming a file unless they own it. The driver log files will be created by Spark with permissions such that only the user and group have read and write access.
