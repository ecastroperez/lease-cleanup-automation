# Lease Cleanup Automation

This project automates the process of cleaning and analyzing lease data from Excel files.

## Features
- Cleans messy data (capitalizes names, strips whitespace, fixes dates)
- Calculates average rent and total leases
- Flags leases ending soon
- Saves cleaned Excel files

## Files
- `lease_report.py`: Main Python script
- `Lease_Information_Raw.xlsx`: Sample input file
- `leases_cleaned_final.xlsx`: Cleaned full data
- `leases_ending_soon_report.xlsx`: Filtered output

## How to Run

1. Install requirements:
   ```bash
   pip install pandas openpyxl
