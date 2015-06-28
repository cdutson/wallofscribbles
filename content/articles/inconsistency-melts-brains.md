Title: Inconsistency Melts Brains
Date: 2008-03-06 00:05
Author: Corey Dutson
Category: Design, Microsoft, Miscellaneous, Self-Improvement, Technology
Tags: consistency, Design, forms, good-practices, Internet, Microsoft, SharePoint, WSS
Slug: inconsistency-melts-brains
Status: published

I'm bringing this up from an exceptionally small thing I noticed while
at work today. As I have previously stated, I work with
[SharePoint](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "Microsoft SharePoint 2007").
Much of the time I am branding it (though not in my current project!)
and so I have a rather intimate and abusive relationship with the
program. I find myself constantly finding weird styling quirks put into
the environment that prove that SharePoint was built by a large group of
people.

There are many instances within SharePoint - and I'm sure within
[WSS](http://office.microsoft.com/en-us/sharepointtechnology/FX100503841033.aspx "Microsoft WSS 3,0")
as well - where certain styles that should be consistent end up being
done completely different ways. I wish I had a screen shot as an
example, but you'll have to use your imagination here. Picture two
dropdown buttons. When you hover over them, they glow, and a menu
appears. No picture the HTML for both dropdown buttons being completely
different, with no shared styles or markup whatsoever.

This happens all over the place. Hell, there is markup all over the
place that is either broken, non-standard ([don't get me
started]({filename}sharepoint-2007-what-the-hell-man.md "SharePoint 2007: What the hell, man?")
on WSS/SharePoint and it's default markup) and over 6 thousand lines of
styles if you add up all the sheets. 6 thousand! There is no need for
that, and yet it exists because of - *say it with me now* - the lack of
consistency.This lack of consistency then cascades down to people like
me, who are stuck styling the damned things. Had there been a discussion
between the differing groups, or the markup left to a third group so
that they could all be structured the same way other peoples lives would
then be made easier.



Another example I can bring up is with code. My code, my co-workers
code, random interweb code, it happens everywhere. It is far more
frequent when you work on rapid products, or many projects that build
off of their predecessor. I can speak from experience that unless you
code with the future in mind you will end up patching things... usually
more than once.

In a perfect world you'd be able to properly scope your work out,
develop your use cases, figure out your flow, and develop in a modular,
expandable way. This of course requires a couple things: Time, patience,
and knowledge. I can assure you that even if you think you have all
three you don't. The only time this can *ever* happen is when you are
developing something for yourself and even then more often than not
you're just throwing something together for your own use, and those tend
to be the worst for patch jobs... at least from my experience.

In the end all I can say is *plan things out*. Figure out a system and
stick to it; even if it's not the best it will at least not be the best
everywhere. This makes it much easier to upgrade/fix later on. If you
come up with 5 different solutions for 5 different things when they
could all share common attributes, you are just making more work for
yourself.

Save your time, your brain, and your fellow workers from the agony of
added work brought about by inconsistency. Get a game plan, stick with
it, and for the love of god: be consistent.

*P.S. I managed to spell consistency wrong every time in this post while
writing it.*

*P.P.S. Except for the one in the first postscript.*

**Update:**

Success! I have a screen shot of the dropdown menus in question!  
*(Technically this update happened before the post went public, but
whatever)*
