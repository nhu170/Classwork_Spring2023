import requests

out_data = {"name": "Nan Hu", "net_id": "nh170",
            "e-mail": "nan.hu@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)

server = "http://vcm-21170.vm.duke.edu:5000"
r = requests.get(server + "/list")
print(r.text)
