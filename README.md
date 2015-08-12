# SM-to-SP-Translation
Convert csv data exported from SM to SP XML for import

Project contains the following files:
Main:  smtest(n).py   Currently on version 5
Includes: fmapv2.py				#maps columns in the input file to constants, making it easier to update if the columns change
		  format.py				#contains formatting routines for different element, and translations to sp or HUD values, where needed
		  elementout.py	     	#contains formatting for specific element statements, to ensure the correct xml tab formatting
		  vfnmap.py      	    #maps virtual field names to variables to make porting to different systems using different question names easier
		  
		  
<<TO DO>>
Translate boolean fields and picklist values
Add the subassessment city and statements
Add logic to process the scores sheet		  
		  
