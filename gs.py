import gspread

# Load credentials from the service account JSON file
gc = gspread.service_account(filename='service.json')

# Open the Google Sheet by its key
worksheet = gc.open_by_key('1DXihUqkbZC8568xN_MjOSQqW9KRvPGmjlYCNVeOASGk')
worksheet_name = 'Sheet1'  # Replace with the name of your worksheet
worksheet = worksheet.worksheet(worksheet_name)

# Update the data in the sheet
cell_to_update = 'A2'  # Replace with the cell you want to update
new_value = 'BSongi Sriiiiiiiiiiiiiiiiiiiiiiiiiiiii'  # Replace with the new value
worksheet.update(cell_to_update, new_value)

all_values = worksheet.get_all_values()

# Extract headers (assuming they are in the first row)
headers = all_values[0]

# Print the retrieved headers
print("Headers:")
for header in headers:
    print(header)

data = worksheet.get_all_records()

print(data)

# Print the retrieved data
for row in data:
    print(row)