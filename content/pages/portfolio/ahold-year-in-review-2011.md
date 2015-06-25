Title: Ahold Year in Review, 2011
Date: 2011-05-12 21:56
Author: Corey Dutson
Tags: 2011, Ahold, Annual Report, development, JavaScript, JQuery, Mobile, php, progressive enhancement
Slug: ahold-year-in-review-2011
Status: published
SlugPic: wp-content/uploads/2013/05/ahold-2011-square.jpg
Summary: Ahold's 2011 Year in review website was a progressively enhanced, javascript-heavy story telling machine. Using a selection of techniques, the website created a strong and interwoven story for users to explore. A dedicated mobile site was served up to save on users bandwidth and processing power.


[![Ahold CR 2011,
Home](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-mac-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-mac-home.jpg)

Overview
--------

Ahold wanted something new, something interesting, and something that
could really delight their clients. After much back and forth with the
team at Radley Yeldar and the client, we ended up with a great solution:
a scrollable, panning grid system that covered specific areas and case
studies that they wanted to highlight. The website had to be carry a lot
of punch, so it also ended up using a lot high-quality photography that
really brought the individual slides to life.

My roll was to take the UX, and working with the designer, create the
experience. From initial prototypes to the final shipped product, I
produced all of the code that made this website come to life. This
wasn't without its challenges, as once again the project had to be built
and delivered in PHP and hosted on a client's server that we had no
control over. Additional points of interest were the use of custom
fonts, a dedicated mobile experience, and a not-quite-responsive setup
that had to fully work in IE7.

[![Ahold CR 2011,
hlghlights](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-mac-brands.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-mac-brands.jpg)

Front-end highlights
--------------------

This was easily my most complex job up to this point in my career. It
was the most front-end heavy website I had ever been given, but I was
excited, because it was a real chance for me to flex my programming
muscles.

### Flexible layout

While not a truly responsive website, the whole website did flex from
1024 up to 1400. This required a light touch with media queries, as well
as also a lot of attention being paid to overall placement of elements,
and heavy use of percentages. This was my first real foray into using
media queries, and there were definite hiccups along the way.

[![Ahold CR 2011, ipad
home](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-ipad-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-ipad-home.jpg)

### AJAX-loaded content and Hashed URLS

Given the unique nature of the website, we had to make sure that the
content was going to work from an SEO standpoint, a search results
standpoint, and for any and all users that didn't have JavaScript
enabled. I decided the best way to approach this was to have the start
page to simply be a long page with first panels of each section loaded
 as static HTML. These panels then had a section navigation that I
picked up and used to load in the various other pages in an asynchronous
manner. Once all of the pages were loaded in, I applied a URL hash
navigation system that would allow you to link around to any part of the
website without reloading the page or having any unexpected jumps.

### Jump navigation

On the subject of navigation, I had to create a way of navigating the
unique nature of the website. I created a system that could hook onto
any link that had a specific class, and then given the URL of the link,
I knew what section and panel the user was going to. By building this
system, we allowed the whole experience to get knit together because we
could now create user journeys throughout the various sections. This was
especially useful near the launch date, when the client was changing
around the stories they wanted to tell.

Glad I thought ahead.

[![Ahold CR 2011, ipad
lightbox](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-ipad-lightbox1.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-ipad-lightbox1.jpg)

### Inline search results

The search was an interesting challenge. We were using Google Mini to
crawl the static version of the website, but clicking on any of the
search results would have yielded unexpected (and unwanted) results.
Thankfully because of the work I had put into the jump navigation, I was
able to re-use some of that code to make sure that when the user clicked
on a search result it could actually navigate them to correct panel, and
if needed it could expand lightbox-ed content or play videos.

### Legacy browser support

We took a two-pronged approach to handling the older browsers. For those
that had JavaScript available to them, we used a browser-enhancing
script to give the browser some shimmed-in support for media queries as
well as some advanced selectors. For those that had JavaScript
disabled *and* weren't using a modern browser, we fell back to using the
conditional HTML tag trick found in the HTML5 boilerplate. This allowed
me to make sure the content didn't spill over into other areas or
otherwise cause unwanted layout issues.

Back-end highlights
-------------------

The whole project was once-again built in PHP, and had to be hosted on
the clients server. I had to make sure that all of the search results
worked, and that the site wasn't susceptible to cross-site scripting
attacks or any other sort of vulnerabilities. We also had to introduce a
mobile detection script to direct a user from the desktop experience to
a stripped-back version made for mobile devices. This script had to be
integrated and tested both locally and on the client server.

Going mobile
------------

[![Ahold CR 2011, mobile
home](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-iphone-home1.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/05/ahold-iphone-home1.jpg)

Given the front-end intensity of the desktop site, it was decided that
trying to force the desktop site down to a mobile experience was neither
fair to the end-user, nor a productive use of my time. As a result, we
decided that a dedicated mobile site was a far more efficient use of
both time and bandwidth.

Using the back-end script to detect for mobile browsers, we redirected
the user to a .mobile domain that made sure to feature all of the
required information.

when doing the mobile website, we tried to make sure that progressive
enhancement was at the forefront, even though it was a smaller site. We
did detection to make sure that the menu system would work properly, and
had a failover to a standard dropdown and go button if required. All of
the videos were done using HTML5 video elements with a YouTube embed
just in case.

The client was exceptionally happy with the end result, and it was
overall very well received.

Website: [View
online](http://2011yearreview.ahold.com "Ahold CR 2011: A Year in Review")
