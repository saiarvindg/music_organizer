# Music Organizer (Morganizer)
##Installation
####Step 1: Python
Download and install Python 3.5  
####Step 2: Python Packages
If you have any of the following packages already, one should still run the commands to update the packages.

1. Download and install the mtagen package:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install mutagen`  
2. Download and install pyacoustid:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install pyacoustid`  
3. Download and install requests package:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install requests`  

####Step 3: Applications
Install either the ChromaPrint Dynamic Library OR the command line tool fpcalc. If you choose to install the command line tool fpcalc, be sure to add the tool to your PATH. Instructions on installation can be found below.  
http://beets.readthedocs.org/en/latest/plugins/chroma.html

##Usage
1. Move all the music you would like to sort into one directory  
  * Skip this step if all the music you'd like to sort is already in one place  
2. Run the organize.py script
  * `python organize.py`
  * Either give the full path to the organize.py script, or run the above command from the directory that contains the organize.py script
3. Give the script the full path to the directory you'd like to organize when prompted
4. Wait while the music is sorted
  * If you chose to install the fpcalc command line tool, do not be suprised to see the terminal or command prompt opening and closing repeatedly at this point


##Acknowledgments
####Authors
Sai Arvind Ganganapelle  
Solomon Kritz  
Aleksey Bychkov  
####Mentors
Ramsey Khadder
