
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    print("Day One Dosing Guidelines")
    print("")

    diagnosis = diagnosis_input()

    weight, units = weight_input()

    if units == "lb":
        weight = weight / 2.205

    dosage_mg_first_day = calculate_dosage(weight, diagnosis)

    report_results(weight, dosage_mg_first_day)

def diagnosis_input():
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))

    return diagnosis

def weight_input():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]

    return weight, units

def calculate_dosage(weight, diagnosis):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg

    return dosage_mg_first_day

def report_results(weight, dosage_result):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_result))


if __name__ == '__main__':
    dose_amount()

