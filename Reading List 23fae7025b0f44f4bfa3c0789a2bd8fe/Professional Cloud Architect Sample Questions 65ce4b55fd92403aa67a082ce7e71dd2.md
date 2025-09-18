# Professional Cloud Architect Sample Questions

Column: https://docs.google.com/forms/d/e/1FAIpQLSdvf8Xq6m0kvyIoysdr8WZYCG32WHENStftiHTSdtW4ad2-0w/viewscore?viewscore=AE0zAgBvG5WDE17-xgjc-P4zw3Q_VyjMD3vnn2vrBjY2chcSZkI6WWSvaBfIuJLCBiGB1YI
Processed: No
created on: May 9, 2023 7:21 PM

[WAHZGrnKPgyH26MQSUxMzPMiQoqsLLE3Ljf1qfW2j6yYYlFBVBI1aLXXI_7RiIuVhckW1u4vgVoX=w1200-h630-p](Professional%20Cloud%20Architect%20Sample%20Questions%2065ce4b55fd92403aa67a082ce7e71dd2/WAHZGrnKPgyH26MQSUxMzPMiQoqsLLE3Ljf1qfW2j6yYYlFBVBI1aLXXI_7RiIuVhckW1u4vgVoXw1200-h630-p)

The Cloud Architect sample questions will familiarize you with the format of exam questions and example content that may be covered on the exam.

The sample questions do not represent the range of topics or level of difficulty of questions presented on the exam. Performance on the sample questions should not be used to predict your Cloud Architect exam result.

Do you have a candidate ID?

If you completed a Google Cloud certification exam, you received a notification email with your candidate ID.

Registration

Last Name *

K

Primary Email *

rnnnhv@gmail.com

Recovery Email

Organization (Employer or School) *

Ms

Organization email (an email associated with your current organization)

Country  *

Choose

Afghanistan

Albania

American Samoa

Algeria

Andorra

Angola

Antigua and Barbuda

Argentina

Armenia

Aruba

Australia

Austria

Azerbaijan

Bahamas, The

Bahrain

Bangladesh

Barbados

Belarus

Belgium

Belize

Benin

Bermuda

Bhutan

Bolivia

Bosnia and Herzegovina

Botswana

Bouvet Island

Brazil

British Indian Ocean Territory

British Virgin Islands

Brunei

Bulgaria

Burkina Faso

Burundi

Cambodia

Cameroon

Canada

Cape Verde

Cayman Islands

Central African Republic

Chad

Chile

China

Christmas Island

Cocos [Keeling] Islands

Colombia

Comoros

Congo, Democratic Republic of the

Congo, Republic of the

Cook Islands

Costa Rica

Cote d'Ivoire

Croatia

Cuba

Curacao

Cyprus

Czech Republic

Denmark

Djibouti

Dominica

Dominican Republic

East Timor (see Timor-Leste)

Ecuador

Egypt

El Salvador

Equatorial Guinea

Eritrea

Estonia

Ethiopia

Falkland Islands [Islas Malvinas]

Faroe Islands

Fiji

Finland

France

French Guiana

French Polynesia

French Southern Territories

Gabon

Gambia, The

Georgia

Germany

Ghana

Gibraltar

Greece

Greenland

Grenada

Guadeloupe

Guam

Guatemala

Guinea

Guinea-Bissau

Guyana

Haiti

Heard Island and McDonald Islands

Honduras

Hong Kong

Hungary

Iceland

India

Indonesia

Iran

Iraq

Ireland

Israel

Italy

Jamaica

Japan

Jordan

Kazakhstan

Kenya

Kiribati

Korea, South

Kuwait

Kyrgyzstan

Laos

Latvia

Lebanon

Lesotho

Liberia

Libya

Liechtenstein

Lithuania

Luxembourg

Macau

Macedonia

Madagascar

Malawi

Malaysia

Maldives

Mali

Malta

Marshall Islands

Mauritania

Mauritius

Mexico

Micronesia

Moldova

Monaco

Mongolia

Montenegro

Morocco

Mozambique

Namibia

Nauru

Nepal

Netherlands

New Zealand

Nicaragua

Niger

Nigeria

North Korea

Norway

Oman

Pakistan

Palau

Palestinian Territories

Panama

Papua New Guinea

Paraguay

Peru

Philippines

Poland

Portugal

Qatar

Romania

Russia

Rwanda

Saint Kitts and Nevis

Saint Lucia

Saint Vincent and the Grenadines

Samoa

San Marino

Sao Tome and Principe

Saudi Arabia

Senegal

Serbia

Seychelles

Sierra Leone

Singapore

Sint Maarten

Slovakia

Slovenia

Solomon Islands

Somalia

South Africa

South Korea

South Sudan

Spain

Sri Lanka

Sudan

Suriname

Swaziland

Sweden

Switzerland

Syria

Taiwan

Tajikistan

Tanzania

Thailand

Timor-Leste

Togo

Tonga

Trinidad and Tobago

Tunisia

Turkey

Turkmenistan

Tuvalu

Uganda

Ukraine

United Arab Emirates

United Kingdom

United States

Uruguay

Uzbekistan

Vanuatu

Venezuela

Vietnam

Yemen

Zambia

Zimbabwe

Primary Relationship to Google *

Choose

Customer

Partner

EDU Partner

Prospect

Employee

Other - End-user

Other - Student

Other - School Administrator

Other

Send me offers, updates and useful tips for getting the most out of Google Cloud training and certification products and services. *

For this question, refer to the TerramEarth case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2)

Because you do not know every possible future use for the data TerramEarth collects, you have decided to build a system that captures and stores all raw data in case you need it later. How can you most cost-effectively accomplish this goal?

A. Have the vehicles in the field stream the data directly into BigQuery.

B. Have the vehicles in the field pass the data to Cloud Pub/Sub and dump it into a Cloud Dataproc cluster that stores data in Apache Hadoop Distributed File System (HDFS) on persistent disks.

C. Have the vehicles in the field continue to dump data via FTP, adjust the existing Linux machines, and use a collector to upload them into Cloud Dataproc HDFS for storage.

D. Have the vehicles in the field continue to dump data via FTP, and adjust the existing Linux machines to immediately upload it to Cloud Storage with gsutil.

Correct answer

D. Have the vehicles in the field continue to dump data via FTP, and adjust the existing Linux machines to immediately upload it to Cloud Storage with gsutil.

Feedback

A is not correct because TerramEarth has cellular service for 200,000 vehicles, and each vehicle sends at least one row (120 fields) per second. This exceeds BigQuery's maximum rows per second per project quota. Additionally, there are 20 million total vehicles, most of which perform uploads when connected by a maintenance port, which drastically exceeds the streaming project quota further.

B is not correct because although Cloud Pub/Sub is a fine choice for this application, Cloud Dataproc is probably not. The question posed asks us to optimize for cost. Because Cloud Dataproc is optimized for ephemeral, job-scoped clusters, a long-running cluster with large amounts of HDFS storage could be very expensive to build and maintain when compared to managed and specialized storage solutions like Cloud Storage.

C is not correct because the question asks us to optimize for cost, and because Cloud Dataproc is optimized for ephemeral, job-scoped clusters, a long-running cluster with large amounts of HDFS storage could be very expensive to build and maintain when compared to managed and specialized storage solutions like Cloud Storage.

D is correct because several load-balanced Compute Engine VMs would suffice to ingest 9 TB per day, and Cloud Storage is the cheapest per-byte storage offered by Google. Depending on the format, the data could be available via BigQuery immediately, or shortly after running through an ETL job. Thus, this solution meets business and technical requirements while optimizing for cost.

[https://cloud.google.com/blog/products/data-analytics/10-tips-for-building-long-running-clusters-using-cloud-dataproc](https://cloud.google.com/blog/products/data-analytics/10-tips-for-building-long-running-clusters-using-cloud-dataproc)

[https://cloud.google.com/blog/products/data-analytics/10-tips-for-building-long-running-clusters-using-cloud-dataproc](https://cloud.google.com/blog/products/data-analytics/10-tips-for-building-long-running-clusters-using-cloud-dataproc)

[https://cloud.google.com/bigquery/quotas#streaming_inserts](https://cloud.google.com/bigquery/quotas#streaming_inserts)

For this question, refer to the TerramEarth case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2)

Today, TerramEarth maintenance workers receive interactive performance graphs for the last 24 hours (86,400 events) by plugging their maintenance tablets into the vehicle. The support group wants support technicians to view this data remotely to help troubleshoot problems. You want to minimize the latency of graph loads. How should you provide this functionality?

D. Execute queries against BigQuery with data stored in Cloud Storage via BigQuery federation.

Correct answer

Feedback

A is not correct because Cloud SQL provides relational database services that are well suited to OLTP workloads, but not storage and low-latency retrieval of time-series data.

B is correct because Cloud Bigtable is optimized for time-series data. It is cost-efficient, highly available, and low-latency. It scales well. Best of all, it is a managed service that does not require significant operations work to keep running.

C is not correct because BigQuery is fast for wide-range queries, but it is not as well optimized for narrow-range queries as Cloud Bigtable is. Latency will be an order of magnitude shorter with Cloud Bigtable for this use.

D is not correct because the objective is to minimize latency, and although BigQuery federation offers tremendous flexibility, it doesn't perform as well as native BigQuery storage, and will have longer latency than Cloud Bigtable for narrow-range queries.

[https://cloud.google.com/bigquery/external-data-sources](https://cloud.google.com/bigquery/external-data-sources)

[https://cloud.google.com/bigtable/docs/schema-design-time-series#time-series-cloud-bigtable](https://cloud.google.com/bigtable/docs/schema-design-time-series#time-series-cloud-bigtable)

For this question, refer to the TerramEarth case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2)

Your agricultural division is experimenting with fully autonomous vehicles. You want your architecture to promote strong security during vehicle operation. Which two architecture characteristics should you consider? (choose two)

C. Enclose the vehicle’s drive electronics in a Faraday cage to isolate chips.

D. Use a functional programming language to isolate code execution cycles.

Correct answer

E. Treat every microservice call between modules on the vehicle as untrusted.

F. Use a Trusted Platform Module (TPM) and verify firmware and binaries on boot.

Feedback

A is not correct because this improves system durability, but it doesn't have any impact on the security during vehicle operation.

B is not correct because IPv6 doesn't have any impact on the security during vehicle operation, although it improves system scalability and simplicity.

C is not correct because it doesn't have any impact on the security during vehicle operation, although it improves system durability.

D is not correct because merely using a functional programming language doesn't guarantee a more secure level of execution isolation. Any impact on security from this decision would be incidental at best.

E is correct because this improves system security by making it more resistant to hacking, especially through man-in-the-middle attacks between modules.

F is correct because this improves system security by making it more resistant to hacking, especially rootkits or other kinds of corruption by malicious actors.

[https://en.wikipedia.org/wiki/Trusted_Platform_Module](https://en.wikipedia.org/wiki/Trusted_Platform_Module)

For this question, refer to the TerramEarth case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2)

Which of TerramEarth’s legacy enterprise processes will experience significant change as a result of increased Google Cloud Platform adoption?

A. OpEx/CapEx allocation, LAN change management, capacity planning

C. Capacity planning, utilization measurement, data center expansion

D. Data center expansion,TCO calculations, utilization measurement

Feedback

A is not correct because LAN change management processes don't need to change significantly. TerramEarth can easily peer their on-premises LAN with their Google Cloud Platform VPCs, and as devices and subnets move to the cloud, the LAN team's implementation will change, but the change management process doesn't have to.

B is correct because all of these tasks are big changes when moving to the cloud. Capacity planning for cloud is different than for on-premises data centers; TCO calculations are adjusted because TerramEarth is using services, not leasing/buying servers; OpEx/CapEx allocation is adjusted as services are consumed vs. using capital expenditures.

C is not correct because measuring utilization can be done in the same way, often with the same tools (along with some new ones). Data center expansion is not a concern for cloud customers; it is part of the undifferentiated heavy lifting that is taken care of by the cloud provider.

D is not correct because data center expansion is not a concern for cloud customers; it is part of the undifferentiated heavy lifting that is taken care of by the cloud provider. Measuring utilization can be done in the same way, often with the same tools (along with some new ones).

[https://assets.kpmg/content/dam/kpmg/pdf/2015/11/cloud-economics.pdf](https://assets.kpmg/content/dam/kpmg/pdf/2015/11/cloud-economics.pdf)

For this question, refer to the TerramEarth case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-terramearth-rev2)

You analyzed TerramEarth’s business requirement to reduce downtime and found that they can achieve a majority of time saving by reducing customers’ wait time for parts. You decided to focus on reduction of the 3 weeks’ aggregate reporting time. Which modifications to the company’s processes should you recommend?

A. Migrate from CSV to binary format, migrate from FTP to SFTP transport, and develop machine learning analysis of metrics.

B. Migrate from FTP to streaming transport, migrate from CSV to binary format, and develop machine learning analysis of metrics.

C. Increase fleet cellular connectivity to 80%, migrate from FTP to streaming transport, and develop machine learning analysis of metrics.

D. Migrate from FTP to SFTP transport, develop machine learning analysis of metrics, and increase dealer local inventory by a fixed factor.

Correct answer

C. Increase fleet cellular connectivity to 80%, migrate from FTP to streaming transport, and develop machine learning analysis of metrics.

Feedback

A is not correct because machine learning analysis is a good means toward the end of reducing downtime, but shuffling formats and transport doesn't directly help at all.

B is not correct because machine learning analysis is a good means toward the end of reducing downtime, and moving to streaming can improve the freshness of the information in that analysis, but changing the format doesn't directly help at all.

C is correct because using cellular connectivity will greatly improve the freshness of data used for analysis from where it is now, collected when the machines are in for maintenance. Streaming transport instead of periodic FTP will tighten the feedback loop even more. Machine learning is ideal for predictive maintenance workloads.

D is not correct because machine learning analysis is a good means toward the end of reducing downtime, but the rest of these changes don't directly help at all.

Your company wants to deploy several microservices to help their system handle elastic loads. Each microservice uses a different version of software libraries. You want to enable their developers to keep their development environment in sync with the various production services. Which technology should you choose?

C. Chef/Puppet

Feedback

A is not correct because although OS packages are a convenient way to distribute and deploy libraries, they don't directly help with synchronizing. Even with a common repository, the development environments will probably deviate from production.

B is correct because using containers for development, test, and production deployments abstracts away system OS environments, so that a single host OS image can be used for all environments. Changes that are made during development are captured using a copy on-write filesystem, and teams can easily publish new versions of the microservices in a repository.

C is not correct because although infrastructure configuration as code can help unify production and test environments, it is very difficult to make all changes during development this way.

D is not correct because virtual machines run their own OS, which will eventually deviate in each environment, just as now.

Your company wants to track whether someone is present in a meeting room reserved for a scheduled meeting. There are 1000 meeting rooms across 5 offices on 3 continents. Each room is equipped with a motion sensor that reports its status every second. You want to support the data ingestion needs of this sensor network. The receiving infrastructure needs to account for the possibility that the devices may have inconsistent connectivity. Which solution should you design?

A. Have each device create a persistent connection to a Compute Engine instance and write messages to a custom application.

B. Have devices poll for connectivity to Cloud SQL and insert the latest messages on a regular interval to a device specific table.

C. Have devices poll for connectivity to Cloud Pub/Sub and publish the latest messages on a regular interval to a shared topic for all devices.

D. Have devices create a persistent connection to an App Engine application fronted by Cloud Endpoints, which ingest messages and write them to Cloud Datastore.

Feedback

A is not correct because having a persistent connection does not handle the case where the device is disconnected.

B is not correct because Cloud SQL is a regional, relational database and not the best fit for sensor data. Additionally, the frequency of the writes has the potential to exceed the supported number of concurrent connections.

C is correct because Cloud Pub/Sub can handle the frequency of this data, and consumers of the data can pull from the shared topic for further processing.

D is not correct because having a persistent connection does not handle the case where the device is disconnected.

[https://cloud.google.com/sql/](https://cloud.google.com/sql/)

[https://cloud.google.com/pubsub/](https://cloud.google.com/pubsub/)

Your company wants to try out the cloud with low risk. They want to archive approximately 100 TB of their log data to the cloud and test the serverless analytics features available to them there, while also retaining that data as a long-term disaster recovery backup. Which two steps should they take? (choose two)

Correct answer

Feedback

A is correct because BigQuery is a serverless warehouse for analytics and supports the volume and analytics requirement.

B is not correct because Cloud SQL does not support the expected 100 TB. Additionally, Cloud SQL is a relational database and not the best fit for time-series log data formats.

C is not correct because Cloud Logging is optimized for monitoring, error reporting, and debugging instead of analytics queries.

D is not correct because Cloud Bigtable is optimized for read-write latency and analytics throughput, not analytics querying and reporting.

E is correct because Cloud Storage provides the Coldline and Archive storage classes to support long-term storage with infrequent access, which would support the long-term disaster recovery backup requirement.

[https://cloud.google.com/storage/docs/storage-classes#coldline](https://cloud.google.com/storage/docs/storage-classes#coldline)

[https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

[https://cloud.google.com/products/operations](https://cloud.google.com/products/operations)

[https://cloud.google.com/sql/](https://cloud.google.com/sql/)

[https://cloud.google.com/bigquery/](https://cloud.google.com/bigquery/)

You set up an autoscaling managed instance group to serve web traffic for an upcoming launch. After configuring the instance group as a backend service to an HTTP(S) load balancer, you notice that virtual machine (VM) instances are being terminated and re-launched every minute. The instances do not have a public IP address. You have verified that the appropriate web response is coming from each instance using the curl command. You want to ensure that the backend is configured correctly. What should you do?

A. Ensure that a firewall rule exists to allow source traffic on HTTP/HTTPS to reach the load balancer.

B. Assign a public IP to each instance, and configure a firewall rule to allow the load balancer to reach the instance public IP.

C. Ensure that a firewall rule exists to allow load balancer health checks to reach the instances in the instance group.

D. Create a tag on each instance with the name of the load balancer. Configure a firewall rule with the name of the load balancer as the source and the instance tag as the destination.

Feedback

A is not correct because the issue to resolve is the VMs being terminated, not access to the load balancer.

B is not correct because this introduces a security vulnerability without addressing the primary concern of the VM termination.

C is correct because health check failures lead to a VM being marked unhealthy and can result in termination if the health check continues to fail. Because you have already verified that the instances are functioning properly, the next step would be to determine why the health check is continuously failing.

D is not correct because the source of the firewall rule that allows load balancer and health check access to instances is defined IP ranges, and not a named load balancer. Tagging the instances for the purpose of firewall rules is appropriate but would probably be a descriptor of the application, and not the load balancer.

[https://cloud.google.com/load-balancing/docs/https/](https://cloud.google.com/load-balancing/docs/https/)

[https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

Your organization has a 3-tier web application deployed in the same Google Cloud Virtual Private Cloud (VPC). Each tier (web, API, and database) scales independently of the others. Network traffic should flow through the web to the API tier, and then on to the database tier. Traffic should not flow between the web and the database tier. How should you configure the network with minimal steps?

B. Set up software-based firewalls on individual VMs.

C. Add tags to each tier and set up routes to allow the desired traffic flow.

D. Add tags to each tier and set up firewall rules to allow the desired traffic flow.

Feedback

A is not correct because the subnetwork alone will not allow and restrict traffic as required without firewall rules.

B is not correct because this adds complexity to the architecture and the instance configuration.

C is not correct because routes still require firewall rules to allow traffic as requests. Additionally, the tags are used for defining the instances the route applies to, and not for identifying the next hop. The next hop is either an IP range or instance name, but in the proposed solution the tiers are only identified by tags.

D is correct because as instances scale, they will all have the same tag to identify the tier. These tags can then be leveraged in firewall rules to allow and restrict traffic as required, because tags can be used for both the target and source.

[https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

[https://cloud.google.com/vpc/docs/routes](https://cloud.google.com/vpc/docs/routes)

[https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)

You are designing a large distributed application with 30 microservices. Each of your distributed microservices needs to connect to a database backend. You want to store the credentials securely. Where should you store the credentials?

D. In a config file that has restricted access through ACLs

Feedback

A is not correct because storing credentials in source code and source control is discoverable, in plain text, by anyone with access to the source code. This also introduces the requirement to update code and do a deployment each time the credentials are rotated.

B is not correct because consistently populating environment variables would require the credentials to be available, in plain text, when the session is started.

C is correct because a secret management system such as Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. Secret Manager provides a central place and single source of truth to manage, access, and audit secrets across Google Cloud.

D is not correct because instead of managing access to the config file and updating manually as keys are rotated, it would be better to leverage a key management system. Additionally, there is increased risk if the config file contains the credentials in plain text.

[https://cloud.google.com/kubernetes-engine/docs/concepts/secret](https://cloud.google.com/kubernetes-engine/docs/concepts/secret)

[https://cloud.google.com/secret-manager](https://cloud.google.com/secret-manager)

For this question, refer to the Mountkirk Games case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2)

Mountkirk Games wants to set up a real-time analytics platform for their new game. The new platform must meet their technical requirements. Which combination of Google technologies will meet all of their requirements?

B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery

C. Cloud SQL, Cloud Storage, Cloud Pub/Sub, and Cloud Dataflow

D. Cloud Dataproc, Cloud Pub/Sub, Cloud SQL, and Cloud Dataflow

E. Cloud Pub/Sub, Compute Engine, Cloud Storage, and Cloud Dataproc

Correct answer

B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery

Feedback

A is not correct because Cloud SQL is the only storage listed, is limited to 10 TB of storage, and is better suited for transactional workloads. Mountkirk Games needs queries to access at least 30,720 GB of historical data for analytic purposes.

B is correct because:

-Cloud Dataflow dynamically scales up or down, can process data in real time, and is ideal for processing data that arrives late using Beam windows and triggers.

-Cloud Storage can be the landing space for files that are regularly uploaded by users’ mobile devices.

-Cloud Pub/Sub can ingest the streaming data from the mobile users.

BigQuery can query more than 10 TB of historical data.

C is not correct because Cloud SQL is the only storage listed, is limited to 30,720 GB of storage, and is better suited for transactional workloads. Mountkirk Games needs queries to access at least 10 TB of historical data for analytic purposes.

D is not correct because Cloud SQL is limited to 30,720 GB of storage and is better suited for transactional workloads. Mountkirk Games needs queries to access at least 10 TB of historical data for analytics purposes.

E is not correct because Mountkirk Games needs the ability to query historical data. While this might be possible using workarounds, such as BigQuery federated queries for Cloud Storage or Hive queries for Cloud Dataproc, these approaches are more complex. BigQuery is a simpler and more flexible product that fulfills those requirements.

[https://cloud.google.com/sql/docs/quotas#fixed-limits](https://cloud.google.com/sql/docs/quotas#fixed-limits)

[https://beam.apache.org/documentation/programming-guide/#windowing](https://beam.apache.org/documentation/programming-guide/#windowing)

[https://beam.apache.org/documentation/programming-guide/#triggers](https://beam.apache.org/documentation/programming-guide/#triggers)

[https://cloud.google.com/bigquery/external-data-sources](https://cloud.google.com/bigquery/external-data-sources)

[https://cloud.google.com/solutions/using-apache-hive-on-cloud-dataproc](https://cloud.google.com/solutions/using-apache-hive-on-cloud-dataproc)

For this question, refer to the Mountkirk Games case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2)

Mountkirk Games has deployed their new backend on Google Cloud Platform (GCP). You want to create a thorough testing process for new versions of the backend before they are released to the public. You want the testing environment to scale in an economical way. How should you design the process?

A. Create a scalable environment in Google Cloud for simulating production load.

B. Use the existing infrastructure to test the Google Cloud-based backend at scale.

C. Build stress tests into each component of your application and use resources from the already deployed production backend to simulate load.

D. Create a set of static environments in Google Cloud to test different levels of load—for example, high, medium, and low.

Correct answer

Feedback

A is correct because simulating production load in Google Cloud can scale in an economical way.

B is not correct because one of the pain points about the existing infrastructure was precisely that the environment did not scale well.

C is not correct because it is a best practice to have a clear separation between test and production environments. Generating test load should not be done from a production environment.

D is not correct because Mountkirk Games wants the testing environment to scale as needed. Defining several static environments for specific levels of load goes against this requirement.

[https://cloud.google.com/community/tutorials/load-testing-iot-using-gcp-and-locust](https://cloud.google.com/community/tutorials/load-testing-iot-using-gcp-and-locust)

[https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes)

For this question, refer to the Mountkirk Games case study. [https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2)

Mountkirk Games wants to set up a continuous delivery pipeline. Their architecture includes many small services that they want to be able to update and roll back quickly. Mountkirk Games has the following requirements: (1) Services are deployed redundantly across multiple regions in the US and Europe, (2) Only frontend services are exposed on the public internet, (3) They can reserve a single frontend IP for their fleet of services, and (4) Deployment artifacts are immutable. Which set of products should they use?

B. Cloud Storage, App Engine, Cloud Load Balancing

C. Container Registry, Google Kubernetes Engine, Cloud Load Balancing

D. Cloud Functions, Cloud Pub/Sub, Cloud Deployment Manager

Feedback

A is not correct because Mountkirk Games wants to set up a continuous delivery pipeline, not a data processing pipeline. Cloud Dataflow is a fully managed service for creating data processing pipelines.

B is not correct because a Cloud Load Balancer distributes traffic to Compute Engine instances. App Engine and Cloud Load Balancer are parts of different solutions.

C is correct because:

-Google Kubernetes Engine is ideal for deploying small services that can be updated and rolled back quickly. It is a best practice to manage services using immutable containers. -Cloud Load Balancing supports globally distributed services across multiple regions. It provides a single global IP address that can be used in DNS records. Using URL Maps, the requests can be routed to only the services that Mountkirk wants to expose. -Container Registry is a single place for a team to manage Docker images for the services.

D is not correct because you cannot reserve a single frontend IP for cloud functions. When deployed, an HTTP-triggered cloud function creates an endpoint with an automatically assigned IP.

[https://cloud.google.com/sql/docs/quotas#fixed-limits](https://cloud.google.com/sql/docs/quotas#fixed-limits)

[https://beam.apache.org/documentation/programming-guide/#windowing](https://beam.apache.org/documentation/programming-guide/#windowing)

[https://beam.apache.org/documentation/programming-guide/#triggers](https://beam.apache.org/documentation/programming-guide/#triggers)

[https://cloud.google.com/bigquery/external-data-sources](https://cloud.google.com/bigquery/external-data-sources)

[https://cloud.google.com/solutions/using-apache-hive-on-cloud-dataproc](https://cloud.google.com/solutions/using-apache-hive-on-cloud-dataproc)

Your customer is moving their corporate applications to Google Cloud. The security team wants detailed visibility of all resources in the organization. You use Resource Manager to set yourself up as the Organization Administrator. Which Cloud Identity and Access Management (Cloud IAM) roles should you give to the security team while following Google recommended practices?

Feedback

A is not correct because Project owner is too broad. The security team does not need to be able to make changes to projects.

B is correct because:

-Organization viewer grants the security team permissions to view the organization's display name.

-Project viewer grants the security team permissions to see the resources within projects.

C is not correct because Organization Administrator is too broad. The security team does not need to be able to make changes to the organization.

D is not correct because Project Owner is too broad. The security team does not need to be able to make changes to projects.

[https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles](https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles)

To reduce costs, the Director of Engineering has required all developers to move their development infrastructure resources from on-premises virtual machines (VMs) to Google Cloud. These resources go through multiple start/stop events during the day and require state to persist. You have been asked to design the process of running a development environment in Google Cloud while providing cost visibility to the finance department. Which two steps should you take? (choose two)

Feedback

A is correct because persistent disks will not be deleted when an instance is stopped.

B is not correct because the --auto-delete flag has no effect unless the instance is deleted. Stopping an instance does not delete the instance or the attached persistent disks.

C is not correct because labels are used to organize instances, not to monitor metrics.

D is correct because exporting daily usage and cost estimates automatically throughout the day to a BigQuery dataset is a good way of providing visibility to the finance department. Labels can then be used to group the costs based on team or cost center.

E is not correct because the state stored in local SSDs will be lost when the instance is stopped.

[https://cloud.google.com/compute/docs/instances/instance-life-cycle](https://cloud.google.com/compute/docs/instances/instance-life-cycle)

[https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete#--auto-delete](https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete#--auto-delete)

[https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--disk)

[https://cloud.google.com/compute/docs/disks/local-ssd#data_persistence](https://cloud.google.com/compute/docs/disks/local-ssd#data_persistence)

[https://cloud.google.com/billing/docs/how-to/export-data-bigquery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

[https://cloud.google.com/resource-manager/docs/creating-managing-labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels)

A is not correct because increasing the memory size requires a VM restart.

B is not correct because the DB administration team is requesting help with their MySQL instance. Migration to a different product should not be the solution when other optimization techniques can still be applied first.

C is correct because persistent disk performance is based on the total persistent disk capacity attached to an instance and the number of vCPUs that the instance has. Incrementing the persistent disk capacity will increment its throughput and IOPS, which in turn improve the performance of MySQL.

D is not correct because the DB administration team is requesting help with their MySQL instance. Migration to a different product should not be the solution when other optimization techniques can still be applied first.