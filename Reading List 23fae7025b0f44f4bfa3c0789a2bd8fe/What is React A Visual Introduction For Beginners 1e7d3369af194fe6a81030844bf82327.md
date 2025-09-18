# What is React: A Visual Introduction For Beginners

Column: https://learnreact.design/posts/what-is-react
Processed: No
created on: December 23, 2021 7:30 AM
topics: tech-stuff

![what-is-react-social-card.800708b70b86fbe2a3fee7914aa7f9bc.png](What%20is%20React%20A%20Visual%20Introduction%20For%20Beginners%201e7d3369af194fe6a81030844bf82327/what-is-react-social-card.800708b70b86fbe2a3fee7914aa7f9bc.png)

> React is a JavaScript library for building user interfaces.
> 

This is the official definition of React. But what if you are not familiar with JavaScript? What if you are not a developer? Would you still be able to make sense of (and learn) React?

My answer is a firm YES. That's why I wrote this article: what is React exactly? What is React.js (or ReactJS)? What is React used for? Why is React so popular? What problems does it solve?

This article is an introduction to React for beginners. It's the first post you'd want to read before learning the specifics of React. I'll explain the core ideas of React in plain English (and doodles 🌴). No JavaScript experience? No problem! As long as you have some basic HTML knowledge (e.g. the format of an HTML tag), you should be able to enjoy this article.

This is a bird's-eye view 🦅 but I'll also equip you with a pair of binoculars  . You'll not only see the **big picture** of what makes React special, but also zoom in to get some **hands-on experience** of writing an actual React component. And yes, no JS knowledge required!

Remember: You don't need to be an experienced developer to understand the core ideas of React!

Ready to start the journey?

Of course, eventually you'd need to write code to use React. That's why I'm building an email course to help you on that.

I believe you'd be able to do useful work with React after a few days of learning, **even if you are new to coding**. If you are interested, sign up and I'll let you know when the course is ready!

Let's get started with something you might have heard many times, the DOM.

When you enter the address of your favorite website into a browser, your computer starts a conversation with another computer far away, commonly referred to as *server*. Typically your computer makes a request for some information and the server responds:

> Your computer: Yo, what's good about this random site learnreact.design?
> 
> 
> **The server:** Hang on, let me grab something for you. Beep. Boop.
> 

The main part of the server's response usually includes three items: HTML, CSS and JavaScript.

HTML lists the content of a web page and describes its structure. How many headings and paragraphs are there? What images should a user see? Are this button and that textbox contained in the same box?

Using this information, the browser creates something called... the DOM!

Wait a second, the DOM is a ... tree? Yup, a tree! Oddly enough, a lot of things in our computer look like a tree. Let's give our tree friend a nickname... hmm what about Domo?

Domo works as a model at the prestigious art studio "Web Browser". His job is to pose in front of the artist who paints a portrait (or perhaps millions of portraits).

In real life, DOM stands for Document Object Model. It's indeed a model -- a model of the document (aka the web page). It strikes a pose. The browser paints a portrait. The portraits are what we see on a web page: the textboxes, the paragraphs, the images and so on. A developer's job is like that of a director who tells Domo what to wear and what pose to strike. This determines what those portraits look like in the end.

To check out what the DOM looks like, if you are using a desktop browser, right-click on this very page and choose "Inspect". Can you make sense of what's in the Elements tab?

We often want a web page to be dynamic and interactive -- that means its content changes from time to time: adding or removing text here and there, showing a modal, or updating a chart based on some new data coming from the server.

Remember, in order to change what's on a web page, we need to update the DOM. The artist isn't able to paint new portraits until Domo changes to a new pose.

How would we get Domo to change to a new pose?

We just talk to him. He listens. Interestingly, Domo's ears happen to have a name: *DOM API*.

To manipulate the DOM, a developer would write code in JavaScript which talks to the DOM API, and in turn, updates the content of the web page.

*Directly* talking to Domo has been the standard approach of web development for years, especially when the web content was mostly static. A developer would sprinkle some interactivity on top of the static pages by writing small amount of JavaScript code.

However, with the emergence of SPAs (Single Page Application) such as Gmail and Google Maps, people started to expect a lot more. Instead of mostly static web *pages*, they want web *apps* that are interactive, fast and responsive.

The code required to build web apps becomes increasingly large and complex. It often requires the collaboration of many team members.

The traditional approach stopped working. It becomes chaotic and inefficient to always directly talk to Domo.

Let me introduce you to the superhero, React:

With React, developers no longer directly talk to Domo. React acts as an agent between a developer and Domo. He smoothens the communication and streamlines the process of portrait creation.

React is also referred to as "ReactJS" or "React.js", but "React" is the official name.

React is made up of JavaScript code. It's built in a way that we no longer need to directly work with the DOM API in most cases. Instead, we write simpler code while React handles the conversation with the DOM under the hood.

React has a few superpowers to tackle the ever-growing complexity of web development:

- Components
- Declarative UI
- Reactive DOM updates

If these terms sound scary to you, don't be intimidated! As promised, I'll use plain English and doodles to help you make sense of them. Trust me, it's not that hard!

Just read on!

Components are the flagship feature of React. The core idea is based on a simple strategy: divide-and-conquer. If it's difficult to grok a problem all at once, we break it into smaller problems, solve them one at a time and then combine the results.

Building an app in React is almost all about working with components: breaking the app into components, finding the best components for the job, fitting one with another, creating new components from existing ones etc.

Nowadays, design tools such as Framer and Figma have components too (and symbols in Sketch). They are a lot like React components, except that the latter are more flexible and powerful. In fact, the inspiration of components in design tools came directly from components in software engineering. Once a component is created, we can create multiple instances of it. We can use it to construct other components. If we change a component, everything that includes this component will be updated automatically.

Components in React have two important properties:

1. Components are *composable*. They are made for reuse. We can make a new component with other components.
2. Components are *independent* of each other. If we change the code in one place, other parts don't break.

If this sounds abstract to you, don't worry! I'll show you some examples and explain these properties in details soon.

When directly working with the DOM API, we'd have to specify what element to change at the right time, in the right order. This is equivalent to describing to Domo how to position his head, arms and legs step by step, for each and every portrait.

Heck, this sounds tedious and error-prone! Why can't we just tell Domo *what* we want instead of *how* to pose? In fact, this is exactly how to build a UI in React. A developer draws a quick sketch of what he or she wants. React explains it to Domo how to pose.

Because the apps we build are dynamic, we often want Domo to change poses fairly quickly. We draw many sketches and hand them to React in a big pile. React stacks these sketches together and flips them like a flipbook. A dynamic UI comes live!

In tech terms, if the code defines *how* we want it to be done, it's **imperative**; if it defines *what* we want, it's **declarative**. The traditional way of directly working with the DOM API is imperative, and the React way is declarative.

Imperative programming emerged from the day when the computers were primitive. People had to instruct them in detail: where to store the numbers, how to multiply etc. But this eventually got unmanageable, people wrote smart software that convert definition of problems into detailed instructions. Declarative programming was born.

Besides making the life of a developer easier, declarative programming in React also offers opportunities for performance optimization.

When React has all the sketches beforehand, he can sort through them, remove any duplication and make sure that Domo and the artist do as little work as possible.

These sketches are called *Virtual DOM*. Virtual DOM is much faster to manipulate than the DOM. Developers work with Virtual DOM most of the time instead of directly managing the DOM. React handles the dirty work of managing the slow DOM.

Even cooler, imagine if we can leave placeholders in our sketches to represent different variations of a same pose. This way, when somebody asks for portraits of Domo wearing a different hat, we don't have to talk to React again. We can just sit back and let React change it for us.

The hat here is the data that determine the dynamic content of the UI. We just need to associate UI elements with their corresponding data. When the data change, React automatically updates the related DOM elements for us. It appears that the DOM "reacts" to any changes to the underlying data. No need to track the data. No need to worry about when to update the DOM. It just gets updated automatically (by React).

This trick is how React got its name. The UI built with React is **reactive**. The idea of reactive UI greatly simplifies UI development.

Congrats! You've finished the first important lesson of React! It's about the big picture: why do we need React at all? Here are the three core ideas that make React powerful: Components, Declarative UI and Reactive DOM updates.

In fact, I bet even some experienced React developers (for example, myself!) are not super clear about these concepts. When I wrote the first version of this article a few years ago, I put focus on the wrong things. Hopefully this revision is more accurate!

Here's a list of terms covered in the post:

- The DOM (Document Object Model)
- The DOM API
- React components
- Components are composable and independent
- Imperative vs. declarative programming
- Virtual DOM
- Reactive DOM updates