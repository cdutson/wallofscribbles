Title: Clarksons corporate website
Date: 2013-04-22 10:50
Author: Corey Dutson
Tags: C#, Clarksons, Coding standards, Fluid responsive, JavaScript, JQuery, Project lead, Radley Yeldar, Responsive layout, Umbraco, workflow
Slug: clarksons-corporate-website
Status: published
SlugPic: wp-content/uploads/2013/05/clarksons-square.jpg
Summary: I sketched out, architected, prototyped, lead the development team, debugged, and helped deploy the redesign and rebuild of Clarksons new website.


[![Clarksons.com -
homepage](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-home.jpg)

Overview
--------

[![Clarksons.com - News
(ipad)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarkson-ipad-news-410x550.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/06/clarkson-ipad-news.jpg)

Clarksons has been a long-standing client of Radley Yeldar for many
years. RY built Clarksons' previous website on a proprietary CMS that RY
created and maintained, but it has begun showing its age. They wanted a
new website to replace their existing, and much like the CMS,
tired-feeling one.

Clarksons has a strong history and are a proud, confident company. As
part of the redesign our team came up with a variety of designs, and
convinced the client that they should go bold. I worked with the design
team to see what ideas we could easily pitch, what ideas would be
difficult to execute, and others that should probably live in the
'maybe' pile. The client completely bought into the route we put
forward, and we were on our way.

I was charged with architecting the entire website from the ground up.
The team chose [Umbraco](http://umbraco.com/ "Umbraco") for the project,
and worked hard to push what the CMS could do. I acted as a team lead;
in charge of cutting up the work into smaller pieces and deciding who on
the team - myself as well as others - did what. I worked closely with
the design and UX team members to make sure that everything we were
doing was creating a solid user experience; not just something that
looked good or worked well, but a solution that did both and could
delight the user as well.

The end result was a website that was re-thought from the ground up: the
system running the site, the design, the user experience, the HTML, the
CSS; everything. The client were right along side us during the entire
thing, and they're ecstatic about it.

Front-end highlights
--------------------

[![Clarksons.com -
Services](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-services.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-services.jpg)

### Responsive layout

[![Clarksons.com - Home
(iphone)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-iphone-home-410x621.jpg){: class=alignright }](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-iphone-home.jpg)

One of the biggest challenges from the front-end of the website was the
fact that it was to be fluidly responsive. This means that we had to
cater from large screens all the way down to mobile, and everything
in-between. This was easily my biggest responsive project to date, and
we really had to work on the in-house workflows. We decided to figure
out where the major breakpoints were going to be, and start by making
sure those looked correct. Once we had all of those pinned down I sat
with the designer and we went through every page type at very resolution
to hammer out all of the little parts that didn't look quite right.
There were many, *many* iterations like this throughout the project in
order to ensure a consistent experience across the website.

### Coding standards

[![Clarksons.com - Office map
(iPad)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-map-410x550.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-map.jpg)

One of the big changes that came with this project was my institution of
a standard for our coding. I had been working on it across a couple
previous projects, and Clarksons was where everything came together.
This project acted as the initial test, refinement, and acceptance of
how RY was going to do it's JavaScript. Given how we tend to use most of
our code, I've decided that we should work with an object literal
pattern. This may not end up being where RY rests with it's JavaScript
code development, but I wanted to introduce structured fundamentals to
our development plan.

A major change in our coding process was how code was to be laid out.
Full disclosure that I can be as bad as others when it comes to lazy
coding and creating god functions. With Clarksons, I aimed to put an end
to that. By creating namespaces and standard formats, we could start to
build the code into logical sections. Beyond that, we could start to
breakdown our god functions into smaller, testable pieces of code. my
hope is that with this structure, we will be able to move towards a
proper test-driven development cycle for future projects.

[![Clarksons.com - Containers
(iPad)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-service-1024x731.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-service.jpg)

A fair amount of time was dedicated to the mobile experience of the
Clarksons website. One of the major changes had to do with the
navigation to the website. On small screens, we decided to collapse the
menu and hide it behind a navigation button (a tried and tested method
that web users are used to), and the code to do this was only run on
page load. While I could have very easily attached a monitoring function
to the window resize functionality, I didn't see the point. Users cannot
resize their mobile device screens, so why should there be extra code
written that won't do anything to assist them? By leaving the code to be
onload only, I saved having to import another plugin to throttle the
resize requests, and removed excess code before it became an issue.

Back-end highlights
-------------------

[![Clarksons.com -
Contacts](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-contacts.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-desktop-contacts.jpg)

### CMS Choices

The rebuild of the Clarksons was easily my biggest project to date, as
well as my biggest Umbraco project. We as a team opted to create the
project in Umbraco for a couple reasons. First was cost; we were looking
to find a CMS that worked with the projects' budget. While we could have
gone with something like SiteCore, it was cost prohibitive and Umbraco
ticked most of the boxes right off the bat. Second, Umbraco is an up and
coming CMS with a great community behind it. This will work to our
advantage later on as the projects grows and evolves. Third, the site
structure and format lends itself towards the Umbraco CMS structure.

[![Clarksons.com - Homepage
(iPad)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-home-410x550.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-ipad-home.jpg)

One of the decisions made - for better or worse - was to stick with XSLT
renderings as opposed to switching to Razor. This is mostly due to the
version of Umbraco in which Clarksons was started in. While later
versions of 4.x of Umbraco had Razor support, we weren't comfortable
using something that had been back-patched into the system. Had we
started with Umbraco 6, this would be a totally different matter. The
use of XSLT introduced some interesting challenges when it came to the
Module system I created, but other than that everything worked pretty
much as expected.

This was also my first foray into creating custom Umbraco controls for
the admin panel. It was a fun learning experience, but really helped
hammer in just how powerful Umbraco can be with a little bit of
investigation. With the extensibility of Umbracos control model, I
created various admin sections that would have been awkward or
cumbersome for the user to use if left to the default Umbraco data-type
renderings.

### The Pen is Mightier

[![Clarksons.com - ideas on
paper](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-papers.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-papers.jpg)

Given the overall size of the website and the requirements gathering the
team had done earlier, I decided not to dive right into Umbraco and
start building things. I opted to start as many others do: with pencil
and paper. I spent my first week on the project just sketching out the
overall structure of the website, the doctypes I would probably need,
the various custom data types that were going to be used, as well as the
inheritance structure and overall site structure. I can say with
conviction that taking the time to sketch out the basics of the website
(even with the knowledge that things would change as the project went
along), ended up saving me a lot of time. Sketching everything out
helped solidify the overall systems that I ended up building.

### Going where Umbraco doesn't: Modular layouts

[![Clarksons.com - Broking
(iPhone)](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-iphone-broking-410x621.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/06/clarksons-iphone-broking.jpg)

For all of the great things that Umbraco does, it doesn't make
customising pages an easy thing for end users. Alternate renderings for
pages is straightforward enough, but that is limiting unless you want to
offer every possible permutation of a page and its various models. I
decided to create a system within Umbraco that allowed for a far greater
amount of page customisation. This was created by some creative use of
the document types system within Umbraco, coupled with some elaborate
XSLT.

The end result was that a user could effectively add 1 or more 'Row
Holders' to any given page. These row holders could themselves hold
'Rows', and the rows can all hold 'Modules.' The Modules in the project
are many and varied, but all inherit from a generic module. This allows
every module to work within the system. Each module has its own XSLT
rendering that is imported via the Rows rendering, and this sort
of flexibility really let us move beyond what Umbraco typically allows.

In the end
----------

This was a big project for me. It was full of firsts, and it was a
challenge. It also happens to be one of the best projects I've ever
worked on, let alone completed. The design and construction requirements
were ambitious, and I'm happy to say that it worked out very well.

View the website
[here](http://www.clarksons.com "Clarksons: The heart of global shipping").
