import pandas as pd
import faker as Fakerr
import random
import os
from datetime import datetime, timedelta

fake = Fakerr.Faker()

num_rows = 60
supervisor_probability = 0.2  # Adjust as needed

# Create list of employee codes
employee_codes = [f"E{str(i + 1).zfill(3)}" for i in range(num_rows)]

data = {
    "First Name": [fake.first_name() for _ in range(num_rows)],
    "Last Name": [fake.last_name() for _ in range(num_rows)],
    "Emp Code": employee_codes,
    "Designation": [
        random.choice(["Manager", "Analyst", "Software Developer", "HR", "Sales"])
        for _ in range(num_rows)
    ],
    "Date_of_joining": [
        (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
        for _ in range(num_rows)
    ],
    "Salary": [round(random.uniform(50000, 800000), 2) for _ in range(num_rows)],
    "Supervisor": [
        (
            random.choice(employee_codes)
            if random.random() > supervisor_probability
            else None
        )
        for _ in range(num_rows)
    ],
}

df = pd.DataFrame(data)
df.sort_values(by="Emp Code", inplace=True)  # Sort DataFrame by "Emp Code"
df.set_index("Emp Code", inplace=True)  # Set 'Emp Code' as the primary key

input_dir = "input"
op_file_path = os.path.join(input_dir, "employee_data.xlsx")
os.makedirs(input_dir, exist_ok=True)
df.to_excel(op_file_path)
print(f"Excel file {op_file_path} created successfully")

# openpyxl: could have been used as a 2nd option, as it gives control over data
# but is not as simple as pandas because here we have to do low level manipulation also(complex)
# pandas is flexible with data analysis and it is also simple and easy to integrate
