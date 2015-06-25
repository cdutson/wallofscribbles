Title: SharePoint 2007: Thoughts on Branding
Date: 2007-11-09 01:29
Author: Corey Dutson
Category: Design, Microsoft, Technology
Tags: branding, Cameron Molls, CSS, customization, Design, designing, job, MOSS 2007, SharePoint 2007, Technology
Slug: sharepoint-2007-thoughts-on-branding
Status: published

In any case, my work specializes in [SharePoint
2007](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007")
customization. Some of our stuff can currently be seen on the net,
though for safety-sake I will not mention where. (I'm knew to this
job-related posting thing, cut me some slack.)
[Cameron](http://cameronmoll.com/archives/2007/10/sharepoint_2007_pointedly_unskinnable/ "Cameron Moll")states
that SharePoint is good for CMS or collaboration, but using it for both
is basically a masochistic task branding-wise. This is basically my job.
I do other things too, but for the most part I turn our [very talented
designer's](http://plantt.ca/ "Richard Plantt") visions into realities.
As I stated previously, I manipulate the crap out of
[SharePoint](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007").
It is my domain (or so I keep telling myself) and I turn the sad excuse
for a vanilla theme into something worth looking at.

To be honest: it's a pain. There is no way around that. I've had moments
in my still-new career where I've wanted to put my fist through the
screen in frustration from applying a brand to the system. Now all that
aside - I'm getting worked up here - It doesn't have to be a nightmare.
There are ways to cascade changes throughout a site without sacrificing
a lamb. This is of course assuming you don't have to *also* brand the
administrative side of the whole deal. The reason for this is fairly
simple:
[SharePoint's](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007")
administrative templates are powered from the file system, and not
through their ghosting system.

I'm going to take a moment to clarify "Ghosting".
[SharePoint](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007")
operates on a template basis. That means that when you use what is given
by
[SharePoint](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007"),
it all points to the same file. The second you go and customize that
file, a new copy is created in the database, and so the original is left
in tact. This is called ghosting. Whenever you customize a page, you are
effectively "unghosting" the page. That is to say that you are no longer
living from the predefined, but making your own file in the database.
This is a great idea which can help save on server memory (Hard
disk-wise) and I totally agree with it.

So why the hell did Microsoft decide that all the administrative pages
be fueled by a totally different system? They do indeed say it was
purposely designed that way, but I call bull on that. What it sounds
like to me is that they either ran out of time, or had the front-end
team and the back-end team kept in different buildings, and told never
to talk to one another under pain of death. As a result, when you decide
you want to brand anything in the back end, you have three options:

1.  Stick to manipulating the CSS. I wont get into the agony of
    explaining this in detail simply because it would take too long. The
    short of it is that the CORE.CSS that SharePoint uses is over 4000
    lines by itself. Never mind the other eight they have for
    special instances. On top of that, you are limited to all the
    elements that are on the page. This is severely limiting and at the
    very least, painful. Finding what classes do what can be akin to
    pulling teeth out with a 9 iron.
2.  Make a theme. I hate themes with a passion. They were obviously
    tacked on as an afterthought and it shows. Who's the genius that
    figured that resetting the server in order for any changes you made
    to the core theme folder to appear in your applications. further
    more, why in Gods name would you copy the files to the local site
    instead of referencing them? That means that if there was a critical
    error in your theme and you've already applied it to 60 sites, you
    now have to go into each of those sites and apply the default again
    and *then* apply the now-fixed theme. I hope whoever did that
    was fired.
3.  Change the file-system items. The short of this: Don't. You *can* do
    that, you really can but I will guarantee that this will eventually
    end in heartbreak. What happens when the updates roll out - and you
    know they will- and overwrite your hard work? Now you have to go
    back and re-work everything on the page. God only knows
    what's changed. This is the minor half of the problem though.

The only viable option is the first one. It sucks on levels all unto
itself, however since the second sucks when your site has more then one
sub-site is even worse, and the third option generally leads to tears
and wasted hours (been there, done that) it's still the best option in
the end.  
<!--adsense-->  
"*But Corey! Surely editing the system files allows for the most
customization and look/feel!*" Absolutely right, and I won't argue that
point. I will argue that I'll advocate against it whenever possible
though. Here's why:

The big problem is that since you are editing file-system items, they're
shared. That's right. If you have two totally unique site hosted on the
same box, you're going to notice that one of them is going to the
administrative look of the other site. This could be manageable if only
administrators saw it. The odds of this are that at some point you are
going to go into a list. the master page for viewing *all* lists is one
of those shared items. It's the same one used for branding
administrative panels. See where I'm going with this? Heck, even if its
just a collaboration site, that will still come up.

[Cameron](http://cameronmoll.com/archives/2007/10/sharepoint_2007_pointedly_unskinnable/ "Cameron Moll")
shows off the website "[Hawaiian
Airlines](http://www.hawaiianair.com/Pages/Index.aspx "Hawaiian Airlines")"
which is a pretty nice site. Simple, to the point, and gets the job
done. It's also had every page customized (it appears to be that way to
me, I could be wrong), and custom parts have obviously played a rather
large part of the site. I'm not bashing it in any way here, so please
don't misunderstand. What I'm saying is there was a *lot* of care put
into making that site look the way it does, and I can only pray that
they didn't brand the back-end with the same zeal as they did the front.
If they did, i weep at their commitment.

What I'm getting at here is that though there are many ways to brand
[SharePoint](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007"),
none of them are painless. The best route is trying to convince your
client/boss/whoever is paying for the endeavor not to bother branding
the back-end. This is a rare treat and you really shouldn't go expecting
it. Failing that, I suggest going with option 1. It's a pain in the ass
but it's the easiest in the long run. You can also ease the pain by
using tools like [Firebug](http://www.getfirebug.com/ "Firebug") and the
[IE Development
Toolbar](http://www.microsoft.com/downloads/details.aspx?familyid=e59c3964-672d-4511-bb3e-2d5e1db91038&displaylang=en "Internet Explorer Developer Toolbar").
If you have to go beyond that (which I have had to do in the past, and I
am certain I will be doing so in the future as well) then I wish you
luck. You'll need it.

The last point I'll touch on is something [Mr.
Moll](http://cameronmoll.com/archives/2007/10/sharepoint_2007_pointedly_unskinnable/ "Cameron Moll")
covers in the last paragraph. The user experience in Vanilla [MOSS
2007](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007")
is depressing sometimes. Limitations for no real reason, way too much
user effort for minimal gain, and don't get me started on the many,
*many* useless steps to achieve certain things. Welcome to the other
half of my job. I won't get into this part too much, but despite my boss
wanting us to stay away from customization wherever possible, I've
noticed that to really take advantage of what
[SharePoint's](http://office.microsoft.com/en-us/sharepointserver/FX100492001033.aspx "SharePoint 2007")
core ability *can* do... well you need to be there to customize a
solution to access the power. Don't get me wrong, SharePoint can do a
lot of things, but as I have experienced in the past it generally makes
the development team work- and work hard- for it.

And that's my two cents on it.I like my job, I really do. I've learned
what I deem to be 'snoot loads' but it's been a hard way getting here.
I'm glad for it, but seriously: fist through the screen frustrated
sometimes. Good luck people.
