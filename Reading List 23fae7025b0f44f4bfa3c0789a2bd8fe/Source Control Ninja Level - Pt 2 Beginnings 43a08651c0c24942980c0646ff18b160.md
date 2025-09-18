# Source Control Ninja Level - Pt. 2 Beginnings

Column: https://www.shankuehn.io/post/source-control-ninja-level-pt-2-beginnings
Processed: No
created on: September 14, 2022 4:43 PM
topics: tech-stuff

Friends...it's been a long time since I last wrote. I have some exciting news that unfolded since I last wrote. Hopefully it will explain the lack of blog activity. I adopted a son earlier in 2022. His name is Rhys! Now I'm juggling a new task of being a mom and trying to find time to contribute back to the community. The good thing is he's sleeping better and I'm finding productive moments throughout the day so I should be able to start back in on getting some blog content out in the open. I've been asked to dig deeper in demystifying developer concepts from the operations point of view, so I'm looking forward to digging deeper there (hopefully you are, too). I figure if I can help you out related to understanding this software defined universe, the more the merrier! :)

Last I wrote, I started off walking you through what source control is and broke down some of the definitions. Let's pick that ball back up and write the next blog post now!

Note, there will be a few more blog posts that sort of takes it up a level and gets you closer to being a green belt. I like to think this is "ninja level" (and it may very well be for someone with a similar background as myself), but most devs would scoff at the "ninja" label. Don't let that deter you. I will say, for anything deeper than what I will write about, find a developer friend and ask for help. From what I've found, that has proved invaluable for me. As a point of reference, I love to try and fix a borked repository vs. deleting and re-cloning after finding dev friends and having them help me out with understanding the flow of source control.

Unfortunately I mostly build solutions where I'm the sole contributor, so I don't have a lot of good "real life" stories to assist in every scenario. I can tell you that my green belt level is a direct result of me working with the Microsoft Learn team to publish a handful of Learn modules that I talked about during my last blog. I'm trying to be better about documenting my learnings because forking and creating a PR to main is a task that most infrastructure people could benefit from AND there's no graceful way of describing this in regular terms so everyone understands (at least not that I've found).

Additionally, this method of forking, cloning locally, making edits, committing the changes to the local repo, pushing it to the fork, and opening up a PR to main would be how you'd work on helping Microsoft's documentation be better! Microsoft [open sourced](https://github.com/MicrosoftDocs) documentation a number of years back and creating a PR to main from your fork is how you'd submit something that needs to be corrected. Sweet, right? I'll try my best to break this down like everyone is 6 and I'm sure I may come up short. If you like what you read, be sure to follow me for more content as I try and pretend to be a developer. ;)

So, we need to start somewhere, right? As I covered most major source control definitions in my [previous post](https://www.shankuehn.io/post/source-control-ninja-level-pt-1-definitions), please review that post if certain phrases or words don't make sense to you within this post. We're going to start slow and then take it up a notch in the remaining blog posts.

Rather than go through the installation with you, please reference the [following instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on how to install git on your local machine. Git is essential in understanding the flows that most of the software developers and programmers use (now traditional sysadmins and engineers as well).

I think the biggest thing to highlight is git commands start with **git** and then the action at the command line. So **git checkout** or **git pull** or **git status**: all of these do something to the local git repository and/or to the remote repository.

I know, I know...you're probably like: "I have to learn another command line tool?" I suppose you don't necessarily have to. There are quite a number of [software GUI clients you could download and use](https://git-scm.com/downloads/guis). I will say knowing the git commands are invaluable, so if you're like me and you're slowly moving your entire skillset to a software defined world, I challenge you to use the git commands from the command line. Again, if I can do it, so can you!

I think the biggest piece of advice I received was to start by using a bunch of plain .txt files vs. actual source code. Git works for those files as well. I'll walk you through the basics of source control and hopefully you start to comprehend the magic going on behind the scenes. After this post, I'll walk you through how to effectively fork, clone, and open up a PR to main, which will help you contribute to Microsoft documentation, as I mentioned above. Know that workflow requires a bit more advanced source control commands and knowledge.

Without further ado, head to [this GitHub repo](https://github.com/sbkuehn/sample-git-demo). I built this repo when I built out part of an [AZ-400 course](https://courses.skylinesacademy.com/p/az-400-azure-devops) for Skylines Academy back in 2020. When the repo loads, clone the repository locally to your machine. The easiest way to clone a repo is by clicking on **<> Code** and then copying the HTTPS link to use within your terminal of choice that you're using locally.

After you've copied that HTTPS link, head over to your terminal that you have locally. I tend to use [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install) myself. Type in the following commands:

```
mkdir sample-git-demo
cd sample-git-demo
git clone https://github.com/sbkuehn/sample-git-demo.git
```

This is how it will appear within your terminal:

The demo I have up on GitHub contains a list of Harry Potter characters as basic text files:

Within your local set-up, open up harry.txt and type in **The boy who lived.** Ensure you save the file afterward. As you can see in my examples below, the first image isn't saved, but the second image is. The scale is a bit off, but hopefully that doesn't deter you from learning.

![](Source%20Control%20Ninja%20Level%20-%20Pt%202%20Beginnings%2043a08651c0c24942980c0646ff18b160/file.jpg)

![](Source%20Control%20Ninja%20Level%20-%20Pt%202%20Beginnings%2043a08651c0c24942980c0646ff18b160/52fcb0_c3df373214ca438bb8f5bd9872f92748mv2.jpg)

Flip back to your terminal of choice. Run the following commands:

You're probably wondering what we're doing in these few commands. The first command [git status](https://git-scm.com/docs/git-status) "takes a look at your git branch and inspects differences between the index file and the current HEAD commit." Uh-oh...I didn't cover HEAD in my last blog. In simple terms, think of the HEAD as the snapshot of your last commit. I find this is helpful to run as it helps you understand where you are right now in the repository. Git status is git's way of knowing what you have and haven't committed locally to the main or master branch. So if you've changed anything from your last commit (like we did earlier), when you run **git status**, the terminal will indicate all changes like this:

![](Source%20Control%20Ninja%20Level%20-%20Pt%202%20Beginnings%2043a08651c0c24942980c0646ff18b160/file%201.jpg)

Don't forget that we added **The boy who lived.** to the harry.txt file. The HEAD now tracks that there's been a change to the harry.txt file.

Up next is the [git add .](https://git-scm.com/docs/git-add) command. This takes all changes made to the local repository and commits them to the index or HEAD. I prefer **git add .**, but there are many different ways to add files in for the commit. You can even add only a few files in versus all files. **git add .** adds in ALL files, so this means I'm taking the lazy way out. ;)

[git commit](https://git-scm.com/docs/git-commit) with a commit message (**git commit -m "First commit."**) comes next. This new commit contains the current changes you've made and inputs a log message that describes the changes. This is a requirement before you can merge changes or create a pull request. So do you have the flow thus far?

Here's the quick breakdown:

**1) git clone**

**2) change file**

**3) git status**

**4) git add .**

**5) git commit -m "First commit."**

Now, here's what it looks like in action:

I had to lighten up the screen shot a bit so you could see the -m in my git commit command.

And that's it! At least for now.

Let's review: What have you done? Well you've installed git, you've cloned a remote repository locally, you've edited the harry.txt file, and ran a few git commands to commit the changes to your local repository. These are the beginning steps toward understanding source control better. Even if you're the sole contributor to a repo, STORE YOU CODE IN SOUCE CONTROL! *gets off of soap box*

What you can do next is open up **dumbledore.txt** and write in **Dumbledore died.** Then follow the same flow as earlier to commit your next change. You could then open up the **snape.txt** file and type in **Snape's not a bad guy.** Same sort of thing as with the dumbledore.txt example: keep practicing these basic steps and it'll start making sense related to the flow.

So then what happens? Well, tune into the next blog where I show you how to work with a fork, push your local changes to a remote repository (fork), and open up a PR to main/master. This workflow specifically could help you contribute to Microsoft documentation in the future!

With that...there WILL be more blog posts...AND SOON!

Thanks for reading!