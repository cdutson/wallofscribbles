Title: My jQuery plugin template is open season!
Date: 2011-03-03 15:00
Author: Corey Dutson
Tags: JavaScript, JQuery, plugins, work
Slug: my-jquery-plugin-is-open-season
Status: published

So I've been doing a lot of javascript development at work recently.
I've basically created a lot of our reusable javascript 'plugins' to
cover the common requirements of the work that we do. In many cases,
this resides mostly (but not entirely) in online annual-report creation.

Anyone that's in the business will know that there are some common
functional elements that you end up having to build with javascript:
accordions, tabs, faders, sliders, lightboxes, filters, etc. Many of
these items can bleed over into non-report sites, such as intranets or
even public-facing sites.


<!-- PELICAN_END_SUMMARY -->


Now some of those are fairly straight forward: an accordion is just a
simple animate of a content section, repeat per title; tabs? Same deal.
So you might be pretty inclined to just write the script adhoc on a
project to project basis, copy and pasting it as you go. We were doing
that at my work when I started on, but I found that we kept on having to
add something, remove something, add hooks at certain points etc. In
some cases we used someone else's plugin to do these things, but we ran
into some issues when it came to having to tweak the plugin for our
needs.

As I was hired on as the senior front-ender, I was given the task of
trying to help simplify things in our working process. This required me
to dive right into plugin development, because one spot we were spending
a lot of time was reinventing the wheel project to project. Even more
time was spent debugging random plugins, or lashing them together.

As my place of employment works with jQuery, I wanted to develop
something that could be maintained in-house, and would be a good
starting point for repeating functionality. I ended up developing a
jQuery plugin template, which I am sharing today.

Now, while I can't feature the plugins I've made for my work here on my
site (I'm pretty sure my they'd be less than impressed with that), I
feel it's fairly safe to distribute this template (boiler plate?) to the
internets. It's a compilation of a couple tutorials, as well as my own
exploration into javascript. I'd be more than happy to give credit where
it's due, but I cannot remember where the heck I got some of the
snippets I integrated. If anyone reading this happens to know, leave a
comment and I'll be more than happy to give said credit.

Below you will find my jQuery plugin template code in it's entirety. I'm
open to suggestions on how to improve it, so feel free to comment.



I've tried to comment the hell out of the code, so that it's as
straight-forward as possible. I assume that anyone that uses this will
strip out the comments, as well as any of the functionality that isn't
required.

Please feel free to use this, but If you'd be so kind as to give me
credit, that'd be swell. I can't force you, but we're all friends out
here, aren't we?
