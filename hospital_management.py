# Hospital Management System
# Simple console based project using Python lists and functions.

patients = []
doctors = []
appointments = []
bills = []


#This function adds a new patient to the system. 
def add_patient():
    print("\n--- Add Patient ---")

    patient_id = input("Enter Patient ID: ").strip()

    if find_patient(patient_id) is not None:
        print("A patient with this ID already exists.")
        return

    name = input("Enter Name: ").strip()

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    disease = input("Enter Disease: ").strip()
    phone = input("Enter Phone Number: ").strip()

    patients.append([patient_id, name, age, disease, phone])
    print("Patient added successfully!")


def show_patients():
    print("\n--- Patient Details ---")

    if len(patients) == 0:
        print("No patients found.")
        return

    for patient in patients:
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Disease:", patient[3])
        print("Phone:", patient[4])
        print("-------------------")


def find_patient(patient_id):
    for patient in patients:
        if patient[0].lower() == patient_id.lower():
            return patient
    return None


def search_patient():
    print("\n--- Search Patient ---")
    patient_id = input("Enter Patient ID: ").strip()

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print("\nPatient found!")
    print("ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Disease:", patient[3])
    print("Phone:", patient[4])


def update_patient():
    print("\n--- Update Patient ---")
    patient_id = input("Enter Patient ID: ").strip()

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print("Press Enter if you want to keep the old value.")

    name = input(f"Name [{patient[1]}]: ").strip()
    age = input(f"Age [{patient[2]}]: ").strip()
    disease = input(f"Disease [{patient[3]}]: ").strip()
    phone = input(f"Phone [{patient[4]}]: ").strip()

    if name:
        patient[1] = name

    if age:
        try:
            new_age = int(age)
            if new_age <= 0:
                print("Invalid age. Old age was kept.")
            else:
                patient[2] = new_age
        except ValueError:
            print("Invalid age. Old age was kept.")

    if disease:
        patient[3] = disease

    if phone:
        patient[4] = phone

    print("Patient details updated successfully!")


def delete_patient():
    print("\n--- Delete Patient ---")
    patient_id = input("Enter Patient ID: ").strip()

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    confirm = input("Are you sure you want to delete this patient? (y/n): ")

    if confirm.lower() == "y":
        patients.remove(patient)
        print("Patient deleted successfully.")
    else:
        print("Delete operation cancelled.")


# This function adds a new doctor to the system.
    print("\n--- Add Doctor ---")

    doctor_id = input("Enter Doctor ID: ").strip()

    if find_doctor(doctor_id) is not None:
        print("A doctor with this ID already exists.")
        return

    name = input("Enter Doctor Name: ").strip()
    specialization = input("Enter Specialization: ").strip()
    phone = input("Enter Phone Number: ").strip()

    doctors.append([doctor_id, name, specialization, phone])
    print("Doctor added successfully!")


def show_doctors():
    print("\n--- Doctor Details ---")

    if len(doctors) == 0:
        print("No doctors found.")
        return

    for doctor in doctors:
        print("ID:", doctor[0])
        print("Name:", doctor[1])
        print("Specialization:", doctor[2])
        print("Phone:", doctor[3])
        print("-------------------")


def find_doctor(doctor_id):
    for doctor in doctors:
        if doctor[0].lower() == doctor_id.lower():
            return doctor
    return None


def search_doctor():
    print("\n--- Search Doctor ---")
    doctor_id = input("Enter Doctor ID: ").strip()

    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found.")
        return

    print("\nDoctor found!")
    print("ID:", doctor[0])
    print("Name:", doctor[1])
    print("Specialization:", doctor[2])
    print("Phone:", doctor[3])


def update_doctor():
    print("\n--- Update Doctor ---")
    doctor_id = input("Enter Doctor ID: ").strip()

    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found.")
        return

    print("Press Enter if you want to keep the old value.")

    name = input(f"Name [{doctor[1]}]: ").strip()
    specialization = input(
        f"Specialization [{doctor[2]}]: "
    ).strip()
    phone = input(f"Phone [{doctor[3]}]: ").strip()

    if name:
        doctor[1] = name
    if specialization:
        doctor[2] = specialization
    if phone:
        doctor[3] = phone

    print("Doctor details updated successfully!")


def delete_doctor():
    print("\n--- Delete Doctor ---")
    doctor_id = input("Enter Doctor ID: ").strip()

    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found.")
        return

    confirm = input("Are you sure you want to delete this doctor? (y/n): ")

    if confirm.lower() == "y":
        doctors.remove(doctor)
        print("Doctor deleted successfully.")
    else:
        print("Delete operation cancelled.")


# This function books a new appointment for a patient with a doctor. 

def add_appointment():
    print("\n--- Book Appointment ---")

    patient_id = input("Enter Patient ID: ").strip()
    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found. Add the patient first.")
        return

    doctor_id = input("Enter Doctor ID: ").strip()
    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found. Add the doctor first.")
        return

    date = input("Enter Date (DD-MM-YYYY): ").strip()
    time = input("Enter Time: ").strip()

    appointments.append([
        len(appointments) + 1,
        patient_id,
        doctor_id,
        date,
        time,
        "Scheduled"
    ])

    print("Appointment booked successfully!")


def show_appointments():
    print("\n--- Appointment Details ---")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    for appointment in appointments:
        patient = find_patient(appointment[1])
        doctor = find_doctor(appointment[2])

        patient_name = patient[1] if patient else "Unknown"
        doctor_name = doctor[1] if doctor else "Unknown"

        print("Appointment ID:", appointment[0])
        print("Patient:", patient_name, "(" + appointment[1] + ")")
        print("Doctor:", doctor_name, "(" + appointment[2] + ")")
        print("Date:", appointment[3])
        print("Time:", appointment[4])
        print("Status:", appointment[5])
        print("-------------------")


def cancel_appointment():
    print("\n--- Cancel Appointment ---")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    try:
        appointment_id = int(input("Enter Appointment ID: "))
    except ValueError:
        print("Please enter a valid appointment ID.")
        return

    for appointment in appointments:
        if appointment[0] == appointment_id:
            if appointment[5] == "Cancelled":
                print("This appointment is already cancelled.")
            else:
                appointment[5] = "Cancelled"
                print("Appointment cancelled successfully.")
            return

    print("Appointment not found.")


# This function creates a new bill for a patient.
def create_bill():
    print("\n--- Create Patient Bill ---")

    patient_id = input("Enter Patient ID: ").strip()
    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    try:
        consultation = float(input("Consultation Fee: "))
        medicine = float(input("Medicine Charges: "))
        tests = float(input("Test Charges: "))
    except ValueError:
        print("Please enter valid amounts.")
        return

    if consultation < 0 or medicine < 0 or tests < 0:
        print("Charges cannot be negative.")
        return

    total = consultation + medicine + tests

    bills.append([
        len(bills) + 1,
        patient_id,
        consultation,
        medicine,
        tests,
        total
    ])

    print("Bill created successfully.")
    print("Total Amount: Rs.", format(total, ".2f"))


def show_bills():
    print("\n--- Billing Details ---")

    if len(bills) == 0:
        print("No bills found.")
        return

    for bill in bills:
        patient = find_patient(bill[1])
        patient_name = patient[1] if patient else "Unknown"

        print("Bill ID:", bill[0])
        print("Patient:", patient_name)
        print("Consultation Fee: Rs.", format(bill[2], ".2f"))
        print("Medicine Charges: Rs.", format(bill[3], ".2f"))
        print("Test Charges: Rs.", format(bill[4], ".2f"))
        print("Total: Rs.", format(bill[5], ".2f"))
        print("-------------------")


# This function displays the main menu of the Hospital Management System.
def main_menu():
    while True:
        print("\n========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("========================================")
        print("1.  Add Patient")
        print("2.  Show Patients")
        print("3.  Search Patient")
        print("4.  Update Patient")
        print("5.  Delete Patient")
        print("6.  Add Doctor")
        print("7.  Show Doctors")
        print("8.  Search Doctor")
        print("9.  Update Doctor")
        print("10. Delete Doctor")
        print("11. Book Appointment")
        print("12. Show Appointments")
        print("13. Cancel Appointment")
        print("14. Create Bill")
        print("15. Show Bills")
        print("16. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_patient()
        elif choice == "2":
            show_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            add_doctor()
        elif choice == "7":
            show_doctors()
        elif choice == "8":
            search_doctor()
        elif choice == "9":
            update_doctor()
        elif choice == "10":
            delete_doctor()
        elif choice == "11":
            add_appointment()
        elif choice == "12":
            show_appointments()
        elif choice == "13":
            cancel_appointment()
        elif choice == "14":
            create_bill()
        elif choice == "15":
            show_bills()
        elif choice == "16":
            print("\nThank you for using the Hospital Management System!")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 16.")


if __name__ == "__main__":
    main_menu()
