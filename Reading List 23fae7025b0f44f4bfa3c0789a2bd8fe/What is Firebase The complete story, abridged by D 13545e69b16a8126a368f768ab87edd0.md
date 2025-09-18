# What is Firebase? The complete story, abridged. | by Doug Stevenson | Firebase Developers | Medium

Column: https://medium.com/firebase-developers/what-is-firebase-the-complete-story-abridged-bcc730c5f2c0
Processed: Yes
created on: November 5, 2024 3:06 PM

# What is Firebase? The complete story, abridged.

![](https://miro.medium.com/v2/resize:fill:88:88/1*f87Jht4FrS90aEKRy8BjiA.jpeg)

![](https://miro.medium.com/v2/resize:fill:48:48/1*DoeJ0VLtJ0TX9yZdw_FFfg.png)

[Doug Stevenson](https://medium.com/@CodingDoug?source=post_page-----bcc730c5f2c0--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F6a53613f4e6d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffirebase-developers%2Fwhat-is-firebase-the-complete-story-abridged-bcc730c5f2c0&user=Doug+Stevenson&userId=6a53613f4e6d&source=post_page-6a53613f4e6d----bcc730c5f2c0---------------------post_header-----------)

Published in

[Firebase Developers](https://medium.com/firebase-developers?source=post_page-----bcc730c5f2c0--------------------------------)

·

21 min read

·

Sep 24, 2018

Hello! I’m Firebase!

![](https://miro.medium.com/v2/resize:fit:300/1*R4c8lHBHuH5qyqOtZb3h-w.png)

It seems like there’s an app for everything these days. Well, almost everything. I haven’t found an app that helps me remove impacted earwax. It happens to me sometimes, and it’s super obnoxious. But someone could build it! I’ll contribute to your Kickstarter.

If you’re the enterprising sort of person that tackles humanity’s urgent needs with a mobile app, you’ll want to know about [Firebase](https://firebase.google.com/). Firebase is Google’s mobile application development platform that helps you build, improve, and grow your app.

Here it is again in bigger letters, for impact:

> Firebase is Google’s mobile application development platform that helps you build, improve, and grow your app.
> 

And now you know what Firebase is. In theory, this blog post could be done!

# Beyond the marketing copy

I have mixed feelings when someone asks me “What is Firebase?” (which happens a lot, since I work on it). On the one hand, I’m glad to know there’s interest! Thanks for asking! On the other hand, there’s so much to it, *where do I even begin*? The definition above is accurate, but it’s not very specific at all.

I like retro games, so I’ll try to explain Firebase again with a picture:

[](https://miro.medium.com/v2/resize:fit:657/0*teR3uob3sLgjVCxH)

This makes a lot of sense — if you are me! But I understand that many of you are not me, so I’m sorry if you weren’t helped by that.

All joking aside (for the remainder of this paragraph only), Firebase is a toolset to “build, improve, and grow your app”, and the tools it gives you cover a large portion of the services that developers would normally have to build themselves, but don’t really want to build, because they’d rather be focusing on the app experience itself. This includes things like analytics, authentication, databases, configuration, file storage, push messaging, and the list goes on. The services are hosted in the cloud, and scale with little to no effort on the part of the developer.

When I say “hosted in the cloud”, I mean that the products have backend components that are fully maintained and operated by Google. Client SDKs provided by Firebase interact with these backend services *directly*, with no need to establish any middleware between your app and the service. So, if you’re using one of the Firebase database options, you typically write code to query the database *in your client app*.

This is different than traditional app development, which typically involves writing *both* frontend and backend software. The frontend code just invokes API endpoints exposed by the backend, and the backend code actually does the work. However, with Firebase products, the traditional backend is bypassed, putting the work into the client. Administrative access to each of these products is provided by the [Firebase console](http://console.firebase.google.com/).

You can make your backend vanish!

[](https://miro.medium.com/v2/resize:fit:700/0*DylbZPWyXT7S0Fn5)

If you identify as a “backend engineer”, you might be hearing this and thinking that your job is being eliminated! ***“OMG, no more backends — now I have to learn frontend development!”*** This isn’t really true, as there are some things that simply *ought* to be on the backend for a variety of reasons. Firebase recognizes this, and offers a way to do some backend development, where it makes sense for the app you work on. So, don’t worry, your job is safe, and I’ll talk more about this later on.

Sorry if I gave you a scare, backend devs.

[](https://miro.medium.com/v2/resize:fit:283/0*0YNOhqgNYL48PoZj)

Because of the way Firebase products work, some people might call Firebase a “[platform as a service](https://en.wikipedia.org/wiki/Platform_as_a_service)” or a “[backend as a service](https://en.wikipedia.org/wiki/Mobile_backend_as_a_service)”. I’ve never really felt comfortable wedging Firebase fully into one of these boxes. Firebase is Firebase. (I know, this statement obviously doesn’t help explain *what Firebase is*, which is supposed to be the purpose of this article!)

Anyway, at the time of this writing, I count 17 individual products in the Firebase suite. Here’s another helpful picture:

The Firebase suite. Sweet!

[](https://miro.medium.com/v2/resize:fit:700/0*HORJhBhTELtW9qQw)

It’s said that a picture is worth a thousand words. I counted 37 in the picture, including two things that are not really words. Turns out, you’re in luck today, because I’m going to try to use up the other metaphorical 963 words in this article to help explain that picture a little better. But I’m not going to count them.

And if you want to find out what Firebase *is not*, well, you’ll have to read all the way to the end of this post. **No skipping ahead! You’ll miss all the jokes!**

# What sort of apps is Firebase good for?

There’s really no limit to the *types* of apps that can be helped by Firebase products. There are only limits to the platforms it can be used on. [iOS](https://firebase.google.com/docs/ios/setup) and [Android](https://firebase.google.com/docs/android/setup) are the primary targets for the Firebase SDKs, and there’s increasing support for [web](https://firebase.google.com/docs/web/setup), [Flutter](https://firebase.google.com/docs/flutter/setup), [Unity](https://firebase.google.com/docs/unity/setup), and [C++](https://firebase.google.com/docs/cpp/setup). You should also know there’s an [Admin SDK](https://firebase.google.com/docs/admin/setup) available for a variety of languages, to be used with any backend components you might require.

On top of those SDKs, there’s a library called FirebaseUI ([Android](https://github.com/firebase/FirebaseUI-Android), [iOS](https://github.com/firebase/firebaseui-ios), [web](https://github.com/firebase/firebaseui-web)) that provides a bunch of helpful utilities to make development with Firebase even easier. And there are also projects such as [AngularFire](https://github.com/angular/angularfire2) that wrap the web SDKs for use with Angular. These are open source. [Firebase likes open source.](https://firebaseopensource.com/)

Here are a couple examples of developers using Firebase.

Greta builds mobile games with Unity:

This is Greta, and definitely not a stock photo of someone else.

![](https://miro.medium.com/v2/resize:fit:700/1*Uk5XNs-sf2AMC6rtWyj9GA.jpeg)

And Shawn is building a social networking app:

This is Shawn, also not a stock photo. These are totally real developers.

![](https://miro.medium.com/v2/resize:fit:700/1*EGuo7gHsMf7rPoq2gHYwjg.jpeg)

You can tell from the looks on their faces that they’re *having a blast* building apps with Firebase.

Greta doesn’t think of herself as an “app developer”. Games are not apps! Or are they? I don’t know. But games and traditional apps have a lot of similar needs that could be met by Firebase. For fun, I just imagine that games are apps with a highly customized UI, that happen to have a *really* strong [gamification](https://en.wikipedia.org/wiki/Gamification) strategy. Anyway, Greta and Shawn face similar challenges, despite the fact they’re building very different things.

To get a sense of what Firebase products actually do in an app, I’ll go through the individual products from that image above. You saw, in that image way up there, three main groups of products: “build”, “improve”, and “grow” (but these categorizations are not strict). I’ll talk about the “build” group first, and give some specific cases where Greta and Shawn make use of each product.

# Build your app — creating the “guts”

The “build” group of products are these:

**Authentication** — user login and identity

**Realtime Database** — realtime, cloud hosted, NoSQL database

**Cloud Firestore** — realtime, cloud hosted, NoSQL database

**Cloud Storage** — massively scalable file storage

**Cloud Functions** — “serverless”, event driven backend

**Firebase Hosting** — global web hosting

**ML Kit** —SDK for common ML tasks

[**Firebase Authentication**](https://firebase.google.com/products/auth/) takes care of getting your users logged in and identified. This product is essential to getting some of the other products configured properly, especially if you need to restrict access to per-user data (which nearly every app will want to do).

What’s special about Firebase Authentication is that it makes easy to perform secure logins, which is incredibly difficult to implement correctly on your own. And it’s “federated”, which is to say that the [United Federation of Planets](http://memory-alpha.wikia.com/wiki/United_Federation_of_Planets) encourages its use. Here’s what the Federation’s Captain Picard thinks of implementing your own auth system:

Jean-Luc has experienced enough grief already — please don’t make it worse.

[](https://miro.medium.com/v2/resize:fit:512/0*a2Po4lM88jMF39AU)

Others may say that “[federated identity](https://en.wikipedia.org/wiki/Federated_identity)” means that you can link a user’s accounts from the various identity providers (Facebook, Twitter, Google, GitHub) into a single account on Firebase Authentication. But I like my definition better.

In any event, I strongly recommend learning Authentication and integrating it into your app *first*, which will hopefully prompt you to think about the security of per-user data that you might store using some of the other “build” group products.

[**Firebase Realtime Database**](https://firebase.google.com/products/realtime-database/) and [**Cloud Firestore**](https://firebase.google.com/products/firestore/) provide database services. I listed them both as “realtime, cloud hosted, NoSQL databases”. They have individual strengths and weaknesses, and you may need to [do some research](https://firebase.google.com/docs/firestore/rtdb-vs-firestore) to figure out which one is better for your needs. Hint: start with Cloud Firestore, as it likely addresses more of your needs (and it’s also massively scalable). You can use either one, or both together, if that suits your app.

It’s worth noting that Firestore is technically a [Google Cloud product](https://cloud.google.com/firestore/), not a Firebase product. Why is it listed with Firebase? Firebase adds SDKs to use in your mobile app to make direct data access possible, removing the need for that pesky middleware component. There are other products listed here with a similar relationship with Google Cloud, which I’ll also note.

What’s really special about these databases is that they give you “realtime” updates to data as it changes in the database. You use the client SDK to set up a “listener” at the location of the data your app wants to use, and the listener gets invoked with that data repeatedly, every time a change is observed. This lets you keep your app’s display fresh, without having to poll the data of interest.

I’m paid a cash reward to put this GIF in every presentation where I mention “realtime data”.

[](https://miro.medium.com/v2/resize:fit:700/0*pigb9EpYRdzTuMIX)

With realtime data like this, our friend Greta uses realtime data in her games to maintain live leaderboards of in-game events for everyone to see. Shawn uses them to provide messaging between friends on his social network. Because we just don’t have enough chat apps out there!

Fun fact: Realtime Database was the original “Firebase” before it joined Google in 2014. To this day, people still colloquially (but incorrectly) refer to Realtime Database as just “Firebase”. But you shouldn’t do that, because it’s wrong.

*You should always be right on the internet, and argue fiercely. Firebase is a **platform**, folks, not a* database*! ([view this comic on XKCD](https://xkcd.com/386/))*

[](https://miro.medium.com/v2/resize:fit:300/0*lsrpDWHdRP3Jle6b)

[**Cloud Storage**](https://firebase.google.com/products/storage/) provides massively scalable file storage. It’s also technically a [Google Cloud product](https://cloud.google.com/storage/), not a Firebase product. With Cloud Storage *for Firebase*, you get client SDKs to use in your app that enable you to upload and download files directly to and from your Cloud Storage “[bucket](https://cloud.google.com/storage/docs/key-terms#buckets)”.

This “lolrus” has a Cloud Storage “bucket” that stores “files”. Unfortunately, it didn’t use security rules to protect the contents of the bucket!

![](https://miro.medium.com/v2/resize:fit:600/1*Oi_o9J2iZ8omfis1TLTUmA.jpeg)

Greta’s games use Cloud Storage to let people upload custom avatars for display in the game, and Shawn’s social network lets people share their photos with each other. Neither of them worry about running out of space, because Cloud Storage scales to *exabytes* of data. Have you ever stored an exabyte of data? Do you even have a mental model of how much data that is? I don’t! But I ran some numbers, and let’s just say it’s enough for every person on the planet to store 1000 high quality photos. Ping me if you publish the app that achieves this feat!

**Authentication works extremely well with these three products** with the use of **security rules** (for [Realtime Database](https://firebase.google.com/docs/database/security/), [Firestore](https://firebase.google.com/docs/firestore/security/overview), and [Cloud Storage](https://firebase.google.com/docs/storage/security/)) that you can use to set access control to your data at the source. This ensures that clients can access that data *only* in the ways you allow, avoiding the tragic situation with the lolrus above. Users signed into an app with Authentication will automatically provide an identification token that you can use in your rules to protect who can read and write which items of data. So, if you store personal data about your users, *definitely* use Firebase Authentication with security rules to limit access appropriately. You may even get a gentle reminder from Firebase if your rules appear overly permissive.

***You can’t be ignorant about “personal data”.** I mean, you can, but that’s totally uncool. Use Firebase Security Rules! ([view this comic on XKCD](https://xkcd.com/1971/))*

[](https://miro.medium.com/v2/resize:fit:700/0*piNaOr475_vHrk7O)

[**Cloud Functions**](https://firebase.google.com/products/functions/) is yet another a [Google Cloud product](https://cloud.google.com/functions/) that works well with other Firebase and Cloud products. Using the Firebase SDKs for Cloud Functions, you can write and deploy code, running on Google “serverless” infrastructure, that automatically responds to events coming from other Firebase products. That’s right, it’s serverless!

Thanks for the tip, Morpheus.

![](https://miro.medium.com/v2/resize:fit:462/1*OAJmOpmApIcx5WDcJ-OFRA.jpeg)

When people say “serverless”, they don’t suggest a lack of servers. With a serverless backend architecture, there are still servers in play, you just don’t have to know much about them. You don’t provision, maintain, scale, or do any of the devops required in a traditional (or “serverful”, my word) architecture. You just write and deploy code, and Google does the rest.

Cloud Functions for Firebase is the *one* product of the entire Firebase suite that actually has you writing backend code. In my opinion, some types of code *should* be running in a controlled backend environment. And you should be giving those backend devs a job, because of that promise I made earlier.

The list of things you can do with Cloud Functions is ginormous — [take a look at all these samples](https://github.com/firebase/functions-samples/)! But I’ll boil it down to one main concept: Firebase products (database, storage, auth, etc) emit events when data changes within the product, and your code deployed to Cloud Functions is triggered in response to those events.

Shawn uses Cloud Functions to automatically delete data from his database and storage when someone deletes their account (because user privacy must be protected in many situations, and getting billed for unused data is terrible). Greta uses Cloud Functions to execute game logic and scoring on a secure backend, because she knows that hackers may try to cheat by reverse engineering her game code.

This really is what it looks like when someone hacks your app. Hollywood got it right — don’t hate on them so much!

![](https://miro.medium.com/v2/resize:fit:700/1*qfQIiOG0h816V8WJlkqIcQ.jpeg)

[**Firebase Hosting**](https://firebase.google.com/products/hosting/) is a secure, global web hosting CDN (Content Delivery Network). It’s really good at quickly delivering static content (HTML, CSS, JS, images) using servers that are close to your users. And you can get it set up quickly, with or without your custom domain, along with a provisioned SSL certificate that costs you nothing.

Firebase Hosting has one important point of integration with the rest of Firebase, and that’s [through Cloud Functions](https://firebase.google.com/docs/hosting/functions). Firebase Hosting lets you proxy the request and response to and from Cloud Functions when writing HTTP type functions. And, even better, it’ll cache the responses from your functions, if you configure them properly. What a great way to build a “RESTful” API!

Truth be told, I can’t tell you exactly what “RESTful” means. I’m assuming you know. Feel free to rant in the comments.

[](https://miro.medium.com/v2/resize:fit:400/0*ZlcMUyzvn6uCzH0Z)

[**ML Kit for Firebase**](https://firebase.google.com/products/ml-kit/) lets you take advantage of a wealth of machine learning expertise from Google, without having to know anything about ML. This is great for me, because I don’t know anything about ML! But what I get out of ML Kit is the ability to recognize things that my device camera captures, such as text, faces, and landmarks. And it can work on my mobile device with very limited computing power. For those of your with more advanced understanding of ML (again, not me), you can upload a TensorFlow model for more sophisticated use cases. The roadmap for machine learning products at Firebase will be fully “federated”:

[*Dr. Noonian Soong](http://memory-alpha.wikia.com/wiki/Noonian_Soong) is going to be Google’s employee #540138478.*

[](https://miro.medium.com/v2/resize:fit:400/0*dUagSFC-GnExoasL)

Shawn uses ML Kit to locate faces in the photos and videos uploaded by the users of his social network, then he performs some image manipulation on them. Greta doesn’t use ML Kit yet, because there’s no Unity implementation for the SDK yet. Dang! But if there was, she might use it to let people scan QR “coupon” codes for free promotional in-game items.

And that’s it for the “build” group. Lots of useful tools in there! But there’s still much left to discuss about Firebase.

![](https://miro.medium.com/v2/resize:fit:700/1*PMBwoU5bWkso8M2A1ocS9Q.png)

# Grow your app — attract and retain users

The “grow” group of products are these:

**Analytics** — understand your users, and how they use your app

**Predictions** — apply machine learning to analytics to predict user behavior

**Cloud Messaging** — send messages and notifications to users

**Remote Config** — customize your app without deploying a new version; monitor the changes

**A/B Testing** — run marketing and usability experiments to see what works best

**Dynamic Links** — enable native app conversions, user sharing, and marketing campaigns

**App Indexing** — re-engage users with Google Search integration

**In-App Messaging** — engage your active users with targeted messages

[**Google Analytics for Firebase**](https://firebase.google.com/products/analytics/) is the core of the “grow” offering. If you need to better know your users, and how they make use of your app, Analytics can show you that. When you publish an app for the first time, you might have an idea who your user base is going to be, where they live, and how they might use your app. And those ideas might be completely wrong in practice! The only way to know for sure is to collect data, and that’s where Analytics helps.

Turns out, 9 out of 10 adults prefer Pokemon over CoD. Who knew?

[](https://miro.medium.com/v2/resize:fit:600/0*I-mRTnCm3-SiZ0yP)

There’s *waaay* more to Google Analytics for Firebase than can be summarized here, but there’s one important thing to know, and that’s the concept of an “audience”. An audience is a group of users who have taken some predefined actions in your app, share some user properties, or have common device characteristics. You define the requirements for someone to become a member of an audience, and Analytics will figure out which users belong to it, by analyzing the stream of events that your app generates over time. This concept of an audience segmentation is powerful, because you can *target that audience* with other Firebase products in the “grow” category. Keep this concept of audience in mind as you read on!

Greta’s game defines an audience of “players who have completed level 10, and made an in-game purchase” (core players). Shawn’s social network app defines an audience of “people between the ages of 18–24, who have at least 50 friends on the network” (social young adults). Once these audiences have been defined in the Firebase console, and apps are updated to send the correct events, the audiences will collect members. Greta and Shawn can then target the audience members with information and offers of interest to these groups.

[**Firebase Predictions**](https://firebase.google.com/products/predictions/) builds on top of the data collected by Analytics to make predictions (no surprises there) about which users in your app are likely to *churn* (not open your app), and which will *spend* (money, on your app). These two new categories of users are kind of like Analytics audiences, except you aren’t required to do anything to define how a user ends up in one of these groups. This is the magic of machine learning! It’s just like the magic of the Sorting Hat from Harry Potter, except no one frets about getting sorted into Hufflepuff.

No one would “spend” to watch Harry Potter “churn”.

[](https://miro.medium.com/v2/resize:fit:400/0*wmU0E8P9QCkX7BaC)

Analytics and Predictions are both interesting, but they don’t really *do anything* for your app. But when you team them up with other Firebase “grow” products, you can achieve truly magical results! Let’s see how that works.

[**Firebase Cloud Messaging**](https://firebase.google.com/products/cloud-messaging/) lets you deliver push messages to indicate something of interest to your app, or the user of your app. There are two ways to send a message. First, you can write code on your backend to *ping your app* when something gets updated that your app might want to respond to (for example, a chat room notification). Second, you can compose a message in the Firebase console to *ping your users* with information of interest. It’s the second case — direct user notifications — that I’m more interested in today.

One thing you can do with user messaging, since it’s integrated with Analytics and Predictions, is send a message to members of a particular Analytics audience or Predictions groups. This is valuable, because you can target users with information that they’re more likely to be interested in and click on, keeping them engaged with your app. Targeting a specific group with relevant content is better than just blasting messages to everyone. The reason is clear enough. To illustrate that, here’s a picture of someone getting too many push messages that are irrelevant to their interests:

Seriously, don’t be that spammy app — you’ll get uninstalled. Send only relevant and desired messages to your users, at a reasonable frequency.

![](https://miro.medium.com/v2/resize:fit:700/1*VVVft6nRt-YKuZSnP9eAWQ.jpeg)

Greta might notify her core players audience of new game items for sale. And Shawn might send a reminder to his social young adults to rate and discuss their favorite night clubs. In both cases, people are getting messages they’re more likely to act on, and fewer people are getting spammed, with assistance from Analytics.

[**Firebase In App Messaging**](https://firebase.google.com/products/in-app-messaging/) helps you show targeted, customizable messages to your users to engage with key features of your app. You might be wondering “well, how is this different than FCM?” (And I’m so glad you asked! It means you’re still paying attention!) The key difference here is that messages from FCM originate from a server you control (including the Firebase console), whereas messages from FIAM originate from within the app itself (but configured in the console). The message is guaranteed to be displayed while your user is actually using the app. But FCM and FIAM are alike in that they’re both deeply integrated with Analytics and Predictions.

It’s entirely possible that a message sent by FCM simply won’t be of interest to the user, because of its timing or relevance, or it was even accidentally dismissed. And did you notice that angry-looking woman above with the low tolerance for push messaging?! With FIAM, the message is delivered *at the very moment* it becomes relevant, based on criteria you define, determined by the user’s behavior as measured by Analytics events and Predictions groups.

Relevant messages hold the attention of cats on the internet.

[](https://miro.medium.com/v2/resize:fit:555/0*fhQe615QEOfFCsu2)

For example, Greta’s games allow players to earn virtual currency as they play, and uses FIAM to remind people who *just* earned their first virtual dollar that they can spend it in the game’s store. And Shawn’s social network points out to users the option for sharing content if they’ve been using the app for a while but haven’t yet discovered it.

[**Firebase Remote Config**](https://firebase.google.com/products/remote-config/) lets you make dynamic changes to your app’s behavior and appearance without having to publish an update to your app. The general idea with Remote Config is that you define a bunch of configuration parameters in the Firebase console. Then, your app uses an SDK to periodically fetch those values and make use of them as required. You can think of Remote Config as kind of like a giant set of cloud-hosted key/value pairs. This may sound like a simple database, but there’s far more you can do with it than you might initially imagine.

Remote Config lets you remotely control the way your app works. I use it to “Firebase and chill”.

![](https://miro.medium.com/v2/resize:fit:700/1*T-xVSRAiQGi2R3Wmmabgnw.jpeg)

The way that Remote Config really shines is through its ability to [define conditions for each parameter](https://firebase.google.com/docs/remote-config/parameters). One type of condition lets you [target particular values to specific Analytics audiences](https://firebase.google.com/docs/remote-config/config-analytics). Another lets you target the Predictions groups for “churn” or “spend”. This helps you implement a number of useful features in your app, including giving high-value audience members a premium experience, or infrequent users an incentive to stay.

Shawn uses Remote Config to dynamically promote which social networking features should be promoted to certain users. Greta’s games use it to fine tune the difficulty of some levels and game mechanics, without having to build and publish a new version of the game.

[**Firebase A/B Testing**](https://firebase.google.com/products/ab-testing/) takes the tight integration between Analytics, Remote Config, and FCM *even further*. I imagine you’re constantly making changes to your app, which is good. However, you probably don’t know for sure ahead of time if it’s going to help or hurt, unless you conduct your own studies. If you don’t have those kinds of resources, you can perform your own studies, and back them up with data. If you can figure out how to measure success, you can use Firebase A/B Testing to set up an experiment and conduct it on a handful of users before making a decision. This is wise, because making an uninformed decision about a change to your app could cause this to happen to your users:

OMG you did what to your app??

![](https://miro.medium.com/v2/resize:fit:700/1*5qEuO5SGr6zKWUSMXtyWuw.jpeg)

[**Firebase Dynamic Links**](https://firebase.google.com/products/dynamic-links/) builds on the existing concept of a “deep link” that launches your app to a particular screen or customized experience. Deep links work great if the user already has your app installed, but they don’t work well at all if they have to go install it first. Dynamic links improves on this by surviving the app installation process. When the user clicks a dynamic link, and the app isn’t already installed, they’re directed to the appropriate app marketplace to install it. Then, when the user launches the app for the first time, the context of the link is retained, and the app can start with the experience that you originally intended. Oh, and they work across platforms as well, so you don’t need to have different links for each of your Android, iOS, and web apps.

That little green dude down there isn’t a Dynamic Link. Just your standard Link.

![](https://miro.medium.com/v2/resize:fit:657/1*yDCGm79qB1jXSE7GkSXULw.png)

Greta uses Dynamic Links to conduct marketing campaigns where new users get a free in-game item when they follow the link to install the game for the first time. And Shawn uses them to enable users to easily share posts on his social network, no matter where or how the link is shared.

# Improve your app — stability and performance

The “improve” group of products are these:

**Test Lab** — scalable and automated app testing on cloud-hosted devices

**Crashlytics** — get clear, actionable insight into your app’s crashes

**Performance Monitoring** — gain insight into your app’s performance issues

[**Firebase Test Lab**](https://firebase.google.com/products/test-lab/) provides you access to a large variety of iOS and Android devices, in additional to virtual Android devices, for testing your app. If you build apps for mobile devices, you probably have at least one device at your desk for development and testing. But this one device certainly isn’t representative of what your users are actually using. Mobile devices come in all kinds of sizes, from many different manufacturers, with many different versions of the OS in play. It’s royally expensive and time consuming to try to maintain your own selection of devices, then actually test on all of them.

[*DIY device lab, DIY pain.](https://www.businessinsider.com/why-android-is-so-frusterating-for-developers-2014-10) Why would you do this to yourself?*

[](https://miro.medium.com/v2/resize:fit:700/0*AlkwYbAvfwITGNoD)

Test Lab solves this by hosting a large selection of actual, physical devices that will install your app and run your test suite (Android: Espresso, iOS: XCTest) against it. It also can perform a fully automated test that requires no additional coding, for the truly lazy among us (which is, like all of us, amirite?).

The most interesting man in the world is also the world’s worst software engineer.

[](https://miro.medium.com/v2/resize:fit:615/0*pTzn8wXY58h0gng9)

[**Firebase Crashlytics**](https://firebase.google.com/products/crashlytics/) is the best crash reporting tool in the world. Seriously, it’s the best. I don’t know why I’m even bothering to type stuff about it. It’s been around since forever. Just use it. It’s even integrated with Analytics, so you can measure how crashes are affecting the way users use your app (possibly by uninstalling it). App crashes aren’t even funny, so I won’t bother with a funny picture to illustrate a concept that everyone understands.

Oh, who am I kidding? Here’s the picture.

App crashes are not “federated”.

[](https://miro.medium.com/v2/resize:fit:500/0*KiJiXRUqPH5U3Rpu)

It’s the home stretch! Only one more product to discuss!

[**Firebase Performance Monitoring**](https://firebase.google.com/products/performance/) gives you insights into your app’s performance issues, from your users’ point of view, by measuring its HTTP requests, startup time, and other code using its API. The magic in this Firebase product is that it starts measuring the HTTP request and startup time without you having to write more than a couple lines of code, with the results visible in the Firebase console. Add a few more lines to time anything else your app might be doing.

I’ll underscore the importance of getting metrics *from your users’ point of view*. You probably develop your app using fast devices on fast wifi networks. This setup almost certainly isn’t similar to the conditions that your users face all over the world, on flakey mobile networks with low-end devices. If you want to understand the pain that your users *actually* face when using your app, try pulling out your nose hairs with a pair of rusty pliers. Then, when you finally realize that was a pointless exercise, integrate Performance Monitoring into your app, and study its results in the Firebase console. You’ll be able to see exactly how problematic your app might be in different parts of the world, on different networks, on different devices, with different versions of the OS. And you’ll see which HTTP endpoints are causing the biggest delays in your app, giving you a target on which to focus your optimizations.

[](https://miro.medium.com/v2/resize:fit:552/0*xkY_8sb_3e0-TO9h)

What’s not immediately obvious is how the three products in the “improve” category work well together, even though they don’t have direct integrations like those in the other Firebase categories. What you can do is run a special version of your app in Test Lab, and when that’s done, you’ll be able to see more detailed crash information in Crashlytics (if it crashes, of course) and better performance measurements in Performance Monitoring. I also know someone who was able to use a Crashlytics crash report to find a performance problem in Performance Monitoring. You can be clever like this too!

# Whew, that was a lot of text and pictures

You made it to the end! Guess what? You just found out that **Firebase has a lot of stuff in it**. So what do you take away from all this? I’ll boil it down to a few points so you can get back to building your app:

- Firebase is Google’s mobile application development platform. *(YES, THAT AGAIN.)*
- You’re gonna save a ton of time and money using Firebase products rather than trying to build them yourself.
- You can use all of it, or none of it, or just the bits you want.
- All those bits are designed to work well together, managed in one console.
- You gonna use Firebase to build that earwax-busting app already?

# Addendum: What Firebase isn’t

That’s all great info up there about what Firebase *is*, but it’s come to my attention that we also need a reference for everything that Firebase *is not*. For the record:

- Firebase is a platform, not (just) a database (any more). We already covered this.
- It’s “Firebase”, not “FireBase”. If you write it that way, you will be punched in the throat.
- Similarly, it’s “Firestore”, not “FireStore”, but the punch goes to the kidney.
- It’s NEVER abbreviated FB. Do that, and you’ll be yelled at until your ears bleed.
- If Firebase was an element, it would combat fluorine for the symbol F.
- It’s “realtime”, not “real-time”, despite the suggestion of your grammar checker.
- It’s “Cloud Functions for Firebase”, not “Firebase Functions”. Go ahead, search the docs and prove me wrong. I dare you.
- It’s “Cloud Firestore”, not “Firebase Firestore”. Seriously, who needs that much fire??
- Cloud Firestore is not Cloud Filestore is not Cloud Datastore is not Cloud Memorystore is not Cloud Storage. Got it?

![](https://miro.medium.com/v2/resize:fit:1000/1*f2IVAl0TbsfES9cFGYr40g.png)