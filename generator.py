import faker
import random
from datetime import date
from dateutil.relativedelta import relativedelta

fake = faker.Faker()

# Generate Patients Data with yield
def patients(num=5):
    for i in range(num):
        yield {
            "id": fake.uuid4(),
            "name": fake.name(),
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
            "gender": random.choice(["M", "F"]),
            "contact_number": fake.phone_number(),
            "email": fake.email(),
            "address": fake.address().replace("\n", ", ")
        }

# Example Usage: Iterate through the generated data
# Converting the generator to a list to showcase the output (for demonstration)
print("Patients:")
data_patients = list(patients(5))
for patient in data_patients:
    print(patient)


# Generate Allergies Data
def allergies(patients):
    allergy_types = ['Peanuts', 'Dust', 'Lactose', 'Shellfish', 'Pollen', 'Animal dander']
    severities = ['Low', 'Medium', 'High']
    for i, patient in enumerate(patients):
        yield {
            'id': fake.uuid4(),
            'patient_id': patient['id'],
            'allergy_type': random.choice(allergy_types),
            'severity': random.choice(severities),
            'notes': fake.sentence()
        }

print('Allergies:')
data_allergies = list(allergies(data_patients))
for allergy in data_allergies:
    print(allergy)


# Generate Medications Data with yield
def medications(patients):
    medications_list = ["Lisinopril", "Ibuprofen", "Insulin", "Paracetamol", "Metformin"]
    for i, patient in enumerate(patients):
        yield {
            "medication_id": i + 1,
            "patient_id": patient["id"],
            "medication_name": random.choice(medications_list),
            "dosage": f"{random.randint(5, 50)} mg",
            "frequency": random.choice(["Once daily", "Twice daily", "As needed"]),
            "start_date": fake.date_between(start_date='-6m', end_date="today").strftime("%Y-%m-%d"),
            "end_date": random.choice([None, fake.date_between(start_date="today", end_date='+1y').strftime("%Y-%m-%d")])
        }

print('medications:')
data_medications = list(medications(data_patients))
for medication in data_medications:
    print(medication)


# Generate Doctor Notes Data with yield
def doctor_notes(patients):
    doctor_ids = [101, 102, 103]
    for i, patient in enumerate(patients):
        yield {
            "note_id": i + 1,
            "patient_id": patient["id"],
            "doctor_id": random.choice(doctor_ids),
            "visit_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            "notes": fake.paragraph(),
        }

print('doctor_notes:')
data_doctor_notes = list(doctor_notes(data_patients))
for doctor_note in data_doctor_notes:
    print(doctor_note)


# Generate Doctors Data with yield
def doctors(num_doctors=3):
    specializations = ["Cardiology", "Orthopedics", "Endocrinology", "Neurology", "Pediatrics"]
    for i in range(num_doctors):
        yield {
            "doctor_id": 101 + i,
            "name": fake.name(),
            "specialization": random.choice(specializations),
            "contact_number": fake.phone_number(),
            "email": fake.email(),
        }

# test doctors generator:
print('doctors:')
data_doctors = list(doctors())
for doctor in data_doctors:
    print(doctor)


# Generate Visits Data with yield
def visits(patients, doctors, start_date, end_date):
    types_of_visit = ["Routine Check-up", "Follow-up", "Emergency", "Specialist Consultation"]
    for i, patient in enumerate(patients):
        yield {
            "visit_id": fake.uuid4(),
            "patient_id": patient["id"],
            "doctor_id": random.choice(doctors)['doctor_id'],
            "type_of_visit": random.choice(types_of_visit),
            "visit_date": fake.date_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d"),
            "notes": fake.paragraph(),
        }


# Test visits generator:
print('visit:')
data_visit = list(visits(patients=data_patients, doctors=data_doctors, start_date="-1y", end_date="today"))
for visit in data_visit:
    print(visit)

# Generate Pharmacy Orders Data with yield
def pharmacy_orders(patients, medications):
    for i, (patient, medication) in enumerate(zip(patients, medications)):
        yield {
            "order_id": i + 1,
            "patient_id": patient["id"],
            "medication_id": medication["medication_id"],
            "quantity": random.randint(5, 30),
            "order_date": fake.date_between(start_date="-2m", end_date="today").strftime("%Y-%m-%d"),
            "status": random.choice(["Pending", "Delivered", "Cancelled"]),
        }

# test pharmacy orders generator:
print('pharmacy_orders:')
data_pharmacy_orders = list(pharmacy_orders(data_patients, data_medications))
for pharmacy_order in data_pharmacy_orders:
    print(pharmacy_order)


