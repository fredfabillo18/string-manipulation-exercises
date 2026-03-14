def parse_telemetry(data_list):
    id_dicts = []
    for data in data_list:
        entry=data.split('|') #we now have split the data into each ID entry

        id_dicts.append({
            "id":int(entry[0].split(':')[1]),
            "temp":float(entry[1].split(':')[1]),
            "is_safe": float(entry[1].split(':')[1]) < 30.0
        })

    print(id_dicts)

def parse_telemetry2(data_list):
    id_dicts = {key: value for key, value in (key_value.split(':') for key_value in (entry.split('|') for entry in data_list))}
    print(id_dicts)

def parse_telemetry3(data_list):
    # This creates a list of dictionaries
    id_dicts = [{k: v for k, v in (item.split(':') for item in entry.split('|'))} for entry in data_list]
    print(id_dicts)


sample = ["ID:1|Temp:25.0|Status:OK", "ID:2|Temp:35.5|Status:WARN"]
parse_telemetry(sample)
