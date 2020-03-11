import junit_xml_output
import sys

counter=0
fname=sys.argv[1] # filename to grep
err=sys.argv[2]   # error message to grep for
test_cases = []


f = open(fname, "r")
for x in f:
  if (x.find(err) != -1):
    test_cases.append(junit_xml_output.TestCase("line: " + str(counter) , x, "failure"))
  #print(x)
  counter += 1
f.close()

junit_xml = junit_xml_output.JunitXml(fname, test_cases)
print (junit_xml.dump())
