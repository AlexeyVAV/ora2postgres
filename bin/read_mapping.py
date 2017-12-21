import re

with open("../etc/ora2psql_dt.map") as mf:
    o2p_map = mf.readlines()

o2p_map = [s.split("\t") for s in o2p_map if "#" not in s.lstrip()[0]]

print(o2p_map)

# if string starts from #
# re.match("(?:^#).*", o2p_map)