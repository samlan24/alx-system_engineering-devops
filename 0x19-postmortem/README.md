# Postmortem: Service Outage in London on 11.08.2024
## Issue Summary

On 11.08.2024, customers in London were unable to access services from our app for approximately 20 minutes, from 0900 hrs to 0920 hrs GMT. The outage affected 10k (100%) of users, causing disruptions in their ability to book consultation with real estate agents.

The root cause of the incident was a network issue. This caused a disruption in the service, leading to a temporary loss of access for customers in the affected location.

## Timeline: The Network Adventure No One Asked For
- **0900 hrs**: Issue detected through user reports.
- **0903 hrs**: The on-call engineer is notified and investigations begin.
- **0905 hrs**: Root cause identified as Internet Service Provider (ISP) causing incorrect routing of traffic.
- **0907 hrs**: Issue escalated to the network engineers who then contacted the ISP.
- **0915 hrs**: The ISP calls back assuring the incorrect routing has been fixed.
- **0920 hrs**: The networking and development team ascertain the app is working correctly.

## Root Cause and Resolution
- **Root cause**: The root cause was an ISP routing issue which caused incorrect routing of traffic. This prevented users in London from accessing our app.
- **Resolution**: The resolution involved coordinating with our Internet Service Provider (ISP) after identifying the routing issue through network diagnostics. The ISP's network operations team corrected their routing tables to ensure that traffic from the affected location was properly directed to our servers. Once the routing paths were adjusted, normal service was restored, and users were able to access the app without further issues. We confirmed the fix through additional network tests and monitoring.

## Corrective and Preventive Measures 
To prevent future routing issues, the following can be done:
- Set up multiple ISPs or network paths to ensure that traffic can be rerouted in case of an issue with one provider.
- Implement more comprehensive network monitoring tools to detect routing issues earlier.
- Establish clear communication channels with our ISP and ensure that escalation procedures are in place for faster resolution of network issues.
- Ensure that your ISP's SLAs meet our reliability and response time requirements.
To address the issue, the following steps will be taken:
- Set up secondary ISP connection
- Implement multi-homing 
- Deploy network monitoring tools
- Set up proactive alerts
- Add ISP-specific monitoring 

## Additional Notes 
While the outage was brief, it impacted a significant number of users in London. By analyzing the incident and implementing preventive measures, we aim to reduce the likelihood of similar disruptions in the future and improve our overall service reliability.
