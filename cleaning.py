# importing necessary libraries
import pandas as pd
from datetime import datetime
import numpy as np
#--------------------------------------------------------------#
allergies = pd.read_csv("synthea/allergies.csv")
# STOP column is emtpy, so we can drop it
allergies.drop(columns=['STOP'], inplace=True)
# transform START column to datetime
allergies['START'] = pd.to_datetime(allergies['START']).dt.date
# drop rows where DESCRIPTION1, DESCRIPTION2, REACTION1, and REACTION2 are all null since they are not useful
allergies = allergies.dropna(subset=['DESCRIPTION1', 'DESCRIPTION2', 'REACTION1', 'REACTION2'], how='all')
# replace the null values in SEVERITY1 and SEVERITY2 with 'NEGLIGIBLE', the values in DESCRIPTION1 and DESCRIPTION2 with 'No reaction', and the values in REACTION1 and REACTION2 with 260385009 which is the SNOMED CT code for no reaction
allergies['SEVERITY2'] = allergies['SEVERITY2'].fillna('NEGLIGIBLE')
allergies['SEVERITY1'] = allergies['SEVERITY1'].fillna('NEGLIGIBLE')
allergies['REACTION2'] = allergies['REACTION2'].fillna('NONE')
allergies['DESCRIPTION2'] = allergies['DESCRIPTION2'].fillna('None')
# transform some columns into categories
allergies['SYSTEM'].astype('category')
allergies['TYPE'].astype('category')
allergies['DESCRIPTION1'].astype('category')
allergies['DESCRIPTION2'].astype('category')
allergies['REACTION1'].astype('category')
allergies['REACTION2'].astype('category')
allergies['CATEGORY'].astype('category')
allergies['SEVERITY1'].astype('category')
allergies['SEVERITY2'].astype('category')
#--------------------------------------------------------------#
careplans = pd.read_csv("synthea/careplans.csv")
# replace the null values in STOP with the current date
careplans['STOP'] = careplans['STOP'].fillna(datetime.now().date())
# drop rows where REASONCODE or REASONDESCRIPTION are null
careplans = careplans.dropna(subset=['REASONCODE', 'REASONDESCRIPTION'])
#--------------------------------------------------------------#
claims = pd.read_csv("synthea/claims.csv")
# drop DIAGNOSIS5, DIAGNOSIS6, DIAGNOSIS7, DIAGNOSIS8, REFERRINGPROVIDERID, SECONDARYPATIENTINSURANCEID, OUTSTANDING1, OUTSTANDING2, OUTSTANDINGP because they are mostly null and STATUS1, STATUS2, and STATUSP columns because they are identical to each other and not useful for analysis
claims.drop(columns=['DIAGNOSIS5', 'DIAGNOSIS6', 'DIAGNOSIS7', 'DIAGNOSIS8', 'REFERRINGPROVIDERID', 'SECONDARYPATIENTINSURANCEID', 'OUTSTANDING1', 'OUTSTANDING2', 'OUTSTANDINGP', 'STATUS1', 'STATUS2', 'STATUSP'], inplace=True)
# drop rows where LASTBILLEDDATE1, LASTBILLEDDATE2, or LASTBILLEDDATEP are null and transform them to datetime
claims = claims.dropna(subset=['LASTBILLEDDATE1', 'LASTBILLEDDATE2', 'LASTBILLEDDATEP'])
claims['LASTBILLEDDATE1'] = pd.to_datetime(claims['LASTBILLEDDATE1']).dt.date
claims['LASTBILLEDDATE2'] = pd.to_datetime(claims['LASTBILLEDDATE2']).dt.date
claims['LASTBILLEDDATEP'] = pd.to_datetime(claims['LASTBILLEDDATEP']).dt.date
# transfom CURRENTILLNESSDATE and SERVICEDATE to datetime
claims['CURRENTILLNESSDATE'] = pd.to_datetime(claims['CURRENTILLNESSDATE']).dt.date
claims['SERVICEDATE'] = pd.to_datetime(claims['SERVICEDATE']).dt.date
# categorize some columns
claims['DEPARTMENTID'].astype('category')
claims['PATIENTDEPARTMENTID'].astype('category')
claims['SUPERVISINGPROVIDERID'].astype('category')
claims['HEALTHCARECLAIMTYPEID2'].astype('category')
claims['HEALTHCARECLAIMTYPEID1'].astype('category')
#--------------------------------------------------------------#
claims_transactions = pd.read_csv("synthea/claims_transactions.csv")
# drop rows where AMOUNT, TRANSFERTYPE are null
claims_transactions = claims_transactions.dropna(subset=['AMOUNT', 'TRANSFERTYPE'])
# replace the null values in TRANSFERS with 0
claims_transactions['TRANSFERS'] = claims_transactions['TRANSFERS'].fillna(0)
# drop METHOD, MODIFIER1, MODIFIER2, LINENOTE, FEESCHEDULEID, CHARGEID, and TRANSFEROUTID columns because they are mostly null and not useful for analysis
claims_transactions.drop(columns=['METHOD', 'MODIFIER1', 'MODIFIER2', 'LINENOTE', 'FEESCHEDULEID', 'CHARGEID', 'TRANSFEROUTID', 'UNITS'], inplace=True)
# transform FROMDATE and TODATE to datetime
claims_transactions['FROMDATE'] = pd.to_datetime(claims_transactions['FROMDATE']).dt.date
claims_transactions['TODATE'] = pd.to_datetime(claims_transactions['TODATE']).dt.date
# replace null values in DIAGNOSISREF1, DIAGNOSISREF2, DIAGNOSISREF3, and DIAGONSISREF4 with False and non-null values with True
claims_transactions['DIAGNOSISREF1'] = np.where(claims_transactions['DIAGNOSISREF1'].notnull(), True, False)
claims_transactions['DIAGNOSISREF2'] = np.where(claims_transactions['DIAGNOSISREF2'].notnull(), True, False)
claims_transactions['DIAGNOSISREF3'] = np.where(claims_transactions['DIAGNOSISREF3'].notnull(), True, False)
claims_transactions['DIAGNOSISREF4'] = np.where(claims_transactions['DIAGNOSISREF4'].notnull(), True, False)
# categorize some columns
claims_transactions['TYPE'].astype('category')
claims_transactions['TRANSFERTYPE'].astype('category')
claims_transactions['DIAGNOSISREF1'].astype('category')
claims_transactions['DIAGNOSISREF2'].astype('category')
claims_transactions['DIAGNOSISREF3'].astype('category')
claims_transactions['DIAGNOSISREF4'].astype('category')
claims_transactions['DEPARTMENTID'].astype('category')
#--------------------------------------------------------------#
conditions = pd.read_csv("synthea/conditions.csv")
#drop the system column because it has only one value which is a url for the SNOMED CT code
conditions.drop(columns=['SYSTEM'], inplace=True)
# change START and STOP columns to datetime
conditions['START'] = pd.to_datetime(conditions['START']).dt.date
conditions['STOP'] = pd.to_datetime(conditions['STOP']).dt.date
# replace the values in STOP with the current date if they are null
conditions = conditions.fillna(datetime.now().date())
# categorize some columns
conditions['DESCRIPTION'].astype('category')
#--------------------------------------------------------------#
devices = pd.read_csv("synthea/devices.csv")
#change START and STOP columns to datetime
devices['START'] = pd.to_datetime(devices['START']).dt.date
devices['STOP'] = pd.to_datetime(devices['STOP']).dt.date
# replace the values in STOP with the current date if they are null
devices = devices.fillna(datetime.now().date())
#--------------------------------------------------------------#
encounters = pd.read_csv("synthea/encounters.csv")
# change START and STOP clumns to datetime
encounters['START'] = pd.to_datetime(encounters['START']).dt.date
encounters['STOP'] = pd.to_datetime(encounters['STOP']).dt.date
# drop rows where REASONCODE or REASONDESCRIPTION are null
encounters = encounters.dropna(subset=['REASONCODE', 'REASONDESCRIPTION'], how='all')
# categorize some columns
encounters['ENCOUNTERCLASS'].astype('category')
encounters['DESCRIPTION'].astype('category')
encounters['REASONDESCRIPTION'].astype('category')
#--------------------------------------------------------------#
imaging_studies = pd.read_csv("synthea/imaging_studies.csv")
# change DATE column to datetime
imaging_studies['DATE'] = pd.to_datetime(imaging_studies['DATE']).dt.date
# categorize some columns
imaging_studies['SOP_CODE'].astype('category')
imaging_studies['SOP_DESCRIPTION'].astype('category')
imaging_studies['BODYSITE_CODE'].astype('category')
imaging_studies['BODYSITE_DESCRIPTION'].astype('category')
imaging_studies['MODALITY_CODE'].astype('category')
imaging_studies['MODALITY_DESCRIPTION'].astype('category')
imaging_studies['PROCEDURE_CODE'].astype('category')
#--------------------------------------------------------------#
immunizations = pd.read_csv("synthea/immunizations.csv")
# change DATE column to datetime
immunizations['DATE'] = pd.to_datetime(immunizations['DATE']).dt.date
# cateogrize some columnd
immunizations['CODE'].astype('category')
immunizations['DESCRIPTION'].astype('category')
#--------------------------------------------------------------#
medications = pd.read_csv("synthea/medications.csv")
# change START and STOP columns to datetime
medications['START'] = pd.to_datetime(medications['START']).dt.date
medications['STOP'] = pd.to_datetime(medications['STOP']).dt.date
# replace the values in STOP with the current date if they are null
medications['STOP'] = medications['STOP'].fillna(datetime.now().date())
# drop rows where REASONCODE and REASONDESCRIPTION are null
medications = medications.dropna(subset=['REASONCODE', 'REASONDESCRIPTION'], how='all')
# categorize some columns
medications['CODE'].astype('category')
medications['DESCRIPTION'].astype('category')
medications['REASONCODE'].astype('category')
medications['REASONDESCRIPTION'].astype('category')
#--------------------------------------------------------------#
observations = pd.read_csv("synthea/observations.csv")
#change DATE column to datetime
observations['DATE'] = pd.to_datetime(observations['DATE']).dt.date
#categorize some columns
observations['CATEGORY'].astype('category')
observations['CODE'].astype('category')
observations['DESCRIPTION'].astype('category')
observations['TYPE'].astype('category')
observations['UNITS'].astype('category')
#--------------------------------------------------------------#
organizations = pd.read_csv("synthea/organizations.csv")
# all values in REVENUE column are zero and the values in STATE column are the same, so we can drop them
organizations.drop(columns=['REVENUE', 'STATE'], inplace=True)
#--------------------------------------------------------------#
patients = pd.read_csv("synthea/patients.csv")
# drop SUFFIX and MAIDEN columns because they are mostly null, FIPS and DEATHDATE columns because they are not useful, and STATE columns because it only contains Massauchets as a value
patients.drop(columns=['SUFFIX', 'MAIDEN', 'FIPS', 'STATE', 'DEATHDATE'], inplace=True)
# replace the null values in MARITAL with U standing for unknown
patients['MARITAL'] = patients['MARITAL'].fillna('U')
#--------------------------------------------------------------#
payer_transitions = pd.read_csv("synthea/payer_transitions.csv")
# reaplce the null values in PLAN_OWNERSHIP, OWNER_NAME, and SECONDARY_PAYER
payer_transitions['PLAN_OWNERSHIP'] = payer_transitions['PLAN_OWNERSHIP'].fillna('Uninsured')
payer_transitions['OWNER_NAME'] = payer_transitions['OWNER_NAME'].fillna('None')
payer_transitions['SECONDARY_PAYER'] = payer_transitions['SECONDARY_PAYER'].fillna('None')
# change START_DATE and END_DATE to datetime and clean the output
payer_transitions['START_DATE'] = pd.to_datetime(payer_transitions['START_DATE']).dt.date
payer_transitions['END_DATE'] = pd.to_datetime(payer_transitions['END_DATE'], errors='coerce').dt.date
payer_transitions = payer_transitions.dropna(subset=['END_DATE'])
# drop MEMBERID because it is not useful
payer_transitions.drop(columns=['MEMBERID'], inplace=True)
# categorize some columns
payer_transitions['SECONDARY_PAYER'].astype('category')
payer_transitions['PLAN_OWNERSHIP'].astype('category')
payer_transitions['OWNER_NAME'].astype('category')
#--------------------------------------------------------------#
payers = pd.read_csv("synthea/payers.csv")
# drop the ADDRESS, CITY, STATE_HEADQUARTERED, ZIP, and PHONE columns because they are empty
payers.drop(columns=['ADDRESS', 'CITY', 'STATE_HEADQUARTERED', 'ZIP', 'PHONE'], inplace=True)
# categorize some columns
payers['OWNERSHIP'].astype('category')
#--------------------------------------------------------------#
procedures = pd.read_csv("synthea/procedures.csv")
#change START and STOP to datetime
procedures['START'] = pd.to_datetime(procedures['START']).dt.date
procedures['STOP'] = pd.to_datetime(procedures['STOP']).dt.date
# drop SYSTEM column because it has the same value and is not useful for analysis
procedures.drop(columns=['SYSTEM'], inplace=True)
# replace the null values in REASONCODE and REASON DESCRIPTION with Unknown
procedures['REASONCODE'] = procedures['REASONCODE'].fillna('Unknown')
procedures['REASONDESCRIPTION'] = procedures['REASONDESCRIPTION'].fillna('Unknown')
#--------------------------------------------------------------#
providers = pd.read_csv("synthea/providers.csv")
# remove SPECIALITY, PRCOEDURES, and STATE columns which all contain repeted values
providers.drop(columns=['SPECIALITY', 'PROCEDURES', 'STATE'], inplace=True)
# categorize some columns
providers['GENDER'].astype('category')
#--------------------------------------------------------------#
supplies = pd.read_csv("synthea/supplies.csv")
# change the DATE column to datetime
supplies['DATE'] = pd.to_datetime(supplies['DATE']).dt.date
#--------------------------------------------------------------#
# export the final versions as csv files
allergies.to_csv('allergies.csv')
careplans.to_csv('careplans.csv')
claims_transactions.to_csv('claims_transactions.csv')
claims.to_csv('claims.csv')
conditions.to_csv('conditions.csv')
devices.to_csv('devices.csv')
encounters.to_csv('encounters.csv')
imaging_studies.to_csv('imaging_studies.csv')
immunizations.to_csv('immunizations.csv')
medications.to_csv('medications.csv')
observations.to_csv('observations.csv')
organizations.to_csv('organizations.csv')
patients.to_csv('patients.csv')
payer_transitions.to_csv('payer_transitions.csv')
payers.to_csv('payers.csv')
procedures.to_csv('procedures.csv')
providers.to_csv('providers.csv')
supplies.to_csv('supplies.csv')
