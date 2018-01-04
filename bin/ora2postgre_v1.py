import os
import sys
import pandas as pd

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

def source_load(source_file):
    # example = pd.read_csv(myfile,sep='\t',skiprows=(0,1,2),header=(0))
    # df = pd.read_csv(source_file,sep='\t',skiprows=(0,1,2,3,4,5,6,7,9),header=(0))
    #df = pd.read_csv(source_file, sep=',', skiprows=(0, 1, 2, 3, 4, 5, 6, 7,8,10), header=(0),skipinitialspace=True)
    #print(df.columns.values)

    # pandas approach
    # the line below is working
    #df = pd.read_csv(source_file, sep=',', skiprows=(0, 1, 2, 3, 4, 5, 6), skipinitialspace=True, names=['OWNER','TABLE_NAME','COLUMN_NAME','DATA_TYPE','DATA_LENGTH','DEFAULT_LENGTH'])
    #print(df.head())

    with open(source_file, 'r') as f:
        for line in f:
            #line = f.readline()
            print(line.strip().split(','))


############################################################################################
def main(sys_params):
    #print(sys_params)
    # mapping_load(param_load(sys.argv))

    ora_dt_map = mapping_load("../etc/ora2psql_dt.map")
    if ora_dt_map > 0:
        print("Length: ",len(ora_dt_map))
        print(type(ora_dt_map))
        #source_load('../inbound/2018-01-04_uscomdv1_tab_col.lst')
        source_load('../inbound/2018-01-04_uscomdv1_tab_col_2.lst')
    #dt_replace("../inbound/2017-12-20_uscomdv1_marketplace_tables.sql", "target_file", ora_dt_map)
    #dt_replace("../inbound/2018-01-02_uscomdv1_marketplace_tables.sql", "target_file", ora_dt_map)

   # print

# Main #
if __name__ == "__main__":
    print("Main part")
    params = param_load(sys.argv)
    if params == 0:
        print("Error")
    else:
        main(params)