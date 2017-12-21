import re

# python regex tester
# http://www.pyregex.com/

#pattern = re.compile('VARCHAR2')

with open("../inbound/2017-12-20_uscomdv1_marketplace_tables.sql") as f:
    for line in f:
        # print(line)
        #outLine = pattern.sub(r"VARCHAR", line)
        if re.search("VARCHAR2", line):
            outLine = re.sub(r"VARCHAR2", "VARCHAR", line, flags=re.IGNORECASE)
            print (outLine, re.findall("VARCHAR[(](\d+)", outLine))
