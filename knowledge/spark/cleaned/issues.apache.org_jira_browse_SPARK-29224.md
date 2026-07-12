[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29224)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-29224#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-29224#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29224)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-29224)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-29224](https://issues.apache.org/jira/browse/SPARK-29224)

# Implement Factorization Machines as a ml-pipeline component
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29224 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-29224)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-29224/SPARK-29224.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-29224/SPARK-29224.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-29224/SPARK-29224.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-29224/SPARK-29224.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 3.0.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None

#### Description
Factorization Machines is widely used in advertising and recommendation system to estimate CTR(click-through rate).
Advertising and recommendation system usually has a lot of data, so we need Spark to estimate the CTR, and Factorization Machines are common ml model to estimate CTR.
Goal: Implement Factorization Machines as a ml-pipeline component
Requirements:
1. loss function supports: logloss, mse
2. optimizer: mini batch SGD
References:
1. S. Rendle, “Factorization machines,” in Proceedings of IEEE International Conference on Data Mining (ICDM), pp. 995–1000, 2010.
<https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf>
#### Attachments
#### Attachments
  * Options
    * [Sort By Name](https://issues.apache.org/jira/browse/SPARK-29224?attachmentSortBy=fileName#attachmentmodule "viewissue.subtasks.tab.show.all.name")
    * [Sort By Date](https://issues.apache.org/jira/browse/SPARK-29224?attachmentSortBy=dateTime#attachmentmodule "Sort By Date")
    * [Ascending](https://issues.apache.org/jira/browse/SPARK-29224?attachmentOrder=asc#attachmentmodule "Ascending")
    * [Descending](https://issues.apache.org/jira/browse/SPARK-29224?attachmentOrder=desc#attachmentmodule "Descending")

  1. [](https://issues.apache.org/jira/secure/attachment/12983046/url_loss.xlsx)

[url_loss.xlsx](https://issues.apache.org/jira/secure/attachment/12983046/url_loss.xlsx "Latest  15/Oct/19 11:24 - mob-ai")
    15/Oct/19 11:24     17 kB     mob-ai

#### Issue Links

links to

![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #25909](https://github.com/apache/spark/pull/25909)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #26124](https://github.com/apache/spark/pull/26124)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #27000](https://github.com/apache/spark/pull/27000)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-29224?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-29224?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-29224?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-29224?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-29224?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-29224?actionOrder=desc "Ascending order - Click to sort in descending order")
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [24/Sep/19 02:16](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16936308&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16936308)
This is my implementation of FactorizationMachines:
<https://github.com/mob-ai/spark/tree/2.4/fm>
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [24/Sep/19 02:16](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16936308&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16936308) This is my implementation of FactorizationMachines: https://github.com/mob-ai/spark/tree/2.4/fm
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [24/Sep/19 02:23](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16936311&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16936311)
PR: <https://github.com/apache/spark/pull/25909>
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [24/Sep/19 02:23](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16936311&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16936311) PR: https://github.com/apache/spark/pull/25909
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [15/Oct/19 06:14](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16951639&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16951639)
The convergence curves of Binary Classification are ploted in attached(loss = GD, adamW):
[url_loss.xlsx![](https://issues.apache.org/jira/images/icons/link_attachment_7.gif)](https://issues.apache.org/jira/secure/attachment/12983046/12983046_url_loss.xlsx "url_loss.xlsx attached to SPARK-29224")
dataset: <http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/url_combined.bz2>
[![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34058) mob-ai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mob-ai) added a comment - [15/Oct/19 06:14](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=16951639&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16951639) The convergence curves of Binary Classification are ploted in attached(loss = GD, adamW): url_loss.xlsx dataset: http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/url_combined.bz2
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [23/Dec/19 16:12](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002365&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002365)
Issue resolved by pull request 26124
<https://github.com/apache/spark/pull/26124>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [23/Dec/19 16:12](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002365&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002365) Issue resolved by pull request 26124 https://github.com/apache/spark/pull/26124
[![Tagar](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10448) Ruslan Dautkhanov](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Tagar) added a comment - [23/Dec/19 17:48](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002398&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002398)
That's great.
Out of curiosity - what's largest number of features this was tested with?
[![Tagar](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10448) Ruslan Dautkhanov](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Tagar) added a comment - [23/Dec/19 17:48](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002398&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002398) That's great. Out of curiosity - what's largest number of features this was tested with?
[![Tagar](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10448) Ruslan Dautkhanov](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Tagar) added a comment - [23/Dec/19 17:51](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002402&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002402)
E.g. would this work with 0.1m or 1m sparse features?
[![Tagar](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10448) Ruslan Dautkhanov](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Tagar) added a comment - [23/Dec/19 17:51](https://issues.apache.org/jira/browse/SPARK-29224?focusedCommentId=17002402&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17002402) E.g. would this work with 0.1m or 1m sparse features?
#### People

Assignee:
     ![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=34058) mob-ai

Reporter:
     ![mob-ai](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=34058) mob-ai

Votes:
     0 Vote for this issue

Watchers:
     2 Start watching this issue
#### Dates

Created:
     24/Sep/19 02:13

Updated:
     15/Feb/26 20:05

Resolved:
     23/Dec/19 16:12
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)
