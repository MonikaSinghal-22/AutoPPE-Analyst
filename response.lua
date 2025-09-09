(.venv) PS C:\Users\Monika\Project\Safety> python main.py
user

    Process the csv data for PPE log analysis
    timestamp,worker_id,ppe_item,status,severity,location
    8/30/2025 15:52,W107,Face_Shield,Compliant,None,Yard
    8/28/2025 21:00,W101,Safety_Jacket,Non-Compliant,High,Yard
    8/28/2025 2:48,W104,Gloves,Compliant,None,Yard
    8/25/2025 15:18,W102,Mask,Compliant,None,Maintenance
    8/29/2025 0:28,W110,Helmet,Compliant,None,Meltshop
    8/30/2025 2:53,W104,Safety_Jacket,Compliant,None,Maintenance
    8/29/2025 14:30,W103,Helmet,Compliant,None,Meltshop
    8/27/2025 20:24,W103,Goggles,Compliant,None,Rolling
    8/25/2025 20:44,W110,Goggles,Non-Compliant,Low,Meltshop
    9/1/2025 2:42,W101,Gloves,Compliant,None,Meltshop
    8/30/2025 23:46,W100,Mask,Non-Compliant,Low,Meltshop
    8/30/2025 19:46,W100,Helmet,Compliant,None,Yard
    8/31/2025 18:21,W105,Helmet,Compliant,None,Yard
    9/1/2025 7:02,W107,Helmet,Non-Compliant,Medium,Meltshop
    8/29/2025 23:06,W110,Gloves,Non-Compliant,Low,Meltshop
    8/26/2025 11:28,W106,Mask,Non-Compliant,Medium,Meltshop
    8/26/2025 16:12,W100,Safety_Jacket,Compliant,None,Maintenance
    8/28/2025 3:29,W110,Safety_Jacket,Compliant,None,Yard
    8/31/2025 3:32,W110,Safety_Jacket,Non-Compliant,High,Yard
    8/29/2025 11:05,W107,Goggles,Non-Compliant,Low,Meltshop


###############################################
Data_Preparer_Agent
```json
{
  "source_file": "ppe_log_sample.csv",
  "total_entries": 20,
  "cleaned_entries": [
    {
      "timestamp": "2025-08-30T15:52:00",
      "worker_id": "W107",
      "ppe_item": "Face Shield",
      "status": "Compliant",
      "severity": "Low",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-28T21:00:00",
      "worker_id": "W101",
      "ppe_item": "Safety Jacket",
      "status": "Non-Compliant",
      "severity": "High",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-28T02:48:00",
      "worker_id": "W104",
      "ppe_item": "Gloves",
      "status": "Compliant",
      "severity": "Low",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-25T15:18:00",
      "worker_id": "W102",
      "ppe_item": "Mask",
      "status": "Compliant",
      "severity": "Low",
      "location": "Maintenance"
    },
    {
      "timestamp": "2025-08-29T00:28:00",
      "worker_id": "W110",
      "ppe_item": "Helmet",
      "status": "Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-30T02:53:00",
      "worker_id": "W104",
      "ppe_item": "Safety Jacket",
      "status": "Compliant",
      "severity": "Low",
      "location": "Maintenance"
    },
    {
      "timestamp": "2025-08-29T14:30:00",
      "worker_id": "W103",
      "ppe_item": "Helmet",
      "status": "Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-27T20:24:00",
      "worker_id": "W103",
      "ppe_item": "Goggles",
      "status": "Compliant",
      "severity": "Low",
      "location": "Rolling"
    },
    {
      "timestamp": "2025-08-25T20:44:00",
      "worker_id": "W110",
      "ppe_item": "Goggles",
      "status": "Non-Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-09-01T02:42:00",
      "worker_id": "W101",
      "ppe_item": "Gloves",
      "status": "Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-30T23:46:00",
      "worker_id": "W100",
      "ppe_item": "Mask",
      "status": "Non-Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-30T19:46:00",
      "worker_id": "W100",
      "ppe_item": "Helmet",
      "status": "Compliant",
      "severity": "Low",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-31T18:21:00",
      "worker_id": "W105",
      "ppe_item": "Helmet",
      "status": "Compliant",
      "severity": "Low",
      "location": "Yard"
    },
    {
      "timestamp": "2025-09-01T07:02:00",
      "worker_id": "W107",
      "ppe_item": "Helmet",
      "status": "Non-Compliant",
      "severity": "Medium",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-29T23:06:00",
      "worker_id": "W110",
      "ppe_item": "Gloves",
      "status": "Non-Compliant",
      "severity": "Low",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-26T11:28:00",
      "worker_id": "W106",
      "ppe_item": "Mask",
      "status": "Non-Compliant",
      "severity": "Medium",
      "location": "Meltshop"
    },
    {
      "timestamp": "2025-08-26T16:12:00",
      "worker_id": "W100",
      "ppe_item": "Safety Jacket",
      "status": "Compliant",
      "severity": "Low",
      "location": "Maintenance"
    },
    {
      "timestamp": "2025-08-28T03:29:00",
      "worker_id": "W110",
      "ppe_item": "Safety Jacket",
      "status": "Compliant",
      "severity": "Low",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-31T03:32:00",
      "worker_id": "W110",
      "ppe_item": "Safety Jacket",
      "status": "Non-Compliant",
      "severity": "High",
      "location": "Yard"
    },
    {
      "timestamp": "2025-08-29T11:05:00",
      "worker_id": "W107",
      "ppe_item": "Goggles",
      "status": "Non-Compliant",
      "severity": "Low",
      "location": "Meltshop"
    }
  ],
  "cleaning_notes": "Converted timestamps from 'M/D/YYYY H:MM' format to ISO 8601 (YYYY-MM-DDTHH:MM:SS). Normalized 'ppe_item' names by replacing underscores with spaces (e.g., 'Face_Shield' to 'Face Shield'). Standardized 'severity' by mapping 'None' to 'Low' for compliant entries to adhere to the required schema of 'Low', 'Medium', or 'High'. All 20 raw entries were successfully cleaned and included."  
}
```
###############################################
Analyst_Agent
```json
{
  "compliance_rate": 60.0,
  "non_compliance_counts": {
    "Safety Jacket": 2,
    "Goggles": 2,
    "Mask": 2,
    "Helmet": 1,
    "Gloves": 1
  },
  "high_risk_workers": [
    {
      "worker_id": "W110",
      "issue": "Multiple PPE non-compliance (Goggles, Gloves, Safety Jacket)",
      "count": 3,
      "severity": "High"
    },
    {
      "worker_id": "W107",
      "issue": "Multiple PPE non-compliance (Helmet, Goggles)",
      "count": 2,
      "severity": "Medium"
    }
  ],
  "time_trends": {
    "2025-08-25": 50.0,
    "2025-08-26": 50.0,
    "2025-08-27": 100.0,
    "2025-08-28": 66.67,
    "2025-08-29": 50.0,
    "2025-08-30": 75.0,
    "2025-08-31": 50.0,
    "2025-09-01": 50.0
  },
  "notes": "Overall compliance rate is 60%, falling below the 70% alert threshold. A significant compliance drop of over 20% was detected between 2025-08-27 (100%) and 2025-08-28 (66.67%). Worker W110 is the highest-risk individual with 3 violations, including one of high severity."
}
```
###############################################
Reporter_Agent
```json
{
  "title": "PPE Compliance Report - August 25 to September 1, 2025",
  "executive_summary": "This report summarizes Personal Protective Equipment (PPE) compliance from August 25 to September 1, 2025. The overall compliance rate was 60%, falling below the 70% safety threshold. A sharp decline in compliance was noted after August 27th. Worker W110 has been identified as a high-risk individual with multiple violations, including one of high severity. Targeted interventions are recommended for specific workers and a general review of safety protocols is advised.",
  "key_findings": [
    "The overall PPE compliance rate was 60%, which is below the acceptable 70% threshold.",
    "Worker W110 was the most frequent offender with three non-compliance events, including a high-severity violation related to a Safety Jacket.",
    "Worker W107 also showed a pattern of non-compliance with two recorded violations.",
    "Safety Jackets, Goggles, and Masks were the most common items involved in non-compliance incidents.",
    "A significant drop in daily compliance occurred, falling from 100% on August 27th to approximately 67% on August 28th, with rates remaining low for the rest of the period."
  ],
  "recommendations": [
    "Conduct immediate, targeted safety retraining with workers W110 and W107 to address their repeated non-compliance.",
    "Organize a safety stand-down for all teams to reinforce the critical importance of wearing all required PPE, with a specific focus on Safety Jackets, Goggles, and Masks.",
    "Investigate potential causes for the sharp drop in compliance after August 27th, such as changes in shift patterns, new tasks, or supervision.",
    "Increase the frequency of random spot-checks for PPE compliance across all locations, particularly in the Meltshop and Yard where most violations occurred."
  ],
  "visualizations": [
    "/reports/charts/compliance_over_time_09012025.png",
    "/reports/charts/noncompliance_by_worker_09012025.png"
  ],
  "approval_status": "Pending"
}
```
###############################################
