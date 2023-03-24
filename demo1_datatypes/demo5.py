desired_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "mobileNumber": 87878787,
    "iemi": [78877, 9898989],
    "account": {'name1': 'john', 'name2': 'peter'}
}
print(type(desired_cap))
print(desired_cap)

print(desired_cap['deviceName'])

print(desired_cap["iemi"][0])

print(desired_cap['account']['name2'])