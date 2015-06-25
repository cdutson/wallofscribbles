Title: Flöff website
Date: 2012-10-20 10:30
Author: Corey Dutson
Tags: alcohol, beer, bilingual, Flöff, JavaScript, JQuery, multilingual, php, website
Slug: floff-website
Status: published
SlugPic: wp-content/uploads/2013/05/floeff-square.jpg
Summary: A bilingual brochure website for a winter-themed German beer. Built in PHP, this website has a running twitter feed, age verification, a contact form, and an interactive Google map.


[![Flöff -
Homepage](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-home.jpg)

About Flöff
-----------

Flöff is not your typical beer.

First off, it's meant to be enjoyed hot; second, it has apples and
cinnamon; and third, they have some of the most creative backstory
writing for a beer that I've ever heard of. You see the beer is named
after a mythical mountain creature that lives in the frosty mountain
ranges of Germany. It's attracted to this particular brand of brew, and
the people who have spotted the elusive Flöff all drink it in hopes that
it will one day return.

Crazy right? I love how much effort they put into the whole thing, and I
liked the fact that they weren't trying to pitch to party bros. They
event went so far as to get a couple moving image pieces made; they are
*fantastic* and you should totally
[check](http://vimeo.com/51590559 "Vimeo - Flöff Brewer")
[them](http://vimeo.com/51677458 "Vimeo - Flöff Look-alike")
[out](http://vimeo.com/52325591 "Vimeo - Flöff Lover").

About the project
-----------------

[![Flöff -
map](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-map-410x262.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-map.jpg)

I was approached by a friend and designer with an opportunity for a
small brochure site for a new beer. I'd never done a website for a beer
company, so I gave the proposal a listen. Once I learned more about
them, I was keen and opted to get their website wishlist to put forward
a rough costing proposal. With a little bit of back and forth, we landed
at something that would work for everyone.

One of the stipulations was that the budget for the overall project
wasn't massive, so we had to be smart with how we got things done. We
didn't want to cut corners, but we weren't going to over-deliver on a
project when we knew there wasn't going to be compensation for it (they
literally had no spare money for such things). So the first thing we did
was sit down and come up with a layout that we could re-use, discussed
how we could simplify elements, and generally figure out ways to cut
costs down without delivering a sub-par project.

Front-end highlights
--------------------

[![Flöff - twitter and
fader](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-lower-410x262.jpg){: class=alignright }](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-lower.jpg)

The website was, technically speaking, not that difficult. The hardest
part was actually making sure that my solutions were reasonably
low-impact on my logged hours and worked across all the typical
browsers.

An entertaining challenge throughout the website was the fact that the
client wanted to use a lot of moving image. This was, for obvious
reasons, a bit of an issue. We opted to bring back some tricks from the
times of old: GIFs. To help simplify things, we swapped out a couple
would-be videos with some much more manageable GIF images.

One place we did use video was for the background. We could then fall
back to an image for any browser that didn't support native video.

[![Flöff -
camera](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-cam-410x262.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-cam.jpg)One
of the more irritating challenges ended up being the custom font used
for all of the headings in the website. Turns out that the font in
question has very specific licensing that disallows the use of anything
like cufon or sIFR (not that I would ever use those technologies at this
point), and while the font can be used for web stuff (we eventually
found out), the foundry took 5 months or so to actually return our
email. By that time the website was already done and out the door. We
ended up having to fall back to the less than perfect but still workable
'titles as images' solution; sure, it's irritating when you have a
multilingual website, but it was the best we could do at the time.

Back-end highlights
-------------------

The back-end of the website provided far more challenges to me. For
starters, it had to all be in PHP. While I can work in PHP, it's not my
go-to language for projects. This feeling was compounded by the fact
that the website needed a contact form, twitter integration, and an
age-restriction barrier that allowed web crawlers through, but stopped
people; all things I had never done in PHP. In addition to this, I
didn't have much control over the server, so when it came to things like
caching, I had to get creative.

The first major hurdle was the contact form. Very straight-forward but
not something I've done much of. To save costs, we stuck to server-side
validation only. I wasn't keen on that, but again, we had to figure out
where we could cut down on the overall price.

[![floeff-age](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-age.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/floeff-age.jpg)

The second big bit of backend work revolved around twitter. We didn't
have the time to do a proper integration of the twitter stream into the
website, but we still wanted to have a feed pulling into the website. My
solution, low-tech that it turned out to be, was to do a filesystem
cached file of the twitter feed. When a user hits the website, the
file's update stamp is checked and if it's older than a specified time,
a new fetch is executed; otherwise the file was simply read in and
rendered. Not the fanciest of solutions, but it works.

The third, and most interesting of the problems I solved had to be the
age-restriction splash page  As the contents of the website revolve
around alcohol, the website needed to have a age verification to stop
the young and impressionable from seeing the website. With that though,
I had to make sure the contents would still be crawled by the heartless
robots that power the internet. It took some research, but with a
combination of a robots.txt file, some htaccess work, and some session
cookie work, I ended up with a something that worked.

You can view the website
[here](http://www.floeff.de/ "Here's to the Flöff; the elusive, magical beast that inspired our brew. ").
