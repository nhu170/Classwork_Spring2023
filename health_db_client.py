import requests

server = "http://127.0.0.1:5000"

patient = {"id": 1, "name": "David", "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

test = {"id": 1, "test_name": "HDL", "test_result": 65}
r = requests.post(server + "/new_test", json=test)
print(r.status_code)
print(r.text)