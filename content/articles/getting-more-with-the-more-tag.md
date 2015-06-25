Title: Getting more with the MORE tag
Date: 2008-10-02 09:05
Author: Corey Dutson
Category: Code, Technology, Wordpress
Tags: Code, development, php, Wordpress
Slug: getting-more-with-the-more-tag
Status: published

So who out there uses Wordpress? I've been told it's [somewhat
popular](http://publisherblog.automattic.com/2008/01/23/wordpress-most-popular-cms-in-technoratis-top-100/ "Wordpress: Most popular CMS").

I myself am a fan despite it's [assault on the CPU and
database](http://www.codinghorror.com/blog/archives/001105.html "Coding Horror: Behold Wordpress, destroyer of CPUs").
It's fast, it's simple, and so long as your website isn't gaining huge
traffic (or you're paying peanuts for CPU usage and storage) than it's a
great selection. It's fairly customizable, [has a huge support and user
base](http://wordpress.org/extend/ "Wordress: Extend"), and it's just
damned easy to use. I've been slowly getting more and more into
customizing and extending what Wordpress can do out of the box.There's
more in the code than people think.

Recently I [a friend of mine](http://bart.whahay.net "Bartek Gniado")
ripped a strip off of me for only using summaries in my RSS feed. He
told me that he, along with other net-savvy users, didn't have time to
get teased by RSS summaries.

**UPDATE: As of December 3rd, 2008 I've turned this baby into a plugin!
~~Check it out.~~**

**UPDATE 2: Why my code was in a blockquote I will never, ever know.
I've updated the post to display as code. Thanks
[Pim](#div-comment-1654 "Pim in the comments").**

**UPDATE 3: This is [up on
github](https://github.com/Corey%20Dutson/wp-post-divider "Github - Corey Dutson - wp-post-divider")
now.**

<!--more-->

*For those wishing to skip the lengthy buildup, here is a little table
of contents:*

-   [The Back Story](#solution_history "The Back story")
-   [Solution](#solution "Solution")
-   [Explanation](#solution_explanation "Explanation")
-   [Installation and
    Usage](#solution_installation "Installation and Usage")
-   [Further Notes](#solution_notes "Further Notes")

### The Back Story - To Summarize or not to Summarize {#solution_history}

This is some what of a conundrum, as I want people to actually come to
my site. On the flip side, I want people to read what I write. So I can
force people to come to my site and gain page views, or I can increase
my RSS readership. After careful consideration, I've opted to fix my RSS
feed to display the entire content.

Here's the issue: Until now, I've used 'The Excerpt' field in Wordpress.
Basically this allows me to have a pretty excerpt instead of 55
characters truncated with a "READ MORE PLEAZE!" I use the custom excerpt
for the top part of the post; the preview if you will. The problem with
this is that I had to rip out the first couple paragraphs from the post
area, add some HTML to make sure it worked, and then post. The result
looked pretty, but had some unexpected side-effects on the RSS.

As it turns out, when you decide to use the EXCERPT field, that excerpt
will become the summary in the RSS. That's all well and good, but what
If you want to have the whole post? One would hope that it would stitch
the Excerpt and the Post together, but alas this was not the case.

I turned to the &lt;!--more--&gt; tag to assist me.

What they don't document about the more tag is pretty much all the
bitchy parts of it. When you use the &lt;!--more--&gt; tag, you split
the content, allowing for the excerpt to be defaulted to all the content
preceding the tag. This is great, except for how my layout works. You
see The top have is the Excerpt, and the bottom half is the rest of the
post. Just using the\_content wouldn't work, because I would be
repeating all the pre-more content.

get\_leader

I thought about maybe using an hr tag, or reworking my entire layout,
but I dismissed those due to the complexity of the markup. My only
option was to carve into Wordpress itself. I first checked Google to see
if anyone had come up against what I was facing. As it turns out [people
have asked the
question](http://wordpress.org/support/topic/184581 "Wordpress: Support"),
but no one has posted the answer.

I am fixing that right now.

### Getting the Pre and Post &lt;!--more--&gt; content separately {#solution}

Here is my solution, in full:

\[code language="php"\]  
function the\_formatted\_pre\_more\_from\_content (\$body)  
{  
\$returnVal = get\_the\_formatted\_pre\_more\_from\_content (\$body);  
if (\$returnVal !== FALSE)  
echo get\_the\_formatted\_pre\_more\_from\_content (\$body);  
else  
the\_excerpt();  
}

function get\_the\_formatted\_pre\_more\_from\_content (\$body)  
{  
\$moreTag = '&lt;!--more';  
\$content = FALSE;

\$morePos = stripos(\$body, \$moreTag);  
if (\$morePos !== FALSE || \$morePos &gt; -1)  
\$content = substr(\$body, 0, \$morePos);  
else  
return FALSE;

\$content = apply\_filters('the\_content', \$content);  
\$content = str\_replace('\]\]&gt;', '\]\]&gt;', \$content);

return \$content;  
}

function the\_formatted\_post\_more\_from\_content (\$body)  
{  
echo get\_the\_formatted\_post\_more\_from\_content (\$body);  
}

function get\_the\_formatted\_post\_more\_from\_content (\$body)  
{  
\$moreTag = '&lt;!--more';  
\$content = FALSE;

\$morePos = stripos(\$body, \$moreTag);

if (\$morePos !== FALSE || \$morePos &gt; -1)  
{  
\$content = substr(\$body, \$morePos + strlen(\$moreTag));  
\$morePos = stripos(\$content, '--&gt;'); // reuse variable  
if (\$morePos !== FALSE || \$morePos &gt; -1)  
\$content = substr(\$content, \$morePos + 3); // strip off rest of more
tag  
}  
else  
\$content = \$body;

\$content = apply\_filters('the\_content', \$content);  
\$content = str\_replace('\]\]&gt;', '\]\]&amp;gt;', \$content);

return \$content;  
}  
\[/code\]

### Explanation {#solution_explanation}

The two important functions here are
'get\_the\_formatted\_pre\_more\_from\_content' and
'get\_the\_formatted\_post\_more\_from\_content'. Long names, I know,
but at least their mission is clear.

get\_leader

The other two functions 'the\_formatted\_pre\_more\_from\_content' and
'the\_formatted\_post\_more\_from\_content' pretty much add a bit of
logic and echo the content automatically. I chose this naming structure
and function structure to emulate what is already in Wordpress (e.g.
'the\_content' versus 'get\_the\_content').

### Installation and Usage {#solution_installation}

To use this code, add it all to your functions.php file of your theme.
I'm sure I, or some other enterprising person, could turn this into a
plugin, but at the moment I don't feel it's warranted.

All of the functions take one parameter: **\$body**.

When you call these functions you must be in The Loop.

***example usage**: &lt;?php
the\_formatted\_pre\_more\_from\_content(\$post-&gt;post\_content);
?&gt;*

***explanation**: This call will display the content preceding the
&lt;!--more--&gt; tag.*

***example usage**: &lt;?php
the\_formatted\_post\_more\_from\_content(\$post-&gt;post\_content);
?&gt;*

***explanation**: This call will display the content proceeding the
&lt;!--more--&gt; tag.*

### Further Notes {#solution_notes}

**UPDATE: As of December 3rd, 2008 I've turned this baby into a plugin!
[Check it
out.](/wordpress-plugins/postdivider/ "Corey Dutson: PostDivider") I've
also fixed the post\_content bug!  
**

Note the **\$post-&gt;post\_content** that is passed into the function.
This exists automatically when you are in The Loop. This will pass all
of the posts content to the function without any formatting. The only
thing that isn't straight text - conveniently - is the &lt;!--more--&gt;
tag. As a result the content becomes fairly straight forward.

As of right now you must pass \$post-&gt;post\_content to the functions.
I tried to do it without passing the value, and they don't seem to pick
up the value.

I opted for using a substring functionality as opposed to an array split
function simply because it was 2 am when I finally got this going. I
don't know which is more efficient, so someone who is more knowledgeable
in PHP can comment on this and state which is better.

I only search for '&lt;!--more' because according to the tag
documentation, there is text that can follow the MORE that changes some
functionality. As a result, I have an additional if statement in the
get\_post function that will detect for the end of the tag and substring
the content again to trim that out.

I hope that this helps out some people who may be in a similar boat as I
was.
