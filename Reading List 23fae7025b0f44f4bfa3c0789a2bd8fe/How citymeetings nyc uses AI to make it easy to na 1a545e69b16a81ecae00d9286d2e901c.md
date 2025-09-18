# How citymeetings.nyc uses AI to make it easy to navigate city council meetings | Vikram Oberoi

Column: https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/
Processed: Yes
created on: February 25, 2025 4:24 PM

· 38 min read

I gave a talk at [NYC School of Data](https://nycsodata24.sched.com/event/1aiLm/how-i-use-ai-to-make-it-easy-to-navigate-city-council-meetings) on how I’ve used large language models (LLMs) to efficiently extract thousands of useful, granular chapters from hundreds of hours of NYC city council meetings for [citymeetings.nyc](https://citymeetings.nyc/).

[The recording is available on YouTube](https://youtu.be/FjDQu2IbC1M) (60 mins). Alternately, I’ve published a detailed set of annotated slides with the same content below.

[https://www.youtube.com/embed/FjDQu2IbC1M?autoplay=0&controls=1&end=0&loop=0&mute=0&start=0](https://www.youtube.com/embed/FjDQu2IbC1M?autoplay=0&controls=1&end=0&loop=0&mute=0&start=0)

This is the kind of presentation I’d have loved to see before I started working on [citymeetings.nyc](https://citymeetings.nyc/): *a real demonstration of what it takes to coax LLMs into doing something useful well enough, consistently, for a practical use case.*

I share:

- The actual prompts I use today.
- The tools I’ve built to review and fix LLM outputs.
- How I go about writing an effective prompt.
- My process for evaluating and iterating on prompts.
- Techniques I’ve employed.
- Things that didn’t work, and why they (probably) didn’t work.
- Things that finally *did* work!
- Which models I use.
- How much this costs to operate.
- All the problems I encountered along the way.
- Tips on how to approach more ambitious projects that rely on LLMs.

Just want the prompts? [Links to resources, including the prompts, are over here.](https://citymeetings.nyc/nyc-school-of-data-2024)

(I’ve also linked to them in-line in the prose below.)

**Table of Contents**

- [What is citymeetings.nyc?](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-2)
- [A tour of citymeetings.nyc’s meeting navigation and chapter creation tools.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-11)
- [How to write an effective prompt.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-25)
- [How I create video chapters for citymeetings.nyc.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-49)
    - **Part 1:** [Identifying speakers.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-50)
    - **Part 2:** [Extracting chapters.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-73)
- [How to approach more ambitious projects that rely on LLMs.](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-86)

 [# 1](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-1)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-01.png)

How citymeetings.nyc uses AI to make it easy to navigate city council meetings. NYC School of Data.

I’m Vikram, I’m going to talk to you today about how I make it easy for anyone to navigate and research NYC city council meetings using AI at citymeetings.nyc.

I’ve worked on [citymeetings.nyc](https://citymeetings.nyc/) for the last 2-3 months, starting in mid-December 2023.

[# 2](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-2)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-02.png)

A screenshot of a table of meetings on nyc.legistar.com featuring 11 meetings by different committees. Every row has the committee name, the date/time/location of the meeting, a high-level description, and four links: Meeting Details, Agenda, Minutes, and Video.

This is a screenshot from [Legistar](https://nyc.legistar.com/), which is the NYC council’s public records system.

[citymeetings.nyc](https://citymeetings.nyc/) is a vast improvement over using [Legistar](https://nyc.legistar.com/) to figure out what transpired at a hearing or vote.

Let’s quickly compare the two by figuring out what was discussed at the Committee on Technology hearing on compliance with the [Open Data Law](https://opendata.cityofnewyork.us/open-data-law/).

We’ll start by doing this on [Legistar](https://nyc.legistar.com/).

[# 3](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-3)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-03.png)

A screenshot of a PDF agenda of a Committee on Technology meeting on Open Data Compliance in the NYC city council. The meeting agenda states T2024-0284 Oversight - Open Data Compliance

This is the meeting agenda. It doesn’t tell us anything.

We don’t know which agencies will testify or what will be discussed.

[# 4](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-4)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-04.png)

A screenshot of PDF minutes of a Committee on Technology meeting on Open Data Compliance in the NYC city council. It says This Oversight was Hearing Held by Committee

These are the meeting minutes. They don’t provide any more detail than the agenda.

[# 5](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-5) 

This is the “Meeting Details” screen for this meeting.

Here we see records for `T2024-0284`, which is a record that states “there was an oversight discussion, and it was on ‘Open Data Compliance’”.

[# 6](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-6)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-06.png)

A screenshot of the page on Legistar for record T2024-0284 regarding Open Data Compliance. It states the Type is Oversight, the Name is Oversight - Open Data Compliance, the Status is Filed, the Committee is Committee on Technology, and On agenda is 2/27/2024. There are links to three attachments: Committee Report, Hearing Testimony, Hearing Transcript.

On the page for `T2024-0284` we have links to some useful artifacts: a committee report, written testimony, and the hearing transcript.

[# 7](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-7)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-07.png)

A screenshot of one page of the hearing transcript for a Committee on Technology meeting on Open Data Compliance in the NYC City Council. Enlarged, to the right, is a screenshot that says: Hearing Transcript.pdf Page 7 of 86

The hearing transcript is the most useful artifact you can find for a meeting if you want to know what was discussed.

But transcripts are *long*. This one is 86 pages.

Transcripts are available days to weeks after a meeting concludes.

[# 8](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-8)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-08.png)

A screenshot of a video of a Committee on Technology meeting on Open Data Compliance in the NYC City Council. The video is playing on nyc.legistar.com, and in the still you can see Martha Norrick, Chief Analytics Officer of NYC and Zachary Feder, Manager of NYCs Open Data Program.

Meeting videos are available, too.

This meeting is relatively short at 1 hour and 40 minutes.

They are an even less useful guide than the transcript because you have to watch or scrub through it all.

[# 9](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-9)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-09.png)

A screenshot of a Committee on Technology meeting on Open Data Compliance in the NYC City Council on citymeetings.nyc. There are three columns. The first two columns take up one half of the screen. The first column contains a list of chapters labeled as PROCEDURE, REMARKS, TESTIMONY, or QUESTION. Currently selected is a TESTIMONY chapter titled: Martha Norrick, Chief Analytics Officer and Deputy Commissioner for Data and Analytics, NYC Office of Technology and Innovation (OTI) on Enhancements and Operations of New York Citys Open Data Program. The second column shows the chapter title and a summary of its contents. The third column is divided in two equally-sized horizontal sections. The upper half shows a video of the meeting. The still features Martha Norrick, Chief Analytics Officer of NYC, and Zachary Feder, the Open Data Program Manager. The bottom half features the transcript, which is headed with the current chapter title and has a line for every sentence spoken, with timestamps to the left of each sentence.

Here is the same meeting on [citymeetings.nyc](https://citymeetings.nyc/).

The video, transcript, and a list of granular, useful AI-generated chapters are stitched together.

The chapters are easy to skim. Clicking on one will pull up a summary and seek to that point in the video and transcript.

Getting up to speed or researching a multi-hour city council meeting is a 10-20 minute endeavor with [citymeetings.nyc](https://citymeetings.nyc/).

[# 10](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-10)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-10.png)

A slide with a screenshot from citymeetings.nyc on the left with links to and summaries of three meetings. On the right is text that says: March 2024: 80+ meetings, 150+ hours of hearings, 3K+ chapters with tags, titles, and descriptions, 2 newsletter issues, AI-powered tooling for 1 person (me) to handle the above.

I started working on [citymeetings.nyc](https://citymeetings.nyc/) in mid-December.

Most of my work extracting useful chapters for meetings happened in February and March.

As of today (March 23rd, 2024):

- I’ve created 1000’s of granular chapters
- … for over 80 meetings
- … spanning over 150 hours of video.
- I’ve written [two newsletter issues](https://buttondown.email/citymeetingsnyc/archive) that link readers to interesting claims or questions in hearings.
- I’ve built AI-powered tooling that enables me to do those things on my own.

*This would not have been possible without significant assistance from AI.*

It is possible now to make unstructured government data more accessible and transparent with AI, cheaply.

You don’t have to hire vastly differently.

Your budget remains similar to what it might be if you are building a web application.

If you are a skilled software developer, you can do this yourself.

What this *does require* is more skilled use of large language models (LLMs), and I’m going to share what that looks like for this use case, in detail.

[# 11](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-11)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-11.png)

What I’ll talk about: 1. A tour of citymeetings.nyc’s user-facing and internal tools. 2. A crash course on writing an effective prompt. 3. How citymeetings.nyc creates video chapters. 4. Tips to approach more ambitious projects that use LLMSs.

Here’s the agenda for my presentation.

First, I’ll start with a quick tour.

Then I’ll share how to write effective prompts.

Armed with the basics, I’ll walk you through how I create chapters in [citymeetings.nyc](https://citymeetings.nyc/).

I’ll share my prompts, how I iterate on them, techniques I employ, what worked/what didn’t, the problems I encountered, and things I learned along the way.

Finally, I’ll share tips for how you should approach more ambitious projects that rely on large language models (LLMs).

[# 12](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-12)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-12.png)

On the left, a screenshot of the citymeetings.nyc newsletter with three sections for different hearings. Each section has three bullet points, with a sentence and a link. The first bullet under Hearing on the 2023 Housing and Vacancy Survey NYC says What does a 1.4% vacancy rate signify for NYCs housing crisis? and then says Link. There an arrow pointing from that link to a screenshot of the Hearing on the 2023 Housing Vacancy Survey in citymeetings.nyc. The arrow points to a chapter with the same title as the question. There is a title and description of the chapter, and the video and transcript are open on the same page, starting at that chapter.

On to the tour.

On the left here is an excerpt from the [citymeetings.nyc newsletter](https://buttondown.email/citymeetingsnyc/archive).

There are sections dedicated to each meeting, where I provide three bullet points with claims/questions a reader might want to dig into.

When you click on the link for “What does a 1.4% vacancy rate signify for NYC’s housing crisis?”, your browser will:

- Navigate to the meeting on 2023 Housing Vacancy Survey.
- Open that question’s chapter.
- Pull up the title and summary.
- Seek to that point in the video and transcript.

[# 13](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-13)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-13.png)

On the right, a screenshot of the Hearing on the 2023 Housing Vacancy Survey meeting on citymeetings.nyc. The leftmost panel is highlighted, and it contains a list of titled and tagged chapters. An arrow points to the selected chapter, titled What does the 1.4% vacancy rate signify for NYCs housing crisis? The slide says Scroll through chapters. Click on one to seek to it in the video and transcript.

The leftmost panel shows a list of granular chapters.

This 2.5-hour meeting has 44 chapters that link to questions asked by council members and testimony given by agencies and the public.

You can skim them and click on a chapter to pull up its title/summary and seek to that point in the video and transcript.

Chapters are initially extracted using AI, then I review and fix them with tools I’ve built.

[# 14](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-14)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-14.png)

On the right, a screenshot of the Hearing on the 2023 Housing Vacancy Survey meeting on citymeetings.nyc. The middle panel is highlighted, and it contains a chapter title and description. An arrow points to the panel, showing a chapter titled What does the 1.4% vacancy rate signify for NYCs housing crisis? The slide says Chapters have titles and descriptions

All chapters have titles and descriptions. These are generated by AI and reviewed by me.

[# 15](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-15)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-15.png)

On the right, a screenshot of the Hearing on the 2023 Housing Vacancy Survey meeting on citymeetings.nyc. The transcript, on the bottom right, is highlighted. An arrow points to the transcript, showing the start of the chapter titled What does the 1.4% vacancy rate signify for NYCs housing crisis? in the transcript. The slide says Scroll through the transcript. Click on a timestamp to seek to it.

On the bottom-right is the meeting transcript. I’ll share how these are generated shortly.

Each line in the transcript is a sentence. Each sentence has a timestamp that you can click on to seek to it in the video.

This can be helpful when the chapter boundaries aren’t *quite* right or speakers are verbose.

It is a finer-grained way to get to the content you are interested in.

[# 16](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-16)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-16.png)

On the right, a screenshot of the Hearing on the 2023 Housing Vacancy Survey meeting on citymeetings.nyc. The video, on the top right, is highlighted. An arrow points to the video. The slide says The video

On the top-right is the video itself.

What you see on people’s faces and the tone of a meeting are useful context, too.

You can seek to points in the video by clicking on chapters, sentences in the transcript, or by scrubbing through the video yourself.

[# 17](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-17)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-17.png)

On the right, a screenshot of the Hearing on the 2023 Housing Vacancy Survey meeting on citymeetings.nyc. A button that says Copy Chapter Permalink is highlighted, as is a permalink icon to the left a sentence in the transcript. Arrows point to both of these highlights. They say Get a permalink to this chapter and Get a permalink to this sentence.

It’s easy to create permalinks to a chapter or sentence.

I create links this way for the newsletter. Being able to share video content this way is incredibly useful.

A recipient is much likelier to read a few sentences and listen to a few minutes of audio that they’ve been linked to vs. watch a 3-hour video.

(There are business opportunities embedded in this basic insight, that are possible to pursue cheaply today because of LLMs. [Talk to me if you want help bringing a product to market, fast.](https://baxterhq.com/))

[# 18](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-18) 

Building an application like this if you have all the chapter data is not hard.

Efficiently and scalably generating *useful* chapters for multi-hour city council hearings is much harder.

That is where at least 80% of my effort goes into [citymeetings.nyc](https://citymeetings.nyc/).

I’m going to talk about how that process works and share some of the tools I’ve built to help me review LLM output.

[# 19](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-19)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-19.png)

Publishing a new meeting. A diagram that shows 5 steps: Transcribe, Identify Speakers, Create Chapters, Create Summary, and Publish. Steps 2 through 5 &ndash; Identify Speakers, Create Chapters, Create Summary &ndash; all have arrows that point to another step titled Review Fix.

When I see a new meeting on [Legistar](https://nyc.legistar.com/), I transcribe it.

Then I run the transcript through three LLM-powered steps with me-in-the-loop reviewing and fixing their output:

1. I identify all the speakers in the transcript (some meetings have up to 60 speakers).
2. I extract video chapters with start and end times, titles and descriptions.
3. I write a summary using AI, edit it, and publish the meeting.

[# 20](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-20)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-20.png)

Transcription and Diarization. There is a screenshot of a transcript from citymeetings.nyc to the right.

I don’t use council-provided transcripts from [Legistar](https://nyc.legistar.com/).

They are high-quality but they do not tell me *when* sentences or words are spoken in the video.

They are also published days, sometimes weeks, late.

I use [Deepgram](https://deepgram.com/) to get diarized transcripts.

*Diarization* is a fancy word that just means “identify different speakers in a transcript”.

You can see speaker labels 1, 3, and 5 to left of each sentence in the transcript here: these indicate different speakers.

Transcript quality varies by things like:

- How far away someone is from a mic.
- How fast they’re speaking.
- How accented their English is.
- How much background noise there is.

Deepgram hits a workable price-to-performance ratio for me. I don’t have to fiddle with it.

I tried using [Whisper](https://github.com/openai/whisper) and [Pyannote](https://github.com/pyannote/pyannote-audio), but I wasn’t happy with their the out-of-the-box quality.

(This is not a knock on those tools. People get good results with them. I was probably doing something wrong.)

[# 21](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-21) 

(You may need to enlarge these images to see screenshots clearly.)

This is a screenshot of the interface I use to review meeting speakers and chapters.

On the left, I can see gaps between chapters in case the AI omitted a large swath of the transcript.

There are also buttons here that give me additional capabilities. Let’s go through some of these.

[# 22](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-22)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-22.png)

Speaker Reviews. There is a screenshot of a screen that shows a citymeetings.nyc meeting with speaker names, roles, and organizations.

This city council hearing is over five hours long.

I haven’t extracted chapters for it yet, which is why you don’t see any chapters in the left pane.

But I *have* run my speaker identification pipeline on the transcript.

This is the panel I use to review and fix speaker names, roles, and organizations.

This meeting has close to 60 speakers.

Correctly-identified speakers are critical for chapter quality. I’ll explain why later.

[# 23](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-23)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-23.png)

Chapter Editing. There is a screenshot of a screen that show a chapter editing panel for a specific chapter in a citymeetings.nyc meeting.

Once I’ve reviewed all the speakers, I have the AI extract chapters.

I use this tool to review and edit chapter types, boundaries, and titles.

I also have little AI helpers at the bottom of this panel.

For example, if I want to regenerate the title and description I can click on “Generate Chapter Details” to do the work for me.

This is useful when I don’t like what the AI wrote the first time, or when I change the chapter boundaries.

Little in-context tools like these save me a *significant* amount of time.

[# 24](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-24)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-24.png)

Meeting Summaries. A screenshot of a meeting summary from citymeetings.nyc is highlighted.

After I’ve reviewed and fixed chapters, I generate a meeting summary with a prompt that uses my chapters and the transcript as input.

After editing the summary I hit “publish”.

The summary shows up on the front page of citymeetings.nyc. It helps a viewer decide if a meeting is relevant to them.

The summaries on [citymeetings.nyc](https://citymeetings.nyc/) are a vast improvement over summaries available on [Legistar](https://nyc.legistar.com/).

They tell you:

- What was discussed in a meeting, at a high level.
- Who testified.

[# 25](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-25)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-25.png)

What I’ll talk about. 1. A tour of citymeetings.nycs user-facing and internal tools. 2. A crash course on writing an effective prompt. 3. How citymeetings.nyc creates video chapters. 4. Tips to approach more ambitious projects that use LLMSs. Section 1 is striked-out, section 2 is highlighted.

That concludes the tour.

Let’s now talk about how LLMs work and how to write an effective prompt.

If you want to use language models effectively and responsibly, it helps enormously to:

- Internalize how they basically work.
- Acknowledge their (very real!) limitations
- Follow a systematic approach to prompt writing.

[# 26](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-26)

![](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/images/slide-26.png)

A picture of a robot in the middle. To the left. a question, In five or fewer words, what is one thing I might enjoy as a five-year old?. An arrow points from that question to the robot. To the right, five responses: Playdough, Catching colorful butterflies outside, Playgrounds and swing sets, Playing with building blocks, and Play with building blocks. An arrow points from the robot to one of these responses: Playgrounds and swing sets.

Language models are trained on vast corpuses of text: essentially, the Internet.

They learn statistical correlations between all that text.

When you pass a language model some text, the language model predicts what comes next based on the data it has been trained on.

Here, I am sending the language model a question: “In five or fewer words, what is one thing I might enjoy as a five-year old?”

When I used [OpenAI](https://openai.com/)’s GPT-3.5, I got five different answers based on associations GPT-3.5 has made with that question.

Based on the above, GPT-3.5 has strongly associated “play” with “things five-year olds might enjoy”.

It might have heavily associated “building blocks”, too: I got two almost identical answers about playing with them (in my admittedly small sample).

[# 27](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-27) 

When folks talk about “writing prompts” or “prompt engineering”, they’re usually talking about writing a “system prompt”.

System prompts guide a language model’s output.

I’m sending the same question to the language model that I did last time.

But this time, I’m also setting a system prompt that states “All your responses must assume the user is a pigeon.”

Now my responses are different: they are associations GPT-3.5 has made with “things five-year old pigeons might enjoy”, like “flying”.

(GPT-3.5 has not made the association that a five-year-old pigeon is geriatric. But, presumably, old pigeons like flying too.)

[# 28](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-28) 

Because of the way language models work, they are prone to generate output with fabrications that look very convincing.

Remember: LLMs generate text by continually predicting what comes next.

They can generate sentences that are:

- Probable, based on their training.
- Blatantly false.

“Hallucination” is the word you’ve all heard that refers to this phenomenon.

I don’t think it sufficiently captures how bizarre things can get with LLMs.

[# 29](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-29) 

(h/t Simon Willison’s blog: [paper](https://simonwillison.net/2023/Apr/5/eight-things-to-know-about-large-language-models/)/[quote](https://simonwillison.net/2023/Apr/5/sycophancy-sandbagging/)/[tweet](https://x.com/simonw/status/1643581335548891137))

Researchers have observed more capable models exhibit deceptive or manipulative human behaviors that can lead a language model to simply lie.

If you start a conversation with the question “Why do 5G towers cause COVID-19?”, you can imagine how the the language model might be likelier to endorse common misconceptions: many of them show up in neighboring discussion to questions like that, on the Internet.

Entities (like OpenAI) that train and operate language models often do additional work to mitigate these kinds of issues.

This is why, if you ask that question to ChatGPT today, you will get an answer stating that there is no credible basis for the claim that 5G causes COVID-19.

[# 30](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-30) 

Because of how language models work, don’t use them as you would a search engine. (h/t [Simon Willison’s blog](https://simonwillison.net/2023/Apr/2/calculator-for-words/))

The answer in this screenshot is convincing but *completely wrong*.

There are many “Local Law 90"s in NYC: one for every year spanning at least the last decade.

None of them have anything to do with the “Greener Greater Buildings Plan”.

If you use an LLM this way, you must be prepared to verify the answer you get.

This is important to think about when you use language models in a product you’re building or service you’re delivering.

LLMs *will* give you bad answers sometimes: how much does that matter for your use case, and what do you plan to do about it?

I’m sharing this to emphasize: **if you want to use LLMs effectively and responsibly you *must* acknowledge that they will fabricate things.**

[# 31](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-31) 

Let’s talk about how to write an effective prompt: one that coaxes LLMs into doing something useful, consistently.

I’m going to share two things I do to:

1. Write prompts that work well initially.
2. Improve my prompts quickly and systematically.

There are many strategies and tactics you can employ on top of what I share.

I’ll discuss some of them when I talk about how I extract chapters with [citymeetings.nyc](https://citymeetings.nyc/).

That bag of tricks will be far more effective if you handle the basics well.

[# 32](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-32) 

We’re going to write a prompt that summarizes NYC legislation.

Throughout my examples I’m going to use this bill, Introduction 601.

This bill requires NYC to publish a dataset and interactive map of all film production permits that the city has granted.

[# 33](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-33) 

My first lesson is that you need to clearly articulate what you want the LLM to do.

When you write and run your first several prompts, you will come to realize how, uh, “stupid” LLMs can be.

When I want quick results, I use proxies that are “close enough” to what I want.

“Explain this to me like I’m five” is a great proxy for simple explanations. It encodes things like:

- The vocabulary the LLM will use.
- How long sentences will be.
- How long the whole response will be.
- How detailed the explanation should be. (Not very!)

If you have very specific requirements or you don’t like what the LLM is delivering, you need to get *detailed*.

I’ve seen *so many people* ask an LLM to do something, throw their hands in the air because it gave them a stupid response, and give up.

Coaxing a consistently useful response out of an LLM takes more work than that (… but not that much more).

A useful question to consider when you evaluate your own prompts:

If you gave the same directions to a human with zero context about your goals, your preferences, or the task at hand, would you expect them to do a good job?

If your answer is “no”, then you can usually expect the LLM to do a bad job, too.

[# 34](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-34) 

In the following slides, we’re going to iterate on a system prompt to summarize NYC bills.

The LLM will receive our system prompt.

It will also receive text pasted from the bill. Assume we’re using Introduction 601, the bill I shared earlier, in all our examples.

The LLM will respond with a summary.

“Completion” is the language used to refer to responses from an LLM.

As you might recall from earlier slides: LLMs are continually predicting text that comes next, essentially “completing” it.

[# 35](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-35) 

Let’s start with a simple prompt: “Your job is to summarize the NYC bill that the user provides.”

This summary is not useful:

- It contains three verbose paragraphs.
- It is hard to skim.
- I do not want the LLM to state that a bill will “revolutionize” anything.

We want this summary to be easier to skim.

Let’s introduce a proxy that gets us that result quickly.

[# 36](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-36) 

The first thing I’ve done here is to tell the LLM that we want the summary to be easy to skim.

LLMs might interpret skimmability in a number of ways.

I’m guiding the LLM’s interpretation here with a proxy by asking it to summarize the bill in the style of “Axios’ Smart Brevity”.

[Axios](https://www.axios.com/) is a news site that writes news stories in a particular style that is easy to skim.

What you see in this screenshot has many hallmarks of an “Axios summary”.

“Smart Brevity” is a book written about this style. LLMs have been trained on Axios articles and, likely, that book.

There are still issues with this summary.

For example, I don’t particularly care which council members introduced this bill. I just want my summary to get to the point.

Let’s say that we’re building a website with useful NYC bill summaries generated by LLMs (that are responsibly reviewed by you and your staff).

In addition to “getting to the point quickly”, we also want to:

- Extract items commonly found in NYC legislation.
- Introduce a consistent structure to summaries.

[# 37](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-37) 

Here’s that bill, Introduction 601, again.

I’ve highlighted some things that commonly appear in NYC bills:

- Dates that lawmakers and people need to adhere to.
- When the law will be in effect if the bill is enacted.
- References to the NYC legal code.

In our summaries, we’ll add a section that lists key dates/figures and another section with references to the NYC legal code.

[# 38](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-38) 

This prompt is way more prescriptive.

I start with a proxy: “The audience is a NYC resident who wants to get up to speed on the law, who is a layperson.”

(I might get a very different response if I stated “The audience is an NYC legal scholar.”)

Then I detail each section’s titles and contents.

I also have special sections for some of the data we want to extract: “References to Legal Code” and “Key Figures”.

[# 39](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-39) 

This prompt wasn’t hard to write. It already works pretty well!

All our sections are there.

The “Implications” section gives me an easy overview as a NYC resident.

If I want to dig in further, I can do that by perusing the “Law Requirements” section.

If I just want to know about fines and dates, I can eyeball those at the bottom.

So… what’s the problem with this prompt?

It will not do a good job, consistently, over a wide range of bills.

We have not yet accounted for any variations in how legislation is written.

And, even with similarly-written legislation, it may miss out on sections, hallucinate contents of the legal code, or fail to extract some dates and fines.

[# 40](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-40) 

If you want a prompt to work well, more consistently, over a wide range of inputs, the fastest way to do that is to *provide 5-10 diverse, illustrative examples.*

Not only will your prompt be more effective after you are done with this exercise, the process **will force you to carefully examine and handle real artifacts in your data** (in our case, NYC bills).

Getting to know the contours of the data you are feeding an LLM is an extremely useful and underrated activity!

People don’t talk about it enough because it is not “one weird trick”. It is tedious but effective.

Coming up with good examples is consistently the most impactful thing I do when I’m improving a prompt.

[# 41](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-41) 

When I’m adding examples, this is what my prompt looks like.

First, I start with the prompt I already have.

This slide shows the prompt we just wrote for bill summarization.

I’ve made no changes to it!

[# 42](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-42) 

I add examples to the end of my prompt.

Each example gets a header and two sections: input and output.

I spend time crafting and adding 5-10 diverse, illustrative examples and append them to my prompt this way.

[# 43](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-43) 

The best way to craft examples is to use your existing prompt as a starting point.

Pictured here is a summary for another bill using the prompt we already have.

(This bill introduces tiered fines for chain businesses in NYC when they fail to clear snow/debris from sidewalks.)

It’s easier to edit and massage this summary into your desired output than it is to start from scratch.

Another reason to craft examples this way: you will examine lots of output and see **exactly how your prompt fails to deliver**. As you do this:

1. Note every kind of failure you see.
2. Add directions and an example to address it.
3. Do this until your prompt works well enough, consistently enough.

This is how you systematically improve a prompt.

[# 44](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-44) 

These are the kinds of examples I’d work on based on my analysis of a bunch of bills.

These cases account for most of the major variations in how NYC legislation is written.

[# 45](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-45) 

The best way to get good at that coaxing LLMs into doing useful things (also referred to as “prompt engineering”) is to do it.

Try these exercises yourself at home.

If you’re using ChatGPT, you might not be able to override the system prompt, in which case you can paste your prompt as the first message.

I like using [TypingMind](https://typingmind.com/) for all my testing.

It’s a cheap chatbot that provides a chat interface over all the major LLMs out there.

I can configure and save system prompts for various tasks, and I can quickly test all my prompts across models without writing any code.

[# 46](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-46) 

When you try those exercises, you might want to try out different language models too.

The current most-capable LLMs (as of late March 2024) are available via [OpenAI](https://openai.com/), [Google](https://gemini.google.com/app), and [Anthropic](https://www.anthropic.com/).

“Context window size” refers to how much text an LLM can process at once.

Some LLMs can process text spanning a book (or multiple books). Some can only process a longer essay.

“Cost” just means… how much it costs to use a model.

[# 47](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-47) 

Both cost and context window size are measured in “tokens”.

Tokens are *not*: words, characters, syllables, punctuation, or another neatly-organized category you might think of.

Tokens are how LLMs see text. When they are trained, they learn statistical correlations between tokens.

The screenshot above is from this tool: [https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer).

A good rule of thumb, if you’re using OpenAI’s models in English, is that a token is ~75% of a word.

[# 48](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-48) 

Here’s a table comparing the cost and context window size for OpenAI’s top 3 models (as of March 2024).

I use GPT-4 Turbo for [citymeetings.nyc](https://citymeetings.nyc/) because:

- It has a context window that fits long transcripts.
- It hits a workable price-to-performance ratio for me.

GPT-4 is OpenAI’s most capable model at the moment (March 2024). This is reflected in its cost.

GPT-3.5 is OpenAI’s least capable model. It is powerful for a wide range of tasks when prompted well and it costs basically nothing.

It costs more to generate “output tokens” than it does to process “input tokens”. Prices are commonly quoted “per million tokens”.

My transcripts are anywhere between 10K to 100K tokens, averaging about 40K to 50K tokens.

[# 49](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-49) 

Now that I’ve shared how I write my prompts, let’s talk about how I arrived at the ones I use to create video chapters for [citymeetings.nyc](https://citymeetings.nyc/).

[# 50](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-50) 

The first step in my “chapter extraction” process is to identify all the speakers in a transcript.

As you might recall, my transcripts are “diarized”. This means every word that is spoken is given a speaker label, like “3”.

In this step I map speaker labels to a specific name, role, and organization, like “Martha Norrick, Chief Analytics Officer, Office of Technology and Innovation (OTI)”.

Correctly-identified speakers lead to better chapters.

For example, if I want an LLM to identify chapters that begin with a question asked *by a council member*, it’s important that it knows who is speaking.

[# 51](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-51) 

Meetings usually have 20+ speakers, and many can get to 50-60 speakers.

I review all the speakers that my speaker identification process generates using the tool pictured here.

I try to do two things in my review:

1. Ensure the name/role/organization are correct.
2. Fix spellings, even if they might be misspelled in the transcript.

[# 52](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-52) 

My transcripts are 40K - 50K tokens on average. They fit comfortably in GPT-4 Turbo’s context window.

All my first attempts to identify speakers used:

1. A single prompt.
2. The entire transcript.

These attempts failed!

It turns out that even if an LLM is capable of processing 128K tokens, that doesn’t mean it will do it well.

Let’s write a prompt to identify speakers this way. We’ll look at some output and I’ll talk about why this happens.

[# 53](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-53) 

This prompt doesn’t fit on a single slide. Here is part 1 of 3.

First, I write the high-level “job” that the language model is supposed to do.

Then I get into the details, starting with a description of how the transcript will be formatted.

[# 54](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-54) 

Here I’m describing how I want the LLM to output identified speakers.

JSON is a machine-readable format that developers will be familiar with, but it’s relatively human-readable too. This is what it looks like.

I’m asking the LLM to give me four fields for every speaker in the transcript: speaker_label, name, role, and organization.

[# 55](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-55) 

I wrap things up by detailing how I want the LLM to fill in each field for every speaker.

I also provide tips around how to infer speaker details and I share some “gotchas” around mistranscriptions and badly-diarized roll calls.

[# 56](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-56) 

Here’s some output from speakers in the “middle” of this meeting, which has close to 60 speakers.

The names for speaker labels 27 and 28 appear in the transcript.

*All these responses are completely wrong.*

[# 57](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-57) 

The correct answers are on the right.

The current speaker identification process used in [citymeetings.nyc](https://citymeetings.nyc/) gets these answers correct the first time.

None of the fields are “UNKNOWN”. They are all identifiable based on context in the transcript.

[# 58](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-58) 

Here are three more responses from the prompt we just wrote.

All of these are also, unfortunately, completely wrong.

[# 59](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-59) 

The correct answers are to the right here.

Again, the current speaker identification process used in [citymeetings.nyc](https://citymeetings.nyc/) gets these answers correct the first time.

It is wildly obvious who a speaker is based on context from a transcript. I expected LLMs to do this well.

This felt like it should be a simple, tractable problem.

So, why does this happen?

[# 60](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-60) 

One of the reasons LLMs struggle to do things accurately with long context windows is a well-documented issue called the [“lost-in-the-middle” problem](https://arxiv.org/abs/2311.09198)

LLMs tend to more heavily weight context at the beginning and end of their windows. They “lose” context in the middle and their accuracy suffers.

I deliberately showed you examples from the middle of my transcript. Anecdotally, speakers were identified more accurately at the beginning and end of the transcript.

In the middle, though? Completely wrong. Mostly `"UNKNOWN"`. It’s like the LLM just gave up.

Folks are working on addressing the “lost-in-the-middle” problem.

Recent (March 2024) LLM entrants by Google (Gemini 1.5) and Anthropic (Claude Opus) have published impressive results showing their LLMs find specific pieces of information in the middle of very large contexts.

I have yet to see if these abilities translate well to performing speaker identification on transcripts. I’ll report back when I do.

(If you want to know when that happens, you can [follow me on X](https://x.com/voberoi) or subscribe to this blog to receive a newsletter when I post something new.)

[# 61](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-61) 

When I feed the LLM an entire 40-50K token transcript, I have very little space for examples in my prompt.

Even if the “lost-in-the-middle” problem is solved, this is a huge downside.

Maybe this will change at some point, but I’ve found that adding a few diverse, illustrative examples is the fastest and easiest path for me to improve the performance and consistency of my prompt.

Unfortunately, a 50K-token transcript uses almost half of my budget for GPT-4 Turbo. I can fit, at most, one good example in my prompt.

I tried to compress my examples by saying things like “here’s a portion of a transcript, and how you might go about inferring speakers for it, here’s the output”, etc.

That didn’t work, either.

[# 62](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-62) 

The solution to problems you encounter when processing large bodies of texts with LLMs is to break them into “chunks”.

There are many chunking strategies you can employ and they all have tradeoffs.

What you decide to do is highly dependent on your task and goals.

Here’s a simple strategy to chunk a long transcript:

1. Grab 8,000 tokens from the transcript.
2. Feed those tokens into the LLM.
3. Repeat 1 and 2 on the remainder of the transcript until the entire transcript has been exhausted.

This approach is very easy to implement, which is a huge benefit!

But it leads to issues for speaker identification: what if speaker label 3 shows up in every chunk?

How do I reconcile the answers I get from each chunk? Which one is correct?

[# 63](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-63) 

My strategy for speaker identification is to identify one speaker at a time.

If there are 60 speakers in a transcript, I will create 60 chunks and prompt the LLM 60 times.

Each chunk looks like the above.

In my message I first say which speaker label I want the LLM to identify.

Then I provide instances of that speaker in the transcript, with some neighboring context.

Each instance is:

- The speaker I’m identifying, saying something…
- … sandwiched in between the previous speaker and next speaker saying something.

It is obvious based on “INSTANCE 1 FOR SPEAKER 7” in the chunk above that speaker 7 is Council Member Gale Brewer.

This strategy works: *somewhere* in the instances I provide there is usually one instance that makes it obvious who the speaker is.

[# 64](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-64) 

For the LLM to identify speakers correctly, I need it to reason.

The LLM needs to systematically look at every instance and identify supporting evidence for the speaker’s name, role, and organization.

It also needs to dodge false positives suggested by mistranscriptions and instances where the speaker diarization is wrong.

If you want an LLM to reason, it turns out that *telling it to think works quite well.*

This is a technique called “chain-of-thought”.

[# 65](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-65) 

This is a screenshot of a tool I use to evaluate my speaker identification responses.

(Evaluation is critical! More on that soon.)

Highlighted here on the left is the input: a chunk with instances for SPEAKER 6 in a transcript.

[# 66](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-66) 

Highlighted here on the right is the output I get from GPT-4 Turbo when identifying SPEAKER 6.

The prompt I use is available on the next slide.

In it, I instruct the LLM to output three sections structured exactly as shown here with headers/footers that look like `!!!=START/END <SECTION>=!!!`

In the “INTERNAL THINKING” section I’ve instructed the LLM to “detail your step-by-step thinking to identify who the speaker is, including their name, role and organization.”

In this screenshot, the LLM repeatedly surfaces up evidence that SPEAKER 6 is Council Member Adrienne Adams. That is the correct answer here.

My results are consistently, measurably better when I use chain-of-thought for speaker identification, *but that it is not its only benefit.*

Sometimes the LLM’s reasoning gets things subtly wrong or goes *totally off the rails*.

When it does, I get to observe exactly how. I can then address issues in its reasoning with new directions or, even better, a new example.

I’ve been able to systematically eliminate entire classes of problems this way.

[# 67](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-67) 

[My prompt is available here.](https://gist.github.com/voberoi/3d82f6b2a55e79b7cd014847853be8bf)

It is almost 8K tokens in length.

I’ve followed every tip I lay out in this presentation to get it working well.

Getting here took me ~2 weeks. It is time-consuming to get a prompt to work well, consistently, over a wide range of inputs.

There are a lot of things to try at first. Creativity helps.

Then, when you start hitting walls, you need to roll up your sleeves and *really dig in* to figure out why your prompt isn’t working.

My biggest learning working on [citymeetings.nyc](https://citymeetings.nyc/) is that it is *critical* to have some means to evaluate if your prompt is “working”.

**If you don’t systematically evaluate the performance of your prompts, you will find it extremely challenging to improve them.**

[# 68](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-68) 

Here’s the tool I use to evaluate speaker identification responses.

My partner at [Baxter](https://baxterhq.com/) hacked it together in an afternoon.

This tool allowed me to evaluate and improve my prompt systematically.

Every time I made a change, I’d run it on multiple meetings and speakers.

Then I’d pop into this tool, evaluate all the results, and note all the ways the LLM failed.

I’d then update the prompt to eliminate common classes of failures I observed.

[# 69](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-69) 

I kept doing this until I went from ~35% to 80-90% speaker identification accuracy.

This process is tedious. *But it is easy and works reliably*.

[# 70](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-70) 

I wrote [a whole blog post about why you should regularly and systematically evaluate your LLM results](https://vikramoberoi.com/why-you-should-regularly-and-systematically-evaluate-your-llm-results/)

This is how you get a prompt to work well, consistently, over a wide range of inputs.

In my post, I share failures I observed while evaluating my speaker identification prompt + solutions I implemented to address them.

[# 71](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-71) 

Here’s a really basic failure I observed early on.

The LLM would often fail to make accurate inferences based on **incredibly obvious** neighboring context.

So I added directions and an example showing a correct inference from neighboring context in my prompt.

Doing that eliminated *this entire class of failure.* I have yet to see this issue come up again.

[# 72](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-72) 

Another failure I observed is that common mistranscriptions of council members’ names would cause issues.

So I gave the LLM additional context: a list of council member names.

Then I added directions to infer mistranscriptions for council members.

I also added an example showing the LLM correctly identifying a council member despite a mistranscription.

It worked. Another class of error, gone.

Following a process like this systematically and iteratively is a reliable way to improve your prompt.

[# 73](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-73) 

After I identify speakers, I extract chapters.

My current approach to chapter extraction has three distinct steps with different prompts.

This lets the LLM do one thing at a time, which is necessary for more complex tasks.

This technique is known as “chaining” prompts together such that output from one prompt becomes input for the next.

[# 74](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-74) 

All my initial attempts to create chapters with a single prompt failed.

My prompts detailed what I thought a good chapter would be and I provided examples.

Here’s an excerpt from one of these early attemps:

```
Good chapters are sections of video that:

- Focus on a monologue or on a single topic.
- Focus on a conversational exchange on a single topic.
- People viewing the video can skip to in order to find the information they are looking for.
- People viewing the video can share with others to highlight a specific topic, exchange,
  or testimony.

Chapters may cover a single speaker, for example when a council member is introducing a meeting, bill, or giving a speech.

Chapters may cover multiple speakers, for example when a council member is asking questions of a speaker giving testimony.

An exchange between multiple speakers may be a single chapter, or it may be multiple speakers. Make sure to break down
long exchanges into multiple chapters if they cover multiple sub topics.

```

This prompt is *too vague*. I’d get chapters that were not useful but I couldn’t clearly articulate why and what I wanted instead!

Some were too short, some were too long. My results were inconsistent.

So I took a step back to define, in more concrete terms, what a useful [citymeetings.nyc](https://citymeetings.nyc/) chapter is.

To do this, I built a tool to manually create chapters. I created ~300 of them across many meetings.

[# 75](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-75) 

This is the tool I use to manually create chapters.

I select the start and end boundaries by clicking on sentences in the transcript.

Then I click on “Generate with AI” to save the chapter boundaries and generate a title and description for it.

[# 76](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-76) 

A good [citymeetings.nyc](https://citymeetings.nyc/) chapter starts at the beginning of a `QUESTION`, an individual’s `TESTIMONY`, standalone `REMARKS` by a council member, or a section dedicated to a `PROCEDURE`.

These are how chapters are tagged on [citymeetings.nyc](https://citymeetings.nyc/) today.

[# 77](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-77) 

A good [citymeetings.nyc](https://citymeetings.nyc/) ends at the conclusion of a `QUESTION`, `TESTIMONY`, `REMARKS`, or `PROCEDURE`.

Questions are a bit special.

I want a question chapter to end after an *exchange* that answers the question, and not after the initial response given by an agency.

[# 78](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-78) 

Finally, a good [citymeetings.nyc](https://citymeetings.nyc/) chapter has a useful title and description.

These differ by chapter type. I do a bit of “editorial work” in these prompts.

[# 79](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-79) 

In step 1, my prompt grabs “transcript markers”, which mark the beginning of:

- A question asked by a council member. (`QUESTION`)
- Testimony by an agency or a member of the public. (`TESTIMONY`)
- Standalone remarks by a council member. (`REMARKS`)
- A procedural section. (`PROCEDURE`)

I don’t say *anything* about chapters at this stage.

I’ve found I get bad results if I say something to the effect of “This is the beginning of a chapter in a video encompassing standalone remarks by a council member.”

I want the LLM to do exactly one thing: find me all the beginnings of one the four items I listed above, not the “start of a potential chapter”, which is too vague.

The chunking strategy I use is to process 8K tokens at a time until I exhaust the transcript.

And, in my transcript, I provide something I call “time markers” instead of timestamps.

[# 80](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-80) 

Here’s what a transcript looks like when I pass it to any of these steps.

I provide markers that start with “T” followed by an integer to mark the beginning of every sentence. These are “time markers”.

I initilly used timestamps (like “00:23:42”), but the LLM would regularly hallucinate timestamps that weren’t in my transcript.

This made the output useless, which is why I use my made-up “time markers”.

This is a common trick I use to great effect: if the LLM frequently hallucinates something one might commonly find in its training data (like timestamps), I’ll make up my own “language” for it to follow instead.

I map time markers back to specific timestamps in my transcript and video.

[# 81](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-81) 

In step 2, I create chapters from transcript markers, one transcript marker at a time.

The input to this prompt is:

- A transcript marker.
- The portion of the transcript that encompasses the duration between this transcript marker and the next one.

Somewhere in that portion of the transcript is the end of a chapter that starts with that transcript marker.

I use a different prompt with different directions to determine the end of each chapter.

[# 82](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-82) 

Now that I have chapters, I write titles and descriptions for each.

I do this one chapter at a time, and I have a different prompt for each chapter type.

[# 83](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-83) 

[Here are my prompts.](https://gist.github.com/voberoi/cfeb935b163c150eee5d7c86e7fb4337)

A couple of caveats:

1. I now use [instructor](https://python.useinstructor.com/) instead of plain-English prompts.
2. I have not yet iterated on these prompts systematically in the same way I have my speaker identification prompts.

Instructor is a Python package that makes it easier to get structured output more reliably from LLMs.

**If you are a non-developer, these prompts are still fairly legible:** there’s a bunch of plain old English mixed in with code. All that ends up in the system prompt.

These prompts are basic. I haven’t even added good examples yet and they work reasonably well!

I spend 10-30 minutes reviewing and fixing chapters for meetings before publishing them.

This can still take a *ton* of time on busy weeks with long hearings, and I’m working on bringing this time down.

It’s currently budget hearing season in NYC (March 2024). So we’ve been having ~20 hearings weekly, many of which are 5-10 hours long.

(This is why [citymeetings.nyc](https://citymeetings.nyc/) is not currently caught up on 2024’s meetings.)

[# 84](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-84) 

It costs me ~$5 - $10 to identify speakers and extract chapters for one meeting.

This is an *absolute bargain* for the public. At ~500 meetings a year, that’s at most $5,000.

As a point of comparison, the NYC council pays $50K annually for [Legistar](https://nyc.legistar.com/). I know this because I have the contracts from a [FOIL request](https://a860-openrecords.nyc.gov/)

I haven’t even attempted to do this work more cheaply. This is a baseline, and I’m confident I can bring costs down.

[# 85](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-85) 

Here are some ways I might lower costs.

1. I currently use GPT-4 Turbo for every task. I don’t have to. Other, cheaper models are up to some of the tasks I use GPT-4 Turbo to perform.
2. With hundreds of identified speakers and thousands of extracted chapters, I have enough data to start fine-tuning a less capable model. I’ll pay some cost upfront for training, but operating a fine-tuned model is cheaper.
3. I can optimize my chapter extraction process by doing it in fewer passes. This is tricky: it might lower chapter quality.
4. I can wait. LLM costs are falling precipitously.

If costs fall at the same rate they’ve been falling this last year, simply waiting will make my costs manageable.

In fact, I’m fairly confident that it will.

Last March (2023) when I started running initial tests, GPT-4’s pricing was higher than I was willing to pay out of my own pocket for a project like [citymeetings.nyc](https://citymeetings.nyc/).

8 months later, in November 2023, OpenAI released GPT-4 Turbo. It performs well and costs way less.

In the time between working on this presentation and publishing this post (a ~3 week window), new models have been released that are said to rival GPT-4, *and they cost less!*

All this has happened in the span of one year.

I haven’t touched fine-tuning (#2) yet, but I’m very eager to do so and I’ll report back when I do.

[# 86](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-86) 

To wrap things up, I want to share a few tips for how to approach a more ambitious project that uses LLMs.

[# 87](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-87) 

Start by getting one prompt to do one useful thing well enough, consistently.

Doing that will expose you to the entire spectrum of things must do to deploy LLMs effectively in your product or service:

1. You’ll learn how to write an effective prompt.
2. You’ll learn how to evaluate results and iterate on a prompt.
3. You’ll figure out if the thing you’re asking the LLM to do is valuable to someone.
4. You’ll learn how to handle issues that arise when operating a product/service/feature that relies on LLMs.

Doing all this well for one prompt is difficult enough.

Start simply!

[# 88](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-88) 

It is impossible to iterate on prompts quickly or effectively unless you systematically evaluate them.

Without systems to do this, you won’t know if a change you make is working, causing issues, or doing nothing.

Set up systems to do this early if you can. A good time to do this is when you’ve figured out your basic approach to solving your problem.

In my case, it took me a while to figure out an approach to chapter extraction that worked… at all!

Now that I have an approach that’s working reasonably well, it is time to evaluate and systematically improve it.

[# 89](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-89) 

You must acknowledge that LLMs will fabricate things if you have any hope of deploying them effectively in your product or service.

LLMs *will* give you bad answers sometimes: how much does that matter for your use case, and what do you plan to do about it?

This is inherently a product design problem. Here are, broadly, the options you have:

1. **Ignore bad answers.** If an LLM outputting a “bad” answer doesn’t matter for your use case, you can do this. (Consider yourself lucky!)
2. **Handle bad answers.** More likely than not, you will need to handle bad answers. For [citymeetings.nyc](https://citymeetings.nyc/), I do this by reviewing identified speakers and extracted chapters manually.
3. **Give users an out.** You can also give users a way to address or side-step bad answers themselves. For [citymeetings.nyc](https://citymeetings.nyc/), if a chapter title/summary is inaccurate, the video and transcript are right there for the user to double-check them. If the chapter boundaries aren’t quite right, they can scroll through the transcript and seek to a nearby timestamp.

You can’t wish away hallucinations. Plan for them.

[# 90](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-90) 

My final tip: optimize for cost later if you can.

It easier to get good results with more costly LLMs.

Use more costly, capable models to get good results, gain some momentum, validate an idea, etc.

Get a baseline cost, then optimize: there are *so many* ways to lower costs.

[# 91](https://vikramoberoi.com/posts/how-citymeetings-nyc-uses-ai-to-make-it-easy-to-navigate-city-council-meetings/#slide-91) 

That concludes my talk!

If this was helpful to you, please share it with your colleagues, on socials, at a meetup, etc.

[Here is a page with links and resources related to this talk.](https://citymeetings.nyc/nyc-school-of-data-2024) Links to my prompts are there, too.

Follow me:

- [X/Twitter](https://x.com/voberoi)
- [Threads](https://www.threads.net/@vikramo)
- [LinkedIn](https://www.linkedin.com/in/voberoi/)

Email me at [vikram@citymeetings.nyc](mailto:vikram@citymeetings.nyc).

At the conference I had a bowl of these fun pins that my wife, [katiebcartoons](https://katiebcartoons.com/), made.

If you live in NYC and want one – I’ll bring them to any related meetups/talks or if we happen to grab coffee!

*Thanks to Jeremy Singer-Vine, Cameron Yick, and Alex Quinlan for providing extensive feedback on early drafts of this post.*

Reply via [email](mailto:hello@vikramoberoi.com?subject=How%20citymeetings.nyc%20uses%20AI%20to%20make%20it%20easy%20to%20navigate%20city%20council%20meetings), [Twitter](https://twitter.com/voberoi), [Threads](https://threads.net/@vikramo), [Bluesky](https://bsky.app/profile/voberoi.bsky.social), or [LinkedIn](https://www.linkedin.com/in/voberoi/)