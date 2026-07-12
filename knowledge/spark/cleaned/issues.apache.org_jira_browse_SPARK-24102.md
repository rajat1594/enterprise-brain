[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24102)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-24102#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-24102#sidebar)
Linked Applications
Loading…
[![ASF Jira](https://issues.apache.org/jira/s/-vddc6b/820010/g3jj3a/_/jira-logo-scaled.png)](https://issues.apache.org/jira/secure/MyJiraHome.jspa)
  * [Dashboards](https://issues.apache.org/jira/secure/Dashboard.jspa "View and manage your dashboards")
  * [Projects](https://issues.apache.org/jira/browse/SPARK "View recent projects and browse a list of projects")
  * [Issues](https://issues.apache.org/jira/issues/ "Search for issues and view recent issues")

  *   * [Help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Help")
    * [Jira Core help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Go to the online documentation for Jira Core")
    * [Keyboard Shortcuts](https://issues.apache.org/jira/secure/ViewKeyboardShortcuts!default.jspa "Get more information about Jira's Keyboard Shortcuts \( Type '?' \)")
    * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa "Get more information about Jira")
    * [Jira Credits](https://issues.apache.org/jira/secure/credits/AroundTheWorld!default.jspa "See who did what")
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24102)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-24102)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-24102](https://issues.apache.org/jira/browse/SPARK-24102)

# RegressionEvaluator should use sample weight data
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24102 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-24102)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-24102/SPARK-24102.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-24102/SPARK-24102.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-24102/SPARK-24102.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-24102/SPARK-24102.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 2.0.2
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
    * [starter](https://issues.apache.org/jira/issues/?jql=labels+%3D+starter "starter")

#### Description
The LogisticRegression and LinearRegression models support training with a weight column, but the corresponding evaluators do not support computing metrics using those weights. This breaks model selection using CrossValidator.
#### Attachments
#### Issue Links

is a child of

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-18693](https://issues.apache.org/jira/browse/SPARK-18693) BinaryClassificationEvaluator, RegressionEvaluator, and MulticlassClassificationEvaluator should use sample weight data
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

is duplicated by

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-27153](https://issues.apache.org/jira/browse/SPARK-27153) add weightCol in python RegressionEvaluator
  * ![Minor - Minor loss of function, or other problem where easy workaround is present.](https://issues.apache.org/jira/images/icons/priorities/minor.svg)
  * Resolved

links to

![Pull request #17085](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #17085 (imatiach-msft)](https://github.com/apache/spark/pull/17085)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #17085](https://github.com/apache/spark/pull/17085)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #24197](https://github.com/apache/spark/pull/24197)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-24102?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-24102?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-24102?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-24102?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-24102?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-24102?actionOrder=desc "Ascending order - Click to sort in descending order")
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/May/18 20:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16474756&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474756)
User 'imatiach-msft' has created a pull request for this issue:
<https://github.com/apache/spark/pull/17085>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/May/18 20:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16474756&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474756) User 'imatiach-msft' has created a pull request for this issue: https://github.com/apache/spark/pull/17085
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716193&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716193)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075128>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716193&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716193) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075128 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716194&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716194)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075130>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5950/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716194&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716194) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075130 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5950/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716196&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716196)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075128>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716196&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716196) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075128 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716198&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716198)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075130>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5950/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716198&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716198) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075130 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5950/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716199&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716199)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075219>
**[Test build #99946 has started](https://issues.apache.org/jira/browse/SPARK-24102#99946%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)**> for PR 17085 at commit [`aca6255`](<https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:14](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716199&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716199) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075219 ** Test build #99946 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)** for PR 17085 at commit [`aca6255`] ( https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716220&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716220)
imatiach-msft commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077221>
ping @sethah @WeichenXu123 @jkbradley @actuaryzhang @srowen could you please take a look? I've updated the PR to latest and made it similar to the multiclass PR that was merged: <https://github.com/apache/spark/pull/17086>
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716220&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716220) imatiach-msft commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077221 ping @sethah @WeichenXu123 @jkbradley @actuaryzhang @srowen could you please take a look? I've updated the PR to latest and made it similar to the multiclass PR that was merged: https://github.com/apache/spark/pull/17086 ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716224&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716224)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077714>
**[Test build #99947 has started](https://issues.apache.org/jira/browse/SPARK-24102#99947%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)**> for PR 17085 at commit [`0de3209`](<https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716224&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716224) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077714 ** Test build #99947 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)** for PR 17085 at commit [`0de3209`] ( https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716225&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716225)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077742>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716225&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716225) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077742 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716226&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716226)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077744>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5951/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:30](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716226&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716226) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077744 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5951/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:31](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716227&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716227)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077742>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:31](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716227&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716227) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077742 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:31](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716228&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716228)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077744>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5951/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:31](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716228&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716228) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077744 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5951/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:35](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716231&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716231)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078542>
**[Test build #99948 has started](https://issues.apache.org/jira/browse/SPARK-24102#99948%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)**> for PR 17085 at commit [`0480721`](<https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:35](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716231&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716231) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078542 ** Test build #99948 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)** for PR 17085 at commit [`0480721`] ( https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716232&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716232)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078552>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716232&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716232) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078552 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716233&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716233)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078556>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5952/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716233&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716233) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078556 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5952/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716234&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716234)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078552>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716234&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716234) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078552 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716235&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716235)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078556>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5952/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:36](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716235&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716235) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078556 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5952/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716240&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716240)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079407>
**[Test build #99947 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99947%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)**> for PR 17085 at commit [`0de3209`](<https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5>).
  * This patch * **fails to build** *.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716240&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716240) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079407 ** Test build #99947 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)** for PR 17085 at commit [`0de3209`] ( https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5 ). This patch * fails to build *. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716241&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716241)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079413>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716241&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716241) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079413 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716242&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716242)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079415>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99947/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:41](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716242&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716242) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079415 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99947/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:42](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716243&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716243)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446077714>
**[Test build #99947 has started](https://issues.apache.org/jira/browse/SPARK-24102#99947%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)**> for PR 17085 at commit [`0de3209`](<https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:42](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716243&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716243) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446077714 ** Test build #99947 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99947/testReport)** for PR 17085 at commit [`0de3209`] ( https://github.com/apache/spark/commit/0de3209fa65b6391999668bf9e65042fefd27da5 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:42](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716244&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716244)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079413>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:42](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716244&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716244) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079413 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716246&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716246)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079415>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99947/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716246&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716246) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079415 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99947/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716247&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716247)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079811>
**[Test build #99948 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99948%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)**> for PR 17085 at commit [`0480721`](<https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57>).
  * This patch * **fails to build** *.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716247&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716247) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079811 ** Test build #99948 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)** for PR 17085 at commit [`0480721`] ( https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57 ). This patch * fails to build *. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716248&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716248)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079818>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716248&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716248) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079818 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716249&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716249)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079822>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99948/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:43](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716249&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716249) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079822 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99948/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:44](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716250&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716250)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446078542>
**[Test build #99948 has started](https://issues.apache.org/jira/browse/SPARK-24102#99948%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)**> for PR 17085 at commit [`0480721`](<https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:44](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716250&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716250) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446078542 ** Test build #99948 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99948/testReport)** for PR 17085 at commit [`0480721`] ( https://github.com/apache/spark/commit/04807214d8694dcff7a2fe042457934e67eb8d57 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:44](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716251&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716251)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079818>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:44](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716251&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716251) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079818 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716253&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716253)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446079822>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99948/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 05:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716253&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716253) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446079822 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99948/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716289&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716289)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083121>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716289&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716289) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083121 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716290&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716290)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083128>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5956/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716290&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716290) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083128 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5956/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716291&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716291)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083138>
**[Test build #99952 has started](https://issues.apache.org/jira/browse/SPARK-24102#99952%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)**> for PR 17085 at commit [`0cb2daf`](<https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:02](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716291&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716291) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083138 ** Test build #99952 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)** for PR 17085 at commit [`0cb2daf`] ( https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:03](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716292&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716292)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083121>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:03](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716292&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716292) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083121 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:03](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716293&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716293)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083128>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5956/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 06:03](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716293&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716293) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083128 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5956/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716437&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716437)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108009>
**[Test build #99946 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99946%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)**> for PR 17085 at commit [`aca6255`](<https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3>).
  * This patch * **fails due to an unknown error code, -9** *.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716437&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716437) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108009 ** Test build #99946 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)** for PR 17085 at commit [`aca6255`] ( https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3 ). This patch * fails due to an unknown error code, -9 *. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716438&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716438)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108008>
**[Test build #99952 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99952%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)**> for PR 17085 at commit [`0cb2daf`](<https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383>).
  * This patch * **fails due to an unknown error code, -9** *.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716438&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716438) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108008 ** Test build #99952 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)** for PR 17085 at commit [`0cb2daf`] ( https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383 ). This patch * fails due to an unknown error code, -9 *. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716445&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716445)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108099>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716445&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716445) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108099 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716446&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716446)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108108>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99952/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716446&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716446) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108108 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99952/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716451)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108193>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716451) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108193 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716452&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716452)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108200>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99946/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:05](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716452&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716452) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108200 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99946/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716455&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716455)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108108>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99952/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716455&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716455) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108108 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99952/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716456&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716456)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108099>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716456&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716456) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108099 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716458&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716458)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446083138>
**[Test build #99952 has started](https://issues.apache.org/jira/browse/SPARK-24102#99952%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)**> for PR 17085 at commit [`0cb2daf`](<https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716458&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716458) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446083138 ** Test build #99952 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99952/testReport)** for PR 17085 at commit [`0cb2daf`] ( https://github.com/apache/spark/commit/0cb2daf35888d80c5c223e16505354571d87d383 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716460&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716460)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446075219>
**[Test build #99946 has started](https://issues.apache.org/jira/browse/SPARK-24102#99946%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)**> for PR 17085 at commit [`aca6255`](<https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716460&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716460) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446075219 ** Test build #99946 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99946/testReport)** for PR 17085 at commit [`aca6255`] ( https://github.com/apache/spark/commit/aca62557fe394d500bd084ad840f9c0ff352cde3 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716461)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108193>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:06](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716461) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108193 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716483)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446108200>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99946/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 08:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16716483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716483) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446108200 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99946/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 14:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717220&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717220)
srowen commented on a change in pull request #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#discussion_r240622452>
##########
File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
##########
@@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
private var totalCnt: Long = 0
private var totalWeightSum: Double = 0.0
private var weightSquareSum: Double = 0.0
  * private var weightSum: Array[Double] = _
+ private var currWeightSum: Array[Double] = _

Review comment:
Nit: I don't think the rename was necessary, but it is OK
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 14:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717220&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717220) srowen commented on a change in pull request #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#discussion_r240622452 ########## File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala ########## @@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S private var totalCnt: Long = 0 private var totalWeightSum: Double = 0.0 private var weightSquareSum: Double = 0.0 private var weightSum: Array [Double] = _ + private var currWeightSum: Array [Double] = _ Review comment: Nit: I don't think the rename was necessary, but it is OK ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:11](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717448&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717448)
imatiach-msft commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446259327>
@srowen yes, exactly, there is a third PR here for classification: <https://github.com/apache/spark/pull/17084>
But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:11](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717448&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717448) imatiach-msft commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446259327 @srowen yes, exactly, there is a third PR here for classification: https://github.com/apache/spark/pull/17084 But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:12](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717449&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717449)
imatiach-msft commented on a change in pull request #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#discussion_r240677113>
##########
File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
##########
@@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
private var totalCnt: Long = 0
private var totalWeightSum: Double = 0.0
private var weightSquareSum: Double = 0.0
  * private var weightSum: Array[Double] = _
+ private var currWeightSum: Array[Double] = _

Review comment:
done!
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:12](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717449&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717449) imatiach-msft commented on a change in pull request #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#discussion_r240677113 ########## File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala ########## @@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S private var totalCnt: Long = 0 private var totalWeightSum: Double = 0.0 private var weightSquareSum: Double = 0.0 private var weightSum: Array [Double] = _ + private var currWeightSum: Array [Double] = _ Review comment: done! ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:12](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717450&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717450)
imatiach-msft edited a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446259327>
@srowen yes, exactly, there is a third PR here for classification: <https://github.com/apache/spark/pull/17084>
But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0).
The original PR had all three but it was recommended that I break it up into 3 parts:
<https://github.com/apache/spark/pull/16557>
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:12](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717450&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717450) imatiach-msft edited a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446259327 @srowen yes, exactly, there is a third PR here for classification: https://github.com/apache/spark/pull/17084 But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0). The original PR had all three but it was recommended that I break it up into 3 parts: https://github.com/apache/spark/pull/16557 ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717451)
imatiach-msft edited a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446259327>
@srowen yes, exactly, there is a third PR here for classification: <https://github.com/apache/spark/pull/17084>
But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0).
The original PR had all three but it was recommended that I break it up into 3 parts so I closed it and opened three separate PRs:
<https://github.com/apache/spark/pull/16557>
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:13](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717451) imatiach-msft edited a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446259327 @srowen yes, exactly, there is a third PR here for classification: https://github.com/apache/spark/pull/17084 But I need to update it in a similar way to how I just updated this PR (eg 2.2.0 -> 3.0.0). The original PR had all three but it was recommended that I break it up into 3 parts so I closed it and opened three separate PRs: https://github.com/apache/spark/pull/16557 ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717457&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717457)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262156>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717457&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717457) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262156 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717458&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717458)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262186>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5981/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717458&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717458) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262186 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5981/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717459&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717459)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262302>
**[Test build #99982 has started](https://issues.apache.org/jira/browse/SPARK-24102#99982%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)**> for PR 17085 at commit [`f708edb`](<https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:16](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717459&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717459) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262302 ** Test build #99982 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)** for PR 17085 at commit [`f708edb`] ( https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:17](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717461)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262156>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:17](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717461) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262156 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:17](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717462&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717462)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262186>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5981/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:17](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717462&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717462) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262186 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5981/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717477&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717477)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446265374>
**[Test build #99982 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99982%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)**> for PR 17085 at commit [`f708edb`](<https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b>).
  * This patch * **fails to build** *.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717477&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717477) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446265374 ** Test build #99982 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)** for PR 17085 at commit [`f708edb`] ( https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b ). This patch * fails to build *. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717478&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717478)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446265390>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717478&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717478) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446265390 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717479&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717479)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446265395>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99982/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:24](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717479&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717479) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446265395 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99982/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:26](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717482&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717482)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446262302>
**[Test build #99982 has started](https://issues.apache.org/jira/browse/SPARK-24102#99982%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)**> for PR 17085 at commit [`f708edb`](<https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:26](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717482&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717482) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446262302 ** Test build #99982 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99982/testReport)** for PR 17085 at commit [`f708edb`] ( https://github.com/apache/spark/commit/f708edb341b39544070193a15526e7282c8dfa0b ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:26](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717483)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446265390>
Merged build finished. Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:26](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717483) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446265390 Merged build finished. Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717485&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717485)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446265395>
Test FAILed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99982/>
Test FAILed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:27](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717485&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717485) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446265395 Test FAILed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99982/ Test FAILed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:37](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717505&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717505)
imatiach-msft commented on a change in pull request #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#discussion_r240690346>
##########
File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
##########
@@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
private var totalCnt: Long = 0
private var totalWeightSum: Double = 0.0
private var weightSquareSum: Double = 0.0
  * private var weightSum: Array[Double] = _
+ private var currWeightSum: Array[Double] = _

Review comment:
Nevermind, it looks like the build failed because the private variable conflicts with the public function that was defined:
/**
  * Sum of weights.
*/
override def weightSum: Double = totalWeightSum

I think this may be the best name for the public variable so I would prefer to keep it. The private variable now follows the naming convention of the other private array variables so I think this makes sense.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:37](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717505&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717505) imatiach-msft commented on a change in pull request #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#discussion_r240690346 ########## File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala ########## @@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S private var totalCnt: Long = 0 private var totalWeightSum: Double = 0.0 private var weightSquareSum: Double = 0.0 private var weightSum: Array [Double] = _ + private var currWeightSum: Array [Double] = _ Review comment: Nevermind, it looks like the build failed because the private variable conflicts with the public function that was defined: /** Sum of weights. */ override def weightSum: Double = totalWeightSum I think this may be the best name for the public variable so I would prefer to keep it. The private variable now follows the naming convention of the other private array variables so I think this makes sense. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:39](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717508&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717508)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446271282>
**[Test build #99984 has started](https://issues.apache.org/jira/browse/SPARK-24102#99984%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)**> for PR 17085 at commit [`24b66da`](<https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:39](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717508&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717508) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446271282 ** Test build #99984 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)** for PR 17085 at commit [`24b66da`] ( https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:39](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717509&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717509)
imatiach-msft commented on a change in pull request #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#discussion_r240690346>
##########
File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
##########
@@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
private var totalCnt: Long = 0
private var totalWeightSum: Double = 0.0
private var weightSquareSum: Double = 0.0
  * private var weightSum: Array[Double] = _
+ private var currWeightSum: Array[Double] = _

Review comment:
Nevermind, it looks like the build failed because the private variable conflicts with the public variable that was defined:
/**
  * Sum of weights.
*/
override def weightSum: Double = totalWeightSum

I think this may be the best name for the public variable so I would prefer to keep it. The private variable now follows the naming convention of the other private array variables so I think this makes sense.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:39](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717509&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717509) imatiach-msft commented on a change in pull request #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#discussion_r240690346 ########## File path: mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala ########## @@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S private var totalCnt: Long = 0 private var totalWeightSum: Double = 0.0 private var weightSquareSum: Double = 0.0 private var weightSum: Array [Double] = _ + private var currWeightSum: Array [Double] = _ Review comment: Nevermind, it looks like the build failed because the private variable conflicts with the public variable that was defined: /** Sum of weights. */ override def weightSum: Double = totalWeightSum I think this may be the best name for the public variable so I would prefer to keep it. The private variable now follows the naming convention of the other private array variables so I think this makes sense. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717519&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717519)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446273484>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717519&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717519) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446273484 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717520&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717520)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446273495>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5983/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:45](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717520&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717520) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446273495 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5983/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:47](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717524&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717524)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446273484>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:47](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717524&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717524) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446273484 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:47](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717525&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717525)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446273495>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5983/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 16:47](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717525&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717525) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446273495 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5983/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:50](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717979&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717979)
SparkQA commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446356977>
**[Test build #99984 has finished](https://issues.apache.org/jira/browse/SPARK-24102#99984%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)**> for PR 17085 at commit [`24b66da`](<https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2>).
  * This patch passes all tests.
  * This patch merges cleanly.
  * This patch adds no public classes.

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:50](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717979&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717979) SparkQA commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446356977 ** Test build #99984 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)** for PR 17085 at commit [`24b66da`] ( https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2 ). This patch passes all tests. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:51](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717980&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717980)
SparkQA removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446271282>
**[Test build #99984 has started](https://issues.apache.org/jira/browse/SPARK-24102#99984%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)**> for PR 17085 at commit [`24b66da`](<https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2>).
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:51](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717980&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717980) SparkQA removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446271282 ** Test build #99984 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99984/testReport)** for PR 17085 at commit [`24b66da`] ( https://github.com/apache/spark/commit/24b66da7e67781b85020f167754a9d68dd98b7e2 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:52](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717982&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717982)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446357564>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:52](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717982&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717982) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446357564 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:52](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717983&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717983)
AmplabJenkins commented on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446357573>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99984/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:52](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717983&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717983) AmplabJenkins commented on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446357573 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99984/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:53](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717984&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717984)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446357564>
Merged build finished. Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:53](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717984&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717984) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446357564 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:53](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717985&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717985)
AmplabJenkins removed a comment on issue #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085#issuecomment-446357573>
Test PASSed.
Refer to this link for build results (access rights to CI server needed):
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99984/>
Test PASSed.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 20:53](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16717985&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16717985) AmplabJenkins removed a comment on issue #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085#issuecomment-446357573 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99984/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [12/Dec/18 16:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16719128&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16719128)
Issue resolved by pull request 17085
<https://github.com/apache/spark/pull/17085>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [12/Dec/18 16:07](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16719128&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16719128) Issue resolved by pull request 17085 https://github.com/apache/spark/pull/17085
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 16:10](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16719133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16719133)
srowen closed pull request #17085: [~~SPARK-24102~~](https://issues.apache.org/jira/browse/SPARK-24102 "RegressionEvaluator should use sample weight data")[ML][MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator
URL: <https://github.com/apache/spark/pull/17085>
This is a PR merged from a forked repository.
As GitHub hides the original diff on merge, it is displayed below for
the sake of provenance:
As this is a foreign pull request (from a fork), the diff is supplied
below (as it won't show otherwise due to GitHub magic):
diff --git a/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala b/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala
index 031cd0d635bf4..616569bb55e4c 100644
— a/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala
@@ -19,7 +19,7 @@ package org.apache.spark.ml.evaluation
import org.apache.spark.annotation.
{Experimental, Since}
import org.apache.spark.ml.param.
{Param, ParamMap, ParamValidators}
-import org.apache.spark.ml.param.shared.
{HasLabelCol, HasPredictionCol}
+import org.apache.spark.ml.param.shared.
{HasLabelCol, HasPredictionCol, HasWeightCol}
import org.apache.spark.ml.util.
{DefaultParamsReadable, DefaultParamsWritable, Identifiable, SchemaUtils}
import org.apache.spark.mllib.evaluation.RegressionMetrics
import org.apache.spark.sql.
{Dataset, Row}
@@ -33,7 +33,8 @@ import org.apache.spark.sql.types.
{DoubleType, FloatType}
@Since("1.4.0")
@Experimental
final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val uid: String)
  * extends Evaluator with HasPredictionCol with HasLabelCol with DefaultParamsWritable {
+ extends Evaluator with HasPredictionCol with HasLabelCol
+ with HasWeightCol with DefaultParamsWritable {

@Since("1.4.0")
def this() = this(Identifiable.randomUID("regEval"))
@@ -69,6 +70,10 @@ final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val ui
@Since("1.4.0")
def setLabelCol(value: String): this.type = set(labelCol, value)
+ /** @group setParam */
+ @Since("3.0.0")
+ def setWeightCol(value: String): this.type = set(weightCol, value)
+
setDefault(metricName -> "rmse")
@Since("2.0.0")
@@ -77,11 +82,13 @@ final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val ui
SchemaUtils.checkColumnTypes(schema, $(predictionCol), Seq(DoubleType, FloatType))
SchemaUtils.checkNumericType(schema, $(labelCol))
  * val predictionAndLabels = dataset
  * .select(col($(predictionCol)).cast(DoubleType), col($(labelCol)).cast(DoubleType))
+ val predictionAndLabelsWithWeights = dataset
+ .select(col($(predictionCol)).cast(DoubleType), col($(labelCol)).cast(DoubleType),
+ if (!isDefined(weightCol) || $(weightCol).isEmpty) lit(1.0) else col($(weightCol)))
.rdd
  * .map { case Row(prediction: Double, label: Double) => (prediction, label) }
  * val metrics = new RegressionMetrics(predictionAndLabels)
+ .map { case Row(prediction: Double, label: Double, weight: Double) => + (prediction, label, weight) }
+ val metrics = new RegressionMetrics(predictionAndLabelsWithWeights)
val metric = $(metricName) match {
case "rmse" => metrics.rootMeanSquaredError
case "mse" => metrics.meanSquaredError
diff --git a/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala b/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala
index 020676cac5a64..525047973ad5c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala
+++ b/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala
@@ -27,17 +27,18 @@ import org.apache.spark.sql.DataFrame
/**

  * Evaluator for regression.
*

  * * @param predictionAndObservations an RDD of (prediction, observation) pairs
+ * @param predAndObsWithOptWeight an RDD of either (prediction, observation, weight)
+ * or (prediction, observation) pairs

  * @param throughOrigin True if the regression is through the origin. For example, in linear
  * regression, it will be true without fitting intercept.
*/
@Since("1.2.0")
class RegressionMetrics @Since("2.0.0") (

  * predictionAndObservations: RDD[(Double, Double)], throughOrigin: Boolean)
+ predAndObsWithOptWeight: RDD[_ <: Product], throughOrigin: Boolean)
extends Logging {

@Since("1.2.0")
  * def this(predictionAndObservations: RDD[(Double, Double)]) =
+ def this(predictionAndObservations: RDD[_ <: Product]) =
this(predictionAndObservations, false)

/**
@@ -52,10 +53,13 @@ class RegressionMetrics @Since("2.0.0") (
  * Use MultivariateOnlineSummarizer to calculate summary statistics of observations and errors.
*/
private lazy val summary: MultivariateStatisticalSummary = {

  * val summary: MultivariateStatisticalSummary = predictionAndObservations.map {
  * case (prediction, observation) => Vectors.dense(observation, observation - prediction)
+ val summary: MultivariateStatisticalSummary = predAndObsWithOptWeight.map { + case (prediction: Double, observation: Double, weight: Double) => + (Vectors.dense(observation, observation - prediction), weight) + case (prediction: Double, observation: Double) => + (Vectors.dense(observation, observation - prediction), 1.0) }
.treeAggregate(new MultivariateOnlineSummarizer())(
  * (summary, v) => summary.add(v),
+ (summary, sample) => summary.add(sample._1, sample._2),
(sum1, sum2) => sum1.merge(sum2)
)
summary
@@ -63,11 +67,13 @@ class RegressionMetrics @Since("2.0.0") (

private lazy val SSy = math.pow(summary.normL2(0), 2)
private lazy val SSerr = math.pow(summary.normL2(1), 2)
  * private lazy val SStot = summary.variance(0) * (summary.count - 1)
+ private lazy val SStot = summary.variance(0) * (summary.weightSum - 1)
private lazy val SSreg = {
val yMean = summary.mean(0)
  * predictionAndObservations.map {
  * case (prediction, _) => math.pow(prediction - yMean, 2)
+ predAndObsWithOptWeight.map { + case (prediction: Double, _: Double, weight: Double) => + math.pow(prediction - yMean, 2) * weight + case (prediction: Double, _: Double) => math.pow(prediction - yMean, 2) }
.sum()
}

@@ -79,7 +85,7 @@ class RegressionMetrics @Since("2.0.0") (
*/
@Since("1.2.0")
def explainedVariance: Double =
{ - SSreg / summary.count + SSreg / summary.weightSum }
/**
@@ -88,7 +94,7 @@ class RegressionMetrics @Since("2.0.0") (
*/
@Since("1.2.0")
def meanAbsoluteError: Double =
{ - summary.normL1(1) / summary.count + summary.normL1(1) / summary.weightSum }
/**
@@ -97,7 +103,7 @@ class RegressionMetrics @Since("2.0.0") (
*/
@Since("1.2.0")
def meanSquaredError: Double =
{ - SSerr / summary.count + SSerr / summary.weightSum }
/**
diff --git a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
index 0554b6d8ff5b5..6d510e1633d67 100644
— a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
+++ b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala
@@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
private var totalCnt: Long = 0
private var totalWeightSum: Double = 0.0
private var weightSquareSum: Double = 0.0
  * private var weightSum: Array[Double] = _
+ private var currWeightSum: Array[Double] = _
private var nnz: Array[Long] = _
private var currMax: Array[Double] = _
private var currMin: Array[Double] = _
@@ -78,7 +78,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
currM2n = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
currM2 = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
currL1 = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
  * weightSum = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
+ currWeightSum = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
nnz = Array.ofDim[Long]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
currMax = Array.fill[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)(Double.MinValue)
currMin = Array.fill[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)(Double.MaxValue)
@@ -91,7 +91,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
val localCurrM2n = currM2n
val localCurrM2 = currM2
val localCurrL1 = currL1
  * val localWeightSum = weightSum
+ val localWeightSum = currWeightSum
val localNumNonzeros = nnz
val localCurrMax = currMax
val localCurrMin = currMin
@@ -139,8 +139,8 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
weightSquareSum += other.weightSquareSum
var i = 0
while (i < n) {
  * val thisNnz = weightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png)
  * val otherNnz = other.weightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png)
+ val thisNnz = currWeightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png)
+ val otherNnz = other.currWeightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png)
val totalNnz = thisNnz + otherNnz
val totalCnnz = nnz![](https://issues.apache.org/jira/images/icons/emoticons/information.png) + other.nnz![](https://issues.apache.org/jira/images/icons/emoticons/information.png)
if (totalNnz != 0.0) { @@ -157,7 +157,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S currMax(i) = math.max(currMax(i), other.currMax(i)) currMin(i) = math.min(currMin(i), other.currMin(i)) }
  * weightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png) = totalNnz
+ currWeightSum![](https://issues.apache.org/jira/images/icons/emoticons/information.png) = totalNnz
nnz![](https://issues.apache.org/jira/images/icons/emoticons/information.png) = totalCnnz
i += 1
}
@@ -170,7 +170,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
this.totalCnt = other.totalCnt
this.totalWeightSum = other.totalWeightSum
this.weightSquareSum = other.weightSquareSum
  * this.weightSum = other.weightSum.clone()
+ this.currWeightSum = other.currWeightSum.clone()
this.nnz = other.nnz.clone()
this.currMax = other.currMax.clone()
this.currMin = other.currMin.clone()
@@ -189,7 +189,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
val realMean = Array.ofDim[Double]![](https://issues.apache.org/jira/images/icons/emoticons/thumbs_down.png)
var i = 0
while (i < n) { - realMean(i) = currMean(i) * (weightSum(i) / totalWeightSum) + realMean(i) = currMean(i) * (currWeightSum(i) / totalWeightSum) i += 1 }
Vectors.dense(realMean)
@@ -214,8 +214,8 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
val len = currM2n.length
while (i < len)
{ // We prevent variance from negative value caused by numerical error. - realVariance(i) = math.max((currM2n(i) + deltaMean(i) * deltaMean(i) * weightSum(i) * - (totalWeightSum - weightSum(i)) / totalWeightSum) / denominator, 0.0) + realVariance(i) = math.max((currM2n(i) + deltaMean(i) * deltaMean(i) * currWeightSum(i) * + (totalWeightSum - currWeightSum(i)) / totalWeightSum) / denominator, 0.0) i += 1 }
}
@@ -229,6 +229,11 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S
@Since("1.1.0")
override def count: Long = totalCnt

+ /**
+ * Sum of weights.
+ */
+ override def weightSum: Double = totalWeightSum
+
/**
  * Number of nonzero elements in each dimension.
*
diff --git a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala
index 39a16fb743d64..a4381032f8c0d 100644
    *       * a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala
+++ b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala
@@ -44,6 +44,12 @@ trait MultivariateStatisticalSummary {
@Since("1.0.0")
def count: Long

+ /**
+ * Sum of weights.
+ */
+ @Since("3.0.0")
+ def weightSum: Double
+
/**
  * Number of nonzero elements (including explicitly presented zero values) in each column.
*/
diff --git a/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala b/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala
index f1d517383643d..23809777f7d3a 100644
    *       * a/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala
+++ b/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala
@@ -133,4 +133,54 @@ class RegressionMetricsSuite extends SparkFunSuite with MLlibTestSparkContext { "root mean squared error mismatch") assert(metrics.r2 ~== 1.0 absTol eps, "r2 score mismatch") }
+
+ test("regression metrics with same (1.0) weight samples")
{ + val predictionAndObservationWithWeight = sc.parallelize( + Seq((2.25, 3.0, 1.0), (-0.25, -0.5, 1.0), (1.75, 2.0, 1.0), (7.75, 7.0, 1.0)), 2) + val metrics = new RegressionMetrics(predictionAndObservationWithWeight, false) + assert(metrics.explainedVariance ~== 8.79687 absTol eps, + "explained variance regression score mismatch") + assert(metrics.meanAbsoluteError ~== 0.5 absTol eps, "mean absolute error mismatch") + assert(metrics.meanSquaredError ~== 0.3125 absTol eps, "mean squared error mismatch") + assert(metrics.rootMeanSquaredError ~== 0.55901 absTol eps, + "root mean squared error mismatch") + assert(metrics.r2 ~== 0.95717 absTol eps, "r2 score mismatch") + }
+
+ /**
+ * The following values are hand calculated using the formula:
+ * [[https://en.wikipedia.org/wiki/Weighted_arithmetic_mean#Reliability_weights]](https://issues.apache.org/jira/browse/SPARK-24102#Reliability_weights\])
+ * preds = c(2.25, -0.25, 1.75, 7.75)
+ * obs = c(3.0, -0.5, 2.0, 7.0)
+ * weights = c(0.1, 0.2, 0.15, 0.05)
+ * count = 4
+ *
+ * Weighted metrics can be calculated with MultivariateStatisticalSummary.
+ * (observations, observations - predictions)
+ * mean (1.7, 0.05)
+ * variance (7.3, 0.3)
+ * numNonZeros (0.5, 0.5)
+ * max (7.0, 0.75)
+ * min (-0.5, -0.75)
+ * normL2 (2.0, 0.32596)
+ * normL1 (1.05, 0.2)
+ *
+ * explainedVariance: sum(pow((preds - 1.7),2)*weight) / weightedCount = 5.2425
+ * meanAbsoluteError: normL1(1) / weightedCount = 0.4
+ * meanSquaredError: pow(normL2(1),2) / weightedCount = 0.2125
+ * rootMeanSquaredError: sqrt(meanSquaredError) = 0.46098
+ * r2: 1 - pow(normL2(1),2) / (variance(0) * (weightedCount - 1)) = 1.02910
+ */
+ test("regression metrics with weighted samples")
{ + val predictionAndObservationWithWeight = sc.parallelize( + Seq((2.25, 3.0, 0.1), (-0.25, -0.5, 0.2), (1.75, 2.0, 0.15), (7.75, 7.0, 0.05)), 2) + val metrics = new RegressionMetrics(predictionAndObservationWithWeight, false) + assert(metrics.explainedVariance ~== 5.2425 absTol eps, + "explained variance regression score mismatch") + assert(metrics.meanAbsoluteError ~== 0.4 absTol eps, "mean absolute error mismatch") + assert(metrics.meanSquaredError ~== 0.2125 absTol eps, "mean squared error mismatch") + assert(metrics.rootMeanSquaredError ~== 0.46098 absTol eps, + "root mean squared error mismatch") + assert(metrics.r2 ~== 1.02910 absTol eps, "r2 score mismatch") + }
}
diff --git a/project/MimaExcludes.scala b/project/MimaExcludes.scala
index b3252d70a80c8..883913332ca1e 100644
      * a/project/MimaExcludes.scala
+++ b/project/MimaExcludes.scala
@@ -531,7 +531,10 @@ object MimaExcludes {
ProblemFilters.exclude[ReversedMissingMethodProblem]("org.apache.spark.ml.linalg.Matrix.toDenseColMajor"),
ProblemFilters.exclude[ReversedMissingMethodProblem]("org.apache.spark.ml.linalg.Matrix.toDenseMatrix"),
ProblemFilters.exclude[ReversedMissingMethodProblem]("org.apache.spark.ml.linalg.Matrix.toSparseMatrix"),

  * ProblemFilters.exclude[ReversedMissingMethodProblem]("org.apache.spark.ml.linalg.Matrix.getSizeInBytes")
+ ProblemFilters.exclude[ReversedMissingMethodProblem]("org.apache.spark.ml.linalg.Matrix.getSizeInBytes"),
+
+ // [~~SPARK-18693~~](https://issues.apache.org/jira/browse/SPARK-18693 "BinaryClassificationEvaluator, RegressionEvaluator, and MulticlassClassificationEvaluator should use sample weight data") Added weightSum to trait MultivariateStatisticalSummary
+ ProblemFilters.exclude[MissingMethodProblem]("org.apache.spark.mllib.stat.MultivariateStatisticalSummary.weightSum")
) ++ Seq(
// [~~SPARK-17019~~](https://issues.apache.org/jira/browse/SPARK-17019 "Expose off-heap memory usage in various places") Expose on-heap and off-heap memory usage in various places
ProblemFilters.exclude[DirectMissingMethodProblem]("org.apache.spark.scheduler.SparkListenerBlockManagerAdded.copy"),

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 16:10](https://issues.apache.org/jira/browse/SPARK-24102?focusedCommentId=16719133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16719133) srowen closed pull request #17085: SPARK-24102 [ML] [MLLIB] ML Evaluators should use weight column - added weight column for regression evaluator URL: https://github.com/apache/spark/pull/17085 This is a PR merged from a forked repository. As GitHub hides the original diff on merge, it is displayed below for the sake of provenance: As this is a foreign pull request (from a fork), the diff is supplied below (as it won't show otherwise due to GitHub magic): diff --git a/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala b/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala index 031cd0d635bf4..616569bb55e4c 100644 — a/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.scala @@ -19,7 +19,7 @@ package org.apache.spark.ml.evaluation import org.apache.spark.annotation. {Experimental, Since} import org.apache.spark.ml.param. {Param, ParamMap, ParamValidators} -import org.apache.spark.ml.param.shared. {HasLabelCol, HasPredictionCol} +import org.apache.spark.ml.param.shared. {HasLabelCol, HasPredictionCol, HasWeightCol} import org.apache.spark.ml.util. {DefaultParamsReadable, DefaultParamsWritable, Identifiable, SchemaUtils} import org.apache.spark.mllib.evaluation.RegressionMetrics import org.apache.spark.sql. {Dataset, Row} @@ -33,7 +33,8 @@ import org.apache.spark.sql.types. {DoubleType, FloatType} @Since("1.4.0") @Experimental final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val uid: String) extends Evaluator with HasPredictionCol with HasLabelCol with DefaultParamsWritable { + extends Evaluator with HasPredictionCol with HasLabelCol + with HasWeightCol with DefaultParamsWritable { @Since("1.4.0") def this() = this(Identifiable.randomUID("regEval")) @@ -69,6 +70,10 @@ final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val ui @Since("1.4.0") def setLabelCol(value: String): this.type = set(labelCol, value) + /** @group setParam */ + @Since("3.0.0") + def setWeightCol(value: String): this.type = set(weightCol, value) + setDefault(metricName -> "rmse") @Since("2.0.0") @@ -77,11 +82,13 @@ final class RegressionEvaluator @Since("1.4.0") (@Since("1.4.0") override val ui SchemaUtils.checkColumnTypes(schema, $(predictionCol), Seq(DoubleType, FloatType)) SchemaUtils.checkNumericType(schema, $(labelCol)) val predictionAndLabels = dataset .select(col($(predictionCol)).cast(DoubleType), col($(labelCol)).cast(DoubleType)) + val predictionAndLabelsWithWeights = dataset + .select(col($(predictionCol)).cast(DoubleType), col($(labelCol)).cast(DoubleType), + if (!isDefined(weightCol) || $(weightCol).isEmpty) lit(1.0) else col($(weightCol))) .rdd .map { case Row(prediction: Double, label: Double) => (prediction, label) } val metrics = new RegressionMetrics(predictionAndLabels) + .map { case Row(prediction: Double, label: Double, weight: Double) => + (prediction, label, weight) } + val metrics = new RegressionMetrics(predictionAndLabelsWithWeights) val metric = $(metricName) match { case "rmse" => metrics.rootMeanSquaredError case "mse" => metrics.meanSquaredError diff --git a/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala b/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala index 020676cac5a64..525047973ad5c 100644 a/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala +++ b/mllib/src/main/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.scala @@ -27,17 +27,18 @@ import org.apache.spark.sql.DataFrame /** Evaluator for regression. * * @param predictionAndObservations an RDD of (prediction, observation) pairs + * @param predAndObsWithOptWeight an RDD of either (prediction, observation, weight) + * or (prediction, observation) pairs @param throughOrigin True if the regression is through the origin. For example, in linear regression, it will be true without fitting intercept. */ @Since("1.2.0") class RegressionMetrics @Since("2.0.0") ( predictionAndObservations: RDD [(Double, Double)] , throughOrigin: Boolean) + predAndObsWithOptWeight: RDD [_ <: Product] , throughOrigin: Boolean) extends Logging { @Since("1.2.0") def this(predictionAndObservations: RDD [(Double, Double)] ) = + def this(predictionAndObservations: RDD [_ <: Product] ) = this(predictionAndObservations, false) /** @@ -52,10 +53,13 @@ class RegressionMetrics @Since("2.0.0") ( Use MultivariateOnlineSummarizer to calculate summary statistics of observations and errors. */ private lazy val summary: MultivariateStatisticalSummary = { val summary: MultivariateStatisticalSummary = predictionAndObservations.map { case (prediction, observation) => Vectors.dense(observation, observation - prediction) + val summary: MultivariateStatisticalSummary = predAndObsWithOptWeight.map { + case (prediction: Double, observation: Double, weight: Double) => + (Vectors.dense(observation, observation - prediction), weight) + case (prediction: Double, observation: Double) => + (Vectors.dense(observation, observation - prediction), 1.0) } .treeAggregate(new MultivariateOnlineSummarizer())( (summary, v) => summary.add(v), + (summary, sample) => summary.add(sample._1, sample._2), (sum1, sum2) => sum1.merge(sum2) ) summary @@ -63,11 +67,13 @@ class RegressionMetrics @Since("2.0.0") ( private lazy val SSy = math.pow(summary.normL2(0), 2) private lazy val SSerr = math.pow(summary.normL2(1), 2) private lazy val SStot = summary.variance(0) * (summary.count - 1) + private lazy val SStot = summary.variance(0) * (summary.weightSum - 1) private lazy val SSreg = { val yMean = summary.mean(0) predictionAndObservations.map { case (prediction, _) => math.pow(prediction - yMean, 2) + predAndObsWithOptWeight.map { + case (prediction: Double, _: Double, weight: Double) => + math.pow(prediction - yMean, 2) * weight + case (prediction: Double, _: Double) => math.pow(prediction - yMean, 2) } .sum() } @@ -79,7 +85,7 @@ class RegressionMetrics @Since("2.0.0") ( */ @Since("1.2.0") def explainedVariance: Double = { - SSreg / summary.count + SSreg / summary.weightSum } /** @@ -88,7 +94,7 @@ class RegressionMetrics @Since("2.0.0") ( */ @Since("1.2.0") def meanAbsoluteError: Double = { - summary.normL1(1) / summary.count + summary.normL1(1) / summary.weightSum } /** @@ -97,7 +103,7 @@ class RegressionMetrics @Since("2.0.0") ( */ @Since("1.2.0") def meanSquaredError: Double = { - SSerr / summary.count + SSerr / summary.weightSum } /** diff --git a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala index 0554b6d8ff5b5..6d510e1633d67 100644 — a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala +++ b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateOnlineSummarizer.scala @@ -52,7 +52,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S private var totalCnt: Long = 0 private var totalWeightSum: Double = 0.0 private var weightSquareSum: Double = 0.0 private var weightSum: Array [Double] = _ + private var currWeightSum: Array [Double] = _ private var nnz: Array [Long] = _ private var currMax: Array [Double] = _ private var currMin: Array [Double] = _ @@ -78,7 +78,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S currM2n = Array.ofDim [Double] currM2 = Array.ofDim [Double] currL1 = Array.ofDim [Double] weightSum = Array.ofDim [Double] + currWeightSum = Array.ofDim [Double] nnz = Array.ofDim [Long] currMax = Array.fill [Double] (Double.MinValue) currMin = Array.fill [Double] (Double.MaxValue) @@ -91,7 +91,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S val localCurrM2n = currM2n val localCurrM2 = currM2 val localCurrL1 = currL1 val localWeightSum = weightSum + val localWeightSum = currWeightSum val localNumNonzeros = nnz val localCurrMax = currMax val localCurrMin = currMin @@ -139,8 +139,8 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S weightSquareSum += other.weightSquareSum var i = 0 while (i < n) { val thisNnz = weightSum val otherNnz = other.weightSum + val thisNnz = currWeightSum + val otherNnz = other.currWeightSum val totalNnz = thisNnz + otherNnz val totalCnnz = nnz + other.nnz if (totalNnz != 0.0) { @@ -157,7 +157,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S currMax(i) = math.max(currMax(i), other.currMax(i)) currMin(i) = math.min(currMin(i), other.currMin(i)) } weightSum = totalNnz + currWeightSum = totalNnz nnz = totalCnnz i += 1 } @@ -170,7 +170,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S this.totalCnt = other.totalCnt this.totalWeightSum = other.totalWeightSum this.weightSquareSum = other.weightSquareSum this.weightSum = other.weightSum.clone() + this.currWeightSum = other.currWeightSum.clone() this.nnz = other.nnz.clone() this.currMax = other.currMax.clone() this.currMin = other.currMin.clone() @@ -189,7 +189,7 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S val realMean = Array.ofDim [Double] var i = 0 while (i < n) { - realMean(i) = currMean(i) * (weightSum(i) / totalWeightSum) + realMean(i) = currMean(i) * (currWeightSum(i) / totalWeightSum) i += 1 } Vectors.dense(realMean) @@ -214,8 +214,8 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S val len = currM2n.length while (i < len) { // We prevent variance from negative value caused by numerical error. - realVariance(i) = math.max((currM2n(i) + deltaMean(i) * deltaMean(i) * weightSum(i) * - (totalWeightSum - weightSum(i)) / totalWeightSum) / denominator, 0.0) + realVariance(i) = math.max((currM2n(i) + deltaMean(i) * deltaMean(i) * currWeightSum(i) * + (totalWeightSum - currWeightSum(i)) / totalWeightSum) / denominator, 0.0) i += 1 } } @@ -229,6 +229,11 @@ class MultivariateOnlineSummarizer extends MultivariateStatisticalSummary with S @Since("1.1.0") override def count: Long = totalCnt + /** + * Sum of weights. + */ + override def weightSum: Double = totalWeightSum + /** Number of nonzero elements in each dimension. * diff --git a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala index 39a16fb743d64..a4381032f8c0d 100644 a/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala +++ b/mllib/src/main/scala/org/apache/spark/mllib/stat/MultivariateStatisticalSummary.scala @@ -44,6 +44,12 @@ trait MultivariateStatisticalSummary { @Since("1.0.0") def count: Long + /** + * Sum of weights. + */ + @Since("3.0.0") + def weightSum: Double + /** Number of nonzero elements (including explicitly presented zero values) in each column. */ diff --git a/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala b/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala index f1d517383643d..23809777f7d3a 100644 a/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala +++ b/mllib/src/test/scala/org/apache/spark/mllib/evaluation/RegressionMetricsSuite.scala @@ -133,4 +133,54 @@ class RegressionMetricsSuite extends SparkFunSuite with MLlibTestSparkContext { "root mean squared error mismatch") assert(metrics.r2 ~== 1.0 absTol eps, "r2 score mismatch") } + + test("regression metrics with same (1.0) weight samples") { + val predictionAndObservationWithWeight = sc.parallelize( + Seq((2.25, 3.0, 1.0), (-0.25, -0.5, 1.0), (1.75, 2.0, 1.0), (7.75, 7.0, 1.0)), 2) + val metrics = new RegressionMetrics(predictionAndObservationWithWeight, false) + assert(metrics.explainedVariance ~== 8.79687 absTol eps, + "explained variance regression score mismatch") + assert(metrics.meanAbsoluteError ~== 0.5 absTol eps, "mean absolute error mismatch") + assert(metrics.meanSquaredError ~== 0.3125 absTol eps, "mean squared error mismatch") + assert(metrics.rootMeanSquaredError ~== 0.55901 absTol eps, + "root mean squared error mismatch") + assert(metrics.r2 ~== 0.95717 absTol eps, "r2 score mismatch") + } + + /** + * The following values are hand calculated using the formula: + * [https://en.wikipedia.org/wiki/Weighted_arithmetic_mean#Reliability_weights] + * preds = c(2.25, -0.25, 1.75, 7.75) + * obs = c(3.0, -0.5, 2.0, 7.0) + * weights = c(0.1, 0.2, 0.15, 0.05) + * count = 4 + * + * Weighted metrics can be calculated with MultivariateStatisticalSummary. + * (observations, observations - predictions) + * mean (1.7, 0.05) + * variance (7.3, 0.3) + * numNonZeros (0.5, 0.5) + * max (7.0, 0.75) + * min (-0.5, -0.75) + * normL2 (2.0, 0.32596) + * normL1 (1.05, 0.2) + * + * explainedVariance: sum(pow((preds - 1.7),2)*weight) / weightedCount = 5.2425 + * meanAbsoluteError: normL1(1) / weightedCount = 0.4 + * meanSquaredError: pow(normL2(1),2) / weightedCount = 0.2125 + * rootMeanSquaredError: sqrt(meanSquaredError) = 0.46098 + * r2: 1 - pow(normL2(1),2) / (variance(0) * (weightedCount - 1)) = 1.02910 + */ + test("regression metrics with weighted samples") { + val predictionAndObservationWithWeight = sc.parallelize( + Seq((2.25, 3.0, 0.1), (-0.25, -0.5, 0.2), (1.75, 2.0, 0.15), (7.75, 7.0, 0.05)), 2) + val metrics = new RegressionMetrics(predictionAndObservationWithWeight, false) + assert(metrics.explainedVariance ~== 5.2425 absTol eps, + "explained variance regression score mismatch") + assert(metrics.meanAbsoluteError ~== 0.4 absTol eps, "mean absolute error mismatch") + assert(metrics.meanSquaredError ~== 0.2125 absTol eps, "mean squared error mismatch") + assert(metrics.rootMeanSquaredError ~== 0.46098 absTol eps, + "root mean squared error mismatch") + assert(metrics.r2 ~== 1.02910 absTol eps, "r2 score mismatch") + } } diff --git a/project/MimaExcludes.scala b/project/MimaExcludes.scala index b3252d70a80c8..883913332ca1e 100644 a/project/MimaExcludes.scala +++ b/project/MimaExcludes.scala @@ -531,7 +531,10 @@ object MimaExcludes { ProblemFilters.exclude [ReversedMissingMethodProblem] ("org.apache.spark.ml.linalg.Matrix.toDenseColMajor"), ProblemFilters.exclude [ReversedMissingMethodProblem] ("org.apache.spark.ml.linalg.Matrix.toDenseMatrix"), ProblemFilters.exclude [ReversedMissingMethodProblem] ("org.apache.spark.ml.linalg.Matrix.toSparseMatrix"), ProblemFilters.exclude [ReversedMissingMethodProblem] ("org.apache.spark.ml.linalg.Matrix.getSizeInBytes") + ProblemFilters.exclude [ReversedMissingMethodProblem] ("org.apache.spark.ml.linalg.Matrix.getSizeInBytes"), + + // SPARK-18693 Added weightSum to trait MultivariateStatisticalSummary + ProblemFilters.exclude [MissingMethodProblem] ("org.apache.spark.mllib.stat.MultivariateStatisticalSummary.weightSum") ) ++ Seq( // SPARK-17019 Expose on-heap and off-heap memory usage in various places ProblemFilters.exclude [DirectMissingMethodProblem] ("org.apache.spark.scheduler.SparkListenerBlockManagerAdded.copy"), ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
#### People

Assignee:
     ![imatiach](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ilya Matiach

Reporter:
     ![imatiach](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ilya Matiach

Votes:
     0 Vote for this issue

Watchers:
     5 Start watching this issue
#### Dates

Created:
     26/Apr/18 15:50

Updated:
     15/Feb/26 20:10

Resolved:
     12/Dec/18 16:07
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)
