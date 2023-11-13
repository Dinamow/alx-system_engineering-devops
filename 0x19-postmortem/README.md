# Outage Postmortem: Web Stack Debugging Project

## Issue Summary:

* **Duration:** 4 hours (Start: 2023-11-10 14:00 UTC, End: 2023-11-10 18:00 UTC)
* **Impact:** 75% of users experienced service downtime on our web application, resulting in a significant drop in user engagement and potential revenue loss.

## Root Cause:

* The root cause of the outage was identified as a misconfiguration in the load balancer settings, leading to an uneven distribution of traffic among backend servers. This caused an overload on certain servers, resulting in degraded performance and, ultimately, service unavailability for a large portion of our user base.

## Timeline:

* **14:00 UTC:** The issue detected through automated monitoring alerts indicating increased server response times.
* **14:10 UTC:** The engineering team initiated an investigation into the issue, suspecting a potential server overload.
* **14:30 UTC:** Initial assumption focused on database performance issues; however, subsequent analysis revealed normal database activity.
* **15:00 UTC:** Incident escalated to senior engineering team members for further investigation.
* **15:30 UTC:** Misleading path taken: An initial focus on code deployment as a potential cause resulted in unnecessary rollback of a recent release.
* **16:00 UTC:** Escalated to the DevOps team to examine infrastructure components; load balancer misconfiguration identified.
* **17:00 UTC:** Load balancer settings adjusted to evenly distribute traffic, resolving the issue.
* **18:00 UTC:** Service fully restored, and monitoring confirmed normal server response times.

## Root Cause and Resolution:

* **Root Cause:** Misconfiguration in the load balancer settings led to uneven distribution of traffic, causing server overload.
* **Resolution:** Load balancer settings were corrected to ensure equal distribution of incoming requests among backend servers, resolving the performance degradation.

## Corrective and Preventative Measures:

* **Improvements/Fixes:** 
	* Conduct a thorough review of load balancer configurations regularly to prevent similar misconfigurations.
	* Implement automated tests for load balancing configurations to catch issues before deployment.
	* Enhance monitoring alerts to provide more granular insights into server performance.
* **Tasks to Address the Issue:**
	* Create a checklist for load balancer configurations and ensure it is followed during any updates or deployments.
 	* Develop and implement automated tests for load balancing configurations in the continuous integration/continuous deployment (CI/CD) pipeline.
	* Establish a post-deployment monitoring process to quickly identify and address any anomalies in server performance.

