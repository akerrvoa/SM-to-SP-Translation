##define functions	
def dashssn(ssn_in):
	ssn_in.lstrip()
	ssn_in.rstrip()
	ssn_out = ssn_in[:3] + '-' + ssn_in[3:5] + '-' + ssn_in[5:]
	return ssn_out
	

#parse and format dob  xsd:dateTime  [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] 
#The time zone may be specified as Z (UTC) or (+|-)hh:mm. Time zones that aren't specified are considered undetermined.	
def formatdob(dob_in):
	dob_in.lstrip()
	dob_in.rstrip()
	parts = dob_in.split('/')
	#input is (m)m/(d)d/yyyy   output is yyyy-mm-ddThh:mm:ss-0H:00
	if len(parts[0]) == 1 : 
		mo_out = '0' + parts[0]
	else : 
		mo_out = parts[0]
	if len(parts[1]) == 1 : 
		day_out = "0" + parts[1]
	else :
		day_out = parts[1]
	dob_out = parts[2] + '-' + mo_out + '-' + day_out + "T00:00:00-05:00"
	return dob_out

def formatgender(gender_in):
	gender_out = gender_in
	return gender_out
	
def formatrace(race_in):
	race_out = race_in
	return race_out

def formatveteran(vet_in):
	vet_out = vet_in
	return vet_out