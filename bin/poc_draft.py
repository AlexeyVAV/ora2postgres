import re

with open('../inbound/2017-12-20_uscomdv1_marketplace_tables.sql') as f:
    #print(f.readlines())
    while f:
        print(f.readline())
    #resDDL = re.sub(r'VARCHAR2', 'VARCHAR', f.readlines(), flags=re.IGNORECASE)
    #print resDDL


ddlText = '''CREATE TABLE "MARKETPLACE"."AGGREGATE_FUNCTION_MATRIX"
(    "TABLE_NAME" VARCHAR2(30) NOT NULL ENABLE,
	"PACKAGE_NAME" VARCHAR2(30) NOT NULL ENABLE,
	UNIQUE ("TABLE_NAME")
	USING INDEX  ENABLE
)
'''

#print(ddlText)

#resDDL = re.sub(r'VARCHAR2', 'VARCHAR', ddlText, flags=re.IGNORECASE)

#print(resDDL)

#######################################################
# If you replace each word one at a time, you might replace words several times (and not get what you want). To avoid this, you can use a function or lambda:
#
# d = {'bean':'robert', 'beans':'cars'}
# str_in = 'bean likes to sell his beans'
# str_out = re.sub(r'\b(\w+)\b', lambda m:d.get(m.group(1), m.group(1)), str_in)
#
# That way, once bean is replaced by robert, it won't be modified again (even if robert is also in your input list of words).
#
# As suggested by georg, I edited this answer with dict.get(key, default_value). Alternative solution (also suggested by georg):
#
# str_out = re.sub(r'\b(%s)\b' % '|'.join(d.keys()), lambda m:d.get(m.group(1), m.group(1)), str_in)
#######################################################

