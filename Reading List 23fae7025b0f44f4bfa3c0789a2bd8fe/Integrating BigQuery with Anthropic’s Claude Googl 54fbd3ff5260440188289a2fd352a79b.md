# Integrating BigQuery with Anthropic’s Claude | Google Cloud Blog

Column: https://cloud.google.com/blog/products/data-analytics/integrating-bigquery-with-anthropics-claude
Processed: Yes
created on: September 4, 2024 6:18 PM

![](https://storage.googleapis.com/gweb-cloudblog-publish/images/021624c_GC_GIF_VertexAI_ModelGarden_LogoLo.max-2500x2500.jpg)

Sr. Customer Engineer, Analytics, Google Cloud

### Michael Stern

Senior Data Scientist, Anthropic

The world’s most productive and innovative organizations rely on their trusted business data to inform their decision-making, operational efficiency, insights, and growth. Now, gen AI enters the equation, opening up possibilities to transform this wealth of information into an unprecedented competitive edge.

Google Cloud has been at the forefront of integrating advanced gen AI capabilities directly within [BigQuery,](https://cloud.google.com/bigquery?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665665924750-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt-Data+Analytics-BigQuery-KWID_43700077225652815-kwd-47616965283&utm_term=KW_bigquery-ST_bigquery&gad_source=1&gclid=CjwKCAjw8rW2BhAgEiwAoRO5rDdEcPlaUa4K_VA_jnW9XH5dvtdGzCdH8w3L-cL8SBFomlDu-SQOyBoCi_IQAvD_BwE&gclsrc=aw.ds&e=48754805&hl=en) our gen AI-ready data platform. Organizations are already harnessing gen AI models like Gemini 1.5 Pro on Vertex AI within the BigQuery platform. And today, we're extending Google Cloud’s open platform with the preview of BigQuery’s new integration with [Anthropic's Claude models on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) that connects your data in BigQuery with the powerful intelligence capabilities of Claude models.

Organizations can now access the power of Anthropic's Claude models that offer advanced gen AI capabilities through BigQuery ML (BQML). BQML simplifies the application of machine learning to data within BigQuery, making it accessible to analysts and SQL users. This integration enables tasks such as text generation, summarization, translation, and more, to be performed directly on your data.

## **Powerful use cases**

BigQuery’s integration with Anthropic’s Claude models allows organizations to reimagine data-driven decision making and boost productivity across a variety of tasks including:

1. **Analyzing log data for enhanced security:** Security teams can efficiently analyze log data in BigQuery, converting complex technical information into clear, readable form and generating appropriate response strategies.
2. **Marketing optimization:** Marketing teams can now harness user and product data stored in BigQuery to generate targeted, data-driven campaigns at scale — helping to boost engagement and ROI.
3. **Document summarization:** Organizations can streamline knowledge management by automatically summarizing internal documents stored in Google Cloud Storage, saving time and resources.
4. **Content localization:** Global organizations can quickly translate text content stored in BigQuery, facilitating communication across language barriers.

Let's further explore a couple of examples showcasing the possibilities of using Claude models in BigQuery.

### **Log summarization and recommendations**

Organizations commonly store error log data in BigQuery for its ease of use, scalability, and advanced features such as search and vector indexes, which aid in log analytics. Combining your BigQuery data with the Claude models on Vertex AI can supercharge this use case. For example, organizations can efficiently summarize log entries and generate suggested fixes to streamline issue identification and resolution processes.

Let’s see how:

Loading...

Loading...

Summarizing log entries and recommending fixes

And there you have it! We've generated a concise log summary and recommended solutions using only SQL and the power of Claude's AI capabilities.

### **Translating museum art descriptions**

Let's explore another use case: translating the titles of Korean art pieces stored in a BigQuery table into English. Claude can efficiently handle this task for you.

Loading...

Translating Korean museum art descriptions into English

## **Get started with Claude in BigQuery**

To get started with Claude in BigQuery, you can follow our [documentation](https://cloud.google.com/bigquery/docs/generate-text?hl=en) or import our [sample notebook](https://github.com/GoogleCloudPlatform/professional-services/blob/main/examples/bigquery-ml-claudeintegrations/Python_Notebook_Sample/BQML%2BClaude.ipynb) directly into BigQuery Studio for a hands-on walkthrough.

For users seeking more advanced Python support and configuration flexibility, we also offer two additional integration methods:

1. 
    
    **Python with BigQuery Studio (generally available):** Data scientists and Python developers can utilize notebooks in the BigQuery UI to directly connect BigQuery data to the Claude models using Python. For a quick start guide and example code, refer to our [sample notebook](https://github.com/googleapis/python-bigquery-dataframes/blob/main/notebooks/generative_ai/bq_dataframes_llm_claude3_museum_art.ipynb) that uses BigQuery DataFrames.
    
2. 
    
    **BigQuery remote functions (generally available):** This method is ideal for code-heavy users, offering high flexibility and access to all Claude models. Get started by exploring our [sample GitHub repository](https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/bigquery-ml-claudeintegrations/BQ_RemoteFunction_Sample). You can also use this [sample notebook](https://github.com/googleapis/python-bigquery-dataframes/blob/main/notebooks/remote_functions/remote_function_vertex_claude_model.ipynb), which leverages BigQuery DataFrames to automatically create remote functions and perform inference with Claude.
    

Anthropic’s Claude integration with BigQuery marks a significant step forward in democratizing gen AI and enabling businesses of all sizes to harness the full potential of their data. We encourage you to explore this integration and discover how it can transform your data analytics workflows.