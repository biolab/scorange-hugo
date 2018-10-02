import glob
import shutil
import json


files = glob.glob('content/widget-catalog/*.md', recursive=True)
json_content = {"Data" : []}

for file in files:
    # read content
    if "index" not in file:
        with open(file, 'r') as f:
            content = f.read()
        content = content.split("+++")[1]

        front_matter = content.strip().split("\n")
        tmp_json = {}
        for att in front_matter:
            tmp = att.strip().split("=")
            key = tmp[0].strip().split('"')[1]
            value = tmp[1].strip('').split('"')[1]
            if key == "title":
                url = value.lower().replace(" ", "_")
                tmp_json["url"] = url
            tmp_json[key] = value

        json_content["data"].append(tmp_json)

with open('static/widgets.json', 'w') as outfile:
    json.dump(json_content, outfile)


