# Modern Javascript: Everything you missed over the last 10 years by Sandro Turriate

Column: https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years
Processed: No
created on: December 23, 2021 11:47 AM
topics: tech-stuff

JavaScript has come a long way since I knew it as the “D” in DHTML. For anyone like me, who’s been reluctant to use the latest syntax that could require polyfills or a transpiler, I’ve written this cheatsheet to get you caught up on all the goodness that’s widely supported in modern browsers.

I’ve made this page concise, with runnable examples and links to further documentation. If you have any questions or spot any errata, please [contact me.](https://turriate.com/contact)

Check out all these new built-in array functions! No more need for underscore or lodash!

- Array.every()
- Array.filter()
- Array.find()
- Array.findIndex()
- Array.forEach()
- Array.from()
- Array.includes()
- Array.isArray()
- Array.lastIndexOf()
- Array.map()
- Array.reduce()
- Array.reduceRight()
- Array.some()

[Array docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)

These new keywords declare variables in block scope (as opposed to global or function scope). Using `const` implies that the value will not change as the reference is immutable. Use `let` if the value will change.

The `??` operator checks if the value is null or undefined. No more need to use the `!!` check.

The `?.` operator checks if the value is truthy before calling the next property or function. Extremely useful when dealing with optional props.

[Optional chaining documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

let a, b=1 let result = a ?? b print(result) result = (a !== null && a !== undefined) ? a : b; print(result) print({x:1}?.a?.b ?? "not found")

The async/await keywords are here to save you from callback hell. Use await to make an asynchronous call resemble a synchronous call, i.e. running `await fetchUserName()` will not proceed to the next line until fetchUserName() is complete. Note, in order to use await, you have to be executing a function declared as async, i.e.`async function fn(){ await fetchUserName() }`.

[Async/Await docs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await).

function fetchUserName() { return new Promise(resolve => setTimeout(resolve, 500)) } async function withAsync() { print("withAsync: fetching...") await fetchUserName() print("withAsync: done") } await withAsync() function withoutAsync() { print("withoutAsync: fetching...") fetchUserName().then(()=>print("withoutAsync done")) } withoutAsync()

These are functions that are bound to the current context. There are three main forms you’ll see in the wild:
single argument, single line, multi-line.

The single argument form does not require parenthesis, and the single line form does not require a `return` statement; the return is implicit.

The multi-line form requires a `return` statement if the function intends to returns something. Multiple arguments require parenthesis.

function example() { this.x = 1 this.foo = function() { setTimeout(function() { print("foo lost binding. this = " + JSON.stringify(this)) }) } this.bar = function() { setTimeout(()=> { print("bar this = " + JSON.stringify(this)) }) } } const x = new example() x.foo() x.bar()

Used for looping over an iterator. Similar to `for...in` except you don’t have to check for `hasOwnProperty`. You cannot use this looping syntax on an Object directly because the Object doesn’t have an iterator. Instead use `Object.entries({})` to retrieve an iterable.

[for...of docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)

const x = {a: 1, b: 2} for (const [key, value] of Object.entries(x)) { print(`${key}=${value}`) }

Asynchronous iteration was introduced In 2018. Much like `Promise.all`, it can be used to synchronize many asynchronous tasks. The example below shows 3 tasks happening asynchronously. The loop processes one result at a time, in order; in this case, the quickest tasks to complete are only evident at the end of the iteration.

[for await...of docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)

In 2015, ES6 brought classes to Javascript 🎉. Javascript classes are similar to the classes you know and love from other languages. Inheritance, class methods, getters and setters, properties, etc.

Get and set are functions that are called like properties, i.e. `person.age = 16; person.age > 18`. These are very convenient when you need a dynamic or computed property. And they can be used with both classes and regular objects.

[get/set documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#getter_and_setter_functions)

### Classes with getters and setters

### Objects with getters and setters

Yay! You can now specify default parameters in your function definition. Works as you would expect.

With a bit of object destructuing magic, functions can now have named parameters.

The rest parameter allows a function to accept an arbitrary number of arguments as an array. It’s recommended to use this over `arguments`.

`Object.assign(target, source)` merges two or more objects into one. It modifies the target object in-place, so if you’d prefer a new object be created, pass an empty object literal as the first argument.

Alternatively, you can use the spread operator `...` to merge multiple objects together: `{...obj1, ...obj2}`, though bear in mind, spread will not call setters on the object, so to be the most portable, consider `Object.assign`. The spread operator can also be used on arrays as shown in the last code sample.

### [Destructuring](https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years#destructuring)

Destructuring allows you to extract values from objects and arrays through patterns. It is a complex topic with many applications…far too many for me to enumerate, but I've shown some of the most common uses I can think of.

Functions declared on objects can use a new shorthand style that omits the function keyword.

The two functions (`shorthand()`, `long()`) are equivalent in the sample below.

[Method guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)

### [Promise.all](https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years#promise-all)

I’ve mostly skipped over promises because async/await is preferred, but sometimes you need to synchronize multiple asynchronous calls, and Promise.all is the easiest way to do it.

### [Template literals](https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years#template-literals)

Also known as template strings, this new syntax provides easy string interpolation and multi-line strings.

A Proxy allows you to intercept get/set calls on another object. This could be useful for watching a property for changes, then updating the DOM, or making [innovative APIs](https://github.com/justjavac/proxy-www) like the www proxy below.

[](Modern%20Javascript%20Everything%20you%20missed%20over%20the%20l%204fd872609b2b42c4bf7c1d9421d922b4/D83KejvXYAA1x1O)

### [Module import/export](https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years#modules)

Modules allow you to namespace your code and break down functionality into smaller files. In the example below, we have a module named greet.js that gets included in index.html. Note, module loading is always deferred, so it won’t block the HTML from rendering. There are many ways to import/export functionality from js files, read more in the [export docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export).

[Import docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)

Okay, so I didn't cover everything that’s changed over the last decade, just the items I find most useful. Check out these other topics.

### References

- [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [Generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
- [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [Array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)
- [Object static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#static_methods)
- [Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

### Guides

- [Javascript.info](https://javascript.info/)
- [Exploring ES6](https://exploringjs.com/es6/)
- [Javascript History](https://www.w3schools.com/js/js_history.asp)
- [Non-blocking JS loading with async/defer](https://flaviocopes.com/javascript-async-defer/)