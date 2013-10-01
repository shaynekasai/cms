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


Phase 1 Roadmap
---------------------
- Config
- JSON support
- Page creation

Phase 2 Roadmap
---------------------
- Jinja2 templating
- Markdown content entry
- SASS support
- Site generation

Phase 3 Roadmap
---------------------
- FTP / FS / GIT support
- Minification
- Flask support
- Database support
- Content templates?


Quick Start
---------------------
To create a new project:
cms --create foo

To create a new index page
cd foo
cms --add-root index

To assign a Jinja2 template to index
cms --page index --template layout.html
