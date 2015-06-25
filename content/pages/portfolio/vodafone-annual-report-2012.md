Title: Vodafone Annual Report, 2012
Date: 2012-03-31 10:00
Author: Corey Dutson
Tags: 2012, Annual Report, CSS, HTML, JWPlayer, progressive enhancement, Responsive layout, Vodafone, WinHTTrack, ZoomSearch
Slug: vodafone-annual-report-2012
Status: published
SlugPic: wp-content/uploads/2013/05/vodafone-square.jpg
Summary: A responsive, media-rich website that used progressive-enhancement to ensure a good experience across the user device spectrum. Media queries, HTML5 video, and a whole lot of JavaScript were used to make this website sing.


[![voda-desktop-home](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-desktop-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-desktop-home.jpg)

Overview
--------

Vodafone wanted to change the way they did annual reports. Up until this
project, their AR sites had been fairly traditional, text-heavy beasts
that did little to tell their story or engage with readers or
stake-holders. They wanted to change all of that with a fresh delivery
style. Radley Yeldar pitched a media-rich website that had cut out most
of the traditionally unread pages (based on their analytics data), and
put more focus on the story-telling aspects of the website.

My role was to work directly with the designer to bring the visual
concepts into life. I had to work closely with both the designer and the
UX team to make sure that as the site was expanded or collapsed,
everything fit where it should. I created the templates, all of the
front-end code, as well as all of the supporting back-end code. I also
had to integrate ZoomSearch into the website, as the final product
needed to be a flat website that was integrated into CQ5.

Front-end highlights
--------------------

[![voda-desktop-strategy](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-desktop-strategy.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-desktop-strategy.jpg)

### Progressive enhancement

[![voda-iphone-home](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-iphone-home.jpg){: class=alignright }](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-iphone-home.jpg)

The first port of call developing this project was to figure out just
what we needed to make sure the base experience was pleasant. I sat with
the rest of the team and figured out what needed to work to ensure the
clients requirements were met, and that the end user's experience
wouldn't be compromised. The end result? Tabbed content became stacked,
lightbox content had their own pages with usable navigation, and the
search form was hidden due to the search function requiring JavaScript
to function (more on that later).

Other little enhancements revolved around mobile device support and
making sure the navigation remained usable throughout the website. Where
supported, we took advantage of native tool support such as the iPhone's
dropdown wheel. When that wasn't an option, I swapped it out for a more
traditional dropdown element. If neither of those options were
available, I suggested we display the normal navigation, but worked hard
to make sure that it wasn't taking up any more real estate than was
required.

### Responsive layout

[![voda-iphone-menu](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-iphone-menu.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-iphone-menu.jpg)

This was my first real responsive website. Given our limitations with
the clients server, we weren't afforded the luxury of dedicated desktop
and mobile websites. The designer and I worked together to make sure
that the site responded all the way down to mobile devices. It
was definitely a learning experience for us both, but in the end we were
happy with how it all flexed. There was a big focus on trying not to
have the user scroll any more than was ever needed, so a lot of work
went into reworking the layout to fit it within the constraints of the
viewport.

Other things taken into consideration with the layout were
high-resolution imagery and icons and making sure that retina displays
looked nice and crisp, as opposed to the fuzzy look that is so common
with web development for mobile. I used media queries to target high
resolution devices and serve up 2x style images, and this worked to
fantastic effect. We also swapped out the large background for smaller,
more mobile-friendly versions when the user was at a smaller window
size.

The designer and I also took a look at the footer of the website to see
what we could do to make that as usable as possible. We worked with the
site to add helpful next/previous pages into the footer to make for
easier reading, and also moved the search into the footer. We put a lot
of time into the sizing of links to make sure they were visually
pleasing, but also easy targets for users to tap.

### Custom lightbox

Lightboxes are a common theme in annual reports, and while we tried to
avoid them whenever possible within Vodafone, there were some pages
where it had to happen. I created a custom side-panel that could hold
any content required to display to the user. We ended up using this for
a couple additional panels (such as reading the entire Chairman's
statement), as well as the downloads page.

I opted to create a custom lightbox as opposed to using many of the
alternatives out there because I wanted to make sure that I had total
control over the layout of the plugin, and just how it would react when
resizing the browser window. A limitation to many lightbox scripts is
that they don't have a focus on responsive layouts at all; we had to
make sure that regardless of the resolution, the panel contents would
work.

[![voda-ipad-homepage](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-ipad-homepage.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-ipad-homepage.jpg)

### Video integration

There was a big push for videos with this project, but the client didn't
want to host them using traditional means such as YouTube or Vimeo. This
proposed an interesting challenge for me, as I hadn't done that much
video integration into websites until this point. As an added bonus, the
easy options such as Flowplayer weren't a viable option due to the iPad
and mobile requirements.

The solution selected was JWplayer, due to its HTML5 leanings while
still supporting legacy browsers. I also needed easy hooks for when the
video start and finished, as we wanted to have an overlay that would
present related links to the user when they paused, ended, or finished
the video. JWPlayer (thankfully) made this a simple task from a
JavaScript point-of-view. Getting the video encodes right took a couple
tries but the end result worked pretty well; videos can be played across
all desktops as well as tablet and mobile devices.

Back-end highlights
-------------------

[![voda-ipad-how](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-ipad-how.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/voda-ipad-how.jpg)

### WinHTTrack

One of the stipulations with this project is that the end result had to
be a flattened HTML website. This was due to the fact that the entire
report was going to live within a CQ5 instance, and short of us
producing the report *in* CQ5, we had to make sure there was no back-end
code running this project. WinHTTrack was the tool chosen to convert the
website due to it's cost (or a lack therein) and flexability. Sadly, the
tool isn't perfect, and a couple additional steps needed to be added in
order for the package to be client-ready.

### ZoomSearch

The other major stipulation with the website is that the client required
search. Given that no back-end code could be used this proposed an
interesting challenge. After reviewing various tools I ended up choosing
ZoomSearch. ZoomSearch was a unique product in that it can produce
search code in various languages such as ASP, ASP.Net, PHP, and
JavaScript. The JavaScript option ended up working perfectly for what we
needed, and had a good number of customisation options.

The only drawback with this tool is that it was based entirely in
JavaScript. We talked it over with the client, and this ended up being
acceptable. As a result, I had to make sure the search area was hidden
from the user when JavaScript was disabled.

[View the
website](www.vodafone.com/content/annualreport/annual_report12/index.html "Vodafone Year in review 2012")
