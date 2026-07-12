[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/improvement-proposals.html)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/improvement-proposals.html)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/improvement-proposals.html)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/improvement-proposals.html)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/improvement-proposals.html)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)


  * [ Apache Software Foundation ](https://spark.apache.org/improvement-proposals.html)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)


# Spark Project Improvement Proposals (SPIP)
The purpose of an SPIP is to inform and involve the user community in major improvements to the Spark codebase throughout the development process, to increase the likelihood that user needs are met.
SPIPs should be used for significant user-facing or cross-cutting changes, not small incremental improvements. When in doubt, if a committer thinks a change needs an SPIP, it does.
### What is a SPIP?
An SPIP is similar to a product requirement document commonly used in product management.
An SPIP:
  * Is a JIRA ticket labeled “SPIP” proposing a major improvement or change to Spark
  * Follows the template defined below
  * Includes discussions on the JIRA ticket and dev@ list about the proposal


[Current SPIPs](https://issues.apache.org/jira/issues/?jql=project%20%3D%20SPARK%20AND%20status%20in%20\(Open%2C%20Reopened%2C%20%22In%20Progress%22\)%20AND%20\(labels%20%3D%20SPIP%20OR%20summary%20~%20%22SPIP%22\)%20ORDER%20BY%20createdDate%20DESC)
[Past SPIPs](https://issues.apache.org/jira/issues/?jql=project%20%3D%20SPARK%20AND%20status%20in%20\(Resolved\)%20AND%20\(labels%20%3D%20SPIP%20OR%20summary%20~%20%22SPIP%22\)%20ORDER%20BY%20createdDate%20DESC)
### Who?
Any **community member** can help by discussing whether an SPIP is likely to meet their needs, and by proposing SPIPs.
**Contributors** can help by discussing whether an SPIP is likely to be technically feasible.
**Committers** can help by discussing whether an SPIP aligns with long-term project goals, and by shepherding SPIPs.
**SPIP Author** is any community member who authors a SPIP and is committed to pushing the change through the entire process. SPIP authorship can be transferred.
**SPIP Shepherd** is a PMC member who is committed to shepherding the proposed change throughout the entire process. Although the shepherd can delegate or work with other committers in the development process, the shepherd is ultimately responsible for the success or failure of the SPIP. Responsibilities of the shepherd include, but are not limited to:
  * Be the advocate for the proposed change
  * Help push forward on design and achieve consensus among key stakeholders
  * Review code changes, making sure the change follows project standards
  * Get feedback from users and iterate on the design & implementation
  * Uphold the quality of the changes, including verifying whether the changes satisfy the goal of the SPIP and are absent of critical bugs before releasing them


### SPIP process
#### Proposing an SPIP
Anyone may propose an SPIP, using the document template below. Please only submit an SPIP if you are willing to help, at least with discussion.
After a SPIP is created, the author should email dev@spark.apache.org to notify the community of the SPIP, and discussions should ensue on the JIRA ticket.
If an SPIP is too small or incremental and should have been done through the normal JIRA process, a committer should remove the SPIP label.
#### SPIP document template
A SPIP document is a short document with a few questions, inspired by the Heilmeier Catechism:
**Q1.** What are you trying to do? Articulate your objectives using absolutely no jargon.
**Q2.** What problem is this proposal NOT designed to solve?
**Q3.** How is it done today, and what are the limits of current practice?
**Q4.** What is new in your approach and why do you think it will be successful?
**Q5.** Who cares? If you are successful, what difference will it make?
**Q6.** What are the risks?
**Q7.** How long will it take?
**Q8.** What are the mid-term and final “exams” to check for success?
**Appendix A.** Proposed API Changes. Optional section defining APIs changes, if any. Backward and forward compatibility must be taken into account.
**Appendix B.** Optional Design Sketch: How are the goals going to be accomplished? Give sufficient technical detail to allow a contributor to judge whether it’s likely to be feasible. Note that this is not a full design document.
**Appendix C.** Optional Rejected Designs: What alternatives were considered? Why were they rejected? If no alternatives have been considered, the problem needs more thought.
#### Discussing an SPIP
All discussion of an SPIP should take place in a public forum, preferably the discussion attached to the Jira. Any discussions that happen offline should be made available online for the public via meeting notes summarizing the discussions.
During this discussion, one or more shepherds should be identified among PMC members.
Once the discussion settles, the shepherd(s) should call for a vote on the SPIP moving forward on the dev@ list. The vote should be open for at least 72 hours and follows the typical Apache vote process and passes upon consensus (at least 3 +1 votes from PMC members and no -1 votes from PMC members). dev@ should be notified of the vote result.
If there does not exist at least one PMC member that is committed to shepherding the change within a month, the SPIP is rejected.
If a committer does not think a SPIP aligns with long-term project goals, or is not practical at the point of proposal, the committer should -1 the SPIP explicitly and give technical justifications.
#### Implementing an SPIP
Implementation should take place via the [standard process for code changes](https://spark.apache.org/contributing.html). Changes that require SPIPs typically also require design documents to be written and reviewed.
##### Latest News
  * [Spark 4.0.3 released](https://spark.apache.org/news/spark-4-0-3-released.html) (Jun 11, 2026)
  * [Spark 4.1.2 released](https://spark.apache.org/news/spark-4-1-2-released.html) (May 21, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview5-released.html) (May 01, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview4-released.html) (Apr 09, 2026)


[Archive](https://spark.apache.org/news/index.html)
[ ![](https://www.apache.org/events/current-event-234x60.png) ](https://www.apache.org/events/current-event.html)
[ Download Spark ](https://spark.apache.org/downloads.html)
Built-in Libraries: 
  * [SQL and DataFrames](https://spark.apache.org/sql/)
  * [Spark Streaming](https://spark.apache.org/streaming/)
  * [MLlib (machine learning)](https://spark.apache.org/mllib/)
  * [GraphX (graph)](https://spark.apache.org/graphx/)

[Third-Party Projects](https://spark.apache.org/third-party-projects.html)
* * *
Apache Spark, Spark, Apache, the Apache feather logo, and the Apache Spark project logo are either registered trademarks or trademarks of The Apache Software Foundation in the United States and other countries. See guidance on use of Apache Spark [trademarks](https://spark.apache.org/trademarks.html). All other marks mentioned may be trademarks or registered trademarks of their respective owners. Copyright © 2018 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/). 
