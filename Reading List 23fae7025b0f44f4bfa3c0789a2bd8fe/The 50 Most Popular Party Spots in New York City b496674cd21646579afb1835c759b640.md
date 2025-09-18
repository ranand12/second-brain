# The 50 Most Popular Party Spots in New York City

Column: https://debarghyadas.com/writes/the-50-most-popular-party-spots-in-new-york-city/
Processed: No
created on: June 18, 2022 9:56 AM
topics: food, travel

![](The%2050%20Most%20Popular%20Party%20Spots%20in%20New%20York%20City%20b496674cd21646579afb1835c759b640/nightlife_pickup15-2.png)

Late night pickups, between 1AM - 4AM, by yellow taxis on Friday and Saturday in New York City in 2015, plotted from a set of over 1.1 billion taxi rides. The 15 white dots show the most popular pickup areas.

It’s Friday night. It’s been a long week. You just want to unwind. What do you do? You might head to that same bar you’ve been going to for months. You might tag along with some friends. You might go somewhere off a friend’s recommendation. That one buddy’s Snapchat from last weekend is still playing on your mind. Your last weekend seems to pale in comparison, and you fear a repeat. You whip out your phone. “Best nightlife in new york city”, you type into Google, tilting your phone a little towards yourself lest a passerby see your pitiful search. You find a ton of results - **Timeout**, **NYC.com**, **Thrillist**, **10best**, **NYmag**. You open the first few links. Some of them don’t even have lists. Some have bars only. Some have night clubs only. You ignore the ones which don’t have your favorite club on it, or make an appalling ranking mistake. None of them group by location, and you’re frustated by a cryptic one line address. You see a few names you like, but you Yelp them to find out how they’re like and where they are. You cross off your first few picks on account of them being either too far or too expensive. You then try Yelp directly. “Night clubs in New York”. Moderately better. You see some more you like, but you’re not sure how to pick. You’re faced with the quintessential Yelp user’s dilemma - should I rank by number of reviews or rating? Some great clubs you’ve been to seem to have bad reviews so you decide to [rank](http://www.yelp.com/search?find_desc=Nightlife&find_loc=New+York,+NY&start=0&sortby=review_count) by number. This is the best you’ve got so far.

This still isn’t quite satisfying. More reviews don’t really seem to concord with your idea of what the best places are. As great as it is, [Angel’s Share](http://www.yelp.com/biz/angels-share-new-york) simply cannot be the best nightlife spot in New York. You even check [Facebook](https://www.facebook.com/search/108424279189115/places-in/191478144212980/places/intersect). Knowing what friends went where *can* be useful, but you’re not satisfied.

There is so much pain trying to do something fairly simple. Categories are messy. Night clubs, dance clubs, bars, lounges, gastropubs, dive bars, nightlife - there’s *so* many. It’s also *really* easy to distrust lists that make just one big mistake. Even when you find some places you like, the process of figuring out what their vibe is like, whether you can afford it and where it is can take a frustratingly large amount of time. What you’re really looking for is a great area of town to head to on a Friday or Saturday night and a few places to choose from around the area and an idea of what goes on there. That’s what I provide here.

### The 15 Most Popular areas for Nightlife in New York City

The tiny [Meatpacking District](https://en.wikipedia.org/wiki/Meatpacking_District,_Manhattan) and its distinctive Belgian block paved streets has far transcended what it was when it was first named. Now, Meatpacking is known to be New York’s bacchanalian center, with its plethora of exclusive night clubs.

### Honorable Mentions

### How

I looked at over [**1.1 billion**](https://news.ycombinator.com/item?id=10003118) taxi rides to accurately figure out what the most popular spots for nightlife in the city were. I looked for the spots of highest concentration where passengers were being picked up from very late into the night on Friday and Saturday and used [Yelp](https://www.yelp.com/developers/documentation/v2/overview) and [Google](https://developers.google.com/places/) to figure out what places around those areas people were visiting. I picked the top 15 spots in the city (which were largely concentrated around **Meatpacking District**, **Chelsea**, **East Village**, **West Village** and **Lower East Side**), and used those locations to find popular places. After a *lot* of manual tuning, integration of data from Yelp, Facebook, Google and many curated lists from experts, I had my final product.

### What

I list out each area in order alongside its associated neighborhood in New York. I add a static map of the area with an exact pin at the peak area, and plot the 3 most popular night spots in the vicinity on the map. These places are picked manually using a wide variety of signals, like I talked about earlier. There’s a short description of the area as a whole, and for each of the individual places, I use tiles. The tiles contain the place’s name, a short one line description, and a representative picture. Clicking on it will take you to the Yelp page.

### Other similar work

[Todd Schneider](https://twitter.com/todd_schneider) uses the same data to make similar inferences about nightlife in New York City in this [post](http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/#late-night-taxi-index). While I cannot commend the absolutely fabulous work he’s done in his post, his computation of the “Late Night Taxi Index” uses relative night time ride frequency instead of absolute frequency, which is ineffective in gauging true popular nightlife destinations.In addition to this, I extend the computation to actually figure out the top nighttime destinations and display them in a user friendly way.

If you’re interested in technical details, [reach out to me](https://twitter.com/debarghya_das). I’ll follow up this with a post about the technical details soon.

I love hearing feedback! If you don't like something, let me know in the comments and feel free to reach out to me. If you did, you can [share it with your followers in one click](https://twitter.com/intent/tweet?url=https://debarghyadas.com/writes/the-50-most-popular-party-spots-in-new-york-city/&text=The%2050%20Most%20Popular%20Party%20Spots%20in%20New%20York%20City&via=debarghya_das) or [follow me on Twitter](https://twitter.com/debarghya_das)!