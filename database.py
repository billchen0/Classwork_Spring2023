def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Jerry Yang", 1, 23))
    db.append(create_patient_entry("Vivian Fei", 2, 23))
    db.append(create_patient_entry("Jessilyn Dunn", 3, 36))
    print(db)
    
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)

def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print(f"Patient {patient[0]} is in room {room_numbers[i]}")

    for patient, rn in zip(db, room_numbers):
        print(f"Patient {patient[0]} is in room {rn}")

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Invalid Entry")
    else:
        patient[3].append([test_name, test_value])
    return

        

if __name__ == "__main__":
    main_driver()
