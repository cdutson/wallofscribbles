Title: Ahold Annual Report, 2010
Date: 2011-05-12 19:00
Author: Corey Dutson
Tags: 2010, Ahold, Annual Report, Corporate Responsibility, JavaScript, JQuery, php
Slug: ahold-annual-report-2010
Status: published
SlugPic: wp-content/uploads/2013/05/ahold-2010-square.jpg
Summary: This listing is a two-for-one special. Ahold chose to work with RY because they'd heard good things about us, and we didn't want to disappoint. They wanted a clean, concise website that they would host. It had to surface information easily, be easy to use, and look clean while doing it. Oh, and it needed to be done in PHP.


[![Ahold Annual Report 2010 -
homepage](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.32.11-PM-480x317.png "Ahold Annual Report 2010 - homepage")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.32.11-PM.png)

Layout Highlights
-----------------

Ahold was one of the weirder projects I worked on, layout-wise. While it
may not look like it, the Ahold AR and CR websites had more page layouts
than any other project I had worked on up to this point. Subtle
variations were used between content pages, depending on what needed to
be displayed. Landing pages had to be flexible due to the range of items
that could be displayed as well.

There were many pages that had to be tailored as well, due to the nature
of their content. Not only that, but it should be noted that the AR and
CR, while very similar in look, actually had differences between them,
even so much as to the same layout pages.

[![Ahold Corporate Responsibility Report 2010 - case
study](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.36.48-PM-480x306.png "Ahold Corporate Responsibility Report 2010 - case study")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.36.48-PM.png)

Font replacement technology was used to serve up the Trade Gothic fonts,
and I even managed to find a neat bug with
[fonts.com's](http://webfonts.fonts.com "Webfonts at fonts.com") service
at the time. I'm sure they were pleased with my phone calls. I learned a
lot about font-hinting and font-smoothing across browsers as a result.

I should note that since this went live,
[fonts.com](http://webfonts.fonts.com "Webfonts at fonts.com") have
actually corrected their issue based somewhat on my feedback with their
service.

We also took a mixed approach to certain effects used throughout the
site. Many of the images were cut to be rounded, but much of the
standard layout used CSS3, with a couple of exceptions made to make sure
the user experience didn't collapse when using a browser that couldn't
take advantage of what was applied. Browser-specific tags (that is to
say, IE conditional tags) were used to make sure that the site would
fall back gracefully.

Back-end Highlights
-------------------

[![Ahold Corporate Responsibility Report 2010 -
homepage/footer](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.38.58-PM-480x321.png "Ahold Corporate Responsibility Report 2010 - homepage/footer")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.38.58-PM.png)

Ahold was a different project in many ways. RY tends to host many of the
AR and CR reports that we create; it's an option that we give the
client. As such, nearly all of our AR and CR reports are done using
ASP.Net.

Ahold was different during development because unlike our normal
projects, this one was done entirely in PHP, because of the clients
hosting solution. They use a linux/apache/php setup, and we had to
recreate that locally. This got me some solid WAMP experience, as well
as a refresher course on console and linux navigation. It was also my
first time doing a project that had to be hosted over https during
production - a client stipulation.

[![Ahold Annual Report 2010 - Brand item
page](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.33.54-PM-480x318.png "Ahold Annual Report 2010 - Brand item page")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.33.54-PM.png)

Due to the fact that the project was to be done entirely in PHP, I had
to recreate much of the functionality we had built in ASP.Net that we
use in other projects for this PHP project. This ended up with my
developing a navigation object using a sitemap file, encode/decode
helpers, and a slew of other helper functions. It was a lot of work, but
in the end saved us a lot of agony.

Front-end Highlights
--------------------

[![Ahold Annual Report 2010 - Brand
map](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.34.51-PM-480x334.png "Ahold Annual Report 2010 - Brand map")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.34.51-PM.png)

Tucked away in Aholds AR and CR is a lot of subtle functionality. Some
of the standard items are there, such as sliders and accordions, but we
also added a functional html map, videos, a brand-filter, and an
external link interception script.

The sliders and accordions come from the tried, tested (and being
constantly improved upon) plugins I've developed for RY. We generally
take advantage of
[colorbox](http://colorpowered.com/colorbox/ "Color Powered - colorbox")
for our overlay requirements, and Ahold was no exception. It's easily
one of the nicest and best to use. The interception script was a bit of
jQuery trickery that looks for http links and attaches a colorbox call
to them.

The map took a bit more work. I ended up developing my own semi-plugin
that would attach itself to the list items within the map. The map
displays points on the map, and when you click on them, you are
presented with the brands that exist in that area. You could then click
on the logos to be brought to the related page. I had a lot of fun
developing this, because it presented some unique challenges regarding
the layering of elements, as well as making sure the box would center
itself properly.

[![Ahold Annual Report 2010 - brands
page](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.33.24-PM-480x264.png "Ahold Annual Report 2010 - brands page")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.33.24-PM.png)

The filter plugin was a real treat to make. I opted to use data-
attributes (thanks to my use of the html5 tag, these are valid) to add
the filterable items. The navigation was auto-generated based on the
items found within the data attribute. When it found a new one, it would
add it to the navigation. The filter faded out any of the brands that
didn't match the filter. It also disabled the click event, which helped
steer the user in the correct direction. The best part about the brands
page was that with Javascript turned off, you still got a totally usable
page - minus the filters.

[![Ahold Annual Report 2010 - brands page
(filtered)](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.32.54-PM-480x269.png "Ahold Annual Report 2010 - brands page (filtered)")](http://wallofscribbles.com/wp-content/uploads/2011/03/Screen-shot-2011-03-28-at-11.32.54-PM.png)

In the end, the client was super happy with the end products, and found
working with us to be a refreshing change to some of the unfortunate
situations they'd gone through in the past. It was an interesting
project, and came with its own set of challenges. This project was a
challenge for me technically, but as always an educational experience.
