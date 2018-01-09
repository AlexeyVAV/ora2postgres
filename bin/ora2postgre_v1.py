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

    try:
        o2p_map = [s.split("\t") for s in _o2p_map if len(s) > 0 and "#" not in s.lstrip()[0]]
        return o2p_map
    except IndexError:
        print("Mapping file error")
        return 0


def sub_dt(line_in, mapping):
    #print("Search in line")

    res1 = " {} ({})".format(line_in[3],line_in[4])

    for _i in range(len(mapping)):
        if mapping[_i][0] == line_in[3]:
            res1 = " {}({})".format(mapping[_i][1],line_in[4])
    return res1


def source_load(source_file,ora_dt_map):

    with open(source_file, 'r') as f:

        print_flag = 0
        table_name = ''

        for line in f:

            _line = line.strip().split(',')

            if _line[0][0:10] == '----------':
                print_flag = 1
            elif len(line) == 1:
                print_flag = 0


            if print_flag == 1 and _line[0][0:10] != '----------':

                if table_name != _line[1] and table_name != '':
                    print(');')

                if table_name != _line[1]:

                    table_name = _line[1]

                    print('CREATE TABLE {}.{} ({} {}'.format(
                        _line[0],
                        _line[1],
                        _line[2],
                        sub_dt(_line, ora_dt_map))
                    )

#                    print('CREATE TABLE {}.{} ( {} {}({})'.format(
#                        _line[0],
#                        _line[1],
#                        _line[2],
#                        _line[3],
#                        _line[4]
#                    )
#                    )
                else:
                    print(', {} {}'.format(_line[2], sub_dt(_line, ora_dt_map)))

    print(');')



############################################################################################
def main(sys_params):
    #print(sys_params)
    # mapping_load(param_load(sys.argv))

    ora_dt_map = mapping_load("../etc/ora2psql_dt.map")

    if ora_dt_map > 0:

        print("Length: ",len(ora_dt_map))
        print(ora_dt_map)
        source_load('../inbound/2018-01-08_uscomdv1_tab_col_1.lst',ora_dt_map)

        #l = ['MARKETPLACE', 'USER_QUERIES_TIMING_STATS_VW', 'NUMBER_OF_QUERIES', 'NUMBER', '22', '0']
        #print(sub_dt(l,ora_dt_map))


# Main #
if __name__ == "__main__":
    print("Main part")
    params = param_load(sys.argv)
    if params == 0:
        print("Error")
    else:
        main(params)