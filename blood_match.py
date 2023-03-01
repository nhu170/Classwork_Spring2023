import requests
import json

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nh170")
print(r.text)
patient_id = r.json()
print(patient_id)
id_don = patient_id["Donor"]
print(id_don)
id_rec = patient_id["Recipient"]
print(id_rec)


blood_don = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" +
                         id_don)
print(blood_don.text)
blood_rec = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" +
                         id_rec)
print(blood_rec.text)


out_data = {"Name": "nh170", "Match":  "No"}
r_out = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                      json=out_data)
print(r_out.status_code)
print(r_out.text)
