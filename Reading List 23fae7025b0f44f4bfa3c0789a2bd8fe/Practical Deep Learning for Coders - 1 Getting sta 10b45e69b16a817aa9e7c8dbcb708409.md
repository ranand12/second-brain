# Practical Deep Learning for Coders - 1: Getting started

Column: https://course.fast.ai/Lessons/lesson1.html
Processed: Yes
created on: September 23, 2024 10:02 PM

![](https://course.fast.ai/images/bunny_net.png)

## Video

Click the video below to play. Once it’s playing, you’ll see a little rectangle in the bottom-right—click it to make the video full-screen. Press Esc to remove full-screen view. Press c to turn subtitles on/off.

This lesson is based partly on [chapter 1](https://github.com/fastai/fastbook/blob/master/01_intro.ipynb) of the [book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527).

## How to complete lesson 1

Every lesson includes lots of hands-on exercises for you to try. Most of these are run in interactive notebooks, all of which are available on [Kaggle](https://course.fast.ai/Resources/kaggle.html). If you don’t work through the notebooks yourself, you’re not going to get nearly as much out of this course—so that means you need to get set up on Kaggle. We have a page to help you get going with Kaggle: [click here](https://course.fast.ai/Resources/kaggle.html) to go there now. Instead of using Kaggle, another great option is [Paperspace Gradient](https://gradient.run/notebooks) If you don’t have a Paperspace account yet, sign up with [this link](https://console.paperspace.com/signup?R=lg6rnx) to get $10 credit (and we get a credit too).

Once you’ve got your Kaggle account set up, you’ll need to get familiar with [Jupyter Notebook](https://jupyter.org/), which is the platform we use for most of this course (and which most deep learning researchers and engineers use for their work). Jupyter is the most popular tool for doing data science in Python, for good reason. It is powerful, flexible, and easy to use. We think you will love it! Since the most important thing for learning deep learning is writing code and experimenting, it’s important that you have a great platform for experimenting with code. If you haven’t used it before, we’ve provided this to help you get started: [Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101).

OK, now that you have your Kaggle account and know how to use Jupyter, you’re ready to open the notebook for this lesson: [here it is](https://www.kaggle.com/code/jhoward/is-it-a-bird-creating-a-model-from-your-own-data). For every lesson, you can find links to all notebooks used in the *Resources* section of the lesson web page. For instance, for lesson 1, you’ll see that section immediately below this one.

As well as watching the video and working through the notebooks, you should also read the relevent chapter(s) of the fast.ai book, [Practical Deep Learning for Coders](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch-ebook-dp-B08C2KM7NR/dp/B08C2KM7NR). Each lesson will tell you what chapter you need to read, just below the video. For this lesson, it’s chapter 1. There’s a few ways to read the book – you can buy it as a paper book or Kindle ebook, or you can read it for free as a Jupyter notebook. The whole book is written as Jupyter notebooks, so you can also execute all the code in the book yourself. To go to the interactive Jupyter version of any chapter, click [The book](https://course.fast.ai/Resources/book.html) in the left sidebar, where you’ll find a list of chapter links. You’ll also find links to read-only versions of each chapter there.

## Resources

- [Kaggle](https://course.fast.ai/Resources/kaggle.html) notebooks for this lesson:
    - [Is it a bird? Creating a model from your own data](https://www.kaggle.com/code/jhoward/is-it-a-bird-creating-a-model-from-your-own-data)
    - [Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101)
- The fastai book:
    - [Published version](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch-ebook-dp-B08C2KM7NR/dp/B08C2KM7NR)
    - [Free notebook version](https://github.com/fastai/fastbook)
    - Chapter 1 [notebook](https://github.com/fastai/fastbook/blob/master/01_intro.ipynb)
- Repo containing [all lesson notebooks](https://github.com/fastai/course22)
- [Solutions](https://forums.fast.ai/t/fastbook-chapter-1-questionnaire-solutions-wiki/65647) to chapter 1 questions from the book

## Links

You’ll see that fast.ai’s way of teaching is very different to what you might be used to, if you did a technical degree at university. Nearly all technical subjects at university are taught “bottom up”: start with basic foundations, and gradually work up to complete useful solutions to real world problems. But we go “top down”: start with complete useful solutions to real world problems, and gradually work down to the basic foundations. Education experts recommend this approach for more effective learning. For more information, have a look at this article that discusses the fast.ai teaching philosophy: [Providing a Good Education in Deep Learning](https://www.fast.ai/2016/10/08/teaching-philosophy/).

- How to learn - highly recommended books for fast.ai students
    - [Meta Learning](https://radekosmulski.gumroad.com/l/learn_deep_learning)
    - [A Mathematician’s Lament](https://www.maa.org/external_archive/devlin/LockhartsLament.pdf) by Paul Lockhart
    - [Making Learning Whole](http://www.pz.harvard.edu/resources/making-learning-whole-how-seven-principles-of-teaching-can-transform-education) by David Perkins
- Jupyter
    - Presentations: [RISE](https://rise.readthedocs.io/en/stable/)
    - Blogging: [fastpages](https://github.com/fastai/fastpages)
    - The notebooks used to create the [fastai library](https://github.com/fastai/fastai/tree/master/nbs)
    - [nbdev](https://nbdev.fast.ai/) - the system we built to create Python libraries using Jupyter
- Fastai: A Layered API for Deep Learning paper: [Information Journal](https://www.mdpi.com/2078-2489/11/2/108) or [arxiv](https://arxiv.org/abs/2002.04688) or [fast.ai](https://www.fast.ai/2020/02/13/fastai-A-Layered-API-for-Deep-Learning/)
- [Dall-e 2 illustrations of Twitter bios](https://twitter.com/nickcammarata/status/1511861061988892675)
- [timm](https://timm.fast.ai/): PyTorch Image Models

![](https://course.fast.ai/images/excited_code3.png)

Today you’ll be designing your own machine learning project, creating your own dataset, training a model using your data, and finally deploying an application on the web. We’ll be using a particular deployment target called [Hugging Face Space](https://huggingface.co/spaces) with [Gradio](https://gradio.app/), and will also see how to use JavaScript to implement an interface in the browser. Deploying to other services will look very similar to the approach you’ll study in this lesson.