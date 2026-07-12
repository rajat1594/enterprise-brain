[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-4591)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-4591#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-4591#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-4591)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-4591)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591)


# Algorithm/model parity for spark.ml (Scala)
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-4591 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-4591)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-4591/SPARK-4591.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-4591/SPARK-4591.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-4591/SPARK-4591.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-4591/SPARK-4591.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) Umbrella 
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/critical.svg) Critical 
  * **Resolution:** Done 
  * ** Affects Version/s: ** None 
  * ** Fix Version/s:  ** None 
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None


#### Description
This is an umbrella JIRA for porting spark.mllib implementations to use the DataFrame-based API defined under spark.ml. We want to achieve critical feature parity for the next release.
###  Instructions for 3 subtask types
**Review tasks** : detailed review of a subpackage to identify feature gaps between spark.mllib and spark.ml.
  * Should be listed as a subtask of this umbrella.
  * Review subtasks cover major algorithm groups. To pick up a review subtask, please: 
    * Comment that you are working on it.
    * Compare the public APIs of spark.ml vs. spark.mllib.
    * Comment on all missing items within spark.ml: algorithms, models, methods, features, etc.
    * Check for existing JIRAs covering those items. If there is no existing JIRA, create one, and link it to your comment.


**Critical tasks** : higher priority missing features which are required for this umbrella JIRA.
  * Should be linked as "requires" links.


**Other tasks** : lower priority missing features which can be completed after the critical tasks.
  * Should be linked as "contains" links.


####  Excluded items
This does **not** include:
  * Python: We can compare Scala vs. Python in spark.ml itself.
  * Moving linalg to spark.ml: [~~SPARK-13944~~](https://issues.apache.org/jira/browse/SPARK-13944 "Separate out local linear algebra as a standalone module without Spark dependency")
  * Streaming ML: Requires stabilizing some internal APIs of structured streaming first


###  TODO list
**Critical issues**
  * [~~SPARK-14501~~](https://issues.apache.org/jira/browse/SPARK-14501 "spark.ml parity for fpm - frequent items"): Frequent Pattern Mining
  * [~~SPARK-14709~~](https://issues.apache.org/jira/browse/SPARK-14709 "spark.ml API for linear SVM"): linear SVM
  * [~~SPARK-15784~~](https://issues.apache.org/jira/browse/SPARK-15784 "Add Power Iteration Clustering to spark.ml"): Power Iteration Clustering (PIC)


**Lower priority issues**
  * Missing methods within algorithms (see Issue Links below)
  * evaluation submodule
  * stat submodule (should probably be covered in DataFrames)
  * Developer-facing submodules: 
    * optimization (including [~~SPARK-17136~~](https://issues.apache.org/jira/browse/SPARK-17136 "Design optimizer interface for ML algorithms"))
    * random, rdd
    * util


**To be prioritized**
  * single-instance prediction: [~~SPARK-10413~~](https://issues.apache.org/jira/browse/SPARK-10413 "ML models should support prediction on single instances")
  * pmml [~~SPARK-11171~~](https://issues.apache.org/jira/browse/SPARK-11171 "PMML for Pipelines API")


#### Attachments
#### Issue Links 

contains
    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-13025](https://issues.apache.org/jira/browse/SPARK-13025) Allow user to specify the initial model when training LogisticRegression
  * ![Minor - Minor loss of function, or other problem where easy workaround is present.](https://issues.apache.org/jira/images/icons/priorities/minor.svg)
  * Resolved

    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-14712](https://issues.apache.org/jira/browse/SPARK-14712) spark.ml LogisticRegressionModel.toString should summarize model
  * ![Trivial - Cosmetic problem like misspelt words or misaligned text.](https://issues.apache.org/jira/images/icons/priorities/trivial.svg)
  * Closed



depends upon
    
![Sub-task - The sub-task of the issue](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) [SPARK-3702](https://issues.apache.org/jira/browse/SPARK-3702) Standardize MLlib classes for learners, models
  * ![Critical - Crashes, loss of data, severe memory leak.](https://issues.apache.org/jira/images/icons/priorities/critical.svg)
  * Closed



requires
    
![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-14709](https://issues.apache.org/jira/browse/SPARK-14709) spark.ml API for linear SVM
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

    
![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-15784](https://issues.apache.org/jira/browse/SPARK-15784) Add Power Iteration Clustering to spark.ml
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

    
![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-14501](https://issues.apache.org/jira/browse/SPARK-14501) spark.ml parity for fpm - frequent items
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved


Show 1 more links (1 requires)
#### Sub-Tasks
  * Options
    * [Show All](https://issues.apache.org/jira/browse/SPARK-4591?subTaskView=all#issuetable "Show All")
    * [Show Open](https://issues.apache.org/jira/browse/SPARK-4591?subTaskView=unresolved#issuetable "Show Open")
    * [Bulk operation](https://issues.apache.org/jira/issue/bulkedit/BulkEdit1!default.jspa?reset=true&searchParent=SPARK-4591 "Bulk operation")
    * [Open issue navigator](https://issues.apache.org/jira/issues/?jql=parent%3DSPARK-4591 "Open issue navigator")

  
|  1.  | [spark.ml parity for trees](https://issues.apache.org/jira/browse/SPARK-14376)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14376)  |  Closed  |  [Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb)  |  
| --- | --- | --- | --- | --- |  
|  2.  | [Review spark.ml parity for classification, except trees](https://issues.apache.org/jira/browse/SPARK-14377)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14377)  |  Resolved  |  [Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb)  |  
|  3.  | [Review spark.ml parity for regression, except trees](https://issues.apache.org/jira/browse/SPARK-14378)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14378)  |  Resolved  |  [Yanbo Liang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang)  |  
|  4.  | [Review spark.ml parity for recommendation](https://issues.apache.org/jira/browse/SPARK-14379)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14379)  |  Closed  |  [Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick)  |  
|  5.  | [Review spark.ml parity for clustering](https://issues.apache.org/jira/browse/SPARK-14380)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14380)  |  Resolved  |  _Unassigned_  |  
|  6.  | [Review spark.ml parity for feature transformers](https://issues.apache.org/jira/browse/SPARK-14381)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14381)  |  Resolved  |  [Xusen Yin](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yinxusen)  |  
|  7.  | [Feature parity for ALS ML with MLLIB](https://issues.apache.org/jira/browse/SPARK-13857)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-13857)  |  Closed  |  [Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick)  |  
|  8.  | [Feature parity for Statistics ML with MLlib](https://issues.apache.org/jira/browse/SPARK-14523)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-14523)  |  Closed  |  _Unassigned_  |  
|  9.  | [Feature parity for descriptive statistics in MLlib](https://issues.apache.org/jira/browse/SPARK-19634)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-19634)  |  Closed  |  [Timothy Hunter](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=timhunter)  |  
|  10.  | [Feature parity for Chi-square hypothesis testing in MLlib](https://issues.apache.org/jira/browse/SPARK-19635)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-19635)  |  Closed  |  [Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb)  |  
|  11.  | [Feature parity for correlation statistics in MLlib](https://issues.apache.org/jira/browse/SPARK-19636)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-19636)  |  Closed  |  [Timothy Hunter](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=timhunter)  |  
|  12.  | [Python interface for ml.stats.Correlation](https://issues.apache.org/jira/browse/SPARK-20076)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-20076)  |  Closed  |  [L. C. Hsieh](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=viirya)  |  
|  13.  | [Documentation for ml.stats.Correlation](https://issues.apache.org/jira/browse/SPARK-20077)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-20077)  |  Resolved  |  _Unassigned_  |  
|  14.  | [Feature parity for KolmogorovSmirnovTest in MLlib](https://issues.apache.org/jira/browse/SPARK-21898)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-21898)  |  Closed  |  [Weichen Xu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=weichenxu123)  |  
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-4591?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-4591?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-4591?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-4591?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-4591?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-4591?actionOrder=desc "Ascending order - Click to sort in descending order")
[![zjffdu](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Jeff Zhang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=zjffdu) added a comment - [10/Dec/15 03:35](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15049974&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15049974)
Should this be closed ? Seems many algorithms have been ported, and no subtask is created here. 
[![zjffdu](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Jeff Zhang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=zjffdu) added a comment - [10/Dec/15 03:35](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15049974&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15049974) Should this be closed ? Seems many algorithms have been ported, and no subtask is created here. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [12/Dec/15 03:27](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15054001&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15054001)
Good point...maybe this can become an umbrella for collecting all remaining items. I'll target it at 2.0.0 for that purpose.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [12/Dec/15 03:27](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15054001&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15054001) Good point...maybe this can become an umbrella for collecting all remaining items. I'll target it at 2.0.0 for that purpose. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [04/Apr/16 21:51](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15225133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15225133)
Would others like to help review for parity? Thanks!
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [04/Apr/16 21:51](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15225133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15225133) Would others like to help review for parity? Thanks! 
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Apr/16 18:26](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15226849&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15226849)
Are we explicitly not porting FPM models to ML?
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Apr/16 18:26](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15226849&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15226849) Are we explicitly not porting FPM models to ML? 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [06/Apr/16 00:33](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15227445&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15227445)
We will; eventually, we should support everything. I just noted the highest priority items first.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [06/Apr/16 00:33](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15227445&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15227445) We will; eventually, we should support everything. I just noted the highest priority items first. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [08/Apr/16 22:52](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15233104&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15233104)
Note: I am leaving this task targeted at 2.0 to bring attention to it. However, we will not achieve full parity for 2.0.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [08/Apr/16 22:52](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15233104&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15233104) Note: I am leaving this task targeted at 2.0 to bring attention to it. However, we will not achieve full parity for 2.0. 
[![felixcheung](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Felix Cheung](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=felixcheung) added a comment - [13/Dec/16 07:51](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15744481&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15744481)
Is SVM part of this?
[![felixcheung](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Felix Cheung](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=felixcheung) added a comment - [13/Dec/16 07:51](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15744481&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15744481) Is SVM part of this? 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 21:39](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746350&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746350) - edited
Oh, I see I should reorg how subtasks are done. Editing now...
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 21:39](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746350&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746350) - edited Oh, I see I should reorg how subtasks are done. Editing now... 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 22:26](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746471&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746471)
I just updated this a bit. I did not finish linking all issues mentioned in Review subtasks yet.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 22:26](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746471&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746471) I just updated this a bit. I did not finish linking all issues mentioned in Review subtasks yet. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 22:27](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746473&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746473)
I also removed the target version since this includes non-2.2 subtasks.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [13/Dec/16 22:27](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15746473&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15746473) I also removed the target version since this includes non-2.2 subtasks. 
[![timhunter](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Timothy Hunter](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=timhunter) added a comment - [14/Feb/17 18:09](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15866288&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15866288)
[josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) do you also want some subtasks for KernelDensity and multivariate summaries? They are in the state module but not covered.
[![timhunter](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Timothy Hunter](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=timhunter) added a comment - [14/Feb/17 18:09](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15866288&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15866288) josephkb do you also want some subtasks for KernelDensity and multivariate summaries? They are in the state module but not covered. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [14/Mar/17 00:16](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15923294&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15923294)
For the record:
  * Kernel Density: later, I'd say
  * Multivariate: Now under [~~SPARK-19634~~](https://issues.apache.org/jira/browse/SPARK-19634 "Feature parity for descriptive statistics in MLlib")


[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [14/Mar/17 00:16](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=15923294&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15923294) For the record: Kernel Density: later, I'd say Multivariate: Now under SPARK-19634 
[![dongjin](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Dongjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=dongjin) added a comment - [14/Jun/18 08:32](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16512153&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16512153)
[josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) Excuse me. By [~~SPARK-14376~~](https://issues.apache.org/jira/browse/SPARK-14376 "spark.ml parity for trees") was resolved recently, I think we should make this issue be resolve also.
[![dongjin](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Dongjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=dongjin) added a comment - [14/Jun/18 08:32](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16512153&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16512153) josephkb Excuse me. By SPARK-14376 was resolved recently, I think we should make this issue be resolve also. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [22/Jun/18 18:04](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16520635&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16520635)
There are still a few contained tasks which are incomplete. I'd like to leave this open for now.
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [22/Jun/18 18:04](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16520635&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16520635) There are still a few contained tasks which are incomplete. I'd like to leave this open for now. 
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [10/Jul/19 17:23](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16882286&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16882286)
What else would go under this umbrella?
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [10/Jul/19 17:23](https://issues.apache.org/jira/browse/SPARK-4591?focusedCommentId=16882286&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16882286) What else would go under this umbrella? 
#### People 

Assignee: 
     ![Unassigned](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10453) Unassigned  

Reporter: 
     ![mengxr](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Xiangrui Meng  

Votes:
     4 Vote for this issue 

Watchers:
     18 Start watching this issue
#### Dates 

Created: 
     25/Nov/14 05:18 

Updated: 
     24/Aug/20 20:05 

Resolved: 
     24/Aug/20 20:05
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)
