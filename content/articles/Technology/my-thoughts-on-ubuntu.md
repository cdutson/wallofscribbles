Title: My thoughts on Ubuntu
Date: 2008-02-25 00:05
Author: Corey Dutson
Tags: Apache, D-link, Django, eBay, Linux, Microsoft, Operating systems, OS, Python, Redhat, Technology, Toshiba, Ubuntu
Slug: my-thoughts-on-ubuntu
Status: published



I brought my old laptop out of commission ([Toshiba
A10](http://www.toshiba.ca/web/product.grp?section=1&group=223&product=1911 "Toshiba Satellite A10"),
with a newly purchased [wireless
card](http://www.dlink.com/products/?pid=472&sec=0 "D-Link: Rangebooster G")
and
[battery](http://search.ebay.ca/search/search.dll?from=R40&_trksid=m37&satitle=satellite+a10+battery&category0= "ebay: Toshiba Satellite A10 Batteries"))
and started off by re-imaging the thing to factory settings. This means
I have Windows XP: Home Edition, and not much else. I figured that if
nothing else I could have a laptop with windows on it for when I go
around places. This was not the goal though, as I really want to get
into some python coding. I don't feel like struggling to get python and
Apache running on my main desktop, and even less with fighting with them
to run in Windows.

Enter [Ubuntu](http://www.ubuntu.com/ "Linix: Ubuntu"), stage left.

I like free stuff. Ubuntu is free, so by defenition I like that. I like
even more that it has a CD image that you can burn to work as a boot
disc. The CD allows you to actually give the system a whirl before you
install it by running totally from the CD. Granted you can't do
everything, but it intrigued me enough to actually install the OS (which
is a link on the desktop. Convenient, no?) It gives you the option of
having a boot system picker which was good since I still want Windows on
a partition of the computer. All in all it's an easy and straight
forward installation.

I let it reboot, and once I picked my OS (Ubuntu in this case) I was
presented with the following: Loading... Could not find region 4 of
device 0:00:0 (or something to that effect) and then another Loading...

And then the screen went black. I thought that Ubuntu had shit itself on
the install, and i decided to reinstall it.

Same thing happened. I was a little worried and upset, but I decided to
exercise some patience and see what happens. Two minutes later, the
login screen suddenly appears. I have no idea why, but there we go.
First thing I wanted to get going was my wireless, since I want my
laptop to once again be mobile (the A10 does have a built in wireless,
but it's only WEP and I don't do that in my house.)

Ubuntu has a nifty feature that allows you to install any supported
program right from the menu. No searching for the programs on the
internet and having to do anything manual. What I dislike about what is
otherwise a fantastic little program is that you need a connection to
the Internet in order to have up-to-date lists, as well as download said
programs.



Apparently in order to install
[ndiswrapper](http://ndiswrapper.sourceforge.net/joomla/ "Linux: ndiswrapper")
- a wireless card support program - you need to actually be connected to
the internet in order to make it go in the first place. I couldn't help
but laugh at the irony. In the end I whipped out my trusty Ethernet
cable and hooked into the router, which was awkward given the fact that
it's on a shelf in the basement. Ubuntu was online in seconds, and so
was the update manager. How the hell does one program have 188 updates
off the bat? So I installed all of the updates, as well as ndiswrapper.
Then after that I had to fight with the wireless connection for a good 5
minutes (2 of those were realizing that I missed a character in my
wireless key!) and now I'm up and running.

One of the major things I've noticed with Ubuntu in comparison to
Windows is the battery life. I just got a brand new battery (the A10
battery is notoriously short-lived) and I've run it down on both
operating systems. Windows can run for 3 hours if I turn everything down
to the lowest possible setting, and maximize the power saving tools
given to me. Ubuntu also does about 3 hours of battery life, yet it does
it without sacrificing any of my processing power. Granted it probably
doesn't have nearly as much running in the background, but I'm still
impressed. On the flip side, my battery charges way slower in Ubuntu
than in Windows. (6 hours to charge? What the hell?)  
I am currently installing Apache server (one line in the terminal) and
Django (a couple more lines and God knows what else), though it all
seems fairly straight forward. Getting the needed programs up and
running seems to take very little effort, usually two or three commands.

One thing that bugs me, though I'm not sure I can actually blame this
one on Ubuntu, but there are certain commands and functions that I used
to speed up my computer use. Things like using backspace to navigate to
a previous page doesn't work in Firefox running on Ubuntu. (Note:
Shortly after writing this, I found out that Ubuntu has an installed
modification for Firefox that you can remove) There are other things
like quick keys to minimize everything and jump to the terminal elude
me. I'm sure this is at least half of a training issue.

I'll talk more about the OS as I get more and more into it, right now I
have to figure out how to get DJango running in my environment.

PS, Why is it so
[orange](http://www.productwiki.com/upload/images/ubuntu_7_10_screenshot_1-510-375.jpg "Ubunto is orange!")?
