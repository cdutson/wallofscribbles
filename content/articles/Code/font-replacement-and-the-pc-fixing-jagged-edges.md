Title: Font-replacement and the PC: fixing jagged edges
Date: 2011-03-31 15:45
Author: Corey Dutson
Tags: fonts, pc
Slug: font-replacement-and-the-pc-fixing-jagged-edges
Status: published

Font-replacement is a thing now on the internet. Gone are the days of
Helvetica, Arial, and like, three other fonts. Now designers, coders,
and hacks can add fonts to any web project. Heck, sometimes even for
free!

But of course there are always drawbacks. The number of font-files you
need is staggering, and the CSS you need to set up borders on the
insane. Here's [the best CSS code I've seen for
that](http://www.fontspring.com/blog/the-new-bulletproof-font-face-syntax "fontspring.com - The New Bulletproof @Font-Face Syntax").
Then there's the licensing issues: font's ain't free (mostly). If you
want to use a good collection of the fonts out there, you have to pay.
There are loads of services out there at this point that can serve up
almost every possible font you could ever want.
[Some](http://www.fontspring.com/ "fontspring.com")
[you](http://typekit.com/ "Typekit")
[pay](http://fontdeck.com/ "Fontdeck")
[for](http://webfonts.fonts.com/ "webfonts at fonts.com"), some (like
what I use for my own website)
[are](http://www.fontsquirrel.com/ "font squirrel")
[free](http://www.google.com/webfonts "google webfonts").

Getting past the pay barrier and the CSS file drudgery, you are left
with another issue: rendering. Some fonts, while applicable for the web,
have not been optimized. There's a big difference between a
web-optimized font, and a print font that has been released *to* the
web. That is to say the latter look like shit most of the time. This is
a major difference between a mac and a PC.

Let me explain further.


<!-- PELICAN_END_SUMMARY -->


The problem
-----------

Macs render fonts amazingly out of the box. The webkit engine comes with
a special property for font-smoothing (called -webkit-font-smoothing)
that is used in tandem with this. These properties do affect the PC
versions of Webkit browsers, but not quite. For more info on this css
property, read [this
article](http://maxvoltar.com/archive/-webkit-font-smoothing "Maxvoltar - webkit-font-smoothing"),
which explains it in great detail.

For all the other engines (excluding the recently released Firefox 4,
where fonts look mostly awesome), non-optimized fonts will look ragged
because they aren't aliased at all. Think of what the font looks like on
ie6 (for those that can remember). This is what happens. the Cleartype
property that Windows applies doesn't actually work on these fonts.

The fix
-------

After some playing around, I've come up with a fix, though it does come
with some caveats that I will outline after.



How this works:
---------------

Basically you make a super tiny, light shadow around your text that will
simulate the anti-aliasing that the mac does. The filter: dropshadow
will allow the font to render more smoothly in IE. The
webkit-font-smoothing stops fonts from ending up fat due to the macs
sub-pixel anti-aliasing in addition to a shadow.

Caveats
-------

-   The ie fix works *most* of the time. Far better on
    solid backgrounds. It can (but doesn't always) halo if you put it on
    transparent-background-ed items. Even if that item is in a container
    that has a background color, it can halo. The fix is to put a
    background color on the element itself (not every layout will allow
    for this, obviously)
-   This doesn't work well on small font-sizes. In fact, this will just
    cause your small fonts to look blurry and terrible. This fix works
    best for headings or other larger font-size items.
-   It also seems to have a problem with certain thin fonts. Not all
    thin fonts, just enough to screw with you.

So yeah, this isn't the be all and end all solution. It does however
work in a variety of cases, and like so many other fixes on the net, you
have to know when to use them and when not to. The best fix for web
fonts is, really, to use a web font that has been tailored for the web.
At the very least a font that has had a lot of attention given to its
hinting.

As always I welcome discussion, and ways to improve on this technique.
