import fileinput
import sys
import re

def param_load(sys_argv):
    print("Load parameters")
    if len(sys_argv) < 2:
        return "../etc/ora2psql_dt.map"
    else:
        return sys.argv[0]

def mapping_load(mapping_file):
    print("Load mapping file")

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

def search_in_line(line_in):
    print("Search in line")
    #while not re.search("VARCHAR2", line_in):

def dt_replace(source_file, target_file):
    #with open("../inbound/2017-12-20_uscomdv1_marketplace_tables.sql") as f:
    with open(source_file) as f:
        for line in f:
            # print(line)
            # outLine = pattern.sub(r"VARCHAR", line)
            if re.search("VARCHAR2", line):
                outLine = re.sub(r"VARCHAR2", "VARCHAR", line, flags=re.IGNORECASE)
                print (outLine, re.findall("VARCHAR[(](\d+)", outLine))


def main(sys_params):
    print(sys_params)

    # mapping_load(param_load(sys.argv))
    ora_dt_map = mapping_load("../etc/ora2psql_dt.map")
    if ora_dt_map > 0:
        print(ora_dt_map[2][0])
        print(type(ora_dt_map))

    source_ddl_load("../inbound/ddl_script.sql")


# Main #
if __name__ == "__main__":
    print("Main part")

    if param_load(sys.argv) == 0:
        print("Error")
    else:
        main(param_load(sys.argv))
