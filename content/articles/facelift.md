Title: Facelift!
Date: 2011-02-14 15:00
Author: Corey Dutson
Category: Miscellaneous, Personal, Technology
Tags: Fireworks, JQuery, layouts, newsite, php
Slug: facelift
Status: published

So while I doubt many people come to my actual website anymore, anyone
who has done so in the last week or so will have noticed a... minor
change to the site. That is to say that I've utterly changed everything.
Basically I was getting bored of my old one, and to be honest I wasn't
happy with any part of the design of the old layout from the get go.

I made the last one basically because I have an impulse to change my
layout roughly once every year (or two). I was suckered into the whole
pop-out style that was going around at the time, and I wanted my piece
of the action. As a side-effect, The site sort of fell on its ass when
certain browsers hit it. I had already given up on the layout before I
had even really finished it.

That's always a good sign.

<!-- PELICAN_END_SUMMARY -->First off, you may have noticed that the site has a bit
more... *character* to it. I think this layout is a bit more me. At the
very least, it gives viewers a brief glimpse into the borderline
insanity that is my mind. I've removed my resume from the site, since no
one actually cares about that. I've split the site - quite literally -
down the middle. To the left are my ramblings for your continued
enjoyment. To the right is my portfolio... such as it is.

Changes to the blog
-------------------

So on top of having a bitching yellow background, I've narrowed things
down. Comments are on the left (a couple styles still need to be applied
there) and the main section is more narrow. This makes the page longer,
but is more friendly for mobile readers, and actually is fairly readable
for screen-readers. Pictures should take up the whole width of the
column now. I haven't gone back into old posts to correct them, so the
wide picture thing is a 'from here on out' scenario.

Archive pages exist again for things like Categories, Tabs and such. You
could probably url-hack the site to get the archives for dates 'n the
like, but I have opted to not include any straight-up way of getting to
them. Really they're just not that important.

I've also got search going again! I'm a but surprised that not a single
person complained about that on my old design, despite it being a total
oversite on my part. And when I did notice it, I had absolutely no
intention of adding it (read: giving up on the layout).

Changes to the portfolio
------------------------

The portfolio is far from complete. After talking to some designers that
are far superior to myself, I've had some gentle instruction to rethink
what I was going for. Very valid arguments that I agree with. So as of
right now, it looks the way it looks. When I get done with it, it'll
look totally different. I think I may just skip to the next part, which
will talk about what I did here in greater detail.

Suffice it to say that it's currently an alpha layout at best. I wasn't
happy with it when I started, so think of the current layout as more of
a tech-demo.

Code changey stuff
------------------

First off, with my running this blog in WP 3-point-whatever version it
is this week, I wanted to try and take advantage of some of the new
features.

**Custom content types!** Gone are the hackey days of hidden categories
and private posts. Now I've got Posts, Portfolio items, and Code items
(subject to change). This allows for an easy separation of content,
which has made my life so much easier. It requires me to do some custom
loop stuff on the portfolio page, but man oh man is it easier.

**JQuery stuff!** In the last eight months or so, I've gone from knowing
a smattering of jQuery stuff (how to make plugins go... barely) to
writing my own. This is down mostly to my being a senior front-ender at
[Radley Yeldar](http://ry.com "Radley Yeldar"), and the ever-pressing
advances the designers want to go for with their designs.

Hm. That sounds bitter. I'm not, actually. It's been a great learning
experience for me, and I'm happy to have the challenge. Seriously every
day it's something new. Regardless, I've opted to gussy up my site with
a bunch of interactions based on some more basic jQuery. Some are more
obvious than others. The most noticeable one is the portfolio/code area
functionality.

Basically I've ajax-ed the whole thing so that when you enter an
article, it'll load it up right there. The nice thing about it is that
the fallback for non-js is that it will just link to an article-style
page. Simple but effective. The final version of the portfolio will
probably maintain that functionality, though the layout will be
changing. I'm not sure to what yet (I was just glad to get the layout
complete enough to release), but you can assume that the final version
will be stunning.

Other changes that are afoot
----------------------------

I'm trying to get into a more regular posting schedule, if only to train
myself to stick with anything for longer than a couple of weeks.
Normally on Thursdays, but recent things (like releasing and altering a
new layout) sort of took over. I'll try and do a double-post this week.
Key word: *try*.

I'm also going to be investing some more time into varying my posts up a
bit more. I'll be doing more tech-posting, since I'm back in that world.
They will probably range between 'pointless rants' to 'something useful
and/or downloadable.' Hopefully more of the latter, but knowing me -
which I should - it'll probably be more of the former. I'm a bit of a
bitch that way.

Anyways, I'd love some feedback if anyone has any. I generally take
constructive criticism into consideration, but saying ' It sucks lol'
will just be met with a sage nod, knowing that the Internet is
maintaining the status quo.
