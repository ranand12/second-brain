# Multimodel search using NLP, BigQuery and embeddings | Google Cloud Blog

Column: https://cloud.google.com/blog/products/data-analytics/multimodel-search-using-nlp-bigquery-and-embeddings
Processed: Yes
created on: September 4, 2024 6:51 AM

Generative AI Solutions Architect, Google

### Join us for Gemini at Work

Learn how Gemini can help your business at our digital event

[Register](https://cloudonair.withgoogle.com/events/gemini-at-work-24?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY24-Q3-global-EXP134-onlineevent-er-gemini-at-work-2024-mc&utm_content=left-hand-rail-cta&u)

Today's digital landscape offers a vast sea of information, encompassing not only text, but also images and videos. Traditional enterprise search engines were primarily designed for text-based queries, and often fall short when it comes to analyzing visual content. However, with a combination of natural language processing (NLP) and [multimodal embeddings](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-multimodal-embeddings#use-cases), a new era of search is emerging that lets your customers search for an image or video — or information within it — in the same way they would with text-based content.

In this blog, we showcase a demo for performing text search on images, videos, or both using a powerful multimodal embedding model that’s specifically designed for cross-modal semantic search scenarios such as searching images using text, or finding text in images based on a given query. Multimodal embedding is the key to accomplishing these tasks.

Our demo performs text to image search, text to video search, text to image and video combined search

Let's see how this works!

### **A solution for converged image, video, and text search**

The architecture leverages Google Cloud Storage for storing media files, with BigQuery object tables referencing these files. A multimodal embedding model generates semantic embeddings for the images and videos, which are then indexed in BigQuery for efficient similarity search, enabling seamless cross-modal search experiences.

![](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/image1_CxXpy0v.gif)

From text to visuals: Multimodal search for images and videos

To implement a similar solution, follow the steps below.

**Steps 1 - 2: Upload image and video data to Cloud Storage**

Upload all image and video files to a Cloud Storage bucket. For the demo, we’ve downloaded some images and videos from Google Search that are [available on GitHub](https://github.com/LUJ20/Blog.git). Be sure to remove the README.md file before uploading them to your Cloud Storage bucket.

**Prepare your media files:**

- 
    
    Using your own data, collect all the images and video files you plan to work with.
    
- 
    
    Ensure the files are organized and named appropriately for easy management and access.
    

**Upload data to Cloud Storage:**

- 
    
    Create a Cloud Storage bucket, if you haven't already.
    
- 
    
    Upload your media files into the bucket. You can use the Google Cloud console, the `gsutil` command-line tool, or the Cloud Storage API.
    
- 
    
    Verify that the files are uploaded correctly and note the bucket's name and path where the files are stored (e.g., `gs://your-bucket-name/your-files`).
    

**Step 3: Create an object table in BigQuery**

Create an [Object table](https://cloud.google.com/bigquery/docs/object-table-introduction) in BigQuery to point to your source image and video files in the Cloud Storage bucket. Object tables are read-only tables over unstructured data objects that reside in Cloud Storage. You can learn about other use cases for BigQuery object tables [here](https://cloud.google.com/bigquery/docs/object-table-introduction#use_cases).

Before you create the object table, establish a connection, as described [here](https://cloud.google.com/bigquery/docs/bigquery-ml-remote-model-tutorial#set_up_access). Ensure that the connection's principal has the ‘Vertex AI User’ role and that the Vertex AI API is enabled for your project.

**Create remote connection**

Loading...

**Create object table**

Loading...

**Step 4:** **Create your multimodal embeddings**

We generate embeddings (numerical representations) for your media data using a pre-trained multimodal embedding model. These embeddings capture the semantic information of the content, enabling efficient similarity searches.

Loading...

**Step 5: Create a vector index in BigQuery**

Create a [VECTOR INDEX](https://cloud.google.com/bigquery/docs/vector-index#create_a_vector_index) in BigQuery for the embeddings to efficiently store and query the embeddings generated from your image and video data. This index is essential for performing similarity searches later.

Loading...

**Step 6: Send the user’s query as text input**

A user’s query is sent as text input in simple natural language like “elephant eating grass”. When a user submits a query, the system converts this textual input into an embedding, similar to how it processed the media data.

**Step 7: Create a text embedding for the user query**

You can create a text embedding for the user query using the same multimodal embedding model. To compare the user query with the stored embeddings, first generate an embedding for the query itself using the same multimodal embedding model.

Loading...

**Step 8: Perform similarity search**

Similarity search is performed between the user query and the source data containing images and videos using [VECTOR SEARCH](https://cloud.google.com/bigquery/docs/vector-search-intro). Using the vector index created in Step 4, perform a similarity search to find the most similar media items to the user query. This search compares the user query's embedding with the embeddings of the media data.

Loading...

**Step 9: Return the search results for images and videos to the user**

Finally, the results from the similarity search are presented to the user. The results include the URIs of the most similar images and videos stored in the Cloud Storage bucket, along with their similarity scores (distances). This allows the user to view or download the media items related to their query.

### **Multimodal embeddings powers a new level of search**

Because multimodal embeddings can handle both image and video modalities, building a powerful search experience across your visual content is just a few steps away. No matter if your use case is image search, video search, or image and video search combined, get ready to unlock a new level of search enhancing your users’ experiences and streamlining content discovery.