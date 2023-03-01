import requests

# out_data = {"user": "Bill", "message": "Hi Jerry are you looking at flights to CA? What do you want for lunch?"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
# print(r.status_code)
# print(r.text)

# r_get = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Jerry")
# print(r_get.text)

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/bc299")
print(r.text)

blood_type_M1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1").text
blood_type_F5 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F5").text

print(blood_type_M1)
print(blood_type_F5)

out_data = {"Name": "bc299", "Match": "Yes"}
post_answer = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(post_answer.text)
