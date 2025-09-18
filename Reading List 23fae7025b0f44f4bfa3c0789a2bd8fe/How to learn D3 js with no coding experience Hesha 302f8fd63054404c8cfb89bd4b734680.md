# How to learn D3.js with no coding experience | Hesham Eissa

Column: https://www.heshameissa.com/blog/learn-d3
Processed: No
created on: December 18, 2021 3:04 PM
topics: tech-stuff

![d3-blog-thumbnail.png](How%20to%20learn%20D3%20js%20with%20no%20coding%20experience%20Hesha%20302f8fd63054404c8cfb89bd4b734680/d3-blog-thumbnail.png)

In November 2019 we competed against each other, live and on stage, at the [Iron Viz](https://www.tableau.com/iron-viz) competition to build a complete visualization in just 20 minutes. After the competition was over we discussed what our goals were for the coming year. We both were working as Tableau developers and had experience working with data and designing visualizations. However, we both realized we had a desire to learn how to create beautiful, interactive visualizations outside of the tool. We decided we wanted to learn D3.js but realized we needed to learn web development first, as we both had no coding experience to start.

On January 1, 2020 we began our journey. We spent January through March doing structured learning, watching videos and reading books. Then, we spent two months experimenting with D3.js, creating as many different chart types as we could, with different datasets, in order to get really comfortable with it. We spent around 1-3 hours each day. In June, we put all of our hard work into practice and created our first visualization, [The Inside Scoop of Ben & Jerry's](https://benjerry.heshlindsdataviz.com/).

We divided our learning experience into 5 steps and documented what we did for each. It is mostly in the order of how we learned, but we also modified it to include pieces of information we wish we would have known at that point. Now, let's dive into how someone with experience analyzing and visualizing data in a business intelligence tool, with no coding background, can get started with D3.js.

## Step 1: Web Development foundation

D3.js is a library that requires the use of Javascript, HTML, CSS, and SVG. Therefore before you can successfully begin to use D3.js, it is important to have an understanding of front-end web development.

To learn HTML, CSS, and JavaScript, we took Angela Yu's [Complete 2020 Web Development Bootcamp](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/17039566#content) course on Udemy (recommended to us by [Tim Ngwena](https://twitter.com/TableauTim)).

The course covers everything from front-end web development to React to backend web development. Instead of completing the whole course (as we did) and to save time, we recommend completing the following sections to get started with D3.js:

- Section 1: Front-End Web Development
- Section 2: Introduction to HTML
- Section 3: Intermediate HTML
- Section 4: Introduction to CSS
- Section 5: Intermediate CSS
- Section 6: Introduction to Bootstrap
- Section 7: Intermediate Bootstrap
- Section 9: Introduction to Javascript
- Section 10: Intermediate Javascript
- Section 11: The Document Object Model
- Section 13: Advanced Javascript and DOM Manipulation
- Section 14: jQuery

## Step 2: SVG & D3.js foundation

Now, that you have a basic understanding of front-end web development, the next step is to familiarize yourself with SVG before jumping into D3.js!

SVG is used to draw the pieces of a visualization (rectangles for bars, lines for axes, etc.) and display it on the web. D3.js then allows you to easily create SVG elements for each data point in a dataset. Before attempting D3.js, it is helpful to understand the basics of SVG. Here are a few places to start:

Next, you are (finally) ready to begin using D3.js! We used Amelia Wattenberger's [Full Stack D3 and Data Visualization](https://www.newline.co/fullstack-d3) Book. The book provides full code examples and explanations of each step. We started by only doing the following chapters:

- Chapter 1: Making your First Chart
- Chapter 2: Making a Scatterplot
- Chapter 3: Making a Bar Chart
- Chapter 6: Making a Map

One of the most helpful takeaways from the book was Amelia's process to follow when building a visualization. She summarizes the process in this article, [Prototyping in D3](https://observablehq.com/@wattenberger/prototyping-in-d3).

Amelia also put together a really comprehensive [overview of D3.js](https://wattenberger.com/blog/d3) modules that includes examples, links to resources, and official documentation.

We did not take Shirley Wu's [Introduction to D3.js](https://frontendmasters.com/courses/d3/) course, but based upon looking at the [course materials](https://observablehq.com/@sxywu/introduction-to-svg-and-d3-js?collection=@sxywu/introduction-to-d3-js), it seems like a really great introduction as well. Her visual explanations, especially on [binding data](https://observablehq.com/@sxywu/2-select-existing-petal-s-and-bind-movie-data), are extremely helpful for understanding key concepts.

## Step 3: Practice on a familiar dataset

The best way to find out what you know and don't know is to create a simple chart using a dataset you are familiar with (it doesn't have to be anything fancy or interactive!). This is where you will begin to appreciate the level of control you have over every aspect of your visualization, but will also realize how many different pieces are involved in a simple chart! We started with creating:

- Bar Chart
- Line Chart
- Scatter Plot
- Heat Map

One of the biggest lessons we learned was the value of doing data prep outside of D3.js and instead connecting to your data in a clean, properly aggregated format. However, this is not always possible. We plan to write an additional blog detailing a few useful methods but if you want to do data prep at this point, get familiar with [nesting](https://github.com/d3/d3-collection) and [array iteration methods](https://github.com/d3/d3-array).

## Step 4: Add transitions and interactivity

One of the most exciting (and probably the most satisfying) parts about creating visualizations in D3.js is bringing it to life. We used the concepts below to learn how to build in interactivity and motion to our visualizations. To test out these concepts, we applied them to the static visualizations created in the previous step.

Animations and transitions:

- D3 joins (enter, update, and exit patterns) are a crucial component to making transitions work. However, it can take practice and reading different explanations to really understand just how it works. A few places to start are articles from [D3 in Depth](https://www.d3indepth.com/enterexit/), [Create with Data](https://www.createwithdata.com/enter-exit-with-d3-join/), [Mike Bostock](https://observablehq.com/@d3/selection-join), and [D3.js Playbook](https://gramener.github.io/d3js-playbook/transitions.html)

Interactions:

- Event Listeners fire off when a user interacts with an object through the specified way (click, mouse over, etc.). This allows for the ability to display tooltips, change colors, trigger a transition, etc. These articles from [D3.js Playbook](https://gramener.github.io/d3js-playbook/events.html), [D3 for the Impatient](https://www.oreilly.com/library/view/d3-for-the/9781492046783/ch04.html), and [D3 Graph Gallery](https://www.d3-graph-gallery.com/graph/interactivity_button.html) are good places to start.
- Bisecting is a helpful way to improve interactivity, especially [tooltips](http://www.d3noob.org/2014/07/my-favourite-tooltip-method-for-line.html) and [reference lines](https://observablehq.com/@d3/d3-bisect), as it allows the mouse to not be directly over a point, but in the area nearby

## Step 5: Challenge yourself

The last step to learning D3.js is building advanced chart types and creating your own challenges to complete.

We found these chart types challenging because they all require different data formats, but are very powerful in what they allow you to do:

- Beeswarm
- Treemap or Packed Circles
- Stacked Bar Chart

The last way we challenged ourselves was by replicating other's work (strictly for learning purposes). Find a graph, transition, or piece of someone else's work that is interesting to you and try to recreate it with your own data. Having a strict end result in mind, but no guidance on how to get there, is a great way to check your understanding of D3.js and learn new things!

## Final tips

- Find someone to learn with you! If you don't understand something it is helpful to have someone to talk it over with. It also helps you better understand a topic when you try to explain it to someone else. Alternatively, it's helpful to know when you both are stuck and can spend extra time practicing together (which will probably happen a lot!).
- Get comfortable with [Observable](https://observablehq.com/). A lot of d3 examples will be shown there, so understanding how to use it, how to view underlying code, and the slight syntax differences, will be extremely helpful.
- If you are stuck on how to use a certain visualization, module, or feature search for it on [Observable](https://observablehq.com/). For example, if you are trying to use force, search for `d3.force`. You will find all types of examples of how other people have used the module!
- [D3 Graph Gallery](https://www.d3-graph-gallery.com/index.html) is a great website for finding easy to follow examples of every chart type.
- All of your visualization work doesn't have to be done in D3.js. It is not a rapid prototyping tool by any means, so using a tool/language you are most comfortable with is a great way to explore the data and get a general idea of what you want to create.
- Be patient. Learning takes time and it is completely normal to feel frustrated!

Good luck and happy coding!