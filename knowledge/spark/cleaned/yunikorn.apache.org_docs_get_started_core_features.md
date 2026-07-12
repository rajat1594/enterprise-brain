[Skip to main content](https://yunikorn.apache.org/docs/get_started/core_features/#__docusaurus_skipToContent_fallback)
1.8.0 has been released, check the [DOWNLOADS](https://yunikorn.apache.org/community/download).
[ ![YuniKorn Site Logo](https://yunikorn.apache.org/img/logo/yunikorn_blue_logo.png)![YuniKorn Site Logo](https://yunikorn.apache.org/img/logo/yunikorn_white_logo.png) **Apache YuniKorn**](https://yunikorn.apache.org/)[Docs](https://yunikorn.apache.org/docs/)[Roadmap](https://yunikorn.apache.org/community/roadmap)[Download](https://yunikorn.apache.org/community/download)
[Community](https://yunikorn.apache.org/docs/get_started/core_features/)
  * [Get Involved](https://yunikorn.apache.org/community/get_involved)
  * [How to Contribute](https://yunikorn.apache.org/community/how_to_contribute)
  * [Coding Guidelines](https://yunikorn.apache.org/community/coding_guidelines)
  * [Reporting Issues](https://yunikorn.apache.org/community/reporting_issues)
  * [Release Procedure](https://yunikorn.apache.org/community/release_procedure)
  * [Events](https://yunikorn.apache.org/community/events)
  * [People](https://yunikorn.apache.org/community/people)

[Apache](https://yunikorn.apache.org/docs/get_started/core_features/)
  * [Apache Software Foundation](https://www.apache.org/)
  * [Events](https://www.apache.org/events/current-event)
  * [License](https://www.apache.org/licenses/)
  * [Sponsors](https://www.apache.org/foundation/thanks.html)
  * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
  * [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
  * [Security](https://www.apache.org/security/)

[1.8.0](https://yunikorn.apache.org/docs/get_started/core_features)
  * [Next](https://yunikorn.apache.org/docs/next/get_started/core_features)
  * [1.8.0](https://yunikorn.apache.org/docs/get_started/core_features)
  * [1.7.0](https://yunikorn.apache.org/docs/1.7.0/get_started/core_features)
  * [1.6.3](https://yunikorn.apache.org/docs/1.6.3/get_started/core_features)
  * [1.5.2](https://yunikorn.apache.org/docs/1.5.2/get_started/core_features)
  * [1.4.0](https://yunikorn.apache.org/docs/1.4.0/get_started/core_features)
  * [1.3.0](https://yunikorn.apache.org/docs/1.3.0/get_started/core_features)
  * [1.2.0](https://yunikorn.apache.org/docs/1.2.0/get_started/core_features)
  * [1.1.0](https://yunikorn.apache.org/docs/1.1.0/get_started/core_features)
  * [1.0.0](https://yunikorn.apache.org/docs/1.0.0/get_started/core_features)

[](https://github.com/apache/yunikorn-core)
  * [Get Started](https://yunikorn.apache.org/docs/)
    * [Get Started](https://yunikorn.apache.org/docs/)
    * [Features](https://yunikorn.apache.org/docs/get_started/core_features)
    * [Version details](https://yunikorn.apache.org/docs/get_started/version)
  * [User Guide](https://yunikorn.apache.org/docs/user_guide/deployment_modes)
  * [Developer Guide](https://yunikorn.apache.org/docs/developer_guide/env_setup)
  * [Performance](https://yunikorn.apache.org/docs/performance/evaluate_perf_function_with_kubemark)

  * [](https://yunikorn.apache.org/)
  * Get Started
  * Features

Version: 1.8.0
On this page
# Features
The main features of YuniKorn include:
## App-aware scheduling[​](https://yunikorn.apache.org/docs/get_started/core_features/#app-aware-scheduling "Direct link to App-aware scheduling")
One of the key differences of YuniKorn is that it does app-aware scheduling. The default K8s scheduler simply schedules pod by pod without any context about user, app, or queue. However, YuniKorn recognizes users, apps, and queues, and it considers a lot more factors, e.g resource, ordering etc, while making scheduling decisions. This gives us the possibility to use fine-grained controls on resource quotas, resource fairness, and priorities, which are the most important requirements for a multi-tenancy computing system.
## Hierarchy Resource Queues[​](https://yunikorn.apache.org/docs/get_started/core_features/#hierarchy-resource-queues "Direct link to Hierarchy Resource Queues")
Hierarchy queues provide an efficient mechanism to manage cluster resources. The hierarchy of the queues can logically map to the structure of an organization. This gives fine-grained control over resources for different tenants. The YuniKorn UI provides a centralised view to monitor the usage of resource queues and helps you to gain insight into how the resources are used across different tenants. What's more, by leveraging the min/max queue capacity, it can define how elastic it can be in terms of the resource consumption for each tenant.
## Gang Scheduling[​](https://yunikorn.apache.org/docs/get_started/core_features/#gang-scheduling "Direct link to Gang Scheduling")
An application can request a set of resources, i.e. a gang, to be scheduled all at once. The gang defines all the resources the application requires to start. During the first scheduling phase all resources requested will be reserved. The application will only be started when all requested resources are available.
Reservation duration and application behaviour when the reservation fails are configurable. It is even possible to create multiple gangs of different specifications for one application. See the [gang design](https://yunikorn.apache.org/docs/design/gang_scheduling) and the Gang Scheduling [user guide](https://yunikorn.apache.org/docs/user_guide/gang_scheduling) for more details.
## Job Ordering and Queuing[​](https://yunikorn.apache.org/docs/get_started/core_features/#job-ordering-and-queuing "Direct link to Job Ordering and Queuing")
Applications can be properly queued in working-queues, the ordering policy determining which application can get resources first. There are various policies such as simple `FIFO`, `Fair`, `StateAware`, or `Priority` based. Queues can maintain the order of applications, and based on different policies, the scheduler allocates resources to jobs accordingly. The behavior is much more predictable.
What's more, when the queue max-capacity is configured, jobs and tasks can be properly queued up in the resource queue. If the remaining capacity is not enough, they can be waiting in line until some resources are released. This simplifies the client side operation. Unlike the default scheduler, resources are capped by namespace resource quotas which are enforced by the quota-admission-controller. If the underlying namespace does not have enough quota, pods cannot be created. Client side needs complex logic, e.g retry by condition, to handle such scenarios.
## Resource fairness[​](https://yunikorn.apache.org/docs/get_started/core_features/#resource-fairness "Direct link to Resource fairness")
In a multi-tenant environment, a lot of users share cluster resources. To prevent tenants from competing for resources and potentially getting starved, more fine-grained fairness controls are needed to achieve fairness across users, as well as across teams/organizations. With consideration of weights or priorities, more important applications can demand resources beyond their share. This feature is often considered in relation to resource budgets, where a more fine-grained fairness mode can further improve spending efficiency.
## Resource Reservation[​](https://yunikorn.apache.org/docs/get_started/core_features/#resource-reservation "Direct link to Resource Reservation")
YuniKorn automatically does reservations for outstanding requests. If a pod could not be allocated, YuniKorn will try to reserve it on a qualified node and tentatively allocate the pod on this reserved node (before trying rest of nodes). This mechanism can prevent the pod from being starved by future smaller, less-picky pods. This feature is important in the batch workloads scenario because when a large amount of heterogeneous pods are submitted to the cluster, it's very likely some pods can be starved even when they are submitted much earlier.
## Preemption[​](https://yunikorn.apache.org/docs/get_started/core_features/#preemption "Direct link to Preemption")
YuniKorn's preemption feature allows higher-priority tasks to dynamically reallocate resources by preempting lower-priority ones, ensuring critical workloads get necessary resources in a multi-tenant Kubernetes environment. This proactive mechanism maintains system stability and fairness, integrating with Kubernetes' priority classes and YuniKorn's hierarchical queue system.
## Throughput[​](https://yunikorn.apache.org/docs/get_started/core_features/#throughput "Direct link to Throughput")
Throughput is a key criterion for measuring scheduler performance. It is critical for a large scale distributed system. If throughput is bad, applications may waste time on waiting for scheduling and further impact service SLAs. When the cluster gets bigger, it also means there is a requirement for higher throughput. The [performance evaluation based on Kube-mark](https://yunikorn.apache.org/docs/performance/evaluate_perf_function_with_kubemark) reveals some perf numbers.
## MaxApplication Enforcement[​](https://yunikorn.apache.org/docs/get_started/core_features/#maxapplication-enforcement "Direct link to MaxApplication Enforcement")
The MaxApplication enforcement feature allows users to limit the number of running applications for a configured queue. This feature is critical in large scale batch workloads. Without this feature, when a large number of concurrent jobs are launched, they would compete for resources, and a certain amount of resources would be wasted, which could lead to job failure. The [Partition and Queue Configuration](https://yunikorn.apache.org/docs/user_guide/queue_config) provides configuration examples.
## CPU Architecture support[​](https://yunikorn.apache.org/docs/get_started/core_features/#cpu-architecture-support "Direct link to CPU Architecture support")
YuniKorn supports running on ARM as well as on AMD/Intel CPUs. With the release of YuniKorn 1.1.0, prebuilt convenience images for both architectures are provided in docker hub.
## Event system and application history tracking[​](https://yunikorn.apache.org/docs/get_started/core_features/#event-system-and-application-history-tracking "Direct link to Event system and application history tracking")
Whenever something relevant happens inside the scheduler (eg. request is added, allocation happens in a queue, node removal, queue or user quota is exceeded, etc) an appropriate event is generated. This enables users to reliably generate usage statistics about their workloads over time. Since the event structure is well-defined, this is much more suitable for automated processing than logs. Application history (state transitions & allocations), node, queue, user and group resource usage can be examined without having to look at the logs. The events accessible on the REST interface in two ways: batch or streaming. A [batch query](https://yunikorn.apache.org/docs/api/scheduler#batch-events) simply returns the list of events, while the [streaming](https://yunikorn.apache.org/docs/api/scheduler#event-stream) endpoint keeps the connection open and new events are immediately sent to the client.
[Previous Get Started](https://yunikorn.apache.org/docs/)[Next Version details](https://yunikorn.apache.org/docs/get_started/version)
  * [App-aware scheduling](https://yunikorn.apache.org/docs/get_started/core_features/#app-aware-scheduling)
  * [Hierarchy Resource Queues](https://yunikorn.apache.org/docs/get_started/core_features/#hierarchy-resource-queues)
  * [Gang Scheduling](https://yunikorn.apache.org/docs/get_started/core_features/#gang-scheduling)
  * [Job Ordering and Queuing](https://yunikorn.apache.org/docs/get_started/core_features/#job-ordering-and-queuing)
  * [Resource fairness](https://yunikorn.apache.org/docs/get_started/core_features/#resource-fairness)
  * [Resource Reservation](https://yunikorn.apache.org/docs/get_started/core_features/#resource-reservation)
  * [Preemption](https://yunikorn.apache.org/docs/get_started/core_features/#preemption)
  * [Throughput](https://yunikorn.apache.org/docs/get_started/core_features/#throughput)
  * [MaxApplication Enforcement](https://yunikorn.apache.org/docs/get_started/core_features/#maxapplication-enforcement)
  * [CPU Architecture support](https://yunikorn.apache.org/docs/get_started/core_features/#cpu-architecture-support)
  * [Event system and application history tracking](https://yunikorn.apache.org/docs/get_started/core_features/#event-system-and-application-history-tracking)

Blog
  * [What's YuniKorn?](https://blog.cloudera.com/yunikorn-a-universal-resources-scheduler/)
  * [Spark on Kubernetes – Gang Scheduling with YuniKorn](https://blog.cloudera.com/spark-on-kubernetes-gang-scheduling-with-yunikorn/)

Code Repositories
  * [Core scheduler](https://github.com/apache/yunikorn-core/)
  * [Kubernetes shim](https://github.com/apache/yunikorn-k8shim)
  * [Scheduler Interface](https://github.com/apache/yunikorn-scheduler-interface)
  * [WEB application](https://github.com/apache/yunikorn-web)
  * [Website](https://github.com/apache/yunikorn-site)

Community
  * [Get Involved](https://yunikorn.apache.org/community/get_involved)
  * [People](https://yunikorn.apache.org/community/people)
  * [Issues](https://issues.apache.org/jira/projects/YUNIKORN/issues)

Copyright © 2020-2026 [The Apache Software Foundation](https://www.apache.org/). Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

The Apache Software Foundation Apache YuniKorn, YuniKorn, Apache, the Apache feather, and the Apache YuniKorn project logo are either registered trademarks or trademarks of the Apache Software Foundation.
