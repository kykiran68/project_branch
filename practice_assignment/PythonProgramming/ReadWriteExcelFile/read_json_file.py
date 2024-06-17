import json

def read_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data


# result = read_json_data("test_json_content.json")
# print(result)
# print("Name :", result["Name"])
# print("Name :", result["Email"])


def write_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
    json_data["ip"] = "10.22.33.44"
    print(json_data)

    updated_data = json.dumps(json_data)

    with open(filename, "w") as file:
        file.write(updated_data)

#write_json_data("test_json_content.json")
write_json_data(r"E:\target_location\test_json_content.json")
