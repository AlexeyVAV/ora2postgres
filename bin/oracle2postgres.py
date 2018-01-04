#import fileinput
import sys
import re
import os

def param_load(sys_argv):
    print("Load parameters",sys_argv)
    if len(sys_argv) < 2:
        return "../etc/ora2psql_dt.map"
    else:
        return sys.argv[0]

def mapping_load(mapping_file):
    print("Load mapping file",mapping_file)

    try:
        with open(mapping_file) as _mf:
            _o2p_map = _mf.readlines()
    except:
        print("Error loading mapping file")
        return 0
        raise

    try:
        o2p_map = [s.split("\t") for s in _o2p_map if len(s) > 0 and "#" not in s.lstrip()[0]]
        return o2p_map
    except IndexError:
        print("Mapping file error")
        return 0
        raise


def source_ddl_load(ddl_file):
    print("Load source DDL file:", ddl_file)

def search_in_line(line_in, mapping):
    #print("Search in line")
    line_s = re.split("\W+", line_in)
    r1,r2 = 0,0
    for i in range(len(mapping)):
        if mapping[i][0] in line_s:
            #print("Found",mapping[i][0],"in", line_s,"replace with",mapping[i][1])
            r1,r2 = mapping[i][0],mapping[i][1]
            #return mapping[i][0], mapping[i][1]
        #else:
    return r1,r2

def dt_replace(source_file, target_file, ora_dt_map):
    #with open("../inbound/2017-12-20_uscomdv1_marketplace_tables.sql") as f:
    #ora_dt_map = mapping_load("../etc/ora2psql_dt.map")
    with open(source_file) as f:
        for line in f:
            str1, str2 = search_in_line(line, ora_dt_map)
            #print(str1,str2)
            if str1 != 0:
                if re.search(str1, line):
                    outLine = re.sub(str1, str2, line, flags=re.IGNORECASE)
                    #print (line,"to",outLine)
                    print(outLine)
                    #print (outLine, re.findall("VARCHAR[(](\d+)", outLine))
            else:
                print(line)

def output_file_write(output_file): # ../outbound/output_file_test.sql
    if not os.path.exists(output_file):
        with open(output_file,'wt') as _of:
            _of.write('-- begin file --')


############################################################################################
def main(sys_params):
    #print(sys_params)

    # mapping_load(param_load(sys.argv))
    ora_dt_map = mapping_load("../etc/ora2psql_dt.map")
    if ora_dt_map > 0:
        print("Length: ",len(ora_dt_map))
        print(type(ora_dt_map))

    #source_ddl_load("../inbound/ddl_script.sql")
    dt_replace("../inbound/2017-12-20_uscomdv1_marketplace_tables.sql", "target_file", ora_dt_map)

   # print

# Main #
if __name__ == "__main__":
    print("Main part")
    params = param_load(sys.argv)
    if params == 0:
        print("Error")
    else:
        main(params)
