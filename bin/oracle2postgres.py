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
        with open(mapping_file) as f:
            print(f.readlines())
    except:
        print("Error loading mapping file")
        raise

def source_ddl_load(ddl_file):
    print("Load source DDL file:", ddl_file)

# Main #
if __name__ == "__main__":
    print("Main part")

    if param_load(sys.argv) == 0:
        print("Error")
    else:
        print(param_load(sys.argv))
        mapping_load(param_load(sys.argv))
        source_ddl_load("../inbound/ddl_script.sql")