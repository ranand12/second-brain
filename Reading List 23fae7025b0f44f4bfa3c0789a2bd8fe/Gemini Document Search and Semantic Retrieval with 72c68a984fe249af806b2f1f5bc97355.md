# Gemini Document Search and Semantic Retrieval with Attributed Question Answering.ipynb - Colaboratory

Column: https://colab.research.google.com/drive/1RIDTmqj0JBVX8o7lDqLUAK9edwLwGxjF?usp=sharing
Processed: No
created on: December 17, 2023 2:51 PM

![colab_favicon_256px.png](Gemini%20Document%20Search%20and%20Semantic%20Retrieval%20with%2072c68a984fe249af806b2f1f5bc97355/colab_favicon_256px.png)

#@title Licensed under the Apache License, Version 2.0 (the "License");

# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at

#

# https://www.apache.org/licenses/LICENSE-2.0

#

# Unless required by applicable law or agreed to in writing, software

# distributed under the License is distributed on an "AS IS" BASIS,

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and

# limitations under the License.

<div _="@=3391,dis=none"><div _="@=3392,dis=none,[@=3393]">#@title Licensed under the Apache License, Version 2.0 (the "License"); # you may not use this file except in compliance with the License. # You may obtain a copy of the License at # # https://www.apache.org/licenses/LICENSE-2.0 # # Unless required by applicable law or agreed to in writing, software # distributed under the License is distributed on an "AS IS" BASIS, # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. # See the License for the specific language governing pe</div></div>

(Google's original notebook that this is based on)

## Overview

This example demonstrates how to use the Gemini API to create embeddings so that you can perform document search. You will use the Python client library to build a word embedding that allows you to compare search strings, or questions, to document contents.

In this tutorial, you'll use embeddings to perform document search over a set of documents to ask questions related to the Google Car.

## Prerequisites

You can run this quickstart in Google Colab.

To complete this quickstart on your own development environment, ensure that your envirmonement meets the following requirements:

- Python 3.9+
- An installation of `jupyter` to run the notebook.

## Setup

First, download and install the Gemini API Python library.

## Install Packages and imports

Leo: I've added langchain, tiktoken, and some pdf processing dependencies so that this notebook can process any PDF, from a file or URL.

```
!pip install -U -q google.generativeai

```

```
import textwrap
import numpy as np
import pandas as pd

import google.generativeai as genai
import google.ai.generativelanguage as glm

# Used to securely store your API key
from google.colab import userdata

from IPython.display import Markdown
import os

```

```
!pip install -U -q langchain tiktoken unstructured==0.11.2 pdf2image pdfminer.six pikepdf pypdf unstructured_pytesseract unstructured_inference

```

```
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 16.3 MB/s eta 0:00:00
```

```
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
import pdfminer
import pikepdf
import pypdf
import unstructured_pytesseract
import unstructured_inference
from unstructured.partition.pdf import partition_pdf

```

Over the weekend while writing this, I encountered a problem where the package manager was installing a version of Unstructured 0.11.4 that did not contain the `unstructured.partitions.pdf.py` file. I later verified that the version of unstructured available from PyPl is missing this particular file from the Dec 14 release. As a result, installing from source is necessary to get the full package with PDF support. I'm sure this will get fixed soon. Alternately, you can downgrade to the previous release version of unstructured, provided you know that that is 0.11.2. My packages above reflect this downgrade. The latest unstructured can be installed from git using the code below.

```
pip install git+https://github.com/Unstructured-IO/unstructured.git

```

## Get your Google AI Studio API Key

Before you can use the Gemini API, you must first obtain an API key. If you don't already have one, create a key with one click in Google AI Studio.

[Get an API key](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fmakersuite.google.com%2Fapp%2Fapikey)

In Colab, add the key to the secrets manager under the "🔑" in the left panel. Give it the name `API_KEY`.

Once you have the API key, pass it to the SDK. You can do this in two ways:

- Put the key in the `GOOGLE_API_KEY` environment variable (the SDK will automatically pick it up from there).
- Pass the key to `genai.configure(api_key=...)`

```
from google.colab import userdata
API_KEY = userdata.get('API_KEY')

genai.configure(api_key=API_KEY)

```

## Embedding generation

In this section, you will see how to generate embeddings for a piece of text using the embeddings from the Gemini API.

### API changes to Embeddings with model embedding-001

For the new embeddings model, embedding-001, there is a new task type parameter and the optional title (only valid with task_type=`RETRIEVAL_DOCUMENT`).

These new parameters apply only to the newest embeddings models.The task types are:

| Task Type | Description |
| --- | --- |
| RETRIEVAL_QUERY | Specifies the given text is a query in a search/retrieval setting. |
| RETRIEVAL_DOCUMENT | Specifies the given text is a document in a search/retrieval setting. |
| SEMANTIC_SIMILARITY | Specifies the given text will be used for Semantic Textual Similarity (STS). |
| CLASSIFICATION | Specifies that the embeddings will be used for classification. |
| CLUSTERING | Specifies that the embeddings will be used for clustering. |

This is just a sample embedding created from a portion of the recent Warhol SCOTUS decision. Run this cell to make sure that your API key is working and correctly being passed from the notebook userdata. Note the `title` parameter. This is a new optional parameter that is only used with the `task_type` is `retrieval_document`. It's not yet clear whether this is incorporated into the embedding, or how. Since we are only retrieving from a knowledge base containing a single document, it likely doesn't matter much here.

```
title = "ANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH"
sample_text = ("""In 2016, petitioner Andy Warhol Foundation for the Visual Arts, Inc.
(AWF) licensed to Condé Nast for $10,000 an image of “Orange
Prince”—an orange silkscreen portrait of the musician Prince created
by pop artist Andy Warhol—to appear on the cover of a magazine com-
memorating Prince. Orange Prince is one of 16 works now known as
the Prince Series that Warhol derived from a copyrighted photograph
taken in 1981 by respondent Lynn Goldsmith, a professional photog-
rapher.""")

model = 'models/embedding-001'
embedding = genai.embed_content(model=model,
                                content=sample_text,
                                task_type="retrieval_document",
                                title=title)

print(embedding)

```

```
{'embedding': [-0.004976866, -0.04624615, -0.047661625, -0.04056859, 0.10324767, -0.020868372, 0.023740215, 0.018633293, 0.06901656, 0.0022520986, 0.047237497, 0.05694859, -0.00045273575, -0.0042082793, 0.0348532, -0.06980623, 0.027102608, 0.045155425, -0.012675372, -0.09266169, -0.01417843, 0.03684274, 0.02121998, -0.019039992, -0.028201852, -0.014396963, 0.026175383, -0.08828838, -0.011369659, 0.048632525, -0.042363264, 0.02496338, -0.029759683, 0.061684623, 0.02667723, -0.06739606, -0.017340023, 0.037661646, -0.018567342, 0.020785995, -0.01977513, -0.01946769, -0.013868994, -0.052813265, 0.029303534, 0.016044145, -0.008170931, 0.0526105, -0.010348585, -0.044506326, 0.0566009, -0.05120147, 0.04071312, -0.05216053, -0.01364342, -0.01434613, 0.037146643, -0.040675074, -0.06251755, 0.0070602167, -0.028874312, 0.040811654, -0.024771893, -0.009799687, -0.01386678, -0.029561162, -0.023884322, 0.036670666, 0.003180297, 0.008733685, -0.04203412, -0.030888088, 0.05821382, -0.044809062, -0.007836046, -0.057979353, -0.053682014, 0.041715946, 0.03343989, 0.017519182, 0.010096066, -0.058572616, -0.041040976, -0.00986612, -0.047550675, 0.0295866, -0.0059901397, 0.024811458, 0.048734058, 0.010245747, -0.024484674, 0.023097638, 0.053525995, -0.054138836, 0.00745888, 0.027186904, -0.015356665, -0.06565144, -0.00057914545, -0.024147315, -0.0043678368, 0.011246604, 0.054410085, -0.040422104, -0.01899705, -0.02231439, 0.018256595, -0.02977875, 0.002376362, 0.03554239, -0.07735546, -0.016310833, -0.05506787, -0.0012349872, 0.039004788, 0.0025861477, -0.026286451, 0.091595605, 0.061924864, 0.025823567, 0.0074521434, -0.0076505993, 0.0059091076, -0.016138459, 0.022550078, 0.0041678357, 0.03828429, -0.01965702, 0.040102378, 0.05084113, 0.023000767, -0.09892836, 0.0126591185, -0.0015476356, 0.02237751, 0.07717141, 0.054221172, 0.027722787, 0.049150895, 0.017049037, 0.0028236283, 0.011377431, 0.0010187365, -0.032277815, 0.012968497, 0.025383098, -0.021789124, 0.010297913, 0.015158086, -0.007441771, 0.0010640839, 0.011745505, -0.007570229, 0.07980004, 0.06921349, -0.0046224375, 0.021889577, -0.011153, -0.043268967, 0.058961395, 0.010385791, 0.019070115, 0.019794641, 0.0026808612, 0.01005502, 0.06233039, 0.014149492, -0.042103086, 0.00673105, 0.020235332, -0.012002118, 0.02104095, -0.03021492, -0.066290185, -0.053596694, -0.061571673, -0.0428266, 0.044098012, 0.013838689, -0.0162999, -0.0023573888, -0.015945854, -0.03570554, 0.03577271, 0.06472448, 0.00045588033, 0.03434533, -0.0030392047, 0.005286101, 0.034734067, -0.0037725698, -0.009746132, 0.0016061858, -0.013558318, -0.019982442, 0.0878603, -0.012107704, -0.032460976, -0.025595047, -0.026354378, -0.004993418, 0.09033975, -0.021955723, 0.018615156, 0.02226148, -0.014510714, 0.048399623, -0.0034854033, 0.015284697, 0.03211218, -0.05443323, 0.017524658, -0.044108607, -0.0018872899, 0.02750897, -0.0060320734, 0.03624143, 0.0026784071, -0.052043315, -0.0079826815, -0.0048898445, 0.019683123, -0.074540354, 0.031093197, -0.0060632653, -0.03425535, 0.00014809509, 0.015067251, 0.017436339, -0.07110031, 0.048118122, 0.053694148, 0.039045375, -0.027930705, 0.040523045, -0.026900467, -0.024901109, -0.021535438, 0.010725484, 0.032944117, -0.043211978, 0.094861485, -0.01603096, 0.009223566, -0.03892301, -0.059932195, -0.0048685567, 0.003982606, -0.05548368, 0.062813684, 0.008524085, -0.03230288, -0.0223381, 0.0044777314, -0.020000486, 0.047846723, -0.08918381, -0.015689634, 0.002842541, -0.017398153, 0.008727959, -0.027312998, 0.027783109, 0.0066102506, -0.09342119, 0.05180648, 0.0011522179, -0.018674536, -0.05168957, 0.026749894, 0.018523766, -0.013328173, 0.05730998, 0.00096686743, -0.02785839, 0.030657018, 0.0062646843, 0.02839573, 0.0064440137, -0.08697586, 0.05935754, 0.016646672, 0.051486768, -0.043499928, -0.01749423, -0.016719338, -0.011477549, 0.009062312, -0.002276839, 0.017756555, -0.05692082, 0.012415168, -0.0039454675, -0.023019327, -0.056993056, -0.042334437, -0.010526928, 0.06435221, -0.0016138625, -0.04977949, -0.019988632, -0.071789265, 0.00982892, -0.077348515, -0.024718434, -0.018175531, -0.049225096, -0.019697005, 0.029487386, 0.0009586304, -0.008127651, 0.0227264, -0.024248034, -0.052564133, 0.038140863, 0.068396464, -0.016828915, 0.013358836, -0.036399994, 0.022250148, -0.012388232, -0.0026018661, 0.039909326, 0.001821495, 0.045406174, -0.0063829343, -0.056346122, 0.04624685, -0.00071014895, -0.00042590217, -0.017090486, -0.028406484, -0.010296662, -0.01913015, -0.016079731, 0.036111984, -0.030772744, -0.02043927, -0.05280836, -0.0068901833, 0.024937449, -0.058324646, -0.036902282, -0.011431598, 0.0387638, 0.000426429, 0.010406172, -0.009825656, 0.046508517, 0.0054223957, 0.0047383625, 0.051048208, 0.02700438, 0.015471608, -0.011638636, 0.0069349613, 0.10464443, -0.02687938, 0.025409823, -0.06019871, 0.01070245, 0.06910251, 0.07037577, -0.028926685, 0.012743946, 0.054410513, 0.02850325, 0.01769544, -0.0022389584, -0.002860654, -0.0023848515, 0.033781834, -0.012436793, -0.052994367, 0.016362544, -0.031100288, -0.06686961, -0.016831545, 0.048513778, 0.04289779, 0.005380668, -0.03689105, 0.08826512, 0.025190191, 0.017173167, 0.010546654, 0.0020889016, -0.0006365901, -0.008119783, 0.008659141, 0.0584968, 0.025060097, 0.02078225, 0.038250368, 0.0037360175, -0.036128867, -0.014854318, -0.04285174, 0.007150888, 0.03437074, -0.024843767, 0.019305116, 0.0042649964, 0.022083312, -0.03656576, -0.02002597, 0.0049792537, -0.00765619, -0.02328874, 0.016979784, 0.0642907, 0.03290058, 0.06063606, -0.08694921, -0.026118726, -0.019665148, 0.07599059, 0.0019414877, -0.02669953, 0.03257894, 0.01527187, -0.06738513, -0.04801184, -0.035515655, -0.017880531, -0.0372949, 0.006197591, -0.0042310813, -0.020073345, 0.007671911, 0.026208298, 0.030132346, 0.045866527, 0.038758334, -0.010347052, -0.026372526, -0.007965523, 0.050924808, -0.04237642, -0.013719418, 0.03323391, -0.011611348, 0.018299129, 0.0047581205, -0.066993386, -0.024669617, -0.06290903, 0.016753234, 5.0027586e-05, -0.061581593, 0.038253188, -0.038939033, 0.009455455, -0.029965935, -0.025584431, -0.046781685, -0.0047209626, 0.099781044, 0.0020814072, -0.021897167, -0.014015125, -0.028504018, -0.055796627, -0.04783317, 0.024662666, -0.011065446, -0.03201032, -0.004435861, 0.03368821, 0.03693288, 0.017338622, -0.0046943575, -0.05529277, -0.057380673, -0.0039637215, -0.00642821, -0.022726722, -0.019321265, -0.012506433, -0.05117882, 0.008267896, 0.031969182, 0.08390803, 0.02609052, 0.016715504, 0.013288902, -0.0056785005, -0.009121323, -0.0050255856, 0.02169455, 0.03196497, -0.008054965, -0.041047793, -0.016133664, -0.029178772, 0.029209025, -0.007524306, 0.056839604, 0.06070915, 0.0051792627, -0.029503759, 0.026416129, -0.019293262, 0.020275682, 0.029819764, -0.044806425, 0.02598535, 0.018320289, -0.0019629062, -0.0016480407, -0.031511273, 0.01846828, -0.0064892666, -0.0037554055, 0.03340517, -0.035535887, -0.008508412, 0.0112487115, -0.0058706743, -0.021407945, 0.04292082, 0.011258899, -0.08397664, -0.029328726, 0.030001422, -0.015329121, 0.020574497, 0.051101882, 0.011119426, -0.011534415, -0.038380947, 0.07751051, -0.058573265, -0.03815293, 0.018522678, -0.029504836, -0.020345341, -0.0030705405, 0.0064464156, 0.045636285, 0.008559337, -0.009323995, 0.05708601, -0.004622974, 0.0063397535, -0.012260528, 0.012665184, -0.07564048, -0.0010283159, -0.009371249, 0.054506745, -0.033287022, 0.02634211, -0.015208158, 0.018611675, 0.0046161665, 0.020904956, -0.0014151203, 0.010666072, 0.009324664, -0.030204793, 0.035377886, -0.008936418, -0.002992741, 0.13570507, 0.0190132, -0.037908074, -0.0074627264, 0.0022879948, -0.0058692647, 0.006830382, 0.011454213, 0.026636362, -0.01842619, -0.006431238, -0.0071042483, -0.025320563, -0.0035101161, -0.024867032, -0.030192496, -0.0043509747, 0.028655909, -0.0067975367, 0.06790402, -0.055300362, 0.051891174, 0.055791356, 0.01108429, 0.022244502, -0.015873251, -0.06600406, 0.018006388, -0.048122168, -0.007528033, -0.024238855, -0.012563854, 0.012191923, 0.00019368996, -0.030983496, -0.028985467, -0.017002324, -0.073724516, 0.04652599, -0.05314217, 0.061769247, -0.023091258, 0.03668825, -0.051470954, -0.009936198, -0.014995599, -0.023611967, -0.04588737, 0.020085214, -0.031299524, -0.047516473, -0.01915155, 0.052065786, 0.032320358, -0.04413868, -0.051878702, 0.003780587, -0.039416604, -0.003264194, -0.02274741, 0.034388967, -0.03045532, -0.043385357, -0.017972926, 0.06774251, 0.035700317, 0.043657545, 0.04813205, 0.013287287, 0.00573723, -0.03099538, -0.03649402, 0.00962354, -0.024330162, -0.03530285, 0.010935875, -0.08632706, -0.0027170223, 0.036657847, -0.008484242, -0.04692315, 0.045856282, -0.0059953732, -0.07772597, -0.019331804, 0.05665354, -0.05162865, 0.0037664515, 0.024579085, 0.0031247856, -0.015645359, -0.061431058, -0.03662527, -0.01743288, -0.0024264883, -2.1054851e-05, -0.011493636, 0.018520636, -0.011062931, 0.011163688, -0.001399845, -0.0052850186, -0.07553557, -0.074912764, 0.018374698, 0.0006576773, -0.09801301, 0.04480383, 0.05768064, -0.0462757, 0.028673628, 0.00021379911, -0.02371518, 0.019426644, -0.039137512, 0.01954581, -0.011673203, -0.023930015, 0.006704192, 0.021393925, 0.035598103, 0.0070463372, 0.026794046, 0.015371065, -0.0539309, -0.0070718178, 0.021605283, -0.02545024, 0.018716574, -0.012023479, -0.0034939465, -0.03127053, -0.009451723, 0.0051453314, -0.0032126089, 0.07967532, 0.015575548, -0.021494783, -0.038867254, 0.045997743, -0.035418816, 0.020550694, 0.00067626976, -0.029028593, 0.031141229, 0.06178766, -0.013372712, 0.0033935523, -0.012997967, 0.041284867, -0.036677353, 0.0032814778, -0.034898203, -0.043582983, -0.01787388, 0.05014199, 0.040672254, -0.024764268, 0.0011869374, -0.03481051, -0.012193091, 0.064988196, 0.00083080254, 0.034979027, -0.03806379, 0.06518041, 0.05123647, -0.04649555, -0.032182634, -0.021728221, -0.010576436, 0.069672346, -0.0011587434, 0.014949285, -0.014542972, -0.07958443, -0.07930639, 0.059933573, 0.007296851, 0.014224586, 0.035097294, -0.02258584, -0.00768257, -0.019851163, 0.03540128, -0.05277329, -0.024353035, 0.0026542991, 0.019587073, 0.015392462, 0.055494, -0.049620625, 0.028806835, -0.031015808, -0.018006735, 0.0048832977, 0.0017269496, 0.055692136, -0.00065769756, -0.018113874, 0.016523749, -0.0070332247, -0.06178115, 0.014642825]}

```

## OAuth Shenanigans

In order to send a call to the GenerativeServicesClient for a semantic retrieval call, you need an OAuth token set up. I don't really know what this means, but I used my Google Cloud Platform account to create one using the instructions in this Colab notebook. [https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/docs/semantic_retriever.ipynb#scrollTo=P719DMtK8t-p](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/docs/semantic_retriever.ipynb#scrollTo=P719DMtK8t-p)

I'm not super familiar with this, but I used GCP to create the OAuth Service Account, then from that Service Account, generate a Key, which is downloaded as a JSON file, then uploaded to the Colab notebook and used authenticate the Semantic Retriever request.

We will require this OAuth setup to use the semantic retrieval and complete the AQA "Attributed Question Answering" API call. If you don't want to mess with that model, you can skip these steps.

```
!pip install -U google-auth-oauthlib

```

```
# Rename the uploaded file to `service_account_secret.json` OR
# Change the variable `service_account_file_name` in the code below.
service_account_file_name = '/content/gen-lang-client-0086316029-a94fc89b076e.json'

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(service_account_file_name)

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/generative-language.retriever'])

```

```
generative_service_client = glm.GenerativeServiceClient(credentials=scoped_credentials)
retriever_service_client = glm.RetrieverServiceClient(credentials=scoped_credentials)
permission_service_client = glm.PermissionServiceClient(credentials=scoped_credentials)

```

## Helper functions for processing PDFs

The following functions are used to load and partition PDFs. There's separate loaders depending on whether you are using a local file, or a URL to a PDF online.

```
#utility functions. yes, this is OpenAI's tokenizer. No, Google doesn't seem to provide one.
def tiktoken_len(text, base='cl100k_base'):
  tokenizer = tiktoken.get_encoding(base)
  tokens = tokenizer.encode(
      text,
      disallowed_special=()
  )
return len(tokens)

def doc_loader(file_path):
    loader = UnstructuredPDFLoader(file_path)
    loader_doc = loader.load()
    doc_content = loader_doc[0].page_content[:]
    doc_tokens = tiktoken_len(doc_content)
    doc_name = doc_name = file_path.split('/')[-1]  # Get the name of the document

return loader_doc, doc_content, doc_tokens, doc_name

def online_pdf_loader(url):
    loader = OnlinePDFLoader(url)
    loader_doc = loader.load()
    doc_content = loader_doc[0].page_content[:]
    doc_tokens = tiktoken_len(doc_content)
    doc_name = url.split('/')[-1]
return loader_doc, doc_content, doc_tokens, doc_name

def text_splitter(doc, max_tokens=600, overlap_tokens=50):
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size = int(max_tokens), #chunk_s, # number of units per chunk
      chunk_overlap = int(overlap_tokens), # number of units of overlap
      length_function = tiktoken_len, #use tokens as chunking unit instead of characters.
      separators=['\n\n', '\n', ' '] # our chosen operators for separating
      )
  texts = text_splitter.split_text(doc)
return texts

def chunks_from_file(pdf, max_tokens, overlap_tokens):
  loader_doc, doc_content, doc_tokens, doc_name = doc_loader(pdf)
  chunks = text_splitter(doc_content, max_tokens, overlap_tokens)
return chunks, doc_name

def chunks_from_url(url, max_tokens, overlap_tokens):
  loader_doc, doc_content, doc_tokens, doc_name = online_pdf_loader(url)
  chunks = text_splitter(doc_content, max_tokens, overlap_tokens)
return chunks, doc_name

```

## Add user-defined info here.

❗️ If you are uploading a PDF file, then update the path string for `my_pdf`. Click on the Folder icon on the left-hand edge of the screen, and drag your PDF into the side-panel. The, right-click on the name of the doc and choose "copy path" to get the location of your doc. Paste the result below.

❗️ If you are using a URL to a PDF, then paste your URL in the quotes after `my_url` and the OnlinePDFLoader will download the PDF and process it for chunking.

You can configure chunk size here for the embeddings as well. I am recommending 600 token chunks because the current beta state of Google Semantic Retriever recommends token lengths around 300. I think that's too short for legal RAG, so I'm trying to be reasonable by limiting our chunks to 2x that value.

However, if you are not using Semantic Retriever and/or want to test something specific, you can modify your chunk parameters here.

```
# Enter arguments for your Document embedding
# This notebook is written assuming you will either upload a file OR provide a URL, but not both.

my_pdf = "/content/Caniglia v. Strom 2021 Opinion.pdf"
my_url = "https://www.supremecourt.gov/opinions/22pdf/21-869_87ad.pdf"

max_tokens = 600
overlap_tokens = 50

```

### If you uploaded a file, run this cell

```
# @title If you uploaded a file, run this cell
chunks, doc_name = chunks_from_file(my_pdf, max_tokens, overlap_tokens)

```

### If you are using a pdf URL, run this cell

```
# @title If you are using a pdf URL, run this cell
chunks, doc_name = chunks_from_url(my_url, max_tokens, overlap_tokens)

```

## Building an embeddings database

Let's take a look at a few of these Chunks. You will use the Gemini API to create embeddings of each of the documents. Turn them into a dataframe for better visualization.

Also, the chunking operation also extracts a value for doc_name, which is just the name of the document from the file or URL. Since this value is used as the `title` parameter for the embeddings-001 model, we might want to take a moment to add a more descriptive title now.

If the name of your file wasn't terribly descriptive, add a more descriptive one below. Again, the documentation doesn't indicate what this title does, so not sure what to expect. If it is used as metadata, or if some portion of the embedding space is reserved for document title.

```
# Look at a chunk or two
chunks[0:1]

```

```
['(Slip Opinion)\n\nOCTOBER TERM, 2022\n\nSyllabus\n\nNOTE: Where it is feasible, a syllabus (headnote) will be released, as is being done in connection with this case, at the time the opinion is issued. The syllabus constitutes no part of the opinion of the Court but has been prepared by the Reporter of Decisions for the convenience of the reader. See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.\n\nSUPREME COURT OF THE UNITED STATES\n\nSyllabus\n\nANDY WARHOL FOUNDATION FOR THE VISUAL ARTS, INC. v. GOLDSMITH ET AL.\n\nCERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT\n\nNo. 21–869. Argued October 12, 2022—Decided May 18, 2023']
```

```
# Provide a better document title for embeddings, if you want.
doc_name = "(better title)"

```

Organize the contents of the dictionary into a dataframe for better visualization.

## These functions build our local "vector database"

The first function is the Google AI sample function for getting an embedding vector using the Gemini family "embeddings-001" model. I'm being a bit redundant here in requiring a `model` argument, given that there's only one embedding model currently available on Google AI Studio.

Below, we are creating a dataframe consisting of our original chunks, then adding a column for embedding vectors, and aqa_ids to use later. Our code is processing the dataframe row-by-row, meaning the embeddings are being processed one at a time. If your PDF was extremely long, and you have many hundreds, or thousands, of chunks then this step may take a few minutes. Ordinarily, you can batch embedding requests to send 30-100 at once, subject to the rate limits of the provider.

```
# Get the embeddings of each text and add to an embeddings column in the dataframe
def get_embedding(chunk, doc_name, model="models/embedding-001"):
# title field is optional.
return genai.embed_content(model=model,
                             content=chunk,
                             task_type="retrieval_document",
                             title=doc_name)["embedding"]

def embed_to_dataframe(chunks, doc_name, model):
# Create the dataframe
    df = pd.DataFrame(chunks, columns=['Docs'])

# Apply the embed_fn function to each row in the 'Docs' column
    df['Embeddings'] = df['Docs'].apply(lambda x: get_embedding(x, doc_name, model))

# Add aqa_id column
    df['aqa_id'] = df.index.map(lambda x: '{0:03d}'.format(x))

return df

```

```
#this step creates the embeddings
model = 'models/embedding-001'
df = embed_to_dataframe(chunks, doc_name, model)

```

Now we can take a peek at our completed Knowledge base, which is a pandas dataframe with a "Docs" column for text chunks, "Embeddings" from the Gemini `embeddings-001`, which appear to be 768 dimensional vector blobs of numbers, and then `aqa_id` values which we will use for inline grounding passages for our Semantic Retrieval with Attributed Question Answering.

```
df

```

Use the `retrieve docs` function to calculate the dot products, and then sort the dataframe from the largest to smallest dot product value to retrieve the relevant passages out of the database.

I modified this function to accept a top_k parameter, then, at the bottom of each returned Doc text, I'm appending a "Source Ref" string consisting of the Doc name and the dataframe index, mostly as an experiment to see how well the LLM utilizes in-context source data (spoiler: in general it doesn't work that well). Remember that this is being injected into the returned doc text, and not part of the vectors themselves.

```
#modified function to take a top_k parameter, perform a sort function on the dataframe, and return the top_k results as a list
#modified to include a "Source" attribution based on the dataframe indices pre-argsort
def retrieve_docs(query, dataframe, top_k):
"""
    Compute the dot product similarities between the query and each document in the dataframe,
    and return the top_k best matches with original DataFrame indices.
    """
# Generate the embedding for the query
    query_embedding = genai.embed_content(model='models/embedding-001',
                                          content=query,
                                          task_type="retrieval_query")

# Compute dot products
    dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])

# Get original indices and sort by dot product values
    sorted_indices = np.argsort(dot_products)[::-1]
    original_indices = dataframe.index[sorted_indices]

return original_indices[:top_k]

# Format and return the corresponding texts with original indices
def docs_with_sources(query, dataframe, top_k=3):
    rag_docs = retrieve_docs(query, dataframe, top_k)
    top_k_docs = []
for idx in rag_docs:
        document = dataframe.loc[idx, 'Docs']
        source_ref = f"\n\n(Source: {doc_name} #{idx})"
        top_k_docs.append(document + source_ref)

return top_k_docs

```

```
#Now let's ask a question for our retrieval function
query = "How does transformative use factor into the court's fair use analysis?"

```

```
#Try a few different questions and see how the retrieved docs change.
rag_docs = docs_with_sources(query, df, 3)
for doc in rag_docs:
print(doc, "\n\n")

```

## Question and Answering Application

Let's try to use the text generation API to create a Q & A system. Input your own custom data below to create a simple question and answering example. You will still use the dot product as a metric of similarity.

I'm not in love with this prompt, but this is the suggested format from the Google AI folks. I've adjusted it slightly for tone suitable for a legal audience, but modify this as you see fit, and see how it changes Gemini's answer style.

This function formats and composes the retrieved rag_docs into a prompt suitable for Gemini Pro. This giant string blob that ends with a "\n\nDelimiter" seems awfully familiar. Now what other model uses this format? Oh, right, Anthropic Claude. *Very interesting* to see that they've configured the Google AI studio endpoint to behave this way...

# 🤔

```
def make_prompt(query, rag_docs):
"""
    Create a prompt using the query and a list of relevant passages.
    """
# Escape and format each passage, then join them into a single string
    formatted_passages = " ".join([passage.replace("'", "").replace('"', "").replace("\n", " ") for passage in rag_docs])

    prompt = textwrap.dedent("""\
    You are a helpful and informative bot that answers questions using text from the reference passages included below. \
    Provide a detailed report, being comprehensive, including all relevant background information. \
    Your audience is legal professionals and analysts who need in-depth, details legal analysis and answers \
    So provide competent, accurate answers with "Source" attribution whenever possible \
    If some information in the passages are irrelevant to the answer, you may ignore them. \
    Begin your answer by restating the question, then providing your answer after. \
    QUESTION: '{query}'
    PASSAGES: '{formatted_passages}'

    ANSWER:
    """).format(query=query, formatted_passages=formatted_passages)

return prompt

```

```
#take a look at the prompt results here
prompt = make_prompt(query, rag_docs)
prompt

```

## Let's do some class assignments to set up the LLM calls

For more information regarding Google's LLM parameters, look at their documentation here: [https://ai.google.dev/api/python/google/generativeai/GenerationConfig](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fai.google.dev%2Fapi%2Fpython%2Fgoogle%2Fgenerativeai%2FGenerationConfig)

The first cell is just showing us the Gemini Pro information from the SDK. Next, we are defining `config` and `model` to set the values we will use for our API call.

The line including `answer = model.generate_content()` is sending off the API request to Gemini Pro.

```
#first, let's just take a look at the specs and default config values for Gemini Pro
my_model = genai.get_model('models/gemini-pro')
print(my_model)

```

```
Model(name='models/gemini-pro',
      base_model_id='',
      version='001',
      display_name='Gemini Pro',
      description='The best model for scaling across a wide range of tasks',
      input_token_limit=30720,
      output_token_limit=2048,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=0.9,
      top_p=1.0,
      top_k=1)

```

```
config = genai.GenerationConfig(
    candidate_count = 1,
    stop_sequences = None,
    max_output_tokens = 1200,
    temperature = 0,
    top_p = 1.0,
    top_k = 1
    )
model = genai.GenerativeModel(
    model_name = 'gemini-pro',
    generation_config = config)

```

```
answer = model.generate_content(prompt)
Markdown(answer.text)

```

Let's wrap the RAG retrieval, Prompt formatting, and LLM Call into a single function so that it's a bit easier to work with. I've also just exploded the entire config parameter set according to the documentation in case you want to tweak a value, or change which arguments the function takes.

```
def gemini_rag_answer(query, top_k, model='gemini-pro', temperature=0, max_tokens=1200):
    rag_docs = docs_with_sources(query, df, top_k)
    prompt = make_prompt(query,rag_docs)
    config = genai.GenerationConfig(
        candidate_count = 1,
        stop_sequences = None,
        max_output_tokens = max_tokens,
        temperature = temperature,
        top_p = 1.0,
        top_k = 1
        )
    model = genai.GenerativeModel(
        model_name = model,
        generation_config = config)

return model.generate_content(prompt)

```

Now, test out the rag pipeline with a few different questions/answers. I've configured the function to take a query argument and top_k. The remainder will autofill with reasonable defaults. The function also returns the entire answer object in case you want to poke at it further.

Try modifying top_k to see when answers get better, or worse. The function above doesn't have any guardrails around context length, so even though Gemini Pro has a ~30,000 input token limit (about 50 docs if you used my recommended chunk size of 600), at some point, the calls will error out due to context length limits. You will probably see that answer quality stops improving long before then.

```
my_question = "From the analysis of Campbell v. Acuff Music, how did the opinion distinguish parody from satire?"

```

```
the_answer = gemini_rag_answer(my_question, 2)
Markdown(the_answer.text)

```

## We can go further! Semantic Retrieval and Attributed Question Answering!

Google released this with Gemini, too! Details are sparse on Semantic Retriever, and it doesn't appear that the API documentation is yet available (at the time of this writing). It appears to be a hybrid Embeddings+Retrieval platform that work together to produce "Attributed Question Answering".

My understanding is something like this (I might be wrong): You can set up several document stores consisting of 10,000 documents each, with 20 fields of custom metadata. They are presumably vectorized and indexed. Then, you can send a Query, and get grounding passages returned. The grounding passages are given to a specialized LLM API endpoint called `aqa`, which returns a special response object that contains:

- A generated answer
- The most relevant document
- An `answerable_probability` value corresponding to the estimated confidence that the passage actually answers the question.

I am not setting up a doc store here today, but Semantic Query and Attributed Question Answering can also be used with "inline passages", which are a sequence of docs being sent to the API for evaluation. The model will similarly produce an answer based on the most relevant doc, and return it, as well as the confidence score.

```
#reuses our Pandas dataframe to construct "inline grounding passages" for the AQA model
def get_inline_passages(query, dataframe, top_k=1):
"""
    Compute the dot product similarities between the query and each document in the dataframe,
    and return the top_k best matches with original DataFrame indices.
    """
    top_k_original_indices = retrieve_docs(query, dataframe, top_k)

    grounding_passages = glm.GroundingPassages()
for idx in top_k_original_indices:
      passage_bit = glm.Content(parts=[glm.Part(text=dataframe.loc[idx, 'Docs'])])
      id_bit = dataframe.loc[idx, 'aqa_id']
      grounding_passages.passages.append(glm.GroundingPassage(content=passage_bit, id=id_bit))

return grounding_passages

def aqa_model_call(query, inline_passages):
  query_content = glm.Content(parts=[glm.Part(text=query)])
  req = glm.GenerateAnswerRequest(model='models/aqa',
                                  contents=[query_content],
                                  inline_passages=inline_passages,
#answer_styles to try are 'ABSTRACTIVE', 'VERBOSE', 'EXTRACTIVE'
                                  answer_style='VERBOSE')
  aqa_response = generative_service_client.generate_answer(req)
return aqa_response

def aqa_query(query, dataframe, top_k=3):
  grounding_passages = get_inline_passages(query, dataframe, top_k)
  get_answer = aqa_model_call(query, grounding_passages)
return get_answer

```

The AQA Model is included in the Gemini family, but it's a special purpose model that's not intended for text generation, or chat. More significantly for us is that it has an input token limit of around 7000, meaning that the maximum top_k value before you are exceeding the token limit should be around 11.

```
answer {
  content {
    parts {
      text: "Andy Warhol was a famous American artist who is known for his work in pop art. He used silkscreens to create his paintings, which often depicted celebrities and everyday objects. Warhol was also a pioneer in the use of appropriation, which is the act of taking an existing image and using it as the basis for a new work of art. Some of Warhol\'s most famous works include the Campbell\'s Soup Cans series, the Marilyn Monroe series, and the Elvis Presley series."
    }
  }
  finish_reason: STOP
  grounding_attributions {
    content {
      parts {
        text: "3\n\n4\n\nANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH KAGAN, J., dissenting\n\nundermines creative freedom. I respectfully dissent.2\n\nI A\n\nAndy Warhol is the avatar of transformative copying. Cf. Google, 593 U. S., at ___\342\200\223___ (slip op., at 24\342\200\22325) (selecting Warhol, from the universe of creators, to illustrate what transformative copying is). In his early career, Warhol worked as a commercial illustrator and became experienced in varied techniques of reproduction. By night, he used those techniques\342\200\224in particular, the silkscreen\342\200\224to create his own art. His own\342\200\224even though in one sense not. The silkscreen enabled him to make brilliantly novel art out of existing \342\200\234images carefully selected from popular culture.\342\200\235 D. De Salvo, God Is in the Details, in Andy Warhol Prints 22 (4th rev. ed. 2003). The works he produced, connecting traditions of fine art with mass culture, depended on \342\200\234ap- propriation[s]\342\200\235: The use of \342\200\234elements of an extant image[ ] is Warhol\342\200\231s entire modus operandi.\342\200\235 B. Gopnik, Artistic Ap- propriation vs. Copyright Law, N. Y. Times, Apr. 6, 2021, p. C4 (internal quotation marks omitted). And with that m.o., he changed modern art; his appropriations and his originality were flipsides of each other. To a public accus- tomed to thinking of art as formal works \342\200\234belong[ing] in\n\n\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224\n\n2 One preliminary note before beginning in earnest. As readers are by now aware, the majority opinion is trained on this dissent in a way ma- jority opinions seldom are. Maybe that makes the majority opinion self- refuting? After all, a dissent with \342\200\234no theory\342\200\235 and \342\200\234[n]o reason\342\200\235 is not one usually thought to merit pages of commentary and fistfuls of come- back footnotes. Ante, at 36. In any event, I\342\200\231ll not attempt to rebut point for point the majority\342\200\231s varied accusations; instead, I\342\200\231ll mainly rest on my original submission. I\342\200\231ll just make two suggestions about reading what follows. First, when you see that my description of a precedent differs from the majority\342\200\231s, go take a look at the decision. Second, when you come across an argument that you recall the majority took issue with, go back to its response and ask yourself about the ratio of reasoning to ipse dixit. With those two recommendations, I\342\200\231ll take my chances on readers\342\200\231 good judgment.\n\nCite as: 598 U. S. ____ (2023)\n\nKAGAN, J., dissenting"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "054"
      }
    }
  }
  grounding_attributions {
    content {
      parts {
        text: "Cite as: 598 U. S. ____ (2023)\n\nKAGAN, J., dissenting\n\ngold frames\342\200\235\342\200\224disconnected from the everyday world of products and personalities\342\200\224Warhol\342\200\231s paintings landed like a thunderclap. A. Danto, Andy Warhol 36 (2009). Think Soup Cans or, in another vein, think Elvis. Warhol had cre- ated \342\200\234something very new\342\200\235\342\200\224\342\200\234shockingly important, trans- formative art.\342\200\235 B. Gopnik, Warhol 138 (2020); Gopnik, Ar- tistic Appropriation.\n\nTo see the method in action, consider one of Warhol\342\200\231s pre- Prince celebrity silkscreens\342\200\224this one, of Marilyn Monroe. He began with a publicity photograph of the actress. And then he went to work. He reframed the image, zooming in on Monroe\342\200\231s face to \342\200\234produc[e] the disembodied effect of a cinematic close-up.\342\200\235 1 App. 161 (expert declaration).\n\nAt that point, he produced a high-contrast, flattened image on a sheet of clear acetate. He used that image to trace an outline on the canvas. And he painted on top\342\200\224applying ex- otic colors with \342\200\234a flat, even consistency and an industrial appearance.\342\200\235 Id., at 165. The same high-contrast image was then reproduced in negative on a silkscreen, designed\n\n5\n\n6\n\nANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH KAGAN, J., dissenting\n\nto function as a selectively porous mesh. Warhol would \342\200\234place the screen face down on the canvas, pour ink onto the back of the mesh, and use a squeegee to pull the ink through the weave and onto the canvas.\342\200\235 Id., at 164. On some of his Marilyns (there are many), he reordered the process\342\200\224first ink, then color, then (perhaps) ink again. See id., at 165\342\200\223 166. The result\342\200\224see for yourself\342\200\224is miles away from a lit- eral copy of the publicity photo.\n\nAndy Warhol, Marilyn, 1964, acrylic and silkscreen ink on linen\n\nAnd the meaning is different from any the photo had. Of course, meaning in great art is contestable and contested (as is the premise that an artwork is great). But note what some experts say about the complex message(s) Warhol\342\200\231s Marilyns convey. On one level, those vivid, larger-than-life paintings are celebrity iconography, making a \342\200\234secular, pro- fane subject[ ]\342\200\235 \342\200\234transcendent\342\200\235 and \342\200\234eternal.\342\200\235 Id., at 209 (in- ternal quotation marks omitted). But they also function as a biting critique of the cult of celebrity, and the role it plays"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "055"
      }
    }
  }
  grounding_attributions {
    content {
      parts {
        text: "Cite as: 598 U. S. ____ (2023)\n\nKAGAN, J., dissenting\n\nin American life. With misaligned, \342\200\234Day-Glo\342\200\235 colors sug- gesting \342\200\234artificiality and industrial production,\342\200\235 Warhol portrayed the actress as a \342\200\234consumer product.\342\200\235 The Metro- politan Museum of Art Guide 233 (2012); The Metropolitan Museum of Art, Marilyn (2023) (online source archived athttps://www.supremecourt.gov). And in so doing, he \342\200\234ex- posed the deficiencies\342\200\235 of a \342\200\234mass-media culture\342\200\235 in which \342\200\234such superficial icons loom so large.\342\200\235 1 App. 208, 210 (in- ternal quotation marks omitted). Out of a publicity photo came both memorable portraiture and pointed social com- mentary.\n\nAs with Marilyn, similarly with Prince. In 1984, Vanity Fair commissioned Warhol to create a portrait based on a black-and-white photograph taken by noted photographer Lynn Goldsmith:\n\nAs he did in the Marilyn series, Warhol cropped the photo, so that Prince\342\200\231s head fills the whole frame: It thus becomes \342\200\234disembodied,\342\200\235 as if \342\200\234magically suspended in space.\342\200\235 Id., at\n\n7\n\n8\n\nANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH KAGAN, J., dissenting\n\n174. And as before, Warhol converted the cropped photo into a higher-contrast image, incorporated into a silkscreen. That image isolated and exaggerated the darkest details of Prince\342\200\231s head; it also reduced his \342\200\234natural, angled position,\342\200\235 presenting him in a more face-forward way. Id., at 223. Warhol traced, painted, and inked, as earlier described. See supra, at 5\342\200\2236. He also made a second silkscreen, based on his tracings; the ink he passed through that screen left differently colored, out-of-kilter lines around Prince\342\200\231s face and hair (a bit hard to see in the reproduction below\342\200\224more pronounced in the original). Altogether, Warhol made 14 prints and two drawings\342\200\224the Prince series\342\200\224in a range of unnatural, lurid hues. See Appendix, ante, at 39. Vanity Fair chose the Purple Prince to accompany an article on the musician. Thirty-two years later, just after Prince died, Cond\303\251 Nast paid Warhol (now actually his foundation, see supra, at 1, n. 1) to use the Orange Prince on the cover of a special commemorative magazine. A picture (or two), as the saying goes, is worth a thousand words, so here is what those magazines published:\n\nAndy Warhol, Prince, 1984, synthetic paint and silkscreen ink on canvas\n\nCite as: 598 U. S. ____ (2023)\n\nKAGAN, J., dissenting"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "056"
      }
    }
  }
}
answerable_probability: 1.0
```

```
answer {
  content {
    parts {
      text: "The court discussed Campbell\342\200\231s Soup Cans to illustrate the difference between transformative and non-transformative uses. Campbell\342\200\231s use of the Campbell\342\200\231s Soup can was transformative because it used the image of the soup can to create a new work of art that commented on consumerism. In contrast, the Warhol Foundation\342\200\231s use of Goldsmith\342\200\231s photograph of Prince was not transformative because it did not create a new work of art. The Warhol Foundation simply copied Goldsmith\342\200\231s photograph and added some new colors and shapes."
    }
  }
  finish_reason: STOP
  grounding_attributions {
    content {
      parts {
        text: "The Court\342\200\231s decision in Campbell is instructive. In holding that par- ody may be fair use, the Court explained that \342\200\234parody has an obvious claim to transformative value\342\200\235 because \342\200\234it can provide social benefit, by shedding light on an earlier work, and, in the process, creating a new one.\342\200\235 510 U. S., at 579. The use at issue was 2 Live Crew\342\200\231s copy- ing of Roy Orbison\342\200\231s song, \342\200\234Oh, Pretty Woman,\342\200\235 to create a rap deriva- tive, \342\200\234Pretty Woman.\342\200\235 2 Live Crew transformed Orbison\342\200\231s song by add- ing new lyrics and musical elements, such that \342\200\234Pretty Woman\342\200\235 had a different message and aesthetic than \342\200\234Oh, Pretty Woman.\342\200\235 But that did not end the Court\342\200\231s analysis of the first fair use factor. The Court found it necessary to determine whether 2 Live Crew\342\200\231s transformation rose to the level of parody, a distinct purpose of commenting on the original or criticizing it. Further distinguishing between parody and satire, the Court explained that \342\200\234[p]arody needs to mimic an original to make its point, and so has some claim to use the creation of its vic- tim\342\200\231s (or collective victims\342\200\231) imagination, whereas satire can stand on its own two feet and so requires justification for the very act of borrow- ing.\342\200\235 Id., at 580\342\200\223581. More generally, when \342\200\234commentary has no crit- ical bearing on the substance or style of the original composition, . . . the claim to fairness in borrowing from another\342\200\231s work diminishes ac- cordingly (if it does not vanish), and other factors, like the extent of its commerciality, loom larger.\342\200\235 Id., at 580.\n\nCampbell illustrates two important points. First, the fact that a use is commercial as opposed to nonprofit is an additional element of the first fair use factor. The commercial nature of a use is relevant, but not dispositive. It is to be weighed against the degree to which the use\n\n3\n\n4\n\nANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH Syllabus"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "005"
      }
    }
  }
  grounding_attributions {
    content {
      parts {
        text: "25\n\n26 ANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC.\n\nv. GOLDSMITH Opinion of the Court\n\nuses. In Google, the Court suggested that \342\200\234[a]n \342\200\230artistic painting\342\200\231 might, for example, fall within the scope of fair use even though it precisely replicates a copyrighted \342\200\230adver- tising logo to make a comment about consumerism.\342\200\231 \342\200\235 593 U. S., at ___\342\200\223___ (slip op., at 24\342\200\22325) (quoting 4 M. Nimmer & D. Nimmer, Copyright \302\24713.05[A][1][b] (2019), in turn quoting N. Netanel, Making Sense of Fair Use, 15 Lewis & Clark L. Rev. 715, 746 (2011) (some internal quotation marks omitted)). That suggestion refers to Warhol\342\200\231s works that incorporate advertising logos, such as the Campbell\342\200\231s Soup Cans series. See fig. 7, infra.\n\nYet not all of Warhol\342\200\231s works, nor all uses of them, give rise to the same fair use analysis. In fact, Soup Cans well illustrates the distinction drawn here. The purpose of Campbell\342\200\231s logo is to advertise soup. Warhol\342\200\231s canvases do\n\nFigure 7. A print based on the Campbell\342\200\231s soup can, one of Warhol\342\200\231s works that replicates a copyrighted advertising logo.\n\nCite as: 598 U. S. ____ (2023)\n\nOpinion of the Court\n\nnot share that purpose. Rather, the Soup Cans series uses Campbell\342\200\231s copyrighted work for an artistic commentary on consumerism, a purpose that is orthogonal to advertising soup. The use therefore does not supersede the objects of the advertising logo.15\n\nMoreover, a further justification for Warhol\342\200\231s use of Campbell\342\200\231s logo is apparent. His Soup Cans series targets the logo. That is, the original copyrighted work is, at least in part, the object of Warhol\342\200\231s commentary. It is the very nature of Campbell\342\200\231s copyrighted logo\342\200\224well known to the public, designed to be reproduced, and a symbol of an every- day item for mass consumption\342\200\224that enables the commen- tary. Hence, the use of the copyrighted work not only serves a completely different purpose, to comment on consumer- ism rather than to advertise soup, it also \342\200\234conjures up\342\200\235 the original work to \342\200\234she[d] light\342\200\235 on the work itself, not just the subject of the work. Campbell, 510 U. S., at 579, 588.16 Here, by contrast, AWF\342\200\231s use of Goldsmith\342\200\231s photograph does not target the photograph, nor has AWF offered an- other compelling justification for the use. See infra, at 34\342\200\223 35, and nn. 20\342\200\22321.\n\n\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "031"
      }
    }
  }
  grounding_attributions {
    content {
      parts {
        text: "\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224\342\200\224\n\n15 The situation might be different if AWF licensed Warhol\342\200\231s Soup Cans to a soup business to serve as its logo. That use would share much the same purpose of Campbell\342\200\231s logo, even though Soup Cans has some new meaning or message. This hypothetical, though fanciful, is parallel to the situation here: Both Goldsmith and AWF sold images of Prince (AWF\342\200\231s copying Goldsmith\342\200\231s) to magazines to illustrate stories about the celebrity, which is the typical use made of Goldsmith\342\200\231s photographs.\n\n16 The dissent either does not follow, or chooses to ignore, this analysis. The point is not simply that the Soup Cans series comments on consumer culture, similar to how Warhol\342\200\231s celebrity images comment on celebrity culture. Post, at 15 (opinion of KAGAN, J.). Rather, as the discussion makes clear, the degree of difference in purpose and character between Campbell\342\200\231s soup label and Warhol\342\200\231s painting is nearly absolute. Plus, Warhol\342\200\231s use targets Campbell\342\200\231s logo, at least in part. These features (which are absent in this case) strengthen Warhol\342\200\231s claim to fairness in copying that logo in a painting.\n\n27\n\n28 ANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC.\n\nv. GOLDSMITH Opinion of the Court\n\nB\n\nAWF contends, however, that the purpose and character of its use of Goldsmith\342\200\231s photograph weighs in favor of fair use because Warhol\342\200\231s silkscreen image of the photograph, like the Campbell\342\200\231s Soup Cans series, has a new meaning or message. The District Court, for example, understood the Prince Series works to portray Prince as \342\200\234an iconic, larger-than-life figure.\342\200\235 382 F. Supp. 3d, at 326. AWF also asserts that the works are a comment on celebrity. In par- ticular, \342\200\234Warhol\342\200\231s Prince Series conveys the dehumanizing nature of celebrity.\342\200\235 Brief for Petitioner 44. According to AWF, that new meaning or message, which the Court of Ap- peals ignored, makes the use \342\200\234transformative\342\200\235 in the fair use sense. See id., at 44\342\200\22348. We disagree.\n\n1"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "032"
      }
    }
  }
}
answerable_probability: 1.0
```

```
answer {
  content {
    parts {
      text: "**No, the court did not specifically address trademark fair use in its opinion.** However, the court did discuss the concept of fair use in general, and its decision in this case appears to be consistent with the principles of trademark fair use.\n\nUnder trademark law, fair use allows for the use of trademarks in certain circumstances, such as for parody, criticism, or news reporting. In order for a use to be considered fair, it must be transformative, meaning that it must add something new to the original work and not simply be a copy of it. The use must also be non-commercial or only minimally commercial.\n\nIn the case of Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith, the court found that the Andy Warhol Foundation\'s use of Goldsmith\'s photograph was not fair use. The court reasoned that the Foundation\'s use of the photograph was commercial and that it did not add anything new to the original work."
    }
  }
  finish_reason: STOP
  grounding_attributions {
    content {
      parts {
        text: "The Court\342\200\231s decision in Campbell is instructive. In holding that par- ody may be fair use, the Court explained that \342\200\234parody has an obvious claim to transformative value\342\200\235 because \342\200\234it can provide social benefit, by shedding light on an earlier work, and, in the process, creating a new one.\342\200\235 510 U. S., at 579. The use at issue was 2 Live Crew\342\200\231s copy- ing of Roy Orbison\342\200\231s song, \342\200\234Oh, Pretty Woman,\342\200\235 to create a rap deriva- tive, \342\200\234Pretty Woman.\342\200\235 2 Live Crew transformed Orbison\342\200\231s song by add- ing new lyrics and musical elements, such that \342\200\234Pretty Woman\342\200\235 had a different message and aesthetic than \342\200\234Oh, Pretty Woman.\342\200\235 But that did not end the Court\342\200\231s analysis of the first fair use factor. The Court found it necessary to determine whether 2 Live Crew\342\200\231s transformation rose to the level of parody, a distinct purpose of commenting on the original or criticizing it. Further distinguishing between parody and satire, the Court explained that \342\200\234[p]arody needs to mimic an original to make its point, and so has some claim to use the creation of its vic- tim\342\200\231s (or collective victims\342\200\231) imagination, whereas satire can stand on its own two feet and so requires justification for the very act of borrow- ing.\342\200\235 Id., at 580\342\200\223581. More generally, when \342\200\234commentary has no crit- ical bearing on the substance or style of the original composition, . . . the claim to fairness in borrowing from another\342\200\231s work diminishes ac- cordingly (if it does not vanish), and other factors, like the extent of its commerciality, loom larger.\342\200\235 Id., at 580.\n\nCampbell illustrates two important points. First, the fact that a use is commercial as opposed to nonprofit is an additional element of the first fair use factor. The commercial nature of a use is relevant, but not dispositive. It is to be weighed against the degree to which the use\n\n3\n\n4\n\nANDY WARHOL FOUNDATION FOR VISUAL ARTS, INC. v. GOLDSMITH Syllabus"
      }
    }
    source_id {
      grounding_passage {
        passage_id: "005"
      }
    }
  }
  grounding_attributions {
    content {
      parts {
        text: "21 The dissent wonders: Why does targeting matter? See post, at 24 (opinion of KAGAN, J.). The reason, as this opinion explains, is the first factor\342\200\231s attention to justification. Supra, at 17\342\200\22320, and nn. 7\342\200\2238, 29\342\200\22330, and n. 18 (citing Campbell, 510 U. S., at 580\342\200\223581; Google, 593 U. S., at ___ (slip op., at 26)). Compare, for example, a film adaptation of Gone With the Wind with a novel, The Wind Done Gone, that \342\200\234inverts\342\200\235 the original\342\200\231s \342\200\234portrait of race relations\342\200\235 to expose its \342\200\234romantic, idealized\342\200\235 portrayal of the antebellum South. SunTrust Bank v. Houghton Mifflin Co., 268 F. 3d 1257, 1270 (CA11 2001); id., at 1280 (Marcus, J., specially concurring). Or, to build from one of the artistic works the dissent chooses to feature, consider a secondary use that borrows from Manet\342\200\231s Olympia to shed light on the original\342\200\231s depiction of race and sex. See R. Storr & C. Armstrong, Lunch With Olympia (2016). Although targeting is not always required, fair use is an affirmative defense, and AWF bears the burden to justify its taking of Goldsmith\342\200\231s work with some reason other than, \342\200\234I can make it better.\342\200\235\n\nCite as: 598 U. S. ____ (2023)\n\nOpinion of the Court\n\nHere, the circumstances of AWF\342\200\231s 2016 licensing out- weigh its diminished claim to fairness in copying under the first factor. Like satire that does not target an original work, AWF\342\200\231s asserted commentary \342\200\234can stand on its own two feet and so requires justification for the very act of bor- rowing.\342\200\235 Id., at 581. Moreover, because AWF\342\200\231s commercial use of Goldsmith\342\200\231s photograph to illustrate a magazine about Prince is so similar to the photograph\342\200\231s typical use, a particularly compelling justification is needed. Yet AWF offers no independent justification, let alone a compelling one, for copying the photograph, other than to convey a new meaning or message. As explained, that alone is not enough for the first factor to favor fair use."
      }
    }
    source_id {
      grounding_passage {
        passage_id: "040"
      }
    }
  }
}
answerable_probability: 0.4072054326534271
```