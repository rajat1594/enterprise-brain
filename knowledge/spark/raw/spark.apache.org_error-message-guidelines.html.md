[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/error-message-guidelines.html)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/error-message-guidelines.html)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/error-message-guidelines.html)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/error-message-guidelines.html)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/error-message-guidelines.html)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)


  * [ Apache Software Foundation ](https://spark.apache.org/error-message-guidelines.html)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)


# Error Message Guidelines
This guide is a reference for composing standardized and actionable error messages in Apache Spark.
### Include What, Why, and How
Exceptions thrown from Spark should answer the Five W’s and How:
  * **Who** encountered the problem?
  * **What** was the problem?
  * **When** did the problem happen?
  * **Where** did the problem happen?
  * **Why** did the problem happen?
  * **How** can the problem be solved?


The context provided by exceptions can help answer **who** (usually the user), **when** (usually included in the log via `log4j`), and **where** (usually included in the stack trace). However, these answers alone are often insufficient for the user to solve the problem. An error message that answers the remaining questions — **what** , **why** , and **how** — minimizes user frustration.
#### Explicitly answer What, Why and How
In many cases, the error message should explicitly answer **what** , **why** , and **how**.
##### Example 1
`        Unable to generate an encoder for inner class {} without access to the     scope that this class was defined in. Try moving this class out of its     parent class.   [](https://github.com/apache/spark/blob/569fb133d09e24e4ed56ed7efff641512d98b01b/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L160) `
  * **What:** Unable to generate encoder inner class.
  * **Why:** Did not have access to the scope that the class was defined in.
  * **How:** Try moving this class out of its parent class.


##### Example 2
If the proposed fix (**how**) feels arbitrary, providing an explanation for **why** the error occurred can reduce user frustration.
**Before**
`        [Unsupported function name {}.   ](https://github.com/apache/spark/blob/03dd33cc982ebb3de4354274ac49da31521b8195/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L498) `
  * **What:** Unsupported function name.
  * **Why:** Unclear.
  * **How:** Unclear.


**After**
_Function name {} is invalid. Temporary functions cannot belong to a catalog. Specify a function name with one or two parts._
  * **What:** Invalid function name.
  * **Why:** Temporary functions cannot belong to a catalog.
  * **How:** Specify a function name with one or two parts.


#### Implicitly answer How
Not all error messages should be this verbose. Sometimes, explicitly explaining **how** to resolve the problem would be redundant; you may skip an explicit explanation in this case.
##### Example 1
`        Invalid pivot column {}. Pivot columns must be comparable.   [](https://github.com/apache/spark/blob/e5d972e84e973d9a2e62312dc471df30c35269bc/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L63) `
  * **What:** Invalid pivot column.
  * **Why:** Pivot columns must be comparable.
  * **How (****_implied by Why_****):** Use comparable pivot columns.


##### Example 2
**Before**
`        Cannot specify window frame for {} function   [](https://github.com/apache/spark/blob/9809a2f1c5187205c81542dbdc84b71db535f6e1/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L325) `
  * **What:** Cannot specify window frame for the function.
  * **Why** : Unclear.
  * **How:** Unclear.


**After**
`   Cannot specify frame for window expression {}. Window expression   contains mismatch between function frame {} and specification frame {}. `
  * **What:** Cannot specify the frame for the window expression.
  * **Why:** Window expression contains mismatch between function frame and specification frame.
  * **How (****_implied by Why_****):** Match the function frame and specification frame.


##### Example 3
**Before**
`        Cannot parse any decimal.   [](https://github.com/apache/spark/blob/aff6c0febb40d9713895ba00d8c77ba00f04bd16/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryExecutionErrors.scala#L93) `
  * **What:** Cannot parse decimal.
  * **Why** : Unclear.
  * **How:** Unclear.


**After**
`   Invalid decimal {}; encountered error while parsing at position {}. `
  * **What:** Invalid decimal.
  * **Why** : The decimal parser encountered an error at the specified position.
  * **How (****_implied by Why_****):** Fix the error at the specified position.


#### Implicitly answer Why and How
Sometimes, even explicitly explaining **why** the problem happened would be redundant; you may skip an explicit explanation in this case.
`        Path does not exist: {}   [](https://github.com/apache/spark/blob/569fb133d09e24e4ed56ed7efff641512d98b01b/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L770) `
  * **What:** Path does not exist.
  * **Why (****_implied by What_****):** User specified an invalid path.
  * **How (****_implied by What_****):** Use a different path.


### Use clear language
#### Diction guide  
| Phrases  | When to use  | Example  |  
| --- | --- | --- |  
| Unsupported  |  The user may reasonably assume that the operation is supported, but it is not. This error may go away in the future if developers add support for the operation.   |  `           Data type {} is unsupported.         `  |  
|  Invalid / Not allowed / Unexpected   |  The user made a mistake when specifying an operation. The message should inform the user of how to resolve the error.   |  `           Array has size {}, index {} is invalid.         `  |  
|  `           Found {} generators for the clause {}. Only one generator is allowed.         `  |  
|  `           Found an unexpected state format version {}. Expected versions 1 or 2.         `  |  
| Failed to  |  The system encountered an unexpected error that cannot be reasonably attributed to user error.   |  `           Failed to compile {}.         `  |  
| Cannot  |  Any time, preferably only if one of the above alternatives does not apply.   |  `           Cannot generate code for unsupported type {}.         `  |  
#### Wording guide  
| Best practice  | Before  | After  |  
| --- | --- | --- |  
|  Use active voice   |  `                        DataType {} is [not supported by {}.           ](https://github.com/apache/spark/blob/73857cdd87757d2888bd92f6b7c2fad709701484/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L704)         `  |  `           {} does not support datatype {}.         `  |  
|  Avoid time-based statements, such as promises of future support   |  `                        Pandas UDF aggregate expressions are [currently not supported in pivot.           ](https://github.com/apache/spark/blob/27bec91bc971b393bd91f2ec8c6483b33f844f12/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L185)         `  |  `           Pivot does not support Pandas UDF aggregate expressions.         `  |  
|  `                        Parquet type not [yet supported: {}.           ](https://github.com/apache/spark/blob/569fb133d09e24e4ed56ed7efff641512d98b01b/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L1076)         `  |  `           {} does not support Parquet type.         `  |  
| Use the present tense to describe the error and provide suggestions  |  `                        [Couldn't find the reference column for {} at {}.           ](https://github.com/apache/spark/blob/9809a2f1c5187205c81542dbdc84b71db535f6e1/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L166)         `  |  `Cannot find the reference column for {} at {}.`  |  
|  `                        Join strategy hint parameter [should be an identifier or string but was {}.           ](https://github.com/apache/spark/blob/9809a2f1c5187205c81542dbdc84b71db535f6e1/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L409)         `  |  `           Cannot use join strategy hint parameter {}. Use a table name or identifier to specify the parameter.         `  |  
| Provide concrete examples if the resolution is unclear  |  `                        {} Hint expects a partition number as a parameter.           [](https://github.com/apache/spark/blob/569fb133d09e24e4ed56ed7efff641512d98b01b/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L422)         `  |  `           {} Hint expects a partition number as a parameter. For example, specify 3 partitions with {}(3).         `  |  
| Avoid sounding accusatory, judgmental, or insulting  |  `                        [You must specify an amount for {}.           ](https://github.com/apache/spark/blob/569fb133d09e24e4ed56ed7efff641512d98b01b/core/src/main/scala/org/apache/spark/resource/ResourceUtils.scala#L143)         `  |  `           {} cannot be empty. Specify an amount for {}.         `  |  
| Be direct  |  `                       LEGACY store assignment policy is disallowed in Spark data source V2. [Please set the configuration spark.sql.storeAssignmentPolicy to other values.           ](https://github.com/apache/spark/blob/4b5fc1da752ec008468ef80a5717c8beab468387/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L119)         `  |  `           Spark data source V2 does not allow the LEGACY store assignment policy. Set the configuration spark.sql.storeAssignment to ANSI or STRICT.         `  |  
| Do not use programming jargon in user-facing errors  |  `                        RENAME TABLE source and destination databases do not match: '{}' [!= '{}'.           ](https://github.com/apache/spark/blob/4b5fc1da752ec008468ef80a5717c8beab468387/sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala#L583)         `  |  `           RENAME TABLE source and destination databases do not match. The source database is {}, but the destination database is {}.         `  |  
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
