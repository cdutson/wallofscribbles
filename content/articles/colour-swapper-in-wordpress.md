Title: Colour Swapper in Wordpress
Date: 2008-10-09 09:05
Author: Corey Dutson
Category: Code, Design, Technology, Wordpress
Tags: Code, colour swapper, JavaScript, JQuery, php, Wordpress
Slug: colour-swapper-in-wordpress
Status: published

Who likes website colour swappers? Anyone?

When I developed the theme I am currently using, I searched high and low
for something I could <span
style="text-decoration: line-through;">steal</span> take inspiration
from. The funny thing is that most people don't even know where the
colour swapper is on my site. So few in fact that I had to add a caption
to it to help make it a little more obvious.

In any case I felt that I would share the method I used to create the
swapping functionality on my website. I'm aware that most of it can be
figured out with a little imagination and some source viewing, but I
think that going through it step by step is more helpful.

**UPDATE - 10/09/2008 -** In record time, a second pair of eyes looking
at this has managed to refine the process. Thank you
[Bart](http://bart.whahay.net "Bartek Gniado") for pointing out that if
the CSS files are named the same as the Title attribute of the Anchor,
then you can drop the whole If statement. I've updated the tutorial
accordingly

<!-- PELICAN_END_SUMMARY -->

Table of contents
-----------------

-   [The idea](#article_idea)
-   [Before we begin](#article_before)
-   [Setting up our files](#article_setup)
-   [Setting up the CSS files](#article_css)
-   [A dash of PHP](#article_php)
-   [The basic markup](#article_markup)
-   [The JavaScript](#article_java)
    -   [Importing the required files](#article_java_import)
    -   [Adding functionality](#article_java_func)
-   [Pulling it all together](#article_together)
    -   [Flow](#article_together_flow)
-   [Conclusion](#article_conclusion)

The idea {#article_idea}
--------

So you want to build a colour swapper? Easy as pie. You want to do it
without causing a postback and sustains itself throughout the
navigation? That's a little more tricky, and what I wanted to do myself.

What, you're too lazy to figure this out for yourself? No problem. Read
on and be merry.

Before we begin {#article_before}
---------------

A few words before we begin:

-   I am not a master of JavaScript, let alone
    [JQuery](http://jquery.com/ "JQuery"). I'm not a novice, but I am in
    no way a master of the language. There are probably many ways in
    which to improve my methods here. I'm going to take another crack at
    them and see what I can come up with. I'll update the code to this
    post If I come up with anything.
-   In addition to the last note, I'm not going to explain how
    JQuery works. they do a [fine job on their
    own](http://docs.jquery.com/How_jQuery_Works "JQuery: How it works").
    If you don't understand it, I suggest you take some time and become
    familiar with it.
-   This whole solution rides on the idea that your users allow
    JavaScript and Cookies. If the Cookies are disabled, the styles will
    still change, but will not persist between
    page refreshes/navigation. If JavaScript is disabled, nothing will
    work because I have not yet implemented a
    postback-friendly alternate. If I find myself with time I'll do this
    as well and update this post.
-   This whole tutorial is based on the idea that you are applying this
    to a Wordpress theme. If you're using something else, you'll need to
    alter this as you need.
-   I have noticed that in some browsers, the swapping is not instant,
    and you may notice somewhat of a flicker. In my case the colours go
    away, and then the new ones are applied. Some browsers do not
    do this. I have no idea why this happens.

Setting up our files {#article_setup}
--------------------

For this solution we're going to need to [get some
files](http://code.google.com/p/jqueryjs/downloads/list?q=label:Featured "JQuery: Featured Downloads")
from the JQuery website (the latest JQuery build), and create some files
in our Theme folder.

You are going to need to make a JavaScript folder - I called mine "js" -
and multiple CSS files. One will be a core style sheet that contains all
of the universal CSS styles, and then alternate sheets that contain the
CSS that is swapped around.

### Example setup: {#article_setup_example}

-   THEME FOLDER
    -   style.css
    -   Yellow Version.css
    -   Red Version.css
    -   Blue Version.css
    -   Green Version.css
    -   JS FOLDER
        -   jquery.js
        -   functions.js

The rest of this example will assume that you have that setup.

.postList

Setting up the CSS files {#article_css}
------------------------

First off, you're going to need some CSS files to play around with.
Generally you would have a core css file that would contain all the
styles that wouldn't be affected by your swapper. Depending on how you
use your swapper, this may or may not be the case. Some people want to
totally alter the website with their swapper; I just wanted a colour
change.

***Note:** I'm not going to paste all the CSS I used to format the
actual tiles, because my layout requirements will be different than
yours. Set the CSS code up however you need to make your selector HTML -
we'll see that in a bit - look right.*

So you have your core css file (style.css for Wordpress users). Do what
you need to in that file and then put it away. We won't be touching it
very much. The only addition I put in my CSS files are the following:

    .red {background-color:#FF3333;}
    .yellow {background-color:#FBDC00;}
    .green {background-color:#1FF900;}
    .blue {background-color:#00CCFF;}

These four styles are in my core CSS file so that my swappers always
have access to correct classes for them. What this means is that
regardless of what CSS file is imported, the swapper tiles will always
look the same.

Next up we have our swapping CSS files: Blue Version, Green Version, Red
Version and Yellow Version.

***Note:** I use Yellow Version as my default, but that doesn't come in
for a little bit yet.*

So in each one of these CSS files, I have the same selectors:

    .specialBGColor {background-color:#FBDC00;}
    a, .specialColourText, #left_bar .widget table th {color:#FBDC00;}
    .specialTopBorder{border-top:20px solid #FBDC00;}

All of your swappable CSS files will have the same selectors with
whatever colour differences you need. In my case The hex colours are
going to change to whatever is appropriate for the file (yellow is
\#FBDC00, red is \#FF3333, etc.) "specialBGColor" is basically a class I
apply to anything that is going to have a swappable background. I also
have a "speciallTopBorder" that does something similar, and some
selectors for links and table headers to change their colours.

All of these swappable CSS files should be in the same directory. Since
I am using Wordpress my CSS files are all kept together in the same
directory: the theme directory. I dislike the lack of separation but
I'll manage.

Once you've got all those set up we can move on to setting up the PHP
functions

A dash of PHP {#article_php}
-------------

We need to add a little function to our functions.php file. The function
will attempt to grab a value from the users cookie cache and return it.
Pretty simple overall. In my case, if the cookie is not found, it
returns a default string that is the URL to my yellow style sheet. As
previously stated, the Yellow CSS file is the same.

Add the following to your functions.php file:

    function getStyleCookie()
    {
       if($_COOKIE["styleHref"] != null && $_COOKIE["styleHref"] != "")
       {
          echo $_COOKIE["styleHref"];
       }
       else
       {
          $url = bloginfo('template_url') + "/Yellow Version.css";
          echo $url;
       }
    }

What this does is if it can get the cookies value - in this case
"styleHref" cookie - this is explained in the JS - it will echo the
value of the cookie. if it can't it returns the default value of the
Yellow Version.css location.

***Note:** I could have made the function a bit more universal by
passing in the cookie name, but as I'm only using it for this one
instance, I didn't bother.*

The basic markup {#article_markup}
----------------

Alright lets set up the markup. Lets start with the header.

Locate the &lt;head&gt;&lt;/head&gt; section of your website (for
Wordpress users, this is usually the header.php file).

You'll need to find where you have any current CSS files linked and
paste the following over or after the CSS tags. I say over or after
because depending how much of this you're following, you may already
have a core CSS file that you don't want to remove.

    <!-- THIS IS YOUR CORE CSS FILE. IGNORE THIS LINE IF YOU ALREADY HAVE THIS IN YOUR HEADER -->
    <link rel="stylesheet" href="<?php bloginfo('stylesheet_url'); ?>" type="text/css"/>

    <!-- some dynamic stuff that won't make any sense yet, but it will later -->
    <?php if($_COOKIE["styleHref"] != null && $_COOKIE["styleHref"] != "") : ?>
       <link id="altsheet" rel="stylesheet" href="<?php echo $_COOKIE["styleHref"]; ?>" type="text/css"/>
    <?php else : ?>
       <link id="altsheet" rel="stylesheet" href="<?php bloginfo('template_url'); ?>/Yellow Version.css" type="text/css"/>
    <?php endif; ?>

**What this does:** try and get the URL to the currently used CSS file
and render that CSS file. If nothing can be found, default to the Yellow
Version style sheet. This may seem repetitive given that the
functions.php code we put in also compensates for a lack of cookie. I'm
one for having backup plans, and this was mine. If you don't like it,
you can simply remove the entire else section.

.postList

Next up is the actual swapper markup. I'm going to paste a simplified
version of mine, because as I stated before, your swapper will look
different than mine. As long as the base HMTL is the same, this solution
works. how you style things up is totally up to you.

    <div id="colour_swapper">
       <ul>
          <li>
             <a href="javascript:;" class="green" title="Green Version">Swap to green</a>
          </li>
          <li>
             <a href="javascript:;" class="yellow" title="Yellow Version">Swap to yellow</a>
          </li>
          <li>
             <a href="javascript:;" class="blue" title="Blue Version">Swap to blue</a>
          </li>
          <li>
             <a href="javascript:;" class="red" title="Red Version">Swap to red</a>
          </li>
       </ul>
    </div>

The important parts to this are two-fold.

First, the **ID of the DIV** element is going to be used in the
JavaScript. I'm aware that the DIV isn't really needed, but as I said,
this is a simplified version of what I'm using, and as such I've
actually stripped out additional elements contained in the DIV.

The second thing is the **title of the ANCHOR items**. The title will be
used in the JavaScript to determine what CSS file to get.

***Note:** I'm aware that having a href of 'javascript:;' is a bad
practice. In reality the href should offer a link that would manually
post back the page, and have PHP  code that would look for that action
and set the cookie that way. Doing so would allow for the swapper to
work when JavaScript is disabled.*

The JavaScript {#article_java}
--------------

### Importing the required files {#article_java_import}

This is where everything is tied together and starts working.

First off we need to import some JS files. This solution imports JQuery,
as well as a functions.js file that I created in a sub directory of my
Theme folder called "js". This was explained in the
[Setup](#article_setup "Setting up your files") section, but I'm still
reiterating.

First we need to add a bit more markup within our
&lt;head&gt;&lt;/head&gt; sections:

    <script type="text/JavaScript" src="<?php bloginfo('template_url'); ?>/js/jquery.js"></script>
    <script type="text/javascript">
       var templateUrl = "<?php bloginfo('template_url'); ?>";
    </script>
    <script type="text/JavaScript" src="<?php bloginfo('template_url'); ?>/js/functions.js"></script>

What we're doing here:

1.  Importing the JQuery framework.
2.  Setting a JavaScript variable that contains the template\_url value
    from Wordpress. This makes life easier when we get to the actual
    cookie setting.
3.  Importing our functions.js file that will contain all of
    our functionality.

***Note:** I'm not a JavaScript expert, and part of me thinks that there
should be a way to pass in the template URL to the functions.js import
call. I don't know and if someone can comment on this and explain, I'd
be more than happy to refine my work.*

Next up we need to add some functionality to the functions.js file!

### Adding functionality {#article_java_func}

I'll pase the code first and then explain it:

    var $j = jQuery.noConflict();

    $j(document).ready(function(){
       $j("#colour_swapper a").click( function(){
        var style_title = $j(this).attr("title");
        var style_href= "";
        var altSheet = $j("#altsheet");

        altSheet.attr({"href":templateUrl +"/" + style_title+".css"});

        style_href = altSheet.attr("href");

        var date = new Date();
        date.setTime(date.getTime()+(1*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
        document.cookie = "styleHref="+style_href+"; expires="+date.toGMTString()+"; path=/";
       });
     });

**What the hell is going on:**

1.  Set JQuery to no conflict mode by assigning it to a
    different variable. I had to do this because of other plugins I use
    on my site. I maintain that this is a good idea when you are working
    in a plugin-heavy framework like Wordpress.
2.  For every link found within the element with the id of
    colour\_swapper attach a new click function
3.  Set a variable to the value of the links title (Yellow Version,
    Green Version, etc)
4.  Grab the element with the id of "altsheet" (in our case this is a
    link element in our header) and change it's href value to the url of
    the new style sheet. This url is made up of the template URL and the
    name of the style sheet (title of the anchor)
5.  Set a variable with the URL the new CSS file to be used.
6.  Create a date variable, and set it to the future (exact day eludes
    me at the moment. Part of me thinks that it's either 24 hours into
    the future, or 1000 days. I can't honestly remember at this point).
7.  Convert the date to a GMTString which is used in the creation
    of cookies.
8.  Create a cookie, "styleHref", that stores the URL of the style
    sheet used. This cookie is set to expire in the future, and will
    apply to all pages within the website (that's what the "/" is for)

Whew! That took longer to explain than I thought.

Pulling it all together {#article_together}
-----------------------

So now that we've gone through all that, everything should work. To give
you an idea on how it all comes together I'll explain the general flow.

### Flow {#article_together_flow}

-   While the page is loading, try and grab the cookie and set the
    secondary style sheet. If none is found, apply a default
    (Yellow Version)
-   Import all of the JavaScript needed.
-   User clicks on a style swapping link
-   JavaScript figures out what style sheet to use
-   Changes the secondary sheets href to the new CSS file
-   Sets a cookie to store the URL of the new CSS file

Now if a user navigates to another page in your website, the first step
will apply the change right off the bat.

Conclusion {#article_conclusion}
----------

I hope that this helps someone out there, and comments are more than
appreciated to help improve the solution. I'll try and refine the
solution a little more when I have time.

Good luck and happy coding!
