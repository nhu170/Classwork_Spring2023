from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    # Call other functions to do the work
    answer, status_code = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


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
        return "Input is not dictionary"
    expected_key = ["name", "id", "blood_type"]
    expected_type = [str, int, str]
    for key, value_type in zip(expected_key, expected_type):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True

# Add new test


def add_test_to_db(id, test_name, test_result):
    db[id]["tests"].append((test_name, test_result))
    print(db)


@app.route("/new_test", methods=["POST"])
def post_new_test():
    in_data = request.get_json()
    answer, status_code = new_test_driver(in_data)
    return jsonify(answer), status_code


def does_patient_exist_in_db(id):
    if id in db:
        return True
    else:
        return False


def new_test_driver(in_data):
    # Validate input
    validation = validate_input_test(in_data)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
            .format(in_data["id"]), 400
    # Do the work
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    # Return an answer
    return "Test successfully added", 200


def validate_input_test(in_data):
    if type(in_data) is not dict:
        return "Input is not dictionary"
    expected_key = ["id", "test_name", "test_result"]
    expected_type = [int, str, int]
    for key, value_type in zip(expected_key, expected_type):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


if __name__ == '__main__':
    app.run()
