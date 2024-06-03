import json


def read_json(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data


result = read_json("test_json_content.json")
print(result)
print(result["Name"],result["email"])
