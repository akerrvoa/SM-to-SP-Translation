##import libraries
import csv
import re
from fmapv2 import *
from format import *
from elementout import *
from vfnmap import *
from datetime import datetime

###############################################
###############################################

#Get System DateTime
now = datetime.now()
now_out = now.strftime('%Y-%m-%dT%H:%M:%S-05:00')
print now_out


fname = raw_input("Enter file name: ")	
if len(fname) < 1 : fname = "tx5.csv"

try:
	infile = open(fname, 'r')
	reader = csv.reader(infile, delimiter=',')
except:
	print ("File not found\n")
	exit()	
	
print 'begin writing XML'

#open xml file
try:
	f = open('smtest5.xml', 'w')
except:
	print ("File not found\n")
	exit()
	
#XML declaration
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
#XML root element
f.write('\t<records>\n')

###############################
## Provider Records
###############################
#write pre-defined provider section
#write_providers(fh, si, ri, nm, da, du)
si = "600"
ri = "600"
## here here here we are testing adding clients and EEs to an existing provider
## write_providers(f,si,ri,"VOATX Community Re-entry Services", now_out, now_out)



###############################
## Client Records
###############################
f.write('\t\t<clientRecords>\n')

i = 0 
for row in reader:
	i = i+1   #get row number for log
	
	if (row[COL_RID] == "rid") : continue       #skip header

	########   Format Client Data   ########
	
	#cId = "Client_" + str(reader.line_num-1)
	cId = "Client_" + str(row[COL_RID])

	#Get Entry Date
	if ( len(row[COL_ENTRYDT]) >= 8) :
		dynDateList = re.findall('([0-9].+?) ',row[COL_ENTRYDT]) 
		if ( len(dynDateList) > 0) : 
			dynDate = formatdt(dynDateList[0])	

	
	#SSN
	if ( (int(row[COL_SSN]) > 0) or (len(row[COL_SSN]) == 9) ):
		ssnDashed = dashssn(row[COL_SSN])
		ssnDQ = "Full SSN Reported (HUD)"
	else:
		ssnDQ = "Don't Know or Don't Have SSN (HUD)"
		ssnDashed = "000-00-0000"	
		
	#DOB	
	hasDOB = 0
	dob = ""
	if ( len(row[COL_DOB]) >= 8) :
		dobDateList = re.findall('([0-9].+?) ',row[COL_DOB]) 
		if ( len(dobDateList) > 0) : 
			dob = formatdt(dobDateList[0])
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
	if (len(row[COL_GENDER]) > 0) :
		gender = formatgender(row[COL_GENDER])
		hasGender = 1
		
	
	#Race
	hasRace = 0
	if (len(row[COL_RACE]) > 0) :
		race = formatrace(row[COL_RACE])
		hasRace = 1
	
	#Ethnicity
	hasEthnicity = 0
	if hasRace :
		if row[COL_RACE] == "Hispanic" :
			ethnicity = "Hispanic/Latino (HUD)"
			hasEthnicity = 1
		
	#Veteran Status
	hasVetStatus = 0
	if (len(row[COL_VETSTAT]) > 0) :
		veteranStatus = formatveteran(row[COL_VETSTAT])
		hasVetStatus = 1
		
	#Primary Language
	hasPrimLang = 0
	if (len(row[COL_LANG1]) > 0) :
		lang1 = formatlang(row[COL_LANG1])
		hasPrimLang = 1
		
	#Secondary Language
	hasSecLang = 0
	if (len(row[COL_LANG2]) > 0) :
		lang2 = formatlang(row[COL_LANG2])
		hasSecLang = 1

	#Zip
	hasZip = 0
	if (len(row[COL_ZIP]) > 0) :
		zip = formatzip(row[COL_ZIP])
		hasZip = 1
		
	#Employed
	hasEmplStat = 0
	if (len(row[COL_EMPLSTAT]) > 0) :
		emplstat = formatemplstat(row[COL_EMPLSTAT])
		hasEmplStat = 1
	
	#Homeless
	hasHomeStat = 0
	if (len(row[COL_HOMESTAT]) > 0) :
		homestat = formathomestat(row[COL_HOMESTAT])
		hasHomeStat = 1
	
	#Status
	hasStat = 0
	if (len(row[COL_STAT]) > 0) :
		stat = formatstat(row[COL_STAT])
		hasStat = 1
	
	#PrimaryDrug
	hasPrimDrug = 0
	if (len(row[COL_DRUG1]) > 0) :
		drug1 = formatdrug(row[COL_DRUG1])
		hasPrimDrug = 1
	
	#SecondaryDrug
	hasSecDrug = 0
	if (len(row[COL_DRUG2]) > 0) :
		drug2 = formatdrug(row[COL_DRUG2])
		hasSecDrug = 1

	#DisabilityType
	hasDisType = 0
	if (len(row[COL_DISTYPE]) > 0) :
		distype = formatdistype(row[COL_DISTYPE])
		hasDisType = 1

	#unemployable
	hasUnemp = 0
	if (len(row[COL_UNEMP]) > 0) :
		unemp = formatunemp(row[COL_UNEMP])
		hasUnemp = 1

		
	########  Write the XML Child Elements   ########
	f.write("\t\t\t<Client system_id='" + cId + "' record_id='" + cId + "' date_added='" + dynDate + "' date_updated='" + dynDate + "'>\n")
	f.write("\t\t\t\t<firstName>" + row[COL_FNAME] + "</firstName>\n")
	if len(row[COL_MI]) > 0 :
		f.write("\t\t\t\t<middleName>" + row[COL_MI] + "</middleName>\n")
	f.write("\t\t\t\t<lastName>" + row[COL_LNAME] + "</lastName>\n")
	f.write("\t\t\t\t<alias>" + cId + "</alias>\n")
	f.write("\t\t\t\t<socSecNoDashed>" + ssnDashed + "</socSecNoDashed>\n")
	f.write("\t\t\t\t<ssnDataQualityValue>" + ssnDQ + "</ssnDataQualityValue>\n")
	if hasVetStatus == 1 :
		f.write("\t\t\t\t<veteranStatus>" + veteranStatus + "</veteranStatus>\n")

	
	#Assessment Data
	f.write("\t\t\t\t<assessmentData>\n")
	
	#DOB - omit if missing or invalid
	if ( hasDOB == 1):
		writeassessment(f, 5, dobVFN, dob, dynDate, dynDate)
		writeassessment(f, 5, dobTypeVFN, dobDQ, dynDate, dynDate)
		
	### here here here Do we want to set assessment data to time of entry?  For now use import time	
	if ( hasGender == 1) :
		writeassessment(f, 5, genderVFN, gender, dynDate, dynDate)
	if (hasRace == 1) :
		writeassessment(f, 5, raceVFN, race, dynDate, dynDate)
	if (hasEthnicity == 1) :
		writeassessment(f, 5, ethnicityVFN, ethnicity, dynDate, dynDate)
	if (hasPrimLang == 1) :
		writeassessment(f, 5, primaryLanguageVFN, lang1, dynDate, dynDate)
	if (hasSecLang == 1) :
		writeassessment(f, 5, secondaryLanguageVFN, lang2, dynDate, dynDate)
	if (hasZip == 1) :
		writeassessment(f, 5, zipLastPermVFN, zip, dynDate, dynDate)
	if (hasEmplStat == 1) :
		writeassessment(f, 5, employmentStatusVFN, emplstat, dynDate, dynDate)
	if (hasHomeStat == 1) :
		writeassessment(f, 5, homelessVFN, homestat, dynDate, dynDate)
	if (hasStat == 1) :
		writeassessment(f, 5, reentrystatusVFN, stat, dynDate, dynDate)


		
	f.write("\t\t\t\t</assessmentData>\n")
	#finished with assessment data
	f.write('\t\t\t</Client>\n')
	
	# print ("End of Row")
		
f.write('\t\t</clientRecords>\n')

###############################
## Entry/Exit Records
###############################
f.write('\t\t<entryExitRecords>\n')
i = 0 

infile.seek(0)
for row in reader:
	i = i+1   #get row number for log
	
	if (row[COL_RID] == "rid") : continue       #skip header
	
	#get entry date
	if ( len(row[COL_ENTRYDT]) >= 8) :
		eeDateList = re.findall('([0-9].+?) ',row[COL_ENTRYDT]) 
		if ( len(eeDateList) > 0) : 
			entrydate = formatdt(eeDateList[0])
		else : 
			print "WARNING: Problem extracting EE Date, Row: ", i
			print "Using system date for EE Entry Date"
			entrydate = now_out
	else :   #here here here do this better
		print "WARNING: Problem extracting EE Date, Row: ", i
		print "Using system date for EE Entry Date"	
		entrydate = now_out

	cId = "Client_" + str(row[COL_RID])
	eeId = "EE_" + str(row[COL_RID])
	f.write("\t\t\t<EntryExit system_id='" + eeId + "' record_id='" + eeId + "' date_added = '" + entrydate + "' date_updated = '" + entrydate + "'>\n")
	f.write("\t\t\t\t<active>true</active>\n") 
		#here here here  What EE type will we use?  Change to Basic
	f.write("\t\t\t\t<typeEntryExit>Basic</typeEntryExit>\n")
	f.write("\t\t\t\t<client>" + cId + "</client>\n")
		#here here here   Don't hard code the provider
	f.write("\t\t\t\t<provider>" + si + "</provider>\n") 
	

	f.write("\t\t\t\t<entryDate>" + entrydate + "</entryDate>\n")

	if ( len(row[COL_EXITDT]) >= 8) :
		eeDateList = re.findall('([0-9].+?) ',row[COL_EXITDT]) 
		if ( len(eeDateList) > 0) : 
			exitdate = formatdt(eeDateList[0])
			f.write("\t\t\t\t<exitDate>" + exitdate + "</exitDate>\n")
		else : 
			if ( len(row[COL_EXITDT]) > 0) :
				print "WARNING: Problem extracting EE Exit Date, Row: ", i
				print "WARNING: Omitting EE Exit Date for person exited"

	#f.write("\t\t\t\t<reasonLeavingValue>Death</reasonLeavingValue>\n") 
	#f.write("\t\t\t\t<destinationValue>Deceased (HUD)</destinationValue>\n") 
	f.write("\t\t\t</EntryExit>\n")
			
			
f.write('\t\t</entryExitRecords>\n')

f.write('\t</records>\n')
f.close()
print 'finished writing XML'
	
	