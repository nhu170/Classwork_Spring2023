# list_database.py

def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    new_patient = {"First name": first_name, "Last name": last_name,
                   "MRN": patient_mrn, "Age": patient_age,
                   "Tests": []}
    return new_patient


def main_driver():
    db = {}
    db[1] = (create_patient_entry("Ann", "Ables", 1, 34))
    db[2] = (create_patient_entry("Bob", "Boyles", 2, 45))
    db[3] = (create_patient_entry("Chris", "Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "HDL", 99)
    # room_numbers = ["103","202","333"]
    print(db)
    print_database(db)
    # print_directory(db, room_numbers)
    print(get_test_value(db, 1, "HDL"))
    return

    # print("Get patient Ann")
    # mrn_to_find = 1
    # found_patient = get_patient_entry(db, mrn_to_find)
    # Only use "is" to compare Boolean,
    # use == to compare other types of variables
    # if found_patient is False:
    # print("Patient mrn {} not found".format(mrn_to_find))
    # else:
    # print(found_patient)
    # printing Bob's age
    # print(db[1][2])


def get_full_name(patient):
    return "{} {}".format(patient["First name"], patient["Last name"])


def print_database(db):
    for patient in db.values():
        mrn = patient["MRN"]
        age = patient["Age"]
        full_name = get_full_name(patient)
        print("MRN: {}, Full Name: {}, Age: {}".format(mrn, full_name, age))


def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False


def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    # Another way is to zip (2 lists need to be the same size):
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))


def get_patient_entry(db, mrn_to_find):
    patient = db.get(mrn_to_find)
    if patient is None:
        return False
    return patient


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient is False:
        print("Bad entry")
    else:
        patient["Tests"].append([test_name, test_value])
    return


def get_test_value(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_list = patient["Tests"]
    test_value = get_test_value_from_test_list(test_list, test_name)
    return test_value


if __name__ == "__main__":
    main_driver()
