# sublime-text-time-recorder
Sublime Text 3 time recorder plugin


##How to use:

Include this script as a plugin and assign a key to run it (I like to use F5).

###The 'timer'

To start the 'timer', open a blank text file (or any file really) and press F5.  You should see something similar to the following:
<pre>
10/05/2015 08:15PM *In progress* 
</pre>
To stop the 'timer', ensure the same line is selected, then press F5 again.  You should see something like this:
<pre>
10/05/2015 08:15PM - 08:35PM (0:20) 
</pre>

###Calculating total time spent

Highlight the lines created by the script and press F5 again.  The total should be printed at the cursor position.

####For example:

Highlight the following three lines:
<pre>
07/05/2015 08:15PM - 08:35PM (0:20)
09/05/2015 08:40PM - 08:45PM (0:05) 
10/05/2015 08:40AM - 08:45PM (12:05)
</pre>
And press F5:
<pre>
07/05/2015 08:15PM - 08:35PM (0:20)
09/05/2015 08:40PM - 08:45PM (0:05) 
10/05/2015 08:40AM - 08:45PM (12:05)
Total: (12:30)
</pre>

###Note:
You can record time periods longer than 23:59, resulting in something like the following:
<pre>
08/05/2015 08:45PM - 08:50PM (2 days, 0:05) 
</pre>

but the total calculator won't work.  If you want to calculate periods > 24 hours at a time, you'll need to add this functionality yourself.
