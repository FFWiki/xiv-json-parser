# TODO: Make icons work

import urllib.request, json, databases 
xivdb = databases.databases()
DEBUG = True

def decode(url):
    with urllib.request.urlopen(url) as data:
        return json.loads(data.read().decode())

def recover_ids(url):
    print("\tRecovering IDs...")
    ids = []
    for unit in decode(url):
        ids.append(unit['id'])
    return ids

def tostr(v, keys):
    if isinstance(v, bool):
        return (v and 1) or None
    elif isinstance(v, int) or isinstance(v, float):
        if v == 0:
            return None
        return str(v)
    elif isinstance(v, dict):
        return read_table(v, keys)
    elif isinstance(v, str):
        return "[[" + v + "]]"
    elif v is None or v == []:
        return None
    else:
        print("don't know what to do with")
        print(str(v))
        return None

def read_table(v, keys):
    lua = "{"
    for k in keys:
        if k in v:
            s = tostr(v[k], keys[k])
            if s is not None:
                lua += k + "=" + s + ","
    lua += "}"
    return lua

def parse_run(url, keys):
    lua = "return {data={"
    index = ""
    ids = recover_ids(url)
    print("\tDecoding data...")
    debug_halt = False
    for uid in ids:
        if DEBUG and debug_halt:
            break
        if uid % 100 == 0:
            print("\t\tCurrently running UID " + str(uid))
        uid = str(uid)

        v = decode(url + "/" + uid)
        if 'is_in_game' in v and v['is_in_game'] == 0:
            continue
        debug_halt = True
        
        index += "['" + v['name'] + "']="+uid+","
        lua += "[" + uid + "]=" + read_table(v, keys) + ","
    lua += "},index={" + index + "}}"
    return lua

for db in xivdb:
    print("Running parser on database " + db + ":")
    s = parse_run(xivdb[db]['url'], xivdb[db]['keys'])
    if len(s) > 2097150:
        print('\tPossibility of MediaWiki file overflow error.')
    print("\tPrinting to file...")
    with open('lua/' + db + '.lua', 'w') as f:
        f.write(s)
    print("\tDone!")
