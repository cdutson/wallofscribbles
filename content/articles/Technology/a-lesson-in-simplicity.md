Title: A Lesson in Simplicity
Date: 2009-02-26 11:00
Author: Corey Dutson
Tags: DSL, Linksys, Modem, Router, simplicity, Bad bad bad
Slug: a-lesson-in-simplicity
Status: published

So the recently passed weekend offered to me an adventure:
troubleshooting the Internet connection at Theresa's place. Now some of
you may be wondering how troubleshooting someones Internet connection
could be an adventure, and I completely understand your confusion and/or
skepticism. Believe me that I wasn't expecting an adventure for
something that was, at the time, very straight-forward.

You see on Sunday afternoon, the Internet connection at Theresa's house
was dreadfully slow, and would randomly disconnect for a couple seconds
at a time. Just enough time to cancel any sort of operation you were
hoping to do while browsing the Interwebs. I, being the only tech-savvy
person about, was given the … opportunity to correct the situation.

This is not what I wanted to do with my weekend, but sadly when your
girlfriend is Internet dependent and gets frustrated when things don't
work (don't we all though?) it makes fixing said Internet.


<!-- PELICAN_END_SUMMARY -->


Let me run down the possible causes for you really quickly so that you
know where I'm going with this:

1.  GF's laptop was crapping itself
2.  The phone line filters are crapping themselves (the house runs on a
    DSL sytem)
3.  The router is crapping itself
4.  The modem is crapping itself
5.  The provider is crapping itself
6.  The wiring between the modem and router is crapping itself
7.  The phone line to the modem is crapping itself
8.  God hates me.

As you can see, I basically presumed that something had failed along the
way ("crapping itself" is a very technical umbrella term). Note that for
everything but the finale of this sad tale, I was on the phone with
technical support, combining our brains to figure all of this out.

Now I knew it couldn't be her laptop, because everyone on the network
was being effected (my own laptop included). I also knew that it
couldn't be the filters, because not too long ago we had to call tech
support to find out why things weren't working before. One of the steps
they got me to try was to unplug all of the phones and see of that was
the issue, it wasn't. I accessed the router and it was fine; no lag, no
anything. I sat there and pounded the f5 key on the Net connection page
to see if it was disconnecting. As it worked out, it was.

"Ha!" I thought to myself, "easy fix, new modem and we'll be up and
running in no time!" This was, as it turned out, a half-truth.

Attempt One: Modem & Wires
--------------------------

I bought a new modem from the provider (120 dollars, give or take a
little) and went home and plugged it in. The connection became solid,
but still slower than it really should have. "Hmm, alright so the modem
*did* need replacing, but that wasn't the cause for the slowdown." I
then decided to replace the wiring from wall to modem, as well as modem
to router. Shiny, brand new wires were put in, and there was little to
no change.

Attempt Two: Router
-------------------

"HMMMmmm," went I, "okay so it's not anything to do with the modem, so
it must be something to do with the router!" See the router was also
getting on in years, and though it was still functioning it could
probably be upgraded. So I started by upgrading the firmware (**fuck
you** Linksys for making the worst navigation on a website *ever*) and
though the router was happy, it didn't fix anything.



I then opted to upgrade the router (90 dollars after tax for a new
Linksys [Wireless-N Broadband
Router](http://www.linksysbycisco.com/US/en/products/WRT160N "Wireless-N Broadband RouterWRT160N")),
and set that up. Everything was hunky-dory with the router, and the
network was running fine. Sadly though the speed was still painfully
slow. A little faster, thanks to everything I had done, but still
running at about 300 kb/s (thank you
[speedtest.net](http://www.speedtest.net "Speedtest.net") for not going
down via my repeated tests). That's terrible for a DSL, even a DSL at
the maximum range from the switch.

Attempt Three: Filters
----------------------

At this point I've become frustrated, and decide that maybe it *is* a
filter after all. Who knows, between the last time I called them and now
maybe a filter could have died. I ran around the house and unplugged all
of the phones, and did a speed test. Still sitting at 300 or so. "FUCK,"
declared me, "what is going on!? There's nothing left to cause this!"
That's when I decided to canvas the house for any phone that could be
missing a filter. Still nothing, until on a whim I checked the sisters
room.

Attempt Four: Filters (again)
-----------------------------

And here is the finale, folks.

Now I knew that she didn't have a phone. Hell she never answered it
anyways so why would she have one? I had even been in her room recently
playing with the cat, and I had seen no phone. She has a Blackberry that
she uses for everything. She has no need for a land line.

Of course, there was a phone in the room.

A phone lacking a filter.

A filterless, fucking, phone.

I unplugged the phone, and ran another speed test; 1200 kb/s. I plugged
the phone back in and ran the test; 300 kb/s. I then attached a filter
(we had two laying around the house) and ran a speed test; 1200 kb/s.

So 210 dollars later, it was a missing filter that was causing most of
the errors.

What I've learned
-----------------

Sometimes the simple answer really is the right answer.

I replaced everything around the filters figuring that they couldn't be
the issue, but I was only half-right. All the filters were working
properly; it was a lack of one that caused the issue. Had I bothered to
canvas the house *first*, I could have saved the family 210 dollars.
Granted the modem *was* failing slowly and would had to have been
replaced eventually. I rationalize it this way: at least we don't need
to worry about the modem or router failing for another couple years.

Also, I'm pretty sure God still hates me, so I'm going to say it was a
joint problem.
