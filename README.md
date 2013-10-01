cms
===============
I really love how quickly you can do things through the command line.  So, as a little silly project, I decided
to build this app to quickly create websites through the command line.  

Yes, you can drop in a Drupal CMS or WordPress blog, or the one billion tools out there to generate sites, but
I really wanted something lightweight that I could run at the command line, super fast.  Adding content would
be a command line away. 

This is NOT, I repeat, this is NOT meant for production use or the typical user.  But, if you find it useful
then hurrah!

What's in the box?
---------------------


Quick Start
---------------------
To create a new project:
cms --create foo

To create a new index page
cd foo
cms --add-root index

To assign a Jinja2 template to index
cms --page index --template layout.html
