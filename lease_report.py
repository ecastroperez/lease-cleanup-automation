import pandas as pd
from datetime import datetime, timedelta

def lease_report(file_path, alert_days=30):
    df = pd.read_excel(file_path)

    df["Tenant Name"] = df["Tenant Name"].astype(str).str.strip().str.title()
    df["Phone Number"] = df["Phone Number"].astype(str).str.strip()
    df["Rent"] = pd.to_numeric(df["Rent"], errors='coerce')
    df["Lease Start"] = pd.to_datetime(df["Lease Start"], errors='coerce')
    df["Lease End"] = pd.to_datetime(df["Lease End"], errors='coerce')

    avg_rent = df["Rent"].mean()
    total_leases = len(df)
    today = datetime.today()
    upcoming = df[df["Lease End"] <= today + timedelta(days=alert_days)]

    print(f"Average Rent: ${avg_rent:.2f}")
    print(f"Total Leases: {total_leases}")
    print(f"Active Leases: {len(df)}")
    print(f"Leases ending in the next {alert_days} days:")
    print(upcoming[["Tenant Name", "Lease End", "Phone Number"]])

    df.to_excel("leases_cleaned_final.xlsx", index=False)
    print("Full cleaned file saved as 'leases_cleaned_final.xlsx'")

    upcoming.to_excel("leases_ending_soon_report.xlsx", index=False)
    print("Filtered report saved as 'leases_ending_soon_report.xlsx'")

lease_report("Lease_Information_Raw.xlsx", alert_days=30)
