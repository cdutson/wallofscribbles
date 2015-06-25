Title: Intermediate Capital Group
Date: 2011-05-12 18:00
Author: Corey Dutson
Tags: HTML, Intermediate Capital Group plc, SharePoint, templates
Slug: intermediate-capital-group
Status: published
SlugPic: wp-content/uploads/2013/05/icg-square.jpg
Summary: ICG wanted a corporate refresh to their main website. They wanted it to be integrated within their existing CMS, MOSS 2010, allowing them to have as much control as possible over not only what the content was, but how it was presented and where it sat in the site hierarchy. As such, the templates we worked into the system had to be flexible to various contents, but still retain a strong visual structure.


[![Intermediate Capital Group -
Home](http://wallofscribbles.com/wp-content/uploads/2011/02/home3-480x252.png "Intermediate Capital Group - Home")](http://wallofscribbles.com/wp-content/uploads/2011/02/home3.png)

Layout Highlights
-----------------

I was tasked with taking the [super-talented
designer's](http://www.thomasmoeller.com/ "Thomas Moeller") mockups, and
turning them into clean, semantic markup that could easily be integrated
into the CMS of choice. In this case, the CMS was Microsoft Sharepoint
2010. I had to make sure that the normal elements from Sharepoint would
work in the layout, and make sure that nothing broke when It got
integrated.

This was also the first project that required me to do any
font-importing. Since there was such a high number of elements that
needed to use Helvetica Neue, options like sIFR (which is terrible
anyways) and Cufon would have slowed the page down too much. We opted to
go with [webfonts.fonts.com](http://webfonts.fonts.com "fonts.com"), as
they're fast and own the rights to the font we needed.

Portions of the layout required a bit of extra thinking, as there were a
lot of transparent gradients that needed to be incorporated to achieve
the desired effect. I also had to make sure that the layout was flexible
enough with user-generated contend that nothing broke. These two aspects
together made for some interesting challenges.

[![Intermediate Capital Group - News
page](http://wallofscribbles.com/wp-content/uploads/2011/02/news-480x256.png "Intermediate Capital Group - News page")](http://wallofscribbles.com/wp-content/uploads/2011/02/news.png)

Front-end Highlights
--------------------

ICG has a lot of information that they wanted to display to the
end-user. Massing this all on the page would have made things
horrifyingly convoluted, and so an alternate solution needed to be
found. The decision to address this problem was to use javascript
sliders. As I've done previous jQuery plugin development, this wasn't
really an issue. Well, it wasn't an issue at first. As we started
development, we found that the complex nature of some of the panels
caused noticeable lag in certain browsers when being animated.

[![Intermediate Capital Group - Landing
page](http://wallofscribbles.com/wp-content/uploads/2011/02/landing-480x249.png "Intermediate Capital Group - Landing page")](http://wallofscribbles.com/wp-content/uploads/2011/02/landing.png)

The cause of this, as it worked out, was a simple matter of overkill.
The plugin I had originally used (a plugin I developed that we now use
in many projects) needed cleaning up and refining. At the time, I didn't
have time to go line-by-line to fix the plugin as a whole, so I opted to
take option 2: remake it from scratch.

[![Intermediate Capital Group -
Footer](http://wallofscribbles.com/wp-content/uploads/2011/02/footer-480x90.png "Intermediate Capital Group - Footer")](http://wallofscribbles.com/wp-content/uploads/2011/02/footer.png)

I cannibalized the original slider code, but stripped away everything
that wasn't needed for ICGs new website. This resulted in a massive
speed increase that solved the issue.

In the end, the client was happy with what we produced, and are still
using it to this day.

Website - <http://www.icgplc.com/>
