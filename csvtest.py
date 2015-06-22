##import libraries
import csv
import re
from format import *
from elementout import *
from datetime import datetime


###############################################
###############################################

#Get System DateTime
now = datetime.now()
now_out = now.strftime('%Y-%m-%dT%H:%M:%S-05:00')
print now_out


fname = raw_input("Enter file name: ")	
if len(fname) < 1 : fname = "data_dump.csv"

try:
	reader = csv.reader(open(fname, 'r'), delimiter=',')
except:
	print ("File not found\n")
	exit()	
	
print 'begin writing XML'

#open xml file
try:
	f = open('data_dump.xml', 'w')
except:
	print ("File not found\n")
	exit()
	
#XML declaration
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
#XML root element
f.write('\t<records>\n')
f.write('\t\t<clientRecords>\n')

i = 0 
for row in reader:
	i = i+1   #get row number for log
	
	if (row[0] == "Name") : continue       #skip header

	########   Format Client Data   ########
	
	cId = "Client_" + str(reader.line_num-1)
	
	#SSN
	if ( (int(row[1]) > 0) or (len(row[1]) == 9) ):
		ssnDashed = dashssn(row[1])
		ssnDQ = "Full SSN Reported (HUD)"
	else:
		ssnDQ = "Don't Know or Don't Have SSN (HUD)"
		ssnDashed = "000-00-0000"	
		
	#DOB	
	hasDOB = 0
	dob = ""
	if ( len(row[2]) >= 8) :
		dobDateList = re.findall('([0-9].+?) ',row[2]) 
		if ( len(dobDateList) > 0) : 
			dob = formatdob(dobDateList[0])
			dobDQ = "full dob reported(hud)"
			hasDOB = 1
		else : 
			print "WARNING: Problem extracting DOB, Row: ", i
			print row
	else: 
		print "WARNING: Missing or Invalid DOB, Row: ", i
		print row
		
	#Gender
	hasGender = 0
	if (len(row[6]) > 0) :
		gender = formatgender(row[6])
		hasGender = 1
		
	
	#Race
	hasRace = 0
	if (len(row[7]) > 0) :
		race = formatrace(row[7])
		hasRace = 1
		
	#Veteran Status
	hasVetStatus = 0
	if (len(row[11]) > 0) :
		veteranStatus = formatveteran(row[11])
		hasVetStatus = 1

	########  Write the XML Child Elements   ########

	f.write("\t\t\t<Client system_id='" + cId + "' record_id='" + cId + "' date_added='2015-01-01T20:30:5600-05:00' date_updated='2015-01-01T20:30:5600-05:00'>\n")
	f.write("\t\t\t\t<firstName>" + row[3] + "</firstName>\n")
	if len(row[4]) > 0 :
		f.write("\t\t\t\t<middleName>" + row[4] + "</middleName>\n")
	f.write("\t\t\t\t<lastName>" + row[5] + "</lastName>\n")
	f.write("\t\t\t\t<alias>" + cId + "</alias>\n")
	f.write("\t\t\t\t<socSecNoDashed>" + ssnDashed + "</socSecNoDashed>\n")
	f.write("\t\t\t\t<ssnDataQualityValue>" + ssnDQ + "</ssnDataQualityValue>\n")
	
	#Assessment Data
	f.write("\t\t\t\t<assessmentData>\n")
	
	#DOB - omit if missing or invalid
	if ( hasDOB == 1):
		writeassessment(f, 5, "svpprofdob", dob, now_out, now_out)
		writeassessment(f, 5, "svpprofdobtype", dobDQ, now_out, now_out)
		
	### here here here add gender (6) , race (2), etc....	
	if ( hasGender == 1) :
		writeassessment(f, 5, "svpprofgender", gender, now_out, now_out)
	if (hasRace == 1) :
		writeassessment(f, 5, "svpprofrace", race, now_out, now_out)
	if (hasVetStatus == 1) :
		writeassessment(f, 5, "veteran", veteranStatus, now_out, now_out)
	

		
	f.write("\t\t\t\t</assessmentData>\n")
	#finished with assessment data
	f.write('\t\t\t</Client>\n')
	
	# print ("End of Row")
	
	
f.write('\t\t</clientRecords>\n')
f.write('\t</records>\n')
f.close()
print 'finished writing XML'
	
	