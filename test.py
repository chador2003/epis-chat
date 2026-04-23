import requests
import json
import time

# The endpoint and headers
url = "http://aichat.thimphutechpark.bt/chat"
headers = {"Content-Type": "application/json"}

# The list of questions extracted from your FAQ
questions = [
    "How to login to EPIS?",
    "How to access Dialysis Dashboard?",
    "How to search a patient in Dialysis?",
    "How to filter dialysis records?",
    "How to set default filters?",
    "How to schedule a dialysis session?",
    "How to reschedule a dialysis session?",
    "How to view doctor remarks and order request?",
    "How to generate visit for OPD patient?",
    "How to check visit number?",
    "How to fill Dialysis Assessment?",
    "How to view patient details?",
    "How to complete dialysis session?",
    "Why can’t I see dialysis data?",
    "How to create and manage route type?",
    "How to Create Route of Administration?",
    "How to Create a New Drug in Item Catalogue?",
    "How to Update or Delete an Item in Catalogue?",
    "What is Pending Dispense List and How to Use It?",
    "How to Dispense Medicines?",
    "How to View Dispensed Medicines?",
    "What is Named Patient Drug? (NPD)",
    "How to Create Named Patient Requisition?",
    "How to Approve or Reject Named Patient Drug?",
    "What is HTC Approval?",
    "How to Create ADR (Adverse Drug Reaction) Request?",
    "How to Add Stock (Stock Inward)?",
    "Why is my medicine not showing in the system?",
    "Why am I unable to dispense medicine?",
    "How to Access the Grievance Module in EPIS?",
    "How to register a new grievance complaint?",
    "How to Upload Supporting Documents in Grievance Registration?",
    "How to View Registered Grievances?",
    "How to View Details of a Grievance Complaint?",
    "How to set the priority of a grievance?",
    "How to Provide Feedback on a Grievance?",
    "How to Generate a Grievance Summary Report?",
    "How to reopen a grievance complaint?",
    "Why is my grievance not showing in the dashboard?",
    "How to Access the Audiology Module in EPIS?",
    "How do I log into Doctor Desk?",
    "Why can’t I access doctor desk after login?",
    "How do I filter patients in doctor dashboard?",
    "Why can’t I access ER IP and ER OP?",
    "Why are no OPD patients visible in my dashboard?",
    "How do I view patient record/demography (EMR)?",
    "How to enter patient vitals and view vitals trend?",
    "How to add complaints?",
    "Why is IPD Doctor Dashboard blank?",
    "Why is ward not visible in IPD?",
    "How to change admitting doctor to another doctor?",
    "How do I check Doctor availability?",
    "Why are appointments not visible?",
    "Why don’t I have access to register patient?",
    "Why is patient not appearing after registration?",
    "How do I refer a patient?",
    "How to add diagnosis?",
    "What if diagnosis is not available?",
    "How to order lab/radiology tests?",
    "Can I schedule orders for later?",
    "How to prescribe medicine?",
    "What can I do in the IPD module?",
    "How do I admit a patient from OPD referral?",
    "How do I admit a patient from Emergency?",
    "How do I directly admit a patient without referral?",
    "How do I access the Nursing Dashboard?",
    "Why can’t I see a patient in the nursing dashboard?",
    "How do I assign a bed to a patient?",
    "How do I view or complete ordered services?",
    "Can nurses order services?",
    "How do I record Treatments to be given (Prescription)?",
    "How do I order investigations?",
    "How do I register a newborn baby?",
    "When can birth registration be done?",
    "How do I transfer a patient to another bed?",
    "Can I change only the doctor without changing department?",
    "How do I transfer a patient to another department?",
    "How do I discharge a patient as a nurse?",
    "When can a nurse deallocate bed?",
    "What if doctor has not completed discharge summary?",
    "How does a doctor discharge a patient?",
    "How can I search a patient in IPD?",
    "What is 'Planned Discharge'?",
    "How do I log in to the Emergency (EMS) system?",
    "How do I register a patient in Pre-Hospital Care?",
    "What details are required under Incident Information?",
    "What times need to be recorded?",
    "How do I write case summary?",
    "What should be filled under Assessment and Intervention?",
    "How do I access Emergency Registration?",
    "How do I find a patient registered from Pre-Hospital Care?",
    "How do I allocate a bed to a patient?",
    "Why can’t I see some beds?",
    "How do I generate blood bag barcode labels?",
    "How do I print blood bag labels?",
    "How do I register a donor?",
    "What happens after donor registration?",
    "How do I perform donor checkup?",
    "How do I report adverse donor reactions?",
    "How do I perform blood group serology?",
    "How do I use Blood Testing Register?",
    "What happens after blood testing?",
    "How do I perform component separation?",
    "When can component separation be done?",
    "What should be done with leftover or expired blood?",
    "How do I manage blood stock?",
    "How do I raise a blood request?",
    "Is sample dispatch mandatory after blood request?",
    "How do I perform recipient sample testing?",
    "What happens after sample testing?",
    "How do I perform cross match?",
    "How do I issue blood?",
    "How do I perform blood transfusion?",
    "What if a reaction occurs during transfusion?",
    "How to Access the EPIS Website?",
    "What is the Reception Dashboard?",
    "What are the Modules Available in Reception?",
    "Why Are These Modules Included Under Reception?",
    "Which fields are mandatory to be filled up?",
    "How can I quickly pull up a patient's details if they only have their CID?",
    "How do I register a patient who was sent here from another hospital or clinic?",
    "What is mean by Teleconsultation",
    "How do I register a patient for a 'Teleconsultation' visit?",
    "How do I mark a patient who needs to see the doctor urgently?",
    "What should I do if I realize I entered the wrong information before saving?",
    "How do I handle a registration during 'Off-Hours' vs 'Day-Hours'?",
    "How do I register a mother and child for the MCH clinic?",
    "What documents must I bring to the registration counter to get registered?",
    "I have visited this hospital before; do I need to fill out all my details again?",
    "How do I get my UHID (Unique Health Identification) number?",
    "Can I register a family member who is too sick to come to the counter?",
    "How do I know which department or doctor I should register for?",
    "How can I make sure the patient's contact details are correct for follow-up calls?",
    "How do I see if a patient has been marked as a 'Priority' case by the registration desk?",
    "What is UHID No and how is it different from CID?",
    "What if the patient doesn't have a CID? Which 'Document Type' should I select?",
    "How do I select Patient Category? What options are available?",
    "How do I enter Present Address and Permanent Address?",
    "How do I find a specific Village or Zone if it’s not in the dropdown list?",
    "Are 'Mobile No' and 'Emergency Contact No' both mandatory?",
    "When should I check the 'Is Teleconsultation' box?",
    "What is the difference between 'New' and 'Follow-up' in Case Type?",
    "After I click 'Save,' how do I know it was successful?" "How to search for an Audiology service in the system?",
    "How to open the Audiology test report form?",
    "How to enter Audiology test results?",
    "How to enter charting data for an Audiometry Test?",
    "How to save the Audiology test report?",
    "How to print the Audiology test report?",
    "How to reopen the charting page for a patient?",
    "Why is the Audiogram graph not appearing?",
    "Why am I unable to save the Audiology report?",
    "How to advise Physiotherapy service for a patient?",
    "What is the Physiotherapy Dashboard in EPIS?",
    "How to schedule physiotherapy service sessions?",
    "How to reschedule or cancel a physiotherapy session?",
    "How to fill consent for physiotherapy services?",
    "How to fill a physiotherapy session report?",
    "How to dispatch assistive devices to a patient?",
    "How to collect deposit for assistive devices?",
    "How to refund the deposit amount for assistive devices?",
    "How to discontinue physiotherapy services?",
    "Why is the Physiotherapy session not showing on the Dashboard?",
    "Why am I unable to schedule a Physiotherap?"
]

# Open the file to save results
with open("qa_results.txt", "w", encoding="utf-8") as f:
    for i, q in enumerate(questions):
      print(f"Testing Question {i+1}/{len(questions)}: {q}")
      payload = {"query": q}
      
      try:
          # Use stream=True to keep the connection open
          response = requests.post(url, json=payload, stream=True, timeout=60)
          
          if response.status_code == 200:
              full_answer = ""
              # Iterate over the chunks of text as they come in
              for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                  if chunk:
                      full_answer += chunk
              answer = full_answer
          else:
              answer = f"ERROR: Status {response.status_code}"
              
      except Exception as e:
          answer = f"CONNECTION ERROR: {str(e)}"

      # Record in TXT
      with open("qa_results.txt", "a", encoding="utf-8") as f:
          f.write(f"QUESTION: {q}\n")
          f.write(f"ANSWER: {answer}\n")
          f.write("-" * 50 + "\n")

print("Finished! Results saved to qa_results.txt")