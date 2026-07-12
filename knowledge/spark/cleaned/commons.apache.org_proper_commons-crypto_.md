[ ![Apache Commons logo](https://commons.apache.org/proper/commons-crypto/images/commons-logo.png%0A) ](https://commons.apache.org/ "Apache Commons logo") [ ![Commons Crypto™ logo](https://commons.apache.org/proper/commons-crypto/images/logo.png%0A) ](https://commons.apache.org/proper/commons-crypto/index.html "Commons Crypto™ logo")
[Apache Commons Crypto ™](https://commons.apache.org/proper/commons-crypto/)
  * Last Published: 23 January 2023
  * |
  * Version: 1.2.0

  * [ ApacheCon](https://www.apachecon.com/ "ApacheCon")
  * [ Apache](https://www.apache.org "Apache")
  * [ Commons](https://commons.apache.org/ "Commons")

|
  * Documentation
  * [ Overview](https://commons.apache.org/proper/commons-crypto/index.html "Overview")
  * [ Download](https://commons.apache.org/proper/commons-crypto/download_crypto.cgi "Download")
  * [ User Guide](https://commons.apache.org/proper/commons-crypto/userguide.html "User Guide")
  * [ FAQ](https://commons.apache.org/proper/commons-crypto/faq.html "FAQ")
  * [ Javadoc](https://commons.apache.org/proper/commons-crypto/apidocs/index.html "Javadoc")
  * [ Javadoc Archive](https://javadoc.io/doc/org.apache.commons/commons-crypto/ "Javadoc Archive")
  * [ Security](https://commons.apache.org/proper/commons-crypto/security.html "Security")

  * Development
  * [ Mailing Lists](https://commons.apache.org/proper/commons-crypto/mail-lists.html "Mailing Lists")
  * [ Issue Tracking](https://commons.apache.org/proper/commons-crypto/issue-tracking.html "Issue Tracking")
  * [ Source Repository](https://commons.apache.org/proper/commons-crypto/scm.html "Source Repository")

  * Project Documentation
  * [ Project Information](https://commons.apache.org/proper/commons-crypto/project-info.html "Project Information")
    * [ About](https://commons.apache.org/proper/commons-crypto/index.html "About")
    * [ Summary](https://commons.apache.org/proper/commons-crypto/summary.html "Summary")
    * [ Team](https://commons.apache.org/proper/commons-crypto/team.html "Team")
    * [ Source Code Management](https://commons.apache.org/proper/commons-crypto/scm.html "Source Code Management")
    * [ Issue Management](https://commons.apache.org/proper/commons-crypto/issue-management.html "Issue Management")
    * [ Mailing Lists](https://commons.apache.org/proper/commons-crypto/mailing-lists.html "Mailing Lists")
    * [ Dependency Information](https://commons.apache.org/proper/commons-crypto/dependency-info.html "Dependency Information")
    * [ Dependency Management](https://commons.apache.org/proper/commons-crypto/dependency-management.html "Dependency Management")
    * [ Dependencies](https://commons.apache.org/proper/commons-crypto/dependencies.html "Dependencies")
    * [ Dependency Convergence](https://commons.apache.org/proper/commons-crypto/dependency-convergence.html "Dependency Convergence")
    * [ CI Management](https://commons.apache.org/proper/commons-crypto/ci-management.html "CI Management")
    * [ Distribution Management](https://commons.apache.org/proper/commons-crypto/distribution-management.html "Distribution Management")
  * [ Project Reports](https://commons.apache.org/proper/commons-crypto/project-reports.html "Project Reports")

  * Commons
  * [ Home](https://commons.apache.org/ "Home")
  * [ License](https://www.apache.org/licenses/ "License")
  * [ Components](https://commons.apache.org/components.html "Components")
  * [ Sandbox](https://commons.apache.org/sandbox/index.html "Sandbox")
  * [ Dormant](https://commons.apache.org/dormant/index.html "Dormant")

  * General Information
  * [ Security](https://commons.apache.org/security.html "Security")
  * [ Volunteering](https://commons.apache.org/volunteering.html "Volunteering")
  * [ Contributing Patches](https://commons.apache.org/patches.html "Contributing Patches")
  * [ Building Components](https://commons.apache.org/building.html "Building Components")
  * [ Commons Parent POM](https://commons.apache.org/commons-parent-pom.html "Commons Parent POM")
  * [ Commons Build Plugin](https://commons.apache.org/build-plugin/index.html "Commons Build Plugin")
  * [ Commons Release Plugin](https://commons.apache.org/release-plugin/index.html "Commons Release Plugin")
  * [ Site Publication](https://commons.apache.org/site-publish.html "Site Publication")
  * [ Releasing Components](https://commons.apache.org/releases/index.html "Releasing Components")
  * [ Wiki](https://cwiki.apache.org/confluence/display/commons/FrontPage "Wiki")

  * ASF
  * [ How the ASF works](https://www.apache.org/foundation/how-it-works.html "How the ASF works")
  * [ Get Involved](https://www.apache.org/foundation/getinvolved.html "Get Involved")
  * [ Developer Resources](https://www.apache.org/dev/ "Developer Resources")
  * [ Code of Conduct](https://www.apache.org/foundation/policies/conduct.html "Code of Conduct")
  * [ Privacy](https://privacy.apache.org/policies/privacy-policy-public.html "Privacy")
  * [ Sponsorship](https://www.apache.org/foundation/sponsorship.html "Sponsorship")
  * [ Thanks](https://www.apache.org/foundation/thanks.html "Thanks")

[ ![ApacheCon](https://www.apache.org/events/current-event-125x125.png) ](https://www.apache.org/events/current-event.html "ApacheCon") [ ![Maven](https://maven.apache.org/images/logos/maven-feather.png) ](https://maven.apache.org/ "Maven")  |
##  Apache Commons Crypto
Apache Commons Crypto is a cryptographic library optimized with AES-NI (Advanced Encryption Standard New Instructions). Commons Crypto provides Java APIs at the cipher level and Java stream level. Developers can implement high performance AES encryption/decryption with minimum coding and effort. Please note that Commons Crypto doesn't implement the cryptographic algorithm such as AES directly, it wraps OpenSSL and JCE.
##  Features
  * Cipher API for low level cryptographic operations.
  * Secure true random number generator.
  * Java stream API for high level stream encryption/decryption.
  * High performance AES encryption/decryption optimized with Intel AES-NI.
  * Portable across various operating systems (currently only Linux/Mac OS/Windows); Apache Commons Crypto loads the library according to your machine environment (using system properties, os.name and os.arch).
  * Simple usage. Add the commons-crypto-(version).jar file to your classpath.

##  Documentation
An overview of the functionality is provided in the [user guide](https://commons.apache.org/proper/commons-crypto/userguide.html). Various [project reports](https://commons.apache.org/proper/commons-crypto/project-reports.html) are also available.  The Javadoc API documents are available online:
  * [Javadoc](https://commons.apache.org/proper/commons-crypto/apidocs/index.html)

The [git repository](https://commons.apache.org/proper/commons-crypto/scm.html) can be [browsed](https://gitbox.apache.org/repos/asf?p=commons-crypto.git).
##  Releases
  * [Crypto 1.2.0 (mirrors)](https://commons.apache.org/proper/commons-crypto/download_crypto.cgi) requires Java 1.8 and OpenSSL 1.1.x (should also work with 1.0.x)
  * [Crypto 1.1.0 (archives)](https://archive.apache.org/dist/commons/crypto/) requires Java 1.8, built and tested with:
    * darwin64-x86_64-cc; OpenSSL 1.1.1g
    * debian-amd64; OpenSSL 1.0.1f
    * debian-amd64; OpenSSL 1.1.1g
    * debian-arm64; OpenSSL 1.1.1f
    * linux-aarch64; OpenSSL 1.0.2k-fips
    * Linux x86_64; OpenSSL 1.1.1
    * Windows 64 (mingw64); OpenSSL 1.1.1d
  * [Crypto 1.0.0 (archives)](https://archive.apache.org/dist/commons/crypto/) requires Java 1.7.

See the [Download Page](https://commons.apache.org/proper/commons-crypto/download_crypto.cgi) for the latest releases.
[Change reports](https://commons.apache.org/proper/commons-crypto/changes-report.html) are also available.  For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/crypto/)
##  Support
The [commons mailing lists](https://commons.apache.org/proper/commons-crypto/mail-lists.html) act as the main support forum. The user list is suitable for most library usage queries. The dev list is intended for the development discussion. Please remember that the lists are shared between all commons components, so prefix your email by [crypto].  Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-crypto/issue-tracking.html).   |
| --- | --- |
Copyright © 2016-2023 [The Apache Software Foundation](https://www.apache.org/). All Rights Reserved.
Apache Commons, Apache Commons Crypto, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation. All other marks mentioned may be trademarks or registered trademarks of their respective owners.
