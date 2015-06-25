Title: My jQuery plugin template is open season!
Date: 2011-03-03 15:00
Author: Corey Dutson
Category: Code, Javascript, Miscellaneous, Technology
Tags: Code, JavaScript, JQuery, plugins, work
Slug: my-jquery-plugin-is-open-season
Status: published

So I've been doing a lot of javascript development at work recently.
I've basically created a lot of our reusable javascript 'plugins' to
cover the common requirements of the work that we do. In many cases,
this resides mostly (but not entirely) in online annual-report creation.

Anyone that's in the business will know that there are some common
functional elements that you end up having to build with javascript:
accordions, tabs, faders, sliders, lightboxes, filters, etc. Many of
these items can bleed over into non-report sites, such as intranets or
even public-facing sites.

<!--more-->

Now some of those are fairly straight forward: an accordion is just a
simple animate of a content section, repeat per title; tabs? Same deal.
So you might be pretty inclined to just write the script adhoc on a
project to project basis, copy and pasting it as you go. We were doing
that at my work when I started on, but I found that we kept on having to
add something, remove something, add hooks at certain points etc. In
some cases we used someone else's plugin to do these things, but we ran
into some issues when it came to having to tweak the plugin for our
needs.

As I was hired on as the senior front-ender, I was given the task of
trying to help simplify things in our working process. This required me
to dive right into plugin development, because one spot we were spending
a lot of time was reinventing the wheel project to project. Even more
time was spent debugging random plugins, or lashing them together.

As my place of employment works with jQuery, I wanted to develop
something that could be maintained in-house, and would be a good
starting point for repeating functionality. I ended up developing a
jQuery plugin template, which I am sharing today.

Now, while I can't feature the plugins I've made for my work here on my
site (I'm pretty sure my they'd be less than impressed with that), I
feel it's fairly safe to distribute this template (boiler plate?) to the
internets. It's a compilation of a couple tutorials, as well as my own
exploration into javascript. I'd be more than happy to give credit where
it's due, but I cannot remember where the heck I got some of the
snippets I integrated. If anyone reading this happens to know, leave a
comment and I'll be more than happy to give said credit.

Below you will find my jQuery plugin template code in it's entirety. I'm
open to suggestions on how to improve it, so feel free to comment.

\[javascript\]  
/\*  
\*  
Name: my.blank.plugin.js  
Purpose: Shell to use for jQuery plugins  
\*/  
(function (\$) {  
// DONT FORGET TO NAME YOUR PLUGIN  
jQuery.fn.myPlugin = function (options, i) {  
// This handles multiple elements (like a class selector)  
if (this.length &gt; 1) {  
var a = new Array();  
this.each(  
function (i) {  
a.push(\$(this).myPlugin(options, i));  
});  
return a;  
}  
var opts = \$.extend({}, \$().myPlugin.defaults, options);

/\* PUBLIC FUNCTIONS \*/

/\* reInit is a flag that you can pass in case you don't  
want to remove everything during the destroy phase. \*/  
this.Destroy = function (reInit) {  
var container = this;  
var reInit = (reInit != undefined) ? reInit : false;  
\$(container).removeData("myPlugin");  
// this removes the flag so we can re-initialize  
};

this.Update = function (options) {  
opts = null;  
opts = \$.extend({}, \$().myPlugin.defaults, options);  
this.Destroy(true);  
return this.Create();  
};

/\* iteration will give you the index of the item  
in the selection. If not part of a loop, I'm  
prett sure this will be null. You've been warned. \*/  
this.Create = function (iteration) {

// this stops double initialization  
if (\$(container).data("myPlugin") == true)  
return this;

// call a function before you do anything  
if (opts.beforeCreateFunction != null &&
\$.isFunction(opts.beforeCreateFunction))  
opts.beforeCreateFunction(targetSection, opts);

// reference to the object you're manipulating. To jQuery it, use
\$(container).  
var container = this;  
/\* Failing that, you could just use 'this' without the var
declaration,  
but if you are doing a lot of child looping, you'll be glad to have  
a reference to the target object. Also, performance improvements! \*/

////////////////////  
// DO STUFF HERE  
////////////////////

// Set a flag to show that this element has been plugin'd  
\$(container).data("myPlugin", true);

// call a function after you've initialized your plugin  
if (opts.afterCreateFunction != null &&
\$.isFunction(opts.afterCreateFunction))  
opts.afterCreateFunction(targetSection, opts);

/\* Make sure to return, otherwise you can't store the element in a
varaible,  
which means you can't use any of the plubic functions (you may not
need  
them, but it's still good practice.) \*/  
return this;  
};

/\* Example of a public function, this can be used if you store  
this object in a variable.

e.g. var foo = \$("\#target").myPlugin();  
foo.PublicFunction();  
\*/

this.PublicFunction = function () {  
// do something  
myPrivatefunction();  
};

/\* PRIVATE FUNCTIONS \*/

/\* These aren't accessibly externally, and so can only  
be called from within the enclosure code. \*/

function myPrivatefunction() { };

/\* arguably, you could wrap your private (or public)  
functions in an array such as the following: \*/

// Private helper functions  
helper = {  
firstHelper: function () { /\* do something \*/ },  
secondHelper: function (somevalue) { /\* do something with the variable
passed in \*/ }  
};

//Public helper functions  
this.Helper = {  
FirstHelper: function () { /\* do something \*/ },  
SecondHelper: function (somevalue) { /\* do something with the variable
passed in \*/ }  
};

/\* Personally, I don't see the point of doing this for  
anything OTHER than helper functions, I could, and  
probably am, wrong here... or at least ignorant. \*/

// Finally  
return this.Create(i);  
};

// DONT FORGET TO NAME YOUR DEFAULTS WITH THE SAME NAME  
jQuery.fn.myPlugin.defaults = {  
foo: "bar",  
something: "else",

// Remember: these are function \_references\_ not function calls  
beforeCreateFunction: null,  
afterCreateFunction: null  
};  
})(jQuery);  
\[/javascript\]

I've tried to comment the hell out of the code, so that it's as
straight-forward as possible. I assume that anyone that uses this will
strip out the comments, as well as any of the functionality that isn't
required.

Please feel free to use this, but If you'd be so kind as to give me
credit, that'd be swell. I can't force you, but we're all friends out
here, aren't we?
