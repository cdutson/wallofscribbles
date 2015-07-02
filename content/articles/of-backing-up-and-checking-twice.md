Title: Of backing up and checking twice
Date: 2008-07-21 00:05
Author: Corey Dutson
Category: Bad bad bad, Personal, Technology, Wordpress
Tags: backup, Personal, stupid, theme, Wordpress
Slug: of-backing-up-and-checking-twice
Status: published

Being the smart man that I am, I thought "Hell, I'll just roll back a
version to when it worked! It's probably some little bug with Wordpress,
no big deal." I totally forgot my FTP information, so there was 40
minutes of my life I can't bet back.

In the end I rolled everything back and now the site worked again, but I
was still getting an error that I couldn't figure out. I tried
re-installing the latest version, and I was still getting an error which
totally confused me.

Now I'm getting angry. Something had changed between a couple days ago
and now. Could I remember? Of course not. If I could remember what I had
really done, I wouldn't of had a problem. As a result I ended up searing
a bunch and scrambling to get my site working as it should again. I
tried every combination I could think of that involved installing and
uninstalling everything. In this process I told myself, "make sure you
backup that theme you worked so hard on!"

I didn't of course, but we'll get to that.

Eventually I had the bright idea of "Why not just copy my development
version over to of the live version? I mean it works fine there!" I
forgot that when you're going to do a blind copy, it's generally good
practice to back up any and all files you may have changed from one
server to the other. This includes the files that make up my new theme.
The result? I rolled back 2 days worth of changes to the websites theme
and the problem was ***still there***.



Now I'm swearing up and down the walls. I'm saying things that I should
probably seek forgiveness for having said. I'm angry because now not
only have i rolled back my theme and lost so much work, but Isomehow
still have this messed up error!

Now it's time for me to bust out my debugging skills.

-   I removed the entire installation including all theme files,
    plugins, and extras.  
    **Result:** Site is dead. Good start.
-   I reinstall Wordpress and get it pointing to the old database (which
    was a fun time in and of itself, as i forgot my database server
    location)  
    **Result:** site is up, back to the old blue but up.
-   I re-install my theme and apply it  
    **Result:** Site is borked because I need certain things in my
    theme to work. Old error isn't appearing
-   Copy in my plugins  
    **Result:** no change
-   Activate "Hello Dolly" plugin (I like it, shut up)  
    **Result:** Crazy error shows up. I'm now confused.
-   Deactivate Hello Dolly, and activate Twitter.  
    **Result:** Everything's great. Still confused.
-   Activate Hello Dolly again.  
    **Result:** The shit's fucked up again.

Somehow throughout all of my backups and my restores, the Hello Dolly
plugin got rather messed up. I cannot and refuse to explain or
understand why. In the end I lost two days of work, and a day of
progress because of a useless plugin. What have I learned from this?

### Back your shit up before you start, and for the love of all that is sacred and pure, think about what you're doing before you do it.

I eventually got everything running again (as you can see) but believe
me when I say I could have done without the self-loathing, swearing, and
stress.
