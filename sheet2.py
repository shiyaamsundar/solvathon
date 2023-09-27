import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('token.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet by title or URL
sheet = gc.open('Your Google Sheet Name')

# Select a worksheet within the Google Sheet
worksheet = sheet.worksheet('Sheet1')

# CRUD Operations

# 1. Create (Insert) Data
data_to_insert = ["New Data 1", "New Data 2", "New Data 3"]
worksheet.append_row(data_to_insert)

# 2. Read Data
values = worksheet.get_all_values()
for row in values:
    print(row)

# 3. Update Data
# Suppose you want to update a cell in row 2, column 3 (B2)
worksheet.update_cell(2, 3, "Updated Data")

# 4. Delete Data
# Suppose you want to delete the entire row 3
worksheet.delete_row(3)
