from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {
        "id": id,
        "name": name,
        "blood_type": blood_type,
        "test": []
    }

    db[id] = new_patient
    print(db)

def add_test_to_db(id, name, blood_type):
    new_test = {
        "id": id,
        "name": name,
        "blood_type": blood_type
    }

    db[id]["test"].append(new_test)



@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    # Call other functions to do the work
    answer, status_code = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


@app.route("/add_test", methods=["POST"])
def post_new_test():
    in_data = request.get_json()
    answer, status_code = new_test_driver(in_data)
    return jsonify(answer), status_code


def new_test_driver(in_data):
    validation = validate_test_data(in_data)
    if validation is not True:
        return validation, 400
    add_test_to_db(in_data["mrn"], in_data["name"], in_data["blood_type"])
    return "Test successfully added", 200
    


def validate_test_data(in_data):
    expected_keys = ["mrn", "name", "blood_type"]
    expected_types = [int, str, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in expected_keys:
            return f"Key {key} is missing from input"
        if type(in_data[key]) is not value_type:
            return f"Key {key} has the incorrect value type"
    return True


def new_patient_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return f"Key {key} is missing from input"
        if type(in_data[key]) is not value_type:
            return f"Key {key} has the incorrect value type"
    return True


if __name__ == "__main__":
    app.run()
    