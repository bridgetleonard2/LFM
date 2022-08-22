
To run the ACT-R Standalone, extract the "ACT-R" folder from the zip archive and
place it anywhere on your machine.  

Then you just need to double click the "run-act-r.command" script to start 
ACT-R and the ACT-R environment.  That script must be located in the same 
directory as the rest of the ACT-R files, but you may create an alias to it and
put that elsewhere if that is more convenient.

If you get a warning that the file is damaged or cannot be opened then you will
need to Control-click the file and pick Open to run it.  If you are using MacOS
10.13 or newer then you will need an admin password to be able to run the 
software and with 10.14 or newer there are some additional steps necessary to 
allow all of the applications to run before it will work.  Detailed instructions
for that are found below. 

When you run that script, it will open a terminal window titled "ACT-R" and
start the ACT-R Environment "Control Panel".  If you get a dialog window 
which says "Error occurred trying to connect to ACT-R" at the top, press the
No button.  To prevent that from happening everytime you start ACT-R, you
will need to press the "Options" button at the bottom of the "Control Panel"
window, check the box next to "use localhost instead of 127.0.0.1", and 
press the save button.

To close the ACT-R Standalone you need to close the "ACT-R" window.  That will
quit the terminal and the Environment will ask to verify that it should quit.

By default the software will use the localhost address for the ACT-R interface,
but if you need to make external connections, delete the force-local.lisp file 
from the patches directory before starting the software.

The "run-extra-listener.command" script can be run to open another terminal 
running Lisp which connects to the running ACT-R.  That terminal provides 
functions/macros to call the ACT-R commands which are described in the tutorial
and may be useful for inspecting or debugging a model.  By default that terminal
will not display the ACT-R model trace but it does display the other traces.
If the model trace is desired in that terminal, the include-model-trace function
can be called to add it.  Any number of extra listeners may be run at the same
time.

The "run-html-environment.command" script can be run to start an application
which allows one to use an alternate version of the ACT-R Environment that
is implemented in javascript and works from a browser (it can be run instead
of or in addition to the default Tcl/Tk based Environment).  After you start
the application you should then open a browser and open the act-r.html file
which is found in the ACT-R directory.  It will show two links.  One goes
to the Environment tools and the other opens a viewer for the experiment
windows created by the ACT-R AGI tools.


See the tutorial, reference manual, and environment manual for more details.

This distribution is built using Clozure Common Lisp (CCL) which is available
at <http://clozure.com/>.  Clozure Common Lisp is distributed under the Apache
License, and the license is included in the ccl_license folder in the docs 
folder.


Detailed instructions for running with 10.14 or newer:

First, open System Preferences and then Security & Privacy and pick the
General section.  Leave that open.  Now Control-click the run-act-r.command
script and select Open. There will be a dialog which says the file is from
an unidentified developer.  Press the Open button.  That will open another
dialog requesting an admin login to allow the script to run.  After you
enter that information it will open another dialog indicating that the 
Start-environment-osx program is from an unidentified developer.  Press the
Cancel button and then go to the System Preferences window and press the 
"Allow Anyway" button which appears.  Then another dialog should appear 
which says that the act-r-64 application is from an unidentified developer.
Press the cancel button and in the System Preferences window press the "Allow
Anyway" button.  If you get another unidentified developer dialog press the
Open button.  After all that it probably did not start the software 
successfully so quit the application(s) which did run and then Control-click
the run-act-r.command script again.  

If it still does not run, go to the Privacy section and pick "Full Disk
Access" from the items on the left.  If the termial application is not
listed with a checkmark then you will have to add it.  It should be 
located in the Applications/utilities folder.


If you have any questions or problems with this please let me know.

Dan (db30@andrew.cmu.edu)
