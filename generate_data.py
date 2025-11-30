import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

BRANCHES = ['Delhi', 'Bangalore', 'Mumbai', 'Pune']
DEPARTMENTS = ['General Consultation', 'Diagnostics', 'Surgery', 'Follow-Up']
STATUS = ['Completed', 'Cancelled', 'No-Show']
DOCTORS = ['D101', 'D205', 'D120', 'D330', 'D404']
BOOKING_TYPES = ['Online', 'Offline']

def generate_dataset(num_records=500):
    data = []
    start_date = datetime(2025, 6, 1) 
    # Matches report date range 
    
    for i in range(num_records):
        # random date within 45 days
        date = start_date + timedelta(days=random.randint(0, 45), hours=random.randint(9, 19), minutes=random.choice([0, 15, 30, 45]))
        
        dept = random.choices(DEPARTMENTS, weights=[0.4, 0.2, 0.1, 0.3])[0]
        status = random.choices(STATUS, weights=[0.7, 0.2, 0.1])[0] # Mostly completed
        
        #  Cancelled/No-show has 0 duration and 0 billing usually
        if status == 'Completed':
            duration = random.randint(15, 60)
            bill = random.randint(500, 5000)
        else:
            duration = 0
            bill = 0

        record = {
            'Patient_ID': f'P{str(i+1).zfill(3)}',
            'Appointment_Date': date.strftime('%Y-%m-%d %H:%M'),
            'Branch': random.choice(BRANCHES),
            'Department': dept,
            'Doctor_ID': random.choice(DOCTORS),
            'Visit_Status': status,
            'Consultation_Duration': duration,
            'Billing_Amount': bill,
            'Booking_Type': random.choice(BOOKING_TYPES)
        }
        data.append(record)

    df = pd.DataFrame(data)
    
    df.loc[10:15, 'Billing_Amount'] = -100 # Negative billing outlier
    df.loc[20:22, 'Visit_Status'] = np.nan # Missing values
    
    df.to_csv('appointments.csv', index=False)
    print("Dataset 'appointments.csv' generated successfully.")

if __name__ == "__main__":
    generate_dataset()