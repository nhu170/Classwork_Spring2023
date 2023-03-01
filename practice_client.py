import requests

out_data = {"user": "nh170", "message": "hello world"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=out_data)
print(r.status_code)
print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/nh170")
# print(r.text)
