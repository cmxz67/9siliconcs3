# parent class for every patient
class Patient:
  def __init__(self,name,bill_amount):
    self.name=name
    self.bill_amount=bill_amount
  # kinukuha ung name ng patient
  def get_name(self):
    return self.name
  # sets the name for the patient
  def set_name(self):
    self.name=name
  # gets the bill amount
  def get_bill_amount(self):
    return self.bill_amount
  # sets the bill amount
  def set_bill_amount(self):
    self.bill_amount=bill_amount
  # default bill for the regular patient
  def calculate_bill(self):
    return self.bill_amount
  # default patient type
  def display_patient_type(self):
    print("Patient Type: Regular Patient")
# child class para sa senior citizen
class SeniorPatient(Patient):
  # since may 20% na discount(100-20=80), therefore imumultiply sa 0.80 ung original bill amount
  def calculate_bill(self):
    return self.bill_amount*0.80
  #ung patient type naging senior citizen na
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")
# child class para sa PhilHealth member
class PhilhealthPatient(Patient):
  # since may 15% na discount(100-15=85), there imumultiply sa 0.75 ung original bill amount
  def calculate_bill(self):
    return self.bill_amount*0.85
  # the patient type changes
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")
# creates the objects for each patient
regular= Patient("Juan Dela Cruz", 15000)
senior= SeniorPatient("Maria Santos", 15000)
philhealth= PhilhealthPatient("Pedro Reyes", 15000)
# puts the patients in one list
patients= [regular,senior,philhealth]
#formats the code
print("Hospital Billing System")
print("----------------------")
# pinapakita ung information ng bawat patient isa-isa
for patient in patients:
  print("Patient Name:", patient.get_name())
  patient.display_patient_type()
  print("Original Bill: P15,000.00")
  print("Final Bill: P{:,.2f}".format(patient.calculate_bill()))
  print()
