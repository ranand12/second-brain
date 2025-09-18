# Gemini in BigQuery features are now GA | Google Cloud Blog

Column: https://cloud.google.com/blog/products/data-analytics/gemini-in-bigquery-features-are-now-ga
Processed: Yes
created on: September 4, 2024 6:18 PM

### Join us for Gemini at Work

Learn how Gemini can help your business at our digital event

[Register](https://cloudonair.withgoogle.com/events/gemini-at-work-24?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY24-Q3-global-EXP134-onlineevent-er-gemini-at-work-2024-mc&utm_content=left-hand-rail-cta&u)

According to Google’s [Data and AI Trends Report 2024](https://services.google.com/fh/files/misc/data_ai_trends_report.pdf), 84% of organizations believe that generative AI will expedite their access to insights, and notably 52% of non-technical users are already leveraging generative AI to extract valuable insights.

With Google’s Data Cloud, we’re on a mission to bring our decades of research and investments in AI to revolutionize data management and analytics, enabling organizations to reimagine experiences and build data agents grounded in their proprietary data. At Google Cloud Next 2024, we [introduced](https://cloud.google.com/blog/products/data-analytics/introducing-gemini-in-bigquery-at-next24?e=48754805) the preview of [Gemini in BigQuery](https://cloud.google.com/gemini/docs/bigquery/overview), which delivers AI-powered experiences such as data discovery and exploration, data preparation and engineering, analysis and insight generation covering the data journey, as well as intelligent recommendations to enhance user productivity and optimize costs.

“Gemini in BigQuery has transformed our query generation process. The integration into BigQuery makes it easy to generate SQL templates and has helped boost the efficiency of our label and feature engineering, including crucial machine learning model monitoring queries. Gemini’s ability to understand complex data structures and deliver accurate queries has made our workflow smoother and faster than ever.” - Martijn Wieriks, Chief Data Officer, Julo

Today, we are announcing general availability of several Gemini in BigQuery features, including SQL code generation and explanation, Python code generation, data canvas, data insights and partitioning, and clustering recommendations.

Let’s take a closer look at some of the functionality you can enjoy today with Gemini in BigQuery.

### **What makes Gemini in BigQuery different?**

Gemini in BigQuery brings the best of Google’s capabilities across data management and AI infrastructure with state-of-the-art models optimized for your business needs.

- 
    
    Context aware: decodes your intent, understands your goals and proactively engages with you to accelerate your workflows
    
- 
    
    Grounded in your data: continuously learns and adapts to your business data to uncover new opportunities and anticipate issues
    
- 
    
    Integrated experience: directly accessible within the BigQuery interface, providing a seamless experience across the analytics workflows
    

### **Getting started with data insights**

The data analysis journey first begins with data discovery and assessing which insights you can get from your data assets. Imagine having a library of insightful questions tailored specifically to your data – questions you didn't even know you should ask! [Data Insights](https://cloud.google.com/dataplex/docs/data-insights) eliminates the guesswork with pre-validated, ready-to-run queries offering immediate insights. For instance, if you're working with a table containing customer churn data, Data Insights might prompt you to explore the factors contributing to churn within specific customer segments — an angle you might not have thought to investigate.

These actionable queries are built into BigQuery Studio, providing the insights, right where you need them, to advance your analysis with a single-click.

![](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/1._Data_Insights.gif)

Gemini in BigQuery suggests executable queries as natural language insights for tables that you can run with a single click

### **Enhance productivity with SQL and Python code assistance**

Gemini for BigQuery helps you [write and modify SQL or Python code](https://cloud.google.com/bigquery/docs/write-sql-gemini) using straightforward natural language prompts, referencing relevant schemas and metadata. This helps reduce errors and inconsistencies in your code while empowering users to craft complex, accurate queries, even if they have limited coding experience.

“Gemini in BigQuery helps our data teams deliver insight more quickly and reduce the cycle time of data pipelines and analysis. SQL code generation and text-embedding using AI enhances productivity and allows more time to focus on high impact initiatives. Ultimately, this will help us achieve our mission of providing behavioral intelligence to our clients." - Okayasu, Chief Data Scientist at Unerry, Inc.

Gemini in BigQuery comprehends the structure and relationships within your data, so you can receive tailored code suggestions from a straightforward natural-language prompt. For example, you can ask it to:

- 
    
    "Generate a SQL query to calculate the total sales for each product in the table."
    
- 
    
    "Write Python code to correlate between product sales and number of customer reviews using pandas”
    
- 
    
    “Calculate the average trip length by subscriber type”
    

![](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/2._SQL_Code_Generation.gif)

SQL code generation using Gemini in BigQuery

Gemini in BigQuery can also provide [explanations and insights](https://cloud.google.com/bigquery/docs/write-sql-gemini#explain_a_sql_query) to help you understand complex SQL and Python queries, making it easier for users of all skill levels to understand the logic behind the code. This is especially beneficial for those who are new to SQL and Python, or working with unfamiliar datasets.

SQL code explanation using Gemini in BigQuery

### **Reimagined analytics workflows with natural language**

Gemini in BigQuery includes [data canvas](https://cloud.google.com/bigquery/docs/data-canvas), an innovative natural language-based interface for data exploration, curation, wrangling, analysis, and visualization. Data canvas enables you to explore and structure your data journeys through a graphical workflow, for smooth and intuitive data exploration and analysis.

"For any sort of investigation or exploratory exercise you know will result in multiple queries, there really is no replacement. It’s saved us so much time and mental capacity" - Scott Schaen, VP of Analytics, Wunderkind

For example, to analyze revenue across retail stores, you could use simple natural language prompts to gather data from various sources such as a POS system, integrate with inventory, CRM or external data, uncover relationships between factors like store location, product categories, and revenue, or develop reports and visualizations for stakeholders — all within a single user interface. Refer to [this blog](https://cloud.google.com/blog/products/data-analytics/using-bigquery-data-canvas-a-deep-dive) and watch the demo below for a deep dive into BigQuery data canvas.

![](https://storage.googleapis.com/gweb-cloudblog-publish/images/image4_V4N4GUB.max-1200x1200.png)

### **Optimize analytics for performance and speed**

As data volumes grow, data administrators and other analytics professionals face challenges in effectively managing capacity and improving query performance. To address these challenges, Gemini in BigQuery offers AI-powered [recommendations for partitioning and clustering](https://cloud.google.com/bigquery/docs/view-partition-cluster-recommendations) your tables. These recommendations aim to optimize your tables for faster results and lower query costs without requiring any modifications to your queries.

### **Getting started**

General availability of Gemini in BigQuery features will be rolled out in phases over the next few months starting today with SQL code generation and explanation, Python code generation, data canvas, data insights and partitioning and clustering recommendations.

At this time, generally available (GA) features are available to all customers at no additional cost. Please refer to the [pricing details](https://cloud.google.com/products/gemini/pricing#gemini-in-bigquery-pricing) for more information.