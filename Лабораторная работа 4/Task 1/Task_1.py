import json


def task (file_path):
    with open(file_path) as file:
        data = json.load(file)

    total_sum = 0

    for item in data:
        score = item["score"]
        weight = item["weight"]

        product = score * weight
        total_sum += product

    return round(total_sum, 3)


file_path = "input.json"
result = task(file_path)
print(result)
