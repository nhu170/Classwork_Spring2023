# list_database.py

def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    new_patient = {"First name": first_name, "Last name": last_name,
                    "MRN": patient_mrn, "Age": patient_age,
                    "Tests": []}
    return new_patient


def main_driver():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 34))
    db.append(create_patient_entry("Bob", "Boyles", 2, 45))
    db.append(create_patient_entry("Chris", "Chou", 3, 52))
    print(db)
    return
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "HDL", 99)
    room_numbers = ["103","202","333"]
    print(db)
    print_directory(db, room_numbers)
    print(get_test_value(db, 1, "HDL"))

    #print("Get patient Ann")
    #mrn_to_find = 1
    #found_patient = get_patient_entry(db, mrn_to_find)
    # Only use "is" to compare Boolean, use == to compare other types of variables
    #if found_patient is False:
        #print("Patient mrn {} not found".format(mrn_to_find))
    #else:
        #print(found_patient)
    # printing Bob's age
    # print(db[1][2])

def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False


def get_test_value(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_list = patient[3]
    test_value = get_test_value_from_test_list(test_list, test_name)
    return test_value


def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    #Another way is to zip (2 lists need to be the same size):
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))


def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append([test_name, test_value])
    return


if __name__ == "__main__":
    main_driver()
