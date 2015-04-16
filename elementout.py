
def writeassessment(fh, indent, fname, content, da, de):
	for i in range(indent) :
		fh.write("\t")
	fh.write("<" + fname + " date_added='" + da + "' date_effective='" + de + "'>" + content + "</" + fname + ">\n")