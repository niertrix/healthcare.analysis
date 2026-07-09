## Project Summary

This project is aimed at hospitals and medical institutions. It aims to provide a comprehensive and straightforward way to summarise and analyse the records of medical institutions, including details like patient information, medicine availability, and staff shifts.

## Table of Contents

1. [Project Objectives](#project-objectives)
2. [Dataset Overview](#dataset-overview)
3. [Technologies and Tools](#technologies-and-tools)
4. [Methodology](#methodology)
5. [KPIs & Measures](#kpis-and-measures)
6. [Project Timeline & Milestones](#project-timeline--milestones)
7. [Deliverables](#deliverables)
8. [Roles & Responsibilites](#roles-and-responsibilities)
9. [Contact Information](#contact-information)

## Project Objectives

- Analyse the number and frequency of patients visitng medical institutions.
- Determine the most common types of cases based on trends in data
- Create a comprehensive dashboard to visually represent the collected data

## Dataset Overview

- **Source**: [SyntheticMass Dataset](https://synthea.mitre.org/downloads)

 
- **Volume**:

| Table | Size |
|------|-------|
| allergies | 15 columns, 136 rows |
| careplans | 9 columns, 401 rows |
| claims | 31 columns, 14,176 rows |
| claims_transactions | 33 columns, 121,448 rows |
| conditions | 7 columns, 4,023 rows |
| devices | 7 columns, 622 rows |
| encounters | 15 columns, 8,316 rows |
| imaging_studies | 13 columns, 72,757 rows |
| immunizations | 6 columns, 1,619 rows |
| medications | 13 columns, 5,860 rows |
| observations | 9 colummns, 86,634 rows |
| organizations | 11 columns, 274 rows |
| patients | 28 columns, 117 rows |
| payer_transitions | 8 columns, 4,811 rows |
| payers | 22 columns, 10 rows |
| procedure | 10 columns, 20,322 rows |
| providers | 13 columns, 274 rows |
| supplies | 6 columns, 2,918 rows |

## Technologies and Tools

| Task | Tools |
|-------------------------|---------------|
| Data Cleaning | Python(pandas, numpy) |
| Data Manipulation | Python, Power Query |
| Visualisation | Power BI |
| Version Control | Github |

## Methodology

1. Clean the collected data and build a data model using it.
2. Analyse the data model and create the needed measures.
3. Visualize the data using Power BI.

## KPIs and Measures

Due to the dataset's large size and interconnected nature we were able to calculate a variety of measures which we grouped into a number of categories for easier navigation.
<table>
<tr>
<td valign=top>
 
| Patients & Demographics |
| ----------------------- |
| Total Patients |
| Average Income |
| Total Patient Cities |
| Unique Patients Visited |
| Unique Patients Observed |
| Total Healthcare Expenses |
| Average Health Coverage |
| Unique Patients Imaged |
| Unique Patients with Claims |
| Unique Patients with Conditions |
| Total Patients with Transitions |
</td>

<td valign=top>

| Providers & Organizations |
| ------------------------- |
| Total Providers |
| Total Provider Encounters |
| Total Cities Covered |
| Male Encounters |
| Female Encounters |
| Average Provider Encounters |
| Total Organizations |
| Total Cities |
| Total Utilization |
| Avg Utilization |
| Max Utilization |
| Unique Providers |
 
</td>

<td valign=top>
 
| Payers & Covreage |
| ----------------- |
| Total Revenue |
| Total Payers Count |
| Total Amount Covered |
| Total Amount Uncovered |
| Total Uncovered Expenses |
| Total Covered Encounters |
| Total Covered Medications |
| Total Unique Customers |
| Total Transitions |
| Active Transitions |
| Self Paid Transitions |
| Transitions This Year |
| Patients with Multiple Transitions |
| Avg Coverage Duration (Days) |
| Uninsured Rate |

</td>
</tr>
</table>

<table>
<tr>
<td valign=top>
 
| Clinical & Diagnosis |
|----------------------|
| Total Encounters |
| Avg Cost Per Encounter |
| Avg Encounter Duration in Minutes |
| Emergency Encounters |
| Insurance Coverage Rate |
| Total Base Cost |
| Total Insurance Covered |
| Total Out-of-Pocket Cost |
| Total Conditions |
| Active Conditions |
| Total Unique Diseases |
| Avg Conditions Per Encounter |
| Avg Conditions Per Patient |
| Total Encounters with Conditions |
| Total Procedures |
| Total Procedure Cost |
| Average Cost per Procedure |
| Avg Procedures per Patient |
| Total Unique Patients |
| Procedures Cost LY |
| Total Observations Count |
| Vital Signs Observations |
| Laboratory Observations |
| Laboratory Observations Percentage |
| Avg Systolic New |
| Avg Diastolic New |
| Average Body Weight |
| Total Allergies |
| Unique Patients with Allergies |
| Allergy Density |
| Average BMI New |
| Total Imaging Studies |
| Avg Studies Per Patient |
| CT Scans Count |
| CT Scan Rate |
| Thoracic Imaging Count |
| Modality Contribution |
| Severe Allergies Count |
| Severe Allergies Rate |
| Moderate Allergies Count |
| Current Month Allergies |
| Allergies Previous Month |
 
</td>

<td valign=top>
 
| Financial & Costs |
| ----------------- |
| Number of Transactions |
| Transactions Sum |
| Transfers Sum |
| Total Immunization Base Cost |
| Average Immunization Base Cost |
| Total Dispenses |
| Total Medications Cost |
| Average Cost Per Medication |
| Total Payer Coverage |
| Medication Insurance Coverage Rate |
| Out-of-Pocket Rate |
| Total Claims Count |
| Insured Claims Count |
| Insurance Coverage Claims Rate |
| Claims Distribution |
| Total Supplies |
| Total Supply Records |

</td>
</tr>
</table>

## Project Timeline & Milestones

| Key Activities | Duration |
|----------|---------|
| Building Data Model, Data Cleaning, and Preprocessing | 4 Days |
| Data Analysis | 1 Week |
| Visualization Dashboard and Final Presentation | 1 Week | 

## Deliverables

- Full analysis of the dataset.
- Visualization Dashboard in Power BI.

## Roles & Responsibilites
| Member | Role |
|-------|---------|
| Abdulrahman Waheed | Data Cleaning |
| Hoda Elkady | Data Modeling |
| Abdulrahman Hisham | Visualization Wizard |
| Mohammad Abdulhakim | Data Curator |

## Contact Information

| Memeber | Linkedin profile|
|-----------|---------|
| Abdulrahman Waheed | https://www.linkedin.com/in/abdulrahman-waheed|
| Hoda Elkady | https://www.linkedin.com/in/hoda-elkady-6b80a4361|
| Abdulrahman Hisham | https://www.linkedin.com/in/abdulrahman-hisham-b0a55539b|
| Mohammad Abdulhakim | https://www.linkedin.com/in/mohamed-hantour-923925388|
