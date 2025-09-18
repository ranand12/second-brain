# Are you using AKS Log Analytics?. If you’re like a lot of customers, it’s… | by Chase | Dec, 2022 | ITNEXT

Column: https://itnext.io/are-you-using-aks-log-analytics-e0d1881dea29
Processed: No
created on: January 7, 2023 4:54 AM
topics: azure, kubernetes, tech-stuff

![1*iMwOtUqXnZ9TeyzUNDfRig.png](Are%20you%20using%20AKS%20Log%20Analytics%20If%20you%E2%80%99re%20like%20a%20l%205957cb8968e247888c4d3ae558596d19/1iMwOtUqXnZ9TeyzUNDfRig.png)

If you’re like a lot of customers, it’s possible you have deployed [container insights](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) with your AKS cluster and are using it to monitor various health and performance metrics. Also like a lot of customers it’s possible you use, or have tried to use, the built-in workbooks and wondered how you could tweak that data to better meet your needs.

If this is you, then you might enjoy what’s about to happen. We are going on a little adventure, together, so I can show you how you can harness this power and level up your ability to dig into your cluster's usage and health patterns.

> What I am going to cover here assumes you have container insights already running. If you need to be sold on its use cases or would prefer a streamlined example of how to use this successfully, feel free to request.
> 

Let’s jump right in. When you’re in the portal, looking at your cluster blade, under the monitoring section, there is a Logs option. In this section there are a lot of pre-canned queries you can run to get you various bits of information. This is called Log Analytics [Log Analytics tutorial — Azure Monitor | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial). The docs there give you a solid overview of what you can do and outline that KQL is the language used but none of this is terribly contextual.

Let’s take the Container CPU example that is provided to us and customize it to better suit our potential needs that can then be taken across all other examples.

It’s open this up and break it down.

```
// Container CPU
// View all the container CPU usage averaged over 30mins.
// To create an alert for this query, click '+ New alert rule'
//Select the Line chart display option: can we calculate percentage?
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| summarize AvgCPUUsageNanoCores = avg(CounterValue) by bin(TimeGenerated, 30m), InstanceName, _ResourceId
```

Pretty simple. Half of it is just comments, a suggestion (this is a bad one for most people's needs IMHO) and what looks to be a question…which is interesting. The actual query has us looking at the **Perf** table and looking where certain columns are equal something and then summarizing the data over 30 minutes based on our search time frame, which defaults to 24 hours.

> That means we will see 30 minute summaries over 24 hours by default
> 

First thing I want to point out is finding **where** this Perf table is. On the left side of the query there is a Tables option, click that. Once you click that use the search bar and just type in Perf.

Hey-o! So now we know where that table is. If you want, click on it and see all the columns inside of it. One thing I notice is the comments is ‘Select the Line chart display option: can we calculate percentage?’ which I just want to say right now is technically a yes but I want something different. Run the query and choose Chart. The default is stacked column which looks horrible here. Hit the chevrons on the right and let's change this to line.

I have some issues with this data output that we are going to change. I don’t like how anything is named and the nano core value requires someone to know first off what that even is (1 1 billionth of a core) and then possibly do some math. First, the instance name is supposed to be the name of the pod. I don’t want to see the that big URI. Let’s change that.

> There are multiple ways to make this happen, I am going to show quick and easy.
> 

First thing I want to do is verify the index number of the pod names. I am going to do that by creating a new object called PodName and splitting that InstanceName column on ‘/’. I’ll project PodName and distinct it so I can see what’s in there and verify that the index appears to be the same before moving on.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = split(InstanceName, '/')
| project PodName
| distinct tostring(PodName)
```

> Notice I am casting PodName tostring(), if I don’t do that I will get an error that PodName is dynamic, that’s fine for now we are just testing stuff. We will change it later.
> 

Appears that the pod name is going to be index 10. Now technically we could just call index 10 and be done with it:

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = split(InstanceName, '/')[10]
| project PodName
| distinct tostring(PodName)
```

There we are, easy. With a simple split and a call to that known index we have what we need. Maybe we could have used regex, substring, indexof, etc but in this case…why over complicate it? Moving on to the ResourceId column. This is here to separate any possible data that might belong to other clusters potentially using the same log analytics workspace. Still, I don’t care to see the entire URI so let’s rinse and repeat.

Once again, we hit our buddy split() up to do all the work for us in the same manner we got the pod name. This time though our index target is 8, not 10.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = split(InstanceName, '/')[10]
| extend ClusterName = split(_ResourceId, '/')[8]
| project PodName, ClusterName
| take 5
```

What a difference. All that wasted space is gone and now I can easily read the names without having to scroll for an eternity like some kind of cave man. Next, we want to bring back that summarize we had before but before we do that, we need to fix our new name variables we created. By default, Kusto is going to make both PodName and ClusterName a dynamic object. You cannot summarize a dynamic object. To get around this we can tell it that we want to ensure it casts to a string.

```
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
```

Now we can bring back our summarize and take a look.

This is marginally better. Let’s go take a look at our chart to see how it changed our visual.

Now I can SEE the names straight away. That’s a big improvement visually here. I still don’t really like this data overall. We are looking at the average of the counter values (nano cores) over 30 minutes. Let’s tweak our query again and take a look at some of this raw data to see what we are really working with.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| where PodName == 'stress'
| project CounterValue
| take 50
```

We have lots of numbers, or in this case “nano cores” . This isn’t going to do it for me. A nano core is 1 BILLIONTH (yup, B) of a core, so visualizing that number doesn’t help me understand anything other than “bigger number = more pressure” and when we are talking lots of pods in the hundred thousand or millions, I don’t want to have to think about the core usage in that way. Let’s see if we can look at this differently.

If 1 nano core is 1/1000000000 of a core we can calculate to get core usage pretty easily. Let’s go ahead and do that. I am going to use my stress pod, which is stressing the CPU, to look at this. I am going to take a sample from CounterValue, do the calculation and then go LOOK to see if its accurate or not.

> CounterValue/1000000000 is our basic formula here
> 

My value I took was 918,649,861 which is pretty easy. This would be roughly 91% of a core. I debugged my way onto the hosting node of the pod and watched top for a bit. The variance and range of consumption appears to align with the data I am seeing so for now I am happy that this is directionally accurate. I wouldn’t use this data to blast off to space but I am comfortable it would ferry me across the ocean.

So let’s do this in the query and see how it looks. Add in another extend and call it CoreUsage with the CounterValue/1000000000.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| where PodName == 'stress'
| extend CoreUsage = CounterValue/1000000000
| project CounterValue, CoreUsage
| take 50
```

Looking good so far. Notice our pattern? Easily read the core usage in the millions by the first two numbers. In this case, it’s easy, in other cases my feeble brain would need to think too much so I will keep on with the CoreUsage instead.

Let's tie this back in and see how we like our data now. Some small tweaks to the summarize to change the name of the target column and the average column itself and let’s see what we get.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| extend CoreUsage = CounterValue/1000000000
| summarize AvgCPUUsageCores = avg(CoreUsage) by bin(TimeGenerated, 30m), PodName, ClusterName
```

Now we are talking. Plenty of low hitters in here. Let’s go look at our chart. This time notice that the default bar chart is actually useful to us, showing high consumers at a core level CLEARLY.

Our line chart is easier to read now too.

Granted, the visual here is clarifying information, nothing amazing but my goodness does it make a difference to the human eye huh? Let’s talk about the data we are getting for a moment. If you noticed every pod appears to be reporting usage in this table once a minute. More than likely there is a sample frequency that takes place and then aggregates.

I don’t know what the sample frequency is and there are some reasons it matters. First of all, what if our issue isn’t sustained? What if high consumption is something that happens intermittently or ‘randomly’ ? Can we visualize that at all with this data? The answer is, sort of.

Without understanding the sampling frequency and having the min/max averages across that sampling time frame it’s difficult for us to highlight low level paper cuts that so many of us suffer from. You can however still try to do it with the data you have here. This is going to be rough to show but I will try anyway. My cluster isn’t DOING anything real.

First thing to know is that the chart we have been using only works because of the way we are summarizing. We are binning our time and we have X/Y axis data that Kusto is working with for us. We can change that binned time to tighten up or broaden our visuals. To do that I want to scope the query differently to prevent any visualization or data point issues, such as having too many.

We do this by tightly scoping parts of our query to control the output. The first is controlling the time range. If you think you will have a lot of data that might be hard to visualize, carve out smaller time ranges. Don’t go looking for 7 days’ worth of data you won’t easily be able to see or offers you no value — especially if performance is something you care about.

> Pro tip: you care about performance. Being effective isn’t the same thing as being efficient. Think about the time investment that goes into something.
> 

Another method of tightly scoping is to look for specific things only. In my case I am going to EXTEND my time range, but I will limit my output to where CoreUsage is at or above a certain value. Again, my cluster doesn’t have a lot going on so this won’t look amazing, but you will get the point.

Time range is going to extend to 7 days

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| extend CoreUsage = CounterValue/1000000000
| where CoreUsage >= 0.10
| summarize AvgCPUUsageCores = avg(CoreUsage) by bin(TimeGenerated, 30m), PodName, ClusterName
```

While I am looking for more data, I am making sure I only bring back certain data based on the core usage. The interesting part here is that the visual looks better with the stacked columns than it does with the line.

Easy to see our trends, but notice those little blips there? Let’s check the column:

Same data, different perspective, better understanding. Don’t be shy about changing how you visualize your data; the story may appear to change visually even if it doesn’t at the data level. We are visual creatures after all are we not?

Alright great but now I want to get **more** data. I am going to change my bin time to ONE minute because I am a crazy person. We know STRESS is doing a lot of work for me, I am going to unclick on the graph so we can see the other patterns. We can see right away the data patterns didn’t change much, my “blips” really were contained in one minute spans. So changing from 30 to 1 minute bins tells me that the pressure we see other pods put on the node were fairly short lived and there is no real usage pattern to be concerned about (yet).

These examples are half baked in my cluster but potentially valuable in actual clusters that have real workloads. You need to be careful with your scoping though. In my case here I shouldn’t have bothered showing the stress pod at all. All it did was bring back way more data than I needed it to, and I had to filter out the visual anyway.

Before we wrap this up, let’s take a look at how bad what I just did was. First, I took a huge span of days, second, I binned it at the lowest aggregate possible, third, I didn’t exclude known patterns that don’t matter which would make finding other patterns more difficult to sniff out.

At the bottom there is a Query details button. If I hit that we can see some things:

5.5 seconds, and 1470 records.

You might look at that and think hey man that’s not so bad. Isn’t it though? It took 5.5 seconds to get 1470 records, MOST of which I didn’t even care about and 781ms of CPU time. How can we do better then? Let’s make a SMALL tweak to our query.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| extend CoreUsage = CounterValue/1000000000
| where CoreUsage >= 0.10
 and PodName != 'stress'
| summarize AvgCPUUsageCores = avg(CoreUsage) by bin(TimeGenerated, 1m), PodName, ClusterName
```

I am telling Kusto to NOT include stress. Let's look now.

Right away nearly a second and a half faster and only 26 records.

Only 109ms of CPU time vs the other queries 781ms. That first query added 672ms of CPU time. WAY more efficient. Not only that, look at our data now:

No additional filtering needed at all. But wait, there's more! If we just tweak this a little more, we can get more improvements. Take a look at the same query, but a bit different.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
    and InstanceName !has 'stress'
    and CounterValue/1000000000 >= 0.10
| extend PodName = tostring(split(InstanceName, '/')[10])
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| extend CoreUsage = CounterValue/1000000000
| summarize AvgCPUUsageCores = avg(CoreUsage) by bin(TimeGenerated, 1m), PodName, ClusterName
```

Notice we have moved some comparison UP in the query? We even made the exclusion of the stress pod up there, but we are using !has…certainly this will not be as good right?

Oh… 2.5 seconds…that’s uh…interesting.

So we had the same CPU time with that query but it returned FASTER than the other query with the exact same data and we even used has, which technically should require more processing. Let’s do one more thing…let’s change where we are filtering out stress.

```
Perf
| where ObjectName == "K8SContainer" and CounterName == "cpuUsageNanoCores"
    and CounterValue/1000000000 >= 0.10
| extend PodName = tostring(split(InstanceName, '/')[10])
| where PodName != 'stress'
| extend ClusterName = tostring(split(_ResourceId, '/')[8])
| extend CoreUsage = CounterValue/1000000000
| summarize AvgCPUUsageCores = avg(CoreUsage) by bin(TimeGenerated, 1), PodName, ClusterName
```

Now we are going to look right after we create PodName.

2.2 seconds…

But our CPU time went UP? What the heck is this witch craft? Well, what we are seeing is the LOCATION and type of filtering will impact the query performance. More efficient queries put less pressure on the source with targeted resources and get you what you need faster. Play around with stuff like this and make an effort to understand how to format your queries for efficiency.

My numbers here might not concern you. Remember my cluster is TINY and has nothing real happening. If you are creating queries to generate alerts or other metrics people consume to ensure your cluster is healthy, performant and reliable you want to be sure you’re not wasting time.

These articles tend to get away from me. I should perhaps start planning what I want them to be instead of just coming up with ideas as I go huh? :). The basics of splitting and modifying the query logic will be usable across all the examples given. Think about how **you** as the consumer of the data want to see it and don’t be shy about trying to find out how to make that visual a reality.

If you liked this hit that clap button and if you want something else or something more hit the comments and let me know.