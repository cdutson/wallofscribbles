Title: WordPress plugins, I has them
Date: 2009-01-12 14:14
Author: Corey Dutson
Category: Code, Technology, Wordpress
Tags: Code, plugins, PostDivider, RandomQuotr, Wordpress
Slug: wordpress-plugins-i-has-them
Status: published

The [lolcat](http://icanhascheezburger.com/ "Lolcats!") title reference
aside, I have actually started producing WordPress plugins for myself.
I've always wanted to make them, and so a while back I set aside a day
(well two, once I got the hang of it) and learned. Granted I've still
got a ways to go, but at least I've finally got my foot in the door with
it all. The trick is to make sure to create things that are actually
useful so that people will actually use them.

So as a result of my tooling around with WordPress, I've created two
plugins for people to use.

<!--more-->
-----------

RandomQuotr
-----------

In one of my older site lay­outs, I had a random quote dis­play­ing at
the top of the page. The orig­i­nal logic was based very much on the
Hello Dolly plugin that comes shipped with Word­Press. Even though I no
longer use the func­tion within my layout, I still had the code and I
felt that with a little revi­sion, this could be a psudo-​useful plugin.

So one morn­ing I did exactly that.
[Ran­domQuotr](/wordpress-plugins/randomquotr/ "Corey Dutson: RandomQuotr")
was born, and with it came the abil­ity to store all of the quotes
within the WordPress data­base, as opposed to the PHP array that it
started out as. Some more func­tion­al­ity was added to allow the
selec­tion of spe­cific quotes.

PostDivider
-----------

I was a big advo­cate for using “the\_excerpt()” for my sites layout,
because it allowed me to split up my con­tent and work around my theme.
the prob­lem is that using “the\_excerpt()” sucks for many reasons:

1.  The field is HTML only.
2.  The field is tiny and cannot be re-​sized.
3.  It requires you to break up your most in a less than stel­lar way.

Enter
[Post­Di­vider](/wordpress-plugins/postdivider/ "Corey Dutson: PostDivider").

Based on an [old post of
mine](/2008/10/02/getting-more-with-the-more-tag/ "WallOfScribbles.com: More with the More Tag"),
Post­Di­vider allows the user to get the con­tent before and after the
&lt;!–MORE–&gt; tag sep­a­rately. With Post­Di­vider, hooks are
pro­vided to allow the Theme to dis­play the text directly (echo­ing
it), or return­ing the con­tent as a value from the func­tion. If no
&lt;!–MORE–&gt; tag is pro­vided, it will return the\_excerpt() and
the\_content() respectively.

So far those are the only ones I've developed. I've got a couple ideas
for more, when I get around to building my portfolio and the like.

I've also [created a
page](/wordpress-plugins/ "Corey Dutson: WordPress Plugins") that lists
all of the plugins I have developed. They're also hosted over on the
[wordpress.org plugins
directory](http://wordpress.org/extend/plugins/profile/loveless "Wordpress.org: Loveless")
if you want to keep watch there.

I'm always looking for feedback or suggestions, so feel free to email me
or leave a comment.
