def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Jerry Yang", 120, 23))
    db.append(create_patient_entry("Vivian Fei", 60, 23))
    db.append(create_patient_entry("Jessilyn Dunn", 67, 36))
    print(db)
    print("Get patient Jerry")
    mrn_to_find = 120
    found_patient = get_patient_entry(db, mrn_to_find)
    if found_patient is False:
        print(f"Patient mrn {mrn_to_find} not found")
    else:
        print(found_patient)

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    
    return False
        

if __name__ == "__main__":
    main_driver()
