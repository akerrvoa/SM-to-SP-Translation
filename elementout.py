
###############################################
###############################################
def write_providers(fh, si, ri, nm, da, du) : 
	fh.write("\t\t<providerRecords>\n") 
	fh.write("\t\t\t<Provider system_id='" + si + "' record_id='" + ri + "' date_added='" + da + "' date_updated='" + du + "'>\n")
	fh.write("\t\t\t\t<name>" + nm + "</name>\n")
	fh.write("\t\t\t</Provider>\n") 
	fh.write("\t\t</providerRecords>\n")
	
	
###############################################
###############################################
def writeassessment(fh, indent, fname, content, da, de):
	for i in range(indent) :
		fh.write("\t")
	fh.write("<" + fname + " date_added='" + da + "' date_effective='" + de + "'>" + content + "</" + fname + ">\n")