Introducing The ASF’s New Logo [Read Now](https://news.apache.org/foundation/entry/introducing-the-asfs-new-logo)
[![Apache Software Foundation Logo](https://www.apache.org/images/asflogo_horizontal_color.svg)](https://www.apache.org/)
Toggle navigation
  * [Community ](https://www.apache.org/info/verification.html)
    * [Contributor Getting Started](https://community.apache.org/)
    * [Becoming a Committer](https://community.apache.org/contributors/)
    * [Code of Conduct](https://www.apache.org/foundation/policies/conduct)
    * [Community Resources](https://www.apache.org/community-resources/)
    * [Community Over Code](https://communityovercode.org/)
    * [Events](https://events.apache.org/)
  * [Projects ](https://www.apache.org/info/verification.html)
    * [Projects](https://www.apache.org/projects)
    * [Incubator Projects](https://incubator.apache.org/)
    * [Projects Directory ](https://projects.apache.org/)
    * [Mailing Lists ](https://www.apache.org/foundation/mailinglists)
    * [Report a Vulnerability](https://www.apache.org/security)
    * [The Apache Attic](https://attic.apache.org/)
  * [Downloads ](https://www.apache.org/info/verification.html)
    * [Distributions](https://downloads.apache.org/)
    * [Releases](https://projects.apache.org/releases.html)
  * [Learn ](https://www.apache.org/info/verification.html)
    * [Blog](https://news.apache.org/)
    * [How the ASF Works](https://www.apache.org/foundation/how-it-works)
    * [The Apache Way](https://www.apache.org/theapacheway/)
    * [Legal & Trademark](https://www.apache.org/legal/)
    * [Licenses](https://www.apache.org/licenses)
    * [Glossary](https://www.apache.org/foundation/glossary)
    * [FAQ](https://www.apache.org/foundation/faq)
  * [Resources & Tools ](https://www.apache.org/info/verification.html)
    * [Developer Information](https://www.apache.org/dev/)
    * [Wiki](https://cwiki.apache.org/)
    * [Issues](https://issues.apache.org/)
    * [Slack](https://infra.apache.org/slack.html)
    * [Self Serve Portal](https://selfserve.apache.org/)
    * [Infrastructure](https://infra.apache.org/)
    * [Infrastructure Status](https://status.apache.org/)
    * [Infrastructure Statistics](https://infra-reports.apache.org/#uptime)
    * [Whimsy](https://whimsy.apache.org/)
    * [Brand Guidelines](https://www.apache.org/foundation/press/kit/)
    * [Project Logos](https://www.apache.org/logos/)
  * [About ](https://www.apache.org/info/verification.html)
    * [About](https://www.apache.org/foundation/)
    * [Our Sponsors](https://www.apache.org/foundation/sponsors)
    * [Corporate Sponsorship](https://www.apache.org/foundation/sponsorship)
    * [Individual Supporters](https://www.apache.org/foundation/individual-supporters)
    * [Leadership](https://www.apache.org/foundation/leadership)
    * [Members](https://www.apache.org/foundation/members)
    * [Diversity & Inclusion](https://diversity.apache.org/)
    * [Newsroom](https://www.apache.org/press/)
    * [Contact](https://www.apache.org/foundation/contact)
  * [Sponsor](https://www.apache.org/foundation/sponsorship)
  * [Search](https://www.apache.org/info/verification.html)
    * Clear

# Verifying Apache Software Foundation Releases
![ASF Oak Leaf Icon](https://www.apache.org/images/oakleaf.svg)
This page describes how to verify a file you have downloaded from an Apache product releases page, or from the Apache archive, by [checksum](https://www.apache.org/info/verification.html#CheckingHashes) or [signature](https://www.apache.org/info/verification.html#CheckingSignatures).
All official releases of code distributed by the Apache Software Foundation are signed by the release manager for the release. PGP signatures and SHA/MD5 checksums are available along with the distribution.
Signatures and checksums are only available from the official Apache Software Foundation site.
## Checking Hashes[¶](https://www.apache.org/info/verification.html#CheckingHashes "Permalink")
File hashes are used to check that a file has been downloaded correctly. They do not provide any guarantees as to the authenticity of the file.
The _checksum_ of a file is a fixed length string, that (in practice) uniquely identifies the _contents_ of the file. Two files are (only) equal if their checksums are equal. Comparing the checksums of two files is as good as comparing the two files themselves.
There are lots of checksum algorithms. We use SHA-256 and SHA-512. MD5 and SHA-1, which may have been used for older releases, are _deprecated_.
The download page shows which checksum files are available for the _original_ file.
To check a hash, you have to _compute_ the proper checksum of the file you just downloaded ; then _compare_ it with the published checksum of the _original_.
> | _compute the checksum of your file ..._  | _compare with_  |
> | --- | --- |
> |   | Windows  | Linux  | Mac  |   |
> | SHA-1 (deprecated)  | certUtil -hashfile _file_ SHA1  | sha1sum _file_  | shasum -a 1 _file_  |  _file_.sha1  |
> | SHA-256  | certUtil -hashfile _file_ SHA256  | sha256sum _file_  | shasum -a 256 _file_  |  _file_.sha256  |
> | SHA-512  | certUtil -hashfile _file_ SHA512  | sha512sum _file_  | shasum -a 512 _file_  |  _file_.sha512  |
> | MD5 (deprecated)  | certUtil -hashfile _file_ MD5  | md5sum _file_  | md5 _file_  |  _file_.md5  |
Only if you check the hash can you be certain that your download hasn't been modified or is otherwise incomplete or faulty.
## Checking Signatures[¶](https://www.apache.org/info/verification.html#CheckingSignatures "Permalink")
The following example details how signature interaction works. The example is for the Apache HTTP Server project, but applies equally to other ASF projects.
In this example, you are already assumed to have downloaded `httpd-2.0.44.tar.gz` (the release) and `httpd-2.0.44.tar.gz.asc` (the detached signature).
This example uses [The GNU Privacy Guard](https://www.gnupg.org/). Any [OpenPGP](http://www.openpgp.org/)-compliant program should work successfully.
First, we will check the detached signature (`httpd-2.0.44.tar.gz.asc`) against our release (`httpd-2.0.44.tar.gz`).
**N.B. you must specify both the detached signature and the release file.**
If the release file is omitted, GPG will only check the signature against the release file if the signature is a detached signature. If the .asc file is a self-contained signed file, GPG will only check that, and will not verify the release. (This should not happen if the signature file was downloaded from an ASF server, but it is safer to always specify the release filename)

```
% gpg --verify httpd-2.0.44.tar.gz.asc httpd-2.0.44.tar.gz
gpg: Signature made Sat Jan 18 07:21:28 2003 PST using DSA key ID DE885DD3
gpg: Can't check signature: public key not found

```

This means that we don't have the release manager's public key (`DE885DD3`) in our local system. You now need to retrieve the public key. The best source is the project's KEYS file. If you retrieve what seems to be the correct public key from a public key server, you must [validate it](https://www.irif.fr/~jch/software/pgp-validating.html). One popular server is `pgpkeys.mit.edu` (which has a [web interface](http://pgp.mit.edu/) ). The public key servers are linked together, so you should be able to connect to any key server.

```
% gpg --keyserver pgpkeys.mit.edu --recv-key DE885DD3
gpg: requesting key DE885DD3 from HKP keyserver pgpkeys.mit.edu
gpg: trustdb created
gpg: key DE885DD3: public key "Sander Striker <striker@apache.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1

```

In this example, you have now received a public key for an entity known as `Sander Striker <striker@apache.org>`. However, you have no way of verifying this key was created by the person known as Sander Striker. But, let's try to verify the release signature again.

```
% gpg --verify httpd-2.0.44.tar.gz.asc httpd-2.0.44.tar.gz
gpg: Signature made Sat Jan 18 07:21:28 2003 PST using DSA key ID DE885DD3
gpg: Good signature from "Sander Striker <striker@apache.org>"
gpg:                 aka "Sander Striker <striker@striker.nl>"
gpg: checking the trustdb
gpg: no ultimately trusted keys found
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Fingerprint: 4C1E ADAD B4EF 5007 579C  919C 6635 B6C0 DE88 5DD3

```

At this point, the signature is good, but we don't trust this key. A good signature means that the file has not been tampered with. However, due to the nature of public key cryptography, you need to additionally verify that key `DE885DD3` was created by the **real** Sander Striker.
Any attacker can create a public key and upload it to the public key servers. They can then create a malicious release signed by this fake key. Then, if you tried to verify the signature of this corrupt release, it would succeed because the key was not the 'real' key. Therefore, you need to validate the authenticity of this key.
### Validating Authenticity of a Key[¶](https://www.apache.org/info/verification.html#Validating "Permalink")
You may download public keys for the Apache project developers from our website or retrieve them from the public PGP keyservers (see above). However, importing these keys is not enough to verify the integrity of the signatures. If a release verifies as good, you need to validate that the key was created by an official representative of the Apache HTTP Server Project.
The crucial step to validation is to confirm the key fingerprint of the public key.

```
% gpg --fingerprint DE885DD3
pub  1024D/DE885DD3 2002-04-10 Sander Striker <striker@apache.org>
     Key fingerprint = 4C1E ADAD B4EF 5007 579C  919C 6635 B6C0 DE88 5DD3
uid                 Sander Striker <striker@striker.nl>
sub  2048g/532D14CA 2002-04-10

```

A good start to validating a key is by face-to-face communication with multiple government-issued photo identification confirmations. However, each person is free to have their own standards for determining the authenticity of a key. Some people are satisfied by reading the key signature over a telephone (voice verification). For more information on determining what level of trust works best for you, please read the GNU Privacy Handbook section on [Validating other keys on your public keyring](https://www.gnupg.org/gph/en/manual.html#AEN335).
Most of the Apache HTTP Server developers have attempted to sign each others' keys (usually with face-to-face validation). Therefore, in order to enter the web of trust, you should only need to validate one person in our web of trust. (Hint: all of our developers' keys are in the KEYS file.)
For example, the following people have signed the public key for Sander Striker. If you verify any key on this list, you will have a trust path to the `DE885DD3` key. If you verify a key that verifies one of the signatories for `DE885DD3`, then you will have a trust path. (So on, and so on.)

```
pub  1024D/DE885DD3 2002-04-10 Sander Striker <striker@apache.org>
sig        E2226795 2002-05-01   Justin R. Erenkrantz
sig 3      DE885DD3 2002-04-10   Sander Striker
sig        CD4DF205 2002-05-28   Wolfram Schlich
sig        E005C9CB 2002-11-17   Greg Stein
sig        CC8B0F7E 2002-11-18   Aaron Bannert
sig        DFEAC4B9 2002-11-19   David N. Welton
sig 2      82AB7BD1 2002-11-17   Cliff Woolley
sig 2      13046155 2002-11-28   Thom May
sig 3      19311B00 2002-11-17   Chuck Murcko
sig 3      F894BE12 2002-11-17   Brian William Fitzpatrick
sig 3      5C1C3AD7 2002-11-18   David Reid
sig 3      E04F9A89 2002-11-18   Roy T. Fielding
sig 3      CC78C893 2002-11-19   Rich Bowen
sig 3      08C975E5 2002-11-21   Jim Jagielski
sig 3      F88341D9 2002-11-18   Lars Eilebrecht
sig 3      187BD68D 2002-11-21   Ben Hyde
sig 3      49A563D9 2002-11-23   Mark Cox
...more signatures redacted...

```

Since the developers are usually quite busy, you may not immediately find success in someone who is willing to meet face-to-face (they may not even respond to your emails because they are so busy!). If you do not have a developer nearby or have trouble locating a suitable person, please send an email to the address of the key you are attempting to verify. They may be able to find someone who will be willing to validate their key or arrange alternate mechanisms for validation.
Once you have entered the web of trust, you should see the following upon verifying the signature of a release.

```
% gpg --verify httpd-2.0.44.tar.gz.asc httpd-2.0.44.tar.gz
gpg: Signature made Sat Jan 18 07:21:28 2003 PST using DSA key ID DE885DD3
gpg: Good signature from "Sander Striker <striker@apache.org>"
gpg:                 aka "Sander Striker <striker@striker.nl>"

```

## Subscribe to ASF Plus One, Our Monthly Newsletter
[Subscribe Now](https://news.apache.org/newsletter)
![ASF White Logo](https://www.apache.org/images/asf_logo_full_horizontal_white.svg)
Apache and the Apache logo are trademarks of The Apache Software Foundation.
The Apache® Software Foundation is a 501(c)(3) nonprofit organization. Tax ID # 47-0825376
[Donate](https://donate.apache.org/48ff)
[![slack icon](https://www.apache.org/images/slack-icon.svg)](https://infra.apache.org/slack.html) [![github icon](https://www.apache.org/images/github-mark-white.svg)](https://github.com/apache) [![linkedIn icon](https://www.apache.org/images/linkedin-icon.png)](https://www.linkedin.com/company/the-apache-software-foundation/) [![youtube icon](https://www.apache.org/images/youtube-icon.svg)](https://www.youtube.com/c/TheApacheFoundation) [![X icon](https://www.apache.org/images/x-icon.svg)](https://twitter.com/TheASF) [![Bluesky icon](https://www.apache.org/images/bluesky-icon.png)](https://bsky.app/profile/apache.org) [![Mastodon icon](https://www.apache.org/images/mastodon-icon.png)](https://fosstodon.org/@TheASF)
##### Community
  * [Contributor Getting Started](https://community.apache.org/)
  * [Becoming a Committer](https://community.apache.org/contributors/)
  * [Code of Conduct](https://www.apache.org/foundation/policies/conduct)
  * [Community Resources](https://www.apache.org/community-resources/)
  * [Community Over Code](https://communityovercode.org/)
  * [Events](https://events.apache.org/)

##### Learn
  * [Blog](https://news.apache.org/)
  * [How the ASF Works](https://www.apache.org/foundation/how-it-works)
  * [The Apache Way](https://www.apache.org/theapacheway/)
  * [Legal & Trademark](https://www.apache.org/legal/)
  * [Licenses](https://www.apache.org/licenses)
  * [Glossary](https://www.apache.org/foundation/glossary)
  * [FAQ](https://www.apache.org/foundation/faq)

##### Projects
  * [Projects](https://www.apache.org/projects)
  * [Incubator Projects](https://incubator.apache.org/)
  * [Projects Directory ](https://projects.apache.org/)
  * [Mailing Lists ](https://www.apache.org/foundation/mailinglists)
  * [Report a Vulnerability](https://www.apache.org/security)

##### Resources & Tools
  * [Developer Information](https://www.apache.org/dev/)
  * [Wiki](https://cwiki.apache.org/)
  * [Issues](https://issues.apache.org/)
  * [Slack](https://infra.apache.org/slack.html)
  * [Self Serve Portal](https://selfserve.apache.org/)
  * [Infrastructure](https://infra.apache.org/)
  * [Infrastructure Status](https://status.apache.org/)
  * [Infrastructure Statistics](https://infra-reports.apache.org/#uptime)
  * [Whimsy](https://whimsy.apache.org/)
  * [Brand Guidelines](https://www.apache.org/foundation/press/kit/)
  * [Project Logos](https://www.apache.org/logos/)

##### Downloads
  * [Distributions](https://downloads.apache.org/)
  * [Releases](https://projects.apache.org/releases.html)

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

Copyright © 2026 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
