# Intro | Putting the "You" in CPU

Column: https://cpu.land/
Processed: No
created on: January 3, 2024 11:47 AM

I’ve done [a lot of things with computers](https://github.com/kognise), but I’ve always had a gap in my knowledge: what exactly happens when you run a program on your computer? I thought about this gap — I had most of the requisite low-level knowledge, but I was struggling to piece everything together. Are programs really executing directly on the CPU, or is something else going on? I’ve used syscalls, but how do they *work*? What are they, really? How do multiple programs run at the same time?

![](Intro%20Putting%20the%20You%20in%20CPU%2092bd9509e6ad4dc0b44d940b3e810cf7/writing-this-article.png)

A scrawled digital drawing. Someone with long hair is confused as they peer down at a computer ingesting binary. Suddenly, they have an idea! They start researching on a desktop computer with bad posture.

I cracked and started figuring as much out as possible. There aren’t many comprehensive systems resources if you aren’t going to college, so I had to sift through tons of different sources of varying quality and sometimes conflicting information. A couple weeks of research and almost 40 pages of notes later, I think I have a much better idea of how computers work from startup to program execution. I would’ve killed for one solid article explaining what I learned, so I’m writing the article that I wished I had.

And you know what they say… you only truly understand something if you can explain it to someone else.

> In a hurry? Feel like you know this stuff already?
> 
> 
> [Read chapter 3](https://cpu.land/how-to-run-a-program) and I guarantee you will learn something new. Unless you’re like, Linus Torvalds himself.
>