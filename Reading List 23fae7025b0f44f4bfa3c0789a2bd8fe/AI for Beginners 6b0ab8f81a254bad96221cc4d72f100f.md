# AI for Beginners

Column: https://microsoft.github.io/AI-For-Beginners/
Processed: No
created on: December 7, 2023 10:10 AM

![](AI%20for%20Beginners%206b0ab8f81a254bad96221cc4d72f100f/ai-overview.png)

Sketchnote by [(@girlie_mac)](https://twitter.com/girlie_mac)

---

Explore the world of **Artificial Intelligence** (AI) with Microsoft's 12-week, 24-lesson curriculum! Dive into Symbolic AI, Neural Networks, Computer Vision, Natural Language Processing, and more. Hands-on lessons, quizzes, and labs enhance your learning. Perfect for beginners, this comprehensive guide, designed by experts, covers TensorFlow, PyTorch, and ethical AI principles. Start your AI journey today!"

In this curriculum, you will learn:

- Different approaches to Artificial Intelligence, including the "good old" symbolic approach with **Knowledge Representation** and reasoning ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
- **Neural Networks** and **Deep Learning**, which are at the core of modern AI. We will illustrate the concepts behind these important topics using code in two of the most popular frameworks - [TensorFlow](http://tensorflow.org/) and [PyTorch](http://pytorch.org/).
- **Neural Architectures** for working with images and text. We will cover recent models but may lack a little bit on the state-of-the-art.
- Less popular AI approaches, such as **Genetic Algorithms** and **Multi-Agent Systems**.

What we will not cover in this curriculum:

- Business cases of using **AI in Business**. Consider taking [Introduction to AI for business users](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-cacaste) learning path on Microsoft Learn, or [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-cacaste), developed in cooperation with [INSEAD](https://www.insead.edu/).
- **Classic Machine Learning**, which is well described in our [Machine Learning for Beginners Curriculum](http://github.com/Microsoft/ML-for-Beginners).
- Practical AI applications built using [**Cognitive Services**](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-cacaste). For this, we recommend that you start with modules Microsoft Learn for [vision](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-cacaste), [natural language processing](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste), [**Generative AI with Azure OpenAI Service**](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum) and others.
- Specific ML **Cloud Frameworks**, such as [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), or [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-cacaste). Consider using [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-cacaste) and [Build and Operate Machine Learning Solutions with Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-cacaste) learning paths.
- **Conversational AI** and **Chat Bots**. There is a separate [Create conversational AI solutions](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-cacaste) learning path, and you can also refer to [this blog post](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) for more detail.
- **Deep Mathematics** behind deep learning. For this, we would recommend [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) by Ian Goodfellow, Yoshua Bengio and Aaron Courville, which is also available online at [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

For a gentle introduction to *AI in the Cloud* topics you may consider taking the [Get started with artificial intelligence on Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-cacaste) Learning Path.

## [Announcement - New Curriculum on Generative AI was just released!](https://microsoft.github.io/AI-For-Beginners/?id=announcement-new-curriculum-on-generative-ai-was-just-released)

We just released a 12 lesson curriculum on generative AI. Come learn things like:

- prompting and prompt engineering
- text and image app generation
- search apps

As usual, there's a lesson, assignments to complete, knowledge checks and challenges.

Check it out:

> 
> 
> 
> [https://aka.ms/genai-beginners](https://aka.ms/genai-beginners)
> 

# [Content](https://microsoft.github.io/AI-For-Beginners/?id=content)

| No | Lesson | Intro | PyTorch | Keras/TensorFlow | Lab |
| --- | --- | --- | --- | --- | --- |
| I | **Introduction to AI** |  |  |  |  |
| 1 | Introduction and History of AI | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/1-Intro/README.md) |  |  |  |
| II | **Symbolic AI** |  |  |  |  |
| 2 | Knowledge Representation and Expert Systems | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/2-Symbolic/README.md) | [Expert System](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb), [Ontology](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb), [Concept Graph](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) |  |  |
| III | [**Introduction to Neural Networks**](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/README.md) |  |  |  |  |
| 3 | Perceptron | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/03-Perceptron/README.md) | [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) |  | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 4 | Multi-Layered Perceptron and Creating our own Framework | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/04-OwnFramework/README.md) | [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) |  | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 5 | Intro to Frameworks (PyTorch/TensorFlow) and Overfitting | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/05-Frameworks/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) | [Keras](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb)/[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV | [**Computer Vision**](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/README.md) | [*Microsoft Azure AI Fundamentals: Explore Computer Vision*](https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-77998-cacaste) |  |  |  |
|  | *Microsoft Learn Module on Computer Vision* |  | [*PyTorch*](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) | [*TensorFlow*](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste) |  |
| 6 | Intro to Computer Vision. OpenCV | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/06-IntroCV/README.md) | [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) |  | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 7 | Convolutional Neural NetworksCNN Architectures | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/README.md)[Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) | [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 8 | Pre-trained Networks and Transfer LearningTraining Tricks | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/08-TransferLearning/README.md)[Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)[Dropout sample](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb)[Adversarial Cat](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 9 | Autoencoders and VAEs | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/09-Autoencoders/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) |  |
| 10 | Generative Adversarial NetworksArtistic Style Transfer | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/10-GANs/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) | [TensorFlow GAN](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANTF.ipynb)[Style Transfer](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) |  |
| 11 | Object Detection | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/11-ObjectDetection/README.md) | PyTorch | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12 | Semantic Segmentation. U-Net | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/12-Segmentation/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) | [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb) |  |
| V | [**Natural Language Processing**](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/README.md) | [*Microsoft Azure AI Fundamentals: Explore Natural Language Processing*](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste) |  |  |  |
|  | *Microsoft Learn Module on Natural language processing* |  | [*PyTorch*](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) | [*TensorFlow*](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) |  |
| 13 | Text Representation. Bow/TF-IDF | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/13-TextRep/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb) |  |
| 14 | Semantic word embeddings. Word2Vec and GloVe | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/14-Embeddings/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb) |  |
| 15 | Language Modeling. Training your own embeddings | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/15-LanguageModeling/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16 | Recurrent Neural Networks | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/16-RNN/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb) |  |
| 17 | Generative Recurrent Networks | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/README.md) | [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md) | [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18 | Transformers. BERT. | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/18-Transformers/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb) |  |
| 19 | Named Entity Recognition | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/README.md) |  | [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/lab/README.md) |
| 20 | Large Language Models, Prompt Programming and Few-Shot Tasks | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/README.md) | [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) |  |  |
| VI | **Other AI Techniques** |  |  |  |  |
| 21 | Genetic Algorithms | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/6-Other/21-GeneticAlgorithms/README.md) | [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) |  |  |
| 22 | Deep Reinforcement Learning | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/6-Other/22-DeepRL/README.md) | [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) | [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb) | [Lab](https://microsoft.github.io/AI-For-Beginners/lessons/6-Other/22-DeepRL/lab/README.md) |
| 23 | Multi-Agent Systems | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/6-Other/23-MultiagentSystems/README.md) |  |  |  |
| VII | **AI Ethics** |  |  |  |  |
| 24 | AI Ethics and Responsible AI | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/7-Ethics/README.md) | [*MS Learn: Responsible AI Principles*](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) |  |  |
|  | **Extras** |  |  |  |  |
| X1 | Multi-Modal Networks, CLIP and VQGAN | [Text](https://microsoft.github.io/AI-For-Beginners/lessons/X-Extras/X1-MultiModal/README.md) | [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/X-Extras/X1-MultiModal/Clip.ipynb) |  |  |

[**Mindmap of the Course**](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)

Each lesson contains some pre-reading material (linked as **Text** above), and some executable Jupyter Notebooks, which are often specific to the framework (**PyTorch** or **TensorFlow**). The executable notebook also contains a lot of theoretical material, so to understand the topic you need to go through at least one version of the notebooks (either PyTorch or TensorFlow). There are also **Labs** available for some topics, which give you an opportunity to try applying the material you have learned to a specific problem.

Some sections also contain links to **MS Learn** modules that cover related topics. Microsoft Learn provides a convenient GPU-enabled learning environment, although in terms of content you can expect this curriculum to go a bit deeper.

# [Are you a student?](https://microsoft.github.io/AI-For-Beginners/?id=are-you-a-student)

Get started with the following resources:

- [Student Hub page](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) In this page, you will find beginner resources, Student packs and even ways to get a free cert voucher. This is one page you want to bookmark and check from time to time as we switch out content at least monthly.
- [Microsoft Student Learn ambassadors](https://studentambassadors.microsoft.com/?WT.mc_id=academic-77998-cacaste) Join a global community of student ambassadors, this could be your way into Microsoft.

# [Getting Started](https://microsoft.github.io/AI-For-Beginners/?id=getting-started)

**Students**, there are a couple of ways to use the curriculum. First of all, you can just read the text and look through the code directly on GitHub. If you want to run the code in any of the notebook - [read our instructions](https://microsoft.github.io/AI-For-Beginners/etc/how-to-run), and find more advice on how to do it [in this blog post](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> 
> 
> 
> **Note**: [Instructions on how to run the code in this curriculum](https://microsoft.github.io/AI-For-Beginners/etc/how-to-run)
> 

However, if you would like to take the course as a self-study project, we suggest that you fork the entire repo to your own GitHub account and complete the exercises on your own or with a group:

- Start with a pre-lecture quiz.
- Read the intro text for the lecture.
- If the lecture has additional notebooks, go through them, reading and executing the code. If both TensorFlow and PyTorch notebooks are provided, you can focus on one of them - choose your favorite framework.
- Notebooks often contain some of the challenges that require you to tweak the code a little bit to experiment.
- Take the post-lecture quiz.
- If there is a lab attached to the module - complete the assignment.
- Visit the [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions) to "learn out loud".

> 
> 
> 
> For further study, we recommend following these [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) modules and learning paths.
> 

**Teachers**, we have [included some suggestions](https://microsoft.github.io/etc/for-teachers) on how to use this curriculum.

## [Credits](https://microsoft.github.io/AI-For-Beginners/?id=credits)

**✍️ Primary Author:** [Dmitry Soshnikov](http://soshnikov.com/), PhD

**🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD

**🎨 Sketchnote illustrator:** [Tomomi Imura](https://twitter.com/girlie_mac)

**✅ Quiz Creator:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)

**🙏 Core Contributors:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## [Meet the Team](https://microsoft.github.io/AI-For-Beginners/?id=meet-the-team)

[Promo video](https://youtu.be/m2KrAk0cC1c)

![](AI%20for%20Beginners%206b0ab8f81a254bad96221cc4d72f100f/ai-for-beginners.png)

> 
> 
> 
> 🎥 Click the image above for a video about the project and the folks who created it!
> 

## [Pedagogy](https://microsoft.github.io/AI-For-Beginners/?id=pedagogy)

We have chosen two pedagogical tenets while building this curriculum: ensuring that it is hands-on **project-based** and that it includes **frequent quizzes**.

By ensuring that the content aligns with projects, the process is made more engaging for students and retention of concepts will be augmented. In addition, a low-stakes quiz before a class sets the intention of the student towards learning a topic, while a second quiz after class ensures further retention. This curriculum was designed to be flexible and fun and can be taken in whole or in part. The projects start small and become increasingly complex by the end of the 12 week cycle.

> 
> 
> 
> Find our [Code of Conduct](https://microsoft.github.io/AI-For-Beginners/etc/CODE_OF_CONDUCT), [Contributing](https://microsoft.github.io/AI-For-Beginners/etc/CONTRIBUTING), and [Translation](https://microsoft.github.io/AI-For-Beginners/etc/TRANSLATIONS) guidelines. Find our [Support Documentation here](https://microsoft.github.io/AI-For-Beginners/etc/SUPPORT) and [security information here](https://microsoft.github.io/AI-For-Beginners/etc/SECURITY). We welcome your constructive feedback!
> 

> 
> 
> 
> **A note about quizzes**: All quizzes are contained [in this app](https://red-field-0a6ddfd03.1.azurestaticapps.net/), for 50 total quizzes of three questions each. They are linked from within the lessons but the quiz app can be run locally; follow the instruction in the `etc/quiz-app` folder.
> 

## [Offline access](https://microsoft.github.io/AI-For-Beginners/?id=offline-access)

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine, and then in the `etc/docsify` folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`. A pdf of the curriculum is available [at this link](https://microsoft.github.io/etc/pdf/readme.pdf).

## [Help Wanted!](https://microsoft.github.io/AI-For-Beginners/?id=help-wanted)

Would you like to contribute a translation? Please read our [translation guidelines](https://microsoft.github.io/AI-For-Beginners/etc/TRANSLATIONS).

## [Other Curricula](https://microsoft.github.io/AI-For-Beginners/?id=other-curricula)

Our team produces other curricula! Check out:

- [AI for Beginners](https://aka.ms/ai-beginners)