import re

with open("../etc/ora2psql_dt.map") as mf:
    o2p_map = mf.readlines()

try:
    o2p_map = [s.split("\t") for s in o2p_map if len(s) > 0 and "#" not in s.lstrip()[0]]
    print(o2p_map)
except IndexError:
    print("Mapping file error")


# if string starts from #
# re.match("(?:^#).*", o2p_map)