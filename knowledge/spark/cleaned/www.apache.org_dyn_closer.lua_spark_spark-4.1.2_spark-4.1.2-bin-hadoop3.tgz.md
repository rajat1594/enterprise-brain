[Skip to Main Content](https://www.apache.org/#maincontent)
Toggle navigation
[![slack icon](https://www.apache.org/images/slack-icon.svg)](https://infra.apache.org/slack.html) [![github icon](https://www.apache.org/images/github-mark-white.svg)](https://github.com/apache) [![linkedIn icon](https://www.apache.org/images/linkedin-icon.png)](https://www.linkedin.com/company/the-apache-software-foundation/) [![youtube icon](https://www.apache.org/images/youtube-icon.svg)](https://www.youtube.com/c/TheApacheFoundation) [![X icon](https://www.apache.org/images/x-icon.svg)](https://twitter.com/TheASF)
[Sponsor the ASF](https://www.apache.org/foundation/sponsorship)
  * [Community ](https://www.apache.org/)
    * [Contributor Getting Started](https://community.apache.org/)
    * [Becoming a Committer](https://community.apache.org/contributors/)
    * [Code of Conduct](https://www.apache.org/foundation/policies/conduct)
    * [Community Resources](https://www.apache.org/community-resources/)
    * [Community Over Code](https://communityovercode.org/)
    * [Events](https://events.apache.org/)
    * [Store](https://www.redbubble.com/people/comdev/shop)
  * [Projects ](https://www.apache.org/)
    * [Projects](https://www.apache.org/projects)
    * [Incubator Projects](https://incubator.apache.org/)
    * [Projects Directory ](https://projects.apache.org/)
    * [Mailing Lists ](https://www.apache.org/foundation/mailinglists)
    * [Report a Vulnerability](https://www.apache.org/security)
  * [Downloads ](https://www.apache.org/)
    * [Distributions](https://downloads.apache.org/)
    * [Releases](https://projects.apache.org/releases.html)
    * [Infrastructure Status](https://status.apache.org/)
    * [Infrastructure Statistics](https://infra-reports.apache.org/#uptime)
  * [Learn ](https://www.apache.org/)
    * [Blog](https://news.apache.org/)
    * [How the ASF Works](https://www.apache.org/foundation/how-it-works)
    * [The Apache Way](https://www.apache.org/theapacheway/)
    * [Legal & Trademark](https://www.apache.org/legal/)
    * [Licenses](https://www.apache.org/licenses)
    * [Glossary](https://www.apache.org/foundation/glossary)
    * [FAQ](https://www.apache.org/foundation/faq)
  * [Resources & Tools ](https://www.apache.org/)
    * [Developer Information](https://www.apache.org/dev/)
    * [Wiki](https://cwiki.apache.org/)
    * [Issues](https://issues.apache.org/)
    * [Slack](https://infra.apache.org/slack.html)
    * [Self Serve Portal](https://selfserve.apache.org/)
    * [Infrastructure](https://infra.apache.org/)
    * [Whimsy](https://whimsy.apache.org/)
    * [Brand Guidelines](https://www.apache.org/foundation/press/kit/)
    * [Project Logos](https://www.apache.org/logos/)
  * [About ](https://www.apache.org/)
    * [About](https://www.apache.org/foundation/)
    * [Our Sponsors](https://www.apache.org/foundation/sponsors)
    * [Corporate Sponsorship](https://www.apache.org/foundation/sponsorship)
    * [Individual Supporters](https://www.apache.org/foundation/individual-supporters)
    * [Leadership](https://www.apache.org/foundation/leadership)
    * [Members](https://www.apache.org/foundation/members)
    * [Diversity & Inclusion](https://diversity.apache.org/)
    * [Newsroom](https://www.apache.org/press/)
    * [Contact](https://www.apache.org/foundation/contact)
  * [Search](https://www.apache.org/)
    * Clear

[ ![Apache Events](https://www.apache.org/events/current-event-125x125.png) ](https://events.apache.org/x/current-event.html) [![The Apache Software Foundation](https://www.apache.org/img/asf-estd-1999-logo.jpg)](https://www.apache.org/)
![Apache 20th Anniversary Logo](https://www.apache.org/img/asf-estd-1999-logo.jpg)
We suggest the following location for your download:
[ **https://dlcdn.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz** ](https://dlcdn.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz)
Alternate download locations are suggested below.
It is essential that you [verify the integrity](https://www.apache.org/#verify) of the downloaded file using the PGP signature ( `.asc` file) or a hash ( `.md5` or `.sha*` file).
#  HTTP [¶](https://www.apache.org/#http "Permanent link")
[ **https://dlcdn.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz** ](https://dlcdn.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz)

#  Backup Sites [¶](https://www.apache.org/#backup "Permanent link")
[ **https://downloads.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz** ](https://downloads.apache.org/spark/spark-4.1.2/spark-4.1.2-bin-hadoop3.tgz)

#  Verify the integrity of the files [¶](https://www.apache.org/#verify "Permanent link")
It is essential that you verify the integrity of the downloaded file using the PGP signature ( `.asc` file) or a hash ( `.md5` or `.sha*` file). Please read [Verifying Apache Software Foundation Releases](https://www.apache.org/info/verification.html) for more information on why you should verify our releases.
The PGP signature can be verified using PGP or GPG. First download the `KEYS` as well as the `asc` signature file for the relevant distribution. Make sure you get these files from the main distribution site, rather than from a mirror. Then verify the signatures using

```
        % gpg --import KEYS
        % gpg --verify downloaded_file.asc downloaded_file

```

_or_

```
        % pgpk -a KEYS
        % pgpv downloaded_file.asc

```

_or_

```
        % pgp -ka KEYS
        % pgp downloaded_file.asc

```

Alternatively, you can verify the hash on the file.
Hashes can be calculated using GPG:

```
        % gpg --print-md SHA256 downloaded_file

```

The output should be compared with the contents of the SHA256 file. Similarly for other hashes (SHA512, SHA1, MD5 etc) which may be provided.
Windows 7 and later systems should all now have certUtil:

```
        % certUtil -hashfile pathToFileToCheck

```

HashAlgorithm choices: MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512
Unix-like systems (and macOS) will have a utility called md5, md5sum or shasum

##### Community
  * [Contributor Getting Started](https://community.apache.org/)
  * [Becoming a Committer](https://community.apache.org/contributors/)
  * [Code of Conduct](https://www.apache.org/foundation/policies/conduct)
  * [Community Resources](https://www.apache.org/community-resources/)
  * [Community Over Code](https://communityovercode.org/)
  * [Events](https://events.apache.org/)
  * [Store](https://www.redbubble.com/people/comdev/shop)

##### Projects
  * [Projects](https://www.apache.org/projects)
  * [Incubator Projects](https://incubator.apache.org/)
  * [Projects Directory ](https://projects.apache.org/)
  * [Mailing Lists ](https://www.apache.org/foundation/mailinglists)
  * [Report a Vulnerability](https://www.apache.org/security)

##### Downloads
  * [Distributions](https://downloads.apache.org/)
  * [Releases](https://projects.apache.org/releases.html)
  * [Infrastructure Status](https://status.apache.org/)
  * [Infrastructure Statistics](https://infra-reports.apache.org/#uptime)

##### Learn
  * [Blog](https://news.apache.org/)
  * [How the ASF Works](https://www.apache.org/foundation/how-it-works)
  * [The Apache Way](https://www.apache.org/theapacheway/)
  * [Legal & Trademark](https://www.apache.org/legal/)
  * [Licenses](https://www.apache.org/licenses)
  * [Glossary](https://www.apache.org/foundation/glossary)
  * [FAQ](https://www.apache.org/foundation/faq)

##### Resources & Tools
  * [Developer Information](https://www.apache.org/dev/)
  * [Wiki](https://cwiki.apache.org/)
  * [Issues](https://issues.apache.org/)
  * [Slack](https://infra.apache.org/slack.html)
  * [Self Serve Portal](https://selfserve.apache.org/)
  * [Infrastructure](https://infra.apache.org/)
  * [Whimsy](https://whimsy.apache.org/)
  * [Brand Guidelines](https://www.apache.org/foundation/press/kit/)
  * [Project Logos](https://www.apache.org/logos/)

##### About
  * [About](https://www.apache.org/foundation/)
  * [Our Sponsors](https://www.apache.org/foundation/sponsors)
  * [Corporate Sponsorship](https://www.apache.org/foundation/sponsorship)
  * [Individual Supporters](https://www.apache.org/foundation/individual-supporters)
  * [Leadership](https://www.apache.org/foundation/leadership)
  * [Members](https://www.apache.org/foundation/members)
  * [Diversity & Inclusion](https://diversity.apache.org/)
  * [Newsroom](https://www.apache.org/press/)
  * [Contact](https://www.apache.org/foundation/contact)
  * [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)

* * *
Copyright © 2023 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.
