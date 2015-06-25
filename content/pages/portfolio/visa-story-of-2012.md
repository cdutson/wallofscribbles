Title: Visa Story of 2012
Date: 2013-02-02 10:45
Author: Corey Dutson
Tags: 2012, Accessibility, Annual Report, JavaScript, php, Project lead, Responsive layout, SEO, Stepped responsive, Visa Europe
Slug: visa-story-of-2012
Status: published
SlugPic: wp-content/uploads/2013/05/visa-square.jpg
Summary: I acted as the technical lead for the Visa Europe 2012 report. I advised a junior developer on best practices, helped troubleshoot issues, and built the mobile framework for the responsive variations of the website.  


[![Visa AR 2012 -
Home](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-desktop-home.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-desktop-home.jpg)

Overview
--------

Visa was a change of pace for me, as it was one my first projects where
I wasn't going to be the primary builder. I was instead tasked with
advising one of our juniors on how to build a successful responsive
report.

The Visa report was unique in that Visa Europe don't have to report the
same amount as other companies, as they aren’t a publicly-traded
company; as such there was a much greater focus on telling their story
and making them accessible to everyone. A by-product of this was that
the website had to be responsive, and it had to work well within that
responsiveness.

Another big thing hanging over the project was the fact that the
previous years report simply did not work well. It was broken at the
best of times, but quickly degraded into an unusable state. We had to
make sure that this years report worked when things like JavaScript were
disabled, and we had to make sure the pages could be easily shared.

My role throughout the project was that of lead developer. While I made
the decision to let the Junior get his hands on a couple concept he
hadn’t worked with before, it was still my overall responsibility to get
the project out the door. I built the JavaScript framework that ran the
functionality of the website, as well as doing code reviews and code
clean-up with the junior developer on the project. I was also
responsible for debugging some of the trickier issues that popped up.

[![Visa AR 2012 -
Strategy](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-desktop-scrolled.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-desktop-scrolled.jpg)

Front-end highlights
--------------------

[![Visa AR 2012 - Mobile
Home](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-iphone-home-410x621.jpg){: class=alignleft }](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-iphone-home.jpg)The
website had a limited budget. It wasn’t a small budget, but it was small
enough that we had to be pragmatic when suggesting solutions to the
client.

One of the big things Visa desired was a solution that worked all the
way down to mobile. We suggested that the website use what I tend to
call a “stepped responsive” methodology. what that basically means that
instead of a site that flowed from one resolution to the next, we
instead target the most common sizes as based on their historical viewer
statistics. This allowed us to target some key sizes (960, 768, 640 and
smaller), which in turn allowed us far greater control over the design.
This also allowed us to help control design expectation and iterations,
and help cut down overall costs.

The stepped responsive was useful as both a teaching tool and as an
excellent constraint for javascript functionality. I explained the
basics to him and let hm get on his way.

[![Visa AR 2012 - Mobile
content](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-iphone-content-410x621.jpg){: class=alignright }](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-iphone-content.jpg)

The JavaScript for the desktop variations was rather minimal. Most of
the work lay in the mobile side of the layout. At smaller sizes, pages
would have become too long and bulky with the content on them. The
designer proposed a sort of “slide in place” tool that would allow us to
hide excess content, and slide it in as a side panel. While this sounds
straight-forward (and something I have done before) the catch was that
the user would need to slide back to where they were when they pressed
the back button.

I ended up working closely with the design and UX crew while developing
this solution. I worked had to make thee transitions as smooth as
possible; a thing easier said than accomplished. I went through many
iterations and adjustments to the code to come up with something we
could all be happy. This was easily the biggest challenge for me on this
project.

Back-end highlights
-------------------

[![Visa AR 2012 - Ipad
home](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-wide.jpg)](http://wallofscribbles.com/wp-content/uploads/2013/06/visa-wide.jpg)

As previously mentioned, one of the big issues last year revolved around
the accessibility and usability of the website. The previous builders
hadn’t done a very good job of it, and as such the website completely
fell down when viewed on mobile devices or when a user without
JavaScript visited the page. On top of that, content was AJAXed in
without any sort of fallback, and some massive hacks had to be
introduced just to get typical sharing buttons to work.

With these faults in mind, we had to make sure that the entire website
worked well without any additional scripting. This meant that the markup
had to be first-rate, the site structure made sense, and that we had
functioning navigation at the various resolutions. There was a lot of
work put into the scriptless version of the website by both the
development team as well as the designers.

The end result of our dedication was a website that completed the
project objectives without scripting, and was gracefully enhanced with
delightful elements to really make a users’ journey as pleasant as
possible. As a positive side effect to our work, the website also ended
up having rather good SEO.

View the website
[here](http://annualreport.visaeurope.com/ "Visa Annual Report 2012").
