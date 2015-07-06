Title: Powered by Pelican
Date: 2015-07-06
Author: Corey Dutson
Tags: Pelican, blogs, Bartek, Wordpress, G Adventures, SASS, Python, Django, Github
Status: published

Eh, so what if it's been nearly 2 years since my last post? And so what if that last post was a long-form essay about my struggles with depression and attempted suicide? I mean, It's not like there was some chance that I could have written that, then gotten sad, and completed what a younger version of me failed to do! That's just crazy! Not worrying to anyone at all, I'm sure.

So anyways I've changed the website to use Pelican instead of Wordpress.

<!-- PELICAN_END_SUMMARY -->

## Why Pelican

My current place of work, [G Adventures](http://www.gadventures.com), is working on getting a tech blog up and running. When we were looking for a platform to write on, we wanted something easy to set up, easy to write for, and easy to publish.

Wordpress is usually the go-to for blogs, but we're not big fans of PHP. What's more, Wordpress is a resource-hogging beast. Tumblr could have worked as it's a solid platform, but we wanted to self-host, so that makes tumblr a no-go.

Pelican stood out because it generates a static site using a fabric script, so we can hook it into our current deployment systems. On top of that it uses Jinja2 templates, which we're all familiar with since we're a python/django house. So when it came time for me to try and get this blog up and running again, I didn't have to do the research: I already knew what I wanted to use.

## Pros n' Cons

For however great Pelican is, it's got some weird limitations that I had to make peace with. On the flip side, it has a lot of appealing aspects as well, so I thought I'd list out some of the pain points.

### Oddly limited

Pelican doesn't allow for sub-categories out of the gate (there is a [plugin](https://github.com/getpelican/pelican-plugins/tree/master/subcategory) for that). In fact, Pelican, as near as I can tell doesn't allow for multiple categories. What's more, there doesn't really seem to be a way of affecting the contents of the archives page.

_"But Corey! Why would you want to affect the contents of the archive page? It's just the archives!"_ I hear you not asking because who would actually be asking that question? Well I'll tell you anyways!

See, I've set my website up to have a [portfolio section]({filename}../../pages/portfolio.md). I originally had all of the portfolio items as articles, categorized as `portfolio`. So far so good. However I did not want the portfolio items showing up in the general archives. Turns out there's no easy way of doing that. After digging around someone came up with some sort of solution, but it seemed pretty hacky You can see it [here](https://github.com/getpelican/pelican/issues/1771#issuecomment-113950217). Instead I decided to do something else that was equally hacky, just in a different way.

Basically I made pages within a `portfolio` category ([example](https://github.com/cdutson/wallofscribbles/blob/master/content/pages/portfolio/my-wedding.md)), with a special [portfolio landing page](https://github.com/cdutson/wallofscribbles/blob/master/content/pages/portfolio.md), and then hacked up the [pages template](https://github.com/cdutson/wallofscribbles/blob/master/themes/white-n-green/templates/page.html#L5). It's gross, but seems like a better solution than rebuilding the archiving system from scratch.

One thing I have to bitch about is the ability to link to other files by using their article file, instead of the resulting output url. It's a great idea in _theory_, but in practice it's not very intuitive. The compiler will complain about files not being linked to sometimes, but they're actually working fine. Getting my head around the url system was irritating to say the least.

If you look at [their docs](http://docs.getpelican.com/en/3.6.0/content.html#linking-to-internal-content) for linking to internal content, it looks straight-forward. What I learned is to interpret the links as such:

```
{filename}category/article1.rst
 ^start^  ^relative from start^
```

So if you want to link to a file in a totally different area, there doesn't seem to be a way to link from root. If I can figure out how to build a plugin for that, I'm going to. Having to have multiple `../` trailing your links kind of sucks.

### So long, search

Yeah, the search is gone. One of the draw-backs to having a static website is that there's not really a way to have a dynamic search. I could of course add [google custom search](https://cse.google.com/cse/) to the website, or I could use a plugin called [Tipue Search](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search) with some jquery to create my own.

To be honest, I'm not sure anyone used the search in the first place, so until I see someone actually asking for it I'm not going to complicate my installation any more than needed.

### Updating the layout, gettin sassy

Switching to Pelican also allowed me (or somewhat forced my hand, depending on your view of things) to update my layout somewhat and gave me the opportunity to switch over to [SASS](http://sass-lang.com/).

The layout changes came because I had to rebuild the entire thing using pelican's theme system, and so I also took the opportunity to update the font selection (Valera Round and Crimson Text from [Google Fonts](https://www.google.com/fonts) and [Font Awesome](http://fortawesome.github.io/Font-Awesome/) for the icons), clean up some rough edges, and update my footer links some. I'm sure no one but me actually cares about these changes, but I'm happy I finally got around to doing it.

One of the things I _am_ excited about was the chance to start using SASS in my workflow. As much fun as hand-tooling all of my CSS was, SASS just makes updating this website's styles that much easier. It's cut down on the amount of junk in my stylesheets, and finally lets me use little things like variables to maintain consistency.

### Smaller footprint

It's not all bad news of course. Pelican is used by many people, and for a good reason: It's light-weight. The things I'm complaining about above are because in most cases, you don't need to worry about them. Pelican is wonderful if all you want to do is write articles and get them published without a lot of struggle.

There's something refreshing about having only static content to deploy. I got so used to having a million moving parts with Wordpress that when I swapped to Pelican, I kept on assuming there was more I had to do. There isn't! I run my deploy command, and it just moves the changed files onto the server. It's simple, and it works.

Now I'll admit my always-smarter friend [Bartek](http://justbartek.ca/) helped me with the deploy script, but I'm sure I could have figured it out with a little effort. That's more a limit to my knowledge in regards to web servers than it is difficulty in building your own pelican site.

### My host is happy

One of the things about PHP is it has a lot of junk that comes along with it. My host (the previously mentioned Bartek) was running a dedicated server pretty much for my website alone. This was costing him money (money he has never asked me for, which goes to show what a cool dude he is), and lets be real here: my website is not worth the $20 a month/year/whatever for a server.

So when I switched to Pelican - which as mentioned above generates a static output - Bartek was able to move me from the expensive server, to a cheap server he already had in commission. Everyone wins.

### Moving to Github

Another change to my workflow is the fact that my website is now hosted on Github. You can look at it [here](https://github.com/cdutson/wallofscribbles) if you want, though it's nothing special. I use an SSH key deployment, so you can't do too much damage with what's posted there. Hopefully someone can learn from what I'm doing, and that'd be swell.

What is special is that I can use this repo to give myself tasks in the form of issues, and I can create branches for my posts. That way I'm not cluttering my build up unnecessarily. It feels clean, and I like it.

And as a somewhat side bonus, if and when I post code examples, or someone finds a typo in an article, they can create pull-requests for corrections. I'm not sure how often that will happen, but the opportunity is there.

## So long, comments

One of the things with having a static site (and arguably the main reason I stuck with Wordpress for so long), is that you cannot really have a dynamic comment system. That used to be true, anyways. I've swapped the site over to use [Disqus](https://disqus.com), because it's quick, simple, and seems to be the de facto for website comments now. I've no idea what sort of info they may be collecting, but I'm okay with being the product in this instance.

I could have archived all the old comments and worked them in for historical purposes. I could have. I didn't bother. There wasn't really that much stimulating discourse, so I didn't see the need. As such they're _alllllll gone._

## So overall...

Overall I'm really happy with switching over to Pelican. It's been a great learning experience, and the ability to write in markdown really makes the act of writing articles that much easier. Hopefully It will allow me to get back into writing the insightful articles I was once known for.

If anyone wants to know the breakdown of what plugins I'm using and why, I'd be happy to write a follow-up post (or maybe just keep it in the comments section, depending on how much anyone wants to know).
