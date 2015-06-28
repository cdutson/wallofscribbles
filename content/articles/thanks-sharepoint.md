Title: Cannot insert the value NULL into column Name, Thanks SharePoint
Date: 2008-03-07 00:05
Author: Corey Dutson
Category: Bad bad bad, Code, Microsoft, Technology
Tags: Design, good-practices, Internet, Microsoft, MOSS, SharePoint, xml
Slug: thanks-sharepoint
Status: published

My feature code was throwing an error today. For those who don't know
what I'm talking about here is a crash course: A feature basically
allows you to attach functionality to something in SharePoint. Maybe you
want to add a menu option to the 'Site Actions' menu, or import some
files into libraries. In my case I wanted to attach functionality to a
specific list. I wrote my feature code, and it seemed fine. Deployed and
activated just great.

Then I tried to create a Custom List. I had event receivers attached to
custom lists (ListTemplateID=100 for those who care) and i got this:

*Cannot insert the value NULL into column 'Name', table
'.dbo.EventReceivers';  
column does not allow nulls. INSERT fails.  
The statement has been terminated.*

Took me a good two hours of trying everything I could think of with my
XML and code, only to be repeatedly thwarted by this database-level
error! I tried commenting out different sections of my receivers and
still got the error. When I commented the entire <span
style="color: blue">&lt;</span><span
style="color: red">Receivers</span><span style="color: blue">&gt;</span>
section, things ran fine, but not the <span
style="color: blue">&lt;</span><span
style="color: red">Receiver</span><span
style="color: blue">&gt;</span>items inside. What the hell is going on?
Read on!

.postList

I'll give an example of what I'm talking about here - the following
comes from
[MSDN](http://msdn2.microsoft.com/en-us/library/ms460929.aspx "MSDN: Event Registrations"):

**feature.xml**:  
<span style="color: blue">&lt;</span><span
style="color: red">Feature</span>  
Scope="Web"  
Title="Simple Updating Item Event Handler Registration"  
Id="A6B8687A-3200-4b01-AD76-09E8D163FB9A"  
xmlns="http://schemas.microsoft.com/sharepoint/"<span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">ElementManifests</span><span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">ElementManifest</span> Location="elements.xml"<span
style="color: blue">/&gt;</span>  
<span style="color: blue">&lt;/</span><span
style="color: red">ElementManifests</span><span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;/</span><span
style="color: red">Feature</span><span style="color: blue">&gt;</span>

*inside the feature.xml file (above) it references the following file:*

**elements.xml**:

<span style="color: blue">&lt;</span><span
style="color: red">Elements</span>
xmlns="http://schemas.microsoft.com/sharepoint/"<span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Receivers</span>  
ListTemplateOwner="ADDABAAA-1111-2222-3333-111111111111"  
ListTemplateId="104"<span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Receiver</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Name</span><span
style="color: blue">&gt;</span>SimpleUpdateEvent<span
style="color: blue">&lt;/</span><span
style="color: red">Name</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Type</span><span
style="color: blue">&gt;</span>ItemUpdating<span
style="color: blue">&lt;/</span><span
style="color: red">Type</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">SequenceNumber</span><span
style="color: blue">&gt;</span>10000<span
style="color: blue">&lt;/</span><span
style="color: red">SequenceNumber</span><span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Assembly</span><span
style="color: blue">&gt;</span>SimpleUpdateEventHandler,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=10b23036c9b36d6d<span
style="color: blue">&lt;/</span><span
style="color: red">Assembly</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Class</span><span
style="color: blue">&gt;</span>MS.Samples.SimpleItemUpdateHandler<span
style="color: blue">&lt;/</span><span
style="color: red">Class</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Data</span><span
style="color: blue">&gt;&lt;/</span><span
style="color: red">Data</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;</span><span
style="color: red">Filter</span><span
style="color: blue">&gt;&lt;/</span><span
style="color: red">Filter</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;/</span><span
style="color: red">Receiver</span><span style="color: blue">&gt;</span>  
<span style="color: blue">&lt;/</span><span
style="color: red">Receivers</span><span
style="color: blue">&gt;</span>  
<span style="color: blue">&lt;/</span><span
style="color: red">Elements</span><span style="color: blue">&gt;</span>

This works fine. Here's something interesting though: any comments -
<font color="#0000ff">&lt;</font>!-- <font color="#008000">Like
this</font> --<font color="#0000ff">&gt; </font>- you have in the <span
style="color: blue">&lt;</span><span
style="color: red">Receivers</span><span style="color: blue">&gt;</span>
node will be literally interpreted as <span
style="color: blue">&lt;</span><span
style="color: red">Receiver</span><span style="color: blue">&gt;</span>
nodes! That means whenever it tries to attach event receivers to any
list, it treats the comments as actual receivers! That's right, for
whatever reason, the code that ties event receivers to lists literally
loops through every node (comments are still considered nodes!) and
tries to use them instead of using any sort of
[XPath](http://en.wikipedia.org/wiki/XPath "Wikipedia: XPath"). How hard
is it to use "//Elements/Receivers/Receiver" as your node collection
XPath? I really hope whoever wrote that code got the ruler or something.

### The solution: Remove comments from your Feature xml file(s).

I say this because God only knows where else this is happening, and the
odds of you realizing that it is something that should just work, like
comments, are probably not that high. Remember folks, sometimes the most
obtuse problems have the most simple answers. Try not to over-think
things.

A huge thank you must go out to [Janne
Mattila](http://blogs.msdn.com/jannemattila/ "Janne Mattila") for being
the first (and apparently only according to Google) [documenting
this](http://blogs.msdn.com/jannemattila/archive/2007/02/08/moss-and-eventhandler-deployment-with-features-cannot-insert-the-value-null-into-column.aspx "Janne Mattila: MOSS and EventHandler deployment with features + Cannot insert the value NULL into column...").
I wish I had looked sooner.
