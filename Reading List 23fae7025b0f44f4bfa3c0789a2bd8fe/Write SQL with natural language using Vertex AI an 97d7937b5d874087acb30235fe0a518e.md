# Write SQL with natural language using Vertex AI and BigQuery | by Israel Herraiz | Google Cloud - Community | Nov, 2023 | Medium

Column: https://medium.com/google-cloud/write-sql-with-natural-language-using-vertex-ai-and-bigquery-c849559f8a5f
Processed: No
created on: December 11, 2023 6:21 AM

# Write SQL with natural language using Vertex AI and BigQuery

![](Write%20SQL%20with%20natural%20language%20using%20Vertex%20AI%20an%2097d7937b5d874087acb30235fe0a518e/2DMXqCWnuJExXGVov3sZgbQ.png)

![](Write%20SQL%20with%20natural%20language%20using%20Vertex%20AI%20an%2097d7937b5d874087acb30235fe0a518e/1FUjLiCANvATKeaJEeg20Rw.png)

[Israel Herraiz](https://medium.com/@iht?source=post_page-----c849559f8a5f--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fd68053e6f10b&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fwrite-sql-with-natural-language-using-vertex-ai-and-bigquery-c849559f8a5f&user=Israel+Herraiz&userId=d68053e6f10b&source=post_page-d68053e6f10b----c849559f8a5f---------------------post_header-----------)

Published in

[Google Cloud - Community](https://medium.com/google-cloud?source=post_page-----c849559f8a5f--------------------------------)

·

2 min read

·

Nov 26

Picture from devfest, authored by the GDG Cloud Madrid ([https://twitter.com/gdgcloudmadrid/status/1728392858778898587](https://twitter.com/gdgcloudmadrid/status/1728392858778898587))

![](Write%20SQL%20with%20natural%20language%20using%20Vertex%20AI%20an%2097d7937b5d874087acb30235fe0a518e/1sBTdanjhBGJdCJr1TwNVpQ.jpeg)

The last weekend I had the opportunity to speak at the [devfest of the GDG Cloud Madrid](https://gdg.community.dev/events/details/google-gdg-cloud-madrid-presents-devfest-cloud-madrid/), presenting an example of how query a dataset in BigQuery using natural language. This post shares some details about the workshop and all the materials to replicate it or run a demo without having to write any code.

The example is using [langchain](https://github.com/langchain-ai/langchain), [PaLM](https://cloud.google.com/vertex-ai/docs/generative-ai/language-model-overview) and [Codey](https://cloud.google.com/vertex-ai/docs/generative-ai/code/code-models-overview), and [Vertex AI embeddings](https://cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings), to get a question from the user, transform it into a SQL query, run it in BigQuery, get the result in CSV, and interpret all that information to provide an answer to the question. The coordination of all the activities is done with a langchain Agent, that is also using a mathematical tool to be able to do some calculations with the results.

The prompts are using the schema of the tables in the dataset as context. These schemas are converted into embeddings using Vertex AI and ingested into a local [ChromaDb](https://github.com/chroma-core/chroma). Each table's schema is a single document, and only one document is ingested into the prompt.

The agent is using some memory and the prompts are prepared to get that memory ingested into the prompt, so you can make follow-up questions, and the agent will remember the context of the previous question to provide new answers.

The [BigQuery public dataset used in this example](https://console.cloud.google.com/marketplace/product/noaa-public/tsunamis) contains two tables, with very detailed annotations, that really helps the model in the generation of correct queries. If you want to use any other table or dataset, I strongly recommend adding annotations to the schema, to improve the quality of the generated queries.

What do you need to run this workshop? You will need a Google Cloud project with Vertex AI and BigQuery enabled, and permissions to use the PaLM, Codey and embedding APIs, as well as to run BigQuery queries. The cost of running the example and a couple of question is <0.10 USD, so [you can use the free credits offered for new accounts to run the notebooks](https://cloud.google.com/free).

If you want to replicate this workshop, you can use the following materials:

- [Blank Colab notebook that you can share with the attendees to write their own code](https://colab.research.google.com/drive/19G4KmuVSiVxajzoQWhcHW5HAJga_emFZ?usp=sharing).
- [Solution Colab notebook with the full code. You can use this notebook to run a demo without having to write any code](https://colab.research.google.com/drive/1vL8QYCj42uQrMRkCbCvGOemQgmcnygqj?usp=sharing).
- [Code written during the Devfest. This notebook should not differ much from the solution, sharing it here just for attendees of the workshop](https://colab.research.google.com/drive/12MPzLJotIJANgZ7pklfGpMhGDitWjU4Y?usp=sharing).