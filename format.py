##define functions	
def dashssn(ssn_in):
	ssn_in.lstrip()
	ssn_in.rstrip()
	ssn_out = ssn_in[:3] + '-' + ssn_in[3:5] + '-' + ssn_in[5:]
	return ssn_out
	

#parse and format dt  xsd:dateTime  [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] 
#The time zone may be specified as Z (UTC) or (+|-)hh:mm. Time zones that aren't specified are considered undetermined.	
def formatdt(dt_in):
	dt_in.lstrip()
	dt_in.rstrip()
	parts = dt_in.split('/')
	#input is (m)m/(d)d/yyyy   output is yyyy-mm-ddThh:mm:ss-0H:00
	if len(parts[0]) == 1 : 
		mo_out = '0' + parts[0]
	else : 
		mo_out = parts[0]
	if len(parts[1]) == 1 : 
		day_out = "0" + parts[1]
	else :
		day_out = parts[1]
	dt_out = parts[2] + '-' + mo_out + '-' + day_out + "T00:00:00-05:00"
	return dt_out

def formatgender(gender_in):
	gender_out = gender_in
	return gender_out
	
def formatrace(race_in):
	if race_in == "African American" :
		race_out = "Black or African American (HUD)"
	elif race_in == "Caucasian" :
		race_out = "White (HUD)"
	# elif race_in == "Hispanic" or race_in == "Other" or race_in == "Unspecified"
		# race_out = "Data not collected (HUD)"
	else :
		race_out = "Data not collected (HUD)"
	return race_out

def formatveteran(vet_in):
	if vet_in == "Yes" :
		vet_out = "Yes (HUD)"
	elif vet_in == "No" :
		vet_out = "No (HUD)"
	else :
		vet_out = "Data not collected (HUD)"
	return vet_out
	
	
def formatlang(lang_in):
	lang_out = lang_in
	return lang_out
	
def formatzip(zip_in) :
	zip_out = zip_in
	return zip_out
	
def formatemplstat(estat_in) :
	estat_out = estat_in
	return estat_out
	
def formathomestat(hstat_in) :
	hstat_out = hstat_in
	return hstat_out
	
def formatstat(stat_in) :
	stat_out = stat_in
	return stat_out
	
def formatdrug(drug_in) :
	drug_out = drug_in
	return drug_out
	
def formatdistype(dt_in) :
	dt_out = dt_in
	return dt_out
	
def formatunemp(unemp_in) :
	unemp_out = unemp_in	
	return unemp_out

