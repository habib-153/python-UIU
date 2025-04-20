import json
import pandas as pd
import os

# Get directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'response.json')

# Open using the constructed path
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract relevant information
registrations = []

for entry in data.get('data', []):
    # Skip empty entries
    if not entry or 'PaymentTransactionID' not in entry:
        continue

    registrations.append({
        'FullName': entry.get('FullName', ''),
        'Email': entry.get('Email', ''),
        'PhoneNumber': entry.get('PhoneNumber', ''),
        'Department': entry.get('Department', ''),
        'University': entry.get('EventSpecificData', {}).get('university', ''),
        'PersonalEmail': entry.get('EventSpecificData', {}).get('personalEmail', ''),
        'TransactionID': entry.get('PaymentTransactionID', ''),
        'PaymentMethod': entry.get('PaymentMethod', ''),
        'PaymentAmount': entry.get('PaymentAmount', 0),
        'PaymentStatus': entry.get('PaymentStatus', '')
    })

# Create a DataFrame and export to Excel
if registrations:
    df = pd.DataFrame(registrations)

    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)

    # Export to Excel
    excel_path = './DSC_Event.xlsx'
    df.to_excel(excel_path, index=False)
    print(f"Data exported successfully to {excel_path}")
else:
    print("No valid registration data found.")
