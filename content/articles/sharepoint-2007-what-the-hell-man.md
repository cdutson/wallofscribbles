Title: SharePoint 2007: What the hell, man?
Date: 2008-01-31 00:15
Author: Corey Dutson
Category: Bad bad bad, Design, Microsoft
Tags: Bad bad bad, Code, Design, Features, Microsoft, SharePoint 2007
Slug: sharepoint-2007-what-the-hell-man
Status: published

So I've been charged with expanding on the functionality of a [Wiki
Library](http://www.microsoft.com/technet/technetmag/issues/2007/01/Wiki/default.aspx "Microsoft TechNet").
For those not in the know, a Wiki Library is part of SharePoint 2007
(not WSS) and allows for some nifty features such as version viewing,
article linking, and... yeah that's pretty much it. It does all of this
pretty well in and of itself. Woe be upon the person (me) who tries to
crack open this walnut of misery.

As it turns out, customizing a Wiki Library to do anything isn't just
difficult, it's not even a chore. It's a goddamn mission of epically
frustrating scale. Let's start off with some over-all items:

1.  I needed to create custom columns, some of which looked at lists.
2.  I needed to create a content type that was based off of the Wiki
    content type.
3.  I needed to customize the Wiki library to have said content type.
4.  I needed to add custom-made web parts to the various views of the
    Wiki Library (History, Edit, etc)
5.  I needed all of this to work through a feature

Where to start? Lets start from the bottom of the list, because as it
turns out this was the easiest and where I started.

You want to edit those page layouts eh? Well have fun because as it
turns out all of those files are system files, which means they're on
the hard-drive of the server and therefor shared. That means you can't
mess with one without causing a server-wide change. The solution? Copy
those layout pages and rename them. Now add them to your feature. I'm
not going to explain how to get the feature to deploy, that's a
different story all together.

That's sweet! Now how do you make *anything* use those pages? Well in
terms of all the little widgets (Versions tool, History Link, Incoming
Link) You will have to build your own versions of those controls. Why?
Well the URL of the pages that they point to are *hard-coded*. Simple
enough to get around, though annoying as hell. Just to demonstrate, to
the left is a screen shot of what SharePoints' markup looks like just to
recreate some of the controls in HTML. Seriously, that's messed up. In
the end *each link* was surrounded by *two more tables*. What the hell
man?

Okay so you got all of the default pages redirected. What about when you
edit an entry or make a new one? Those pages are tailored specifically
for Wiki Pages (CreateWebPage.aspx) and so you'll have to copy that one.
As for redirecting it? Well you *should* be able to do it via an Event
Receiver attached to the Feature that Installs the custom content type
that this is all based from. please note my use of the word 'should'
because I'm still stuck there.



Let's move onto the library for a moment. Now I have not been able to
replicate the Wiki library properly, without making my list type use the
basetype of '119'. As it turns out, this comes with a whole bunch of
strings attached, like having hidden name columns and a lot of red-tape.
I dare you to try and rename the "Name" column to anything with any sort
of graceful code. I'll leave that one there. For those that are
wondering, the default Feature for Wiki Libraries is called "WebPageLib"
or something of that nature. Try searching the 12 directory for the
content type of Wikis. To find that, go looking for the ctypes Feature
and look in there.

Creating the feature to house all of this turned out to be the easiest
portion of it all, though all of the problems stemmed from it in some
shape, way or form. I can't bitch too much about the feature markup
itself, because all it really lacks is some functionality that should...
well really should just be there. I've had to rig extra code together
just to get what I wanted, but read on and I'll explain.

I managed to create the content type with little issues, though I had to
add Remove references to the WikiPage content type (that does exist by
the way, it's just stored in the '\_Hidden' group which is why you can't
touch it via the site). Adding the new content type to the list template
was fun too, because you have to do it via the feature, since Wiki
libraries do not allow you to edit the Content Types of the list at all.
Like I said, Wikis are sealed, and don't like to play with the other
kids.

The problems really started when I created the site columns. Just a note
to everyone: if you ever feel like creating columns or content types,
then using them, and *then* trying to remove them via a feature, good
luck. SharePoint will not remove anything if it's being used. Just a
helpful tip there. This could be fixed via some EventReceiver code, but
I won't get into that.

Anyways, I had a column. It was a lookup column. It wanted to look at a
specific list, so I gave it the list id (though to be honest this is a
bad way to do it because what happens when you want to deploy this
feature somewhere else?). I deployed the column, and it worked! Then I
tried to use that column in a sub-site, which ended up failing
miserably. Took me forever to find out that you cannot specify a web
property in the feature. webid and scopeid, yes, but nothing generic
(refer to my listId comment here). The solution to this was to add more
custom EventReceiver code that would do this work for me. Which worked
great until I moved the feature to another site.

This is where my night went bollocks.

I installed the feature onto another dev-site and activated it (all
through stsadm). Worked fine. Then I tried to deactivate said feature,
and it would just sit there. I could uninstall it fine, but when I
deactivated it the process would just hang there and I'd be forced to
end it via Task Manager. It took me 6 ruined dev-sites to realize that I
was missing the lists that my lookups were pointing to. Apparently if
you tie a lookup column to a list that doesn't exist via code, it will
cripple the server when you try and remove that column from any content
types that it was attached to. When I say cripple, I'm not kidding.
stsadm.exe ran up 50 Mb of resident memory, and 100% of the CPU. The
best part was that no error would be logged, it would just hang there
forever. I admit I toyed with the idea of letting it run all night and
going home.

I kid you not, I laughed like a madman when I finally figured it out. I
cannot explain why, but that's just how it is. The lesson I learned from
this really was that I shouldn't have expected SharePoint to have any
sort of intelligence sitting behind it, and code for stupidity. Anything
you think SharePoint should probably just do probably doesn't actually
happen, or it happens with a hope and some duct tape.

Oh and for the record, I'm still stuck on how to change the Edit/New
pages properly.
