Title: Do you suffer from Crummy User Experience?
Date: 2008-01-23 00:05
Author: Corey Dutson
Category: Design
Tags: Design, forms, good-practices, Internet
Slug: do-you-suffer-from-crummy-user-experience
Status: published

I consider myself fairly web-competent. I know how to fill out forms on
the Internet and it isn't all that hard in theory. The problem lays in
that if you could fill in forms with whatever you wanted, there'd be no
point to them because everyone's address would be something akin to
"aherhaerhaerumnjmaes"or " " or "buttslolz." Because of this some
enterprising people, institutions, and heartless corporations that want
your input force you to adhere to a set of rules in order to avoid these
scenarios.

Most people have no problem with following these rules, though I will
say that my address will forever be 123 Fake St. unless something is
getting shipped to me. The problem is not in the rules but in their
explanation to us.

Sometimes websites are **very clear about what they want** by specifying
it in clear, concise language: "*Username must be between 5 and 11
characters and contain at least 1 number*" or "*Postal Code example: A1B
2C3*". This is a good practice because assuming your users are idiots
will ironically result in a much lower screwup rate.

The point I'm getting to here is when you don't state you're rules, your
users will default to basic behavior. Most people don't know that
usernames tend to have numbers in them now, and I'm sure even less know
that because of your half-assed attempt at regex the postal code *needs*
to be in capitals.



What does this mean? Well depending on how you set up the form **users
may be forced to fill it all out again**. This is a pain in the ass to
start, and when you throw in the fact that many websites do not include
detailed error messages (error summaries people, error summaries) the
users may -and in my case will- be forced to fill out the same form
multiple times.

This is an example of *CUE*. Lazy programmers and lazy testing tend to
be the main cause of form-based issues. I know this because I was a lazy
programmer who submitted his stuff to a very thorough quality assurance
person. He turned around and ripped my form apart. I learned quickly
that by putting forth the additional effort into planning it all out and
doing the job right, that two things would happen: the first thing is
that I'd have less work coming back from the QA guys. The second was
that I realized I was creating the same thing that annoyed me so often
on the web. I'm a reformed man as a result.

What I'm trying to get at is that when you're building something, no
matter what it is, try and look at it from the end-users stand point.
This can be a difficult task at time and believe me when I say that it
takes some practice. You have to figure how users can screw things up
that you find straight-forward and fix said things.

Once you know how they can screw them up, save yourself some time and
tell them how ***not*** to screw them up. As long as you stop their
input from decimating your server (sanitize your inputs, people) you can
make your life easier by telling the user how to do things the right
way.

That's not *lazy*, that's *empowering*.

Another step is to make sure that when they do screw up (which they
will) make sure you **tell them what they actually did wrong**. DHTML
and AJAX controls depending on your validation requirements, can be
fantastic ways to validate on the fly... assuming you don't make your
error messages jarring (i.e. javascript popup messages are bad, don't do
them) or elusive (top of the page? I'm 15 inches down the form, I'm not
going to see that) or cryptic "An error occurred."

Once again, ask yourself **what you would expect the user to see** when
they go through it. Do you really think big JavaScript popups are the
best way to tell the user that their postal code can't have spaces?
Probably not, but I'm sure it made sense at the time.

I know I'm using submission forms heavily as my example here, but the
idea is still the same. Once you're done building your whateveritis, try
it out yourself. Try drawing up some use-cases get some friends or
colleagues to try it out. Pretend you're a blathering idiot, and see how
well you do then. Hell, find a blathering idiot and point him in your
whatchimacallits direction. Do whatever you have to to get the sense of
the users process. Find the problem areas with your thingimajigs before
they become the bane of every end-users (which in turn will become the
bane of your) life.

Don't be lazy, and do it right the first time people.
