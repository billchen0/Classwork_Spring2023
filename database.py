def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Jerry Yang", 69, 23))
    db.append(create_patient_entry("Vivian Fei", 68, 23))
    db.append(create_patient_entry("Bill Chen", 67, 22))
    print(db)

if __name__ == "__main__":
    main_driver()
