cms
===============
I really love how quickly you can do things through the command line.  So, as a little silly project, I decided
to build this app to quickly create websites and perform content entry operations through the command line.  
My goal is to have a site up and running in a string of commands.  

Yes, you can drop in Drupal, Perch, or WordPress, or the one billion tools out there to generate sites, but
I really wanted something lightweight that I could run at the command line, super fast, without really thinking
about the details.  This is content entry focused and meant for someone like me who is comfortable running
commands in the terminal.

If you want to build something, then you should probably use Mixture, Yeoman or Brunch.

This is NOT, I repeat, this is NOT meant for production use or the typical user.  But, if you find it useful
then hurrah!


Phase 1
---------------------
- Config
- JSON support
- Page creation

Phase 2 
---------------------
- Jinja2 templating
- Markdown content entry
- SASS support
- Site generation

Phase 3 
---------------------
- FTP / FS / GIT support
- Minification
- Flask support
- Database support
- Content templates?


Quick Start
---------------------
For now create an alias like this:

alias cms="python /path/to/your/cms.py" or whatever and then you can run cms.py anywhere.  Eventually I'll make some sort of installer that will do all of this.


To create a new project:<br/>
cms --create foo

To create a new index page:<br/>
cd foo<br/>
cms --add-root index

To assign a Jinja2 template to index:<br/>
cms --page index --template layout.html
