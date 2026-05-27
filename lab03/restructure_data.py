import pandas as pd

df = pd.read_csv('/home/ubuntu/meerachaddha.github.io/lab03/data/lightcast_job_postings.csv')

df[['ID','TITLE_RAW','TITLE_CLEAN','POSTED','EXPIRED','SALARY_FROM','SALARY_TO','MIN_YEARS_EXPERIENCE','MAX_YEARS_EXPERIENCE','SKILLS','SPECIALIZED_SKILLS','SOFTWARE_SKILLS','EMPLOYMENT_TYPE','COMPANY']].rename(columns={'COMPANY':'COMPANY_ID'}).to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/job_postings.csv', index=False)

df[['COMPANY','COMPANY_NAME','COMPANY_RAW','COMPANY_IS_STAFFING']].drop_duplicates().rename(columns={'COMPANY':'COMPANY_ID'}).to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/company.csv', index=False)

df[['ID','CITY','STATE','COUNTY','LOCATION']].to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/job_location.csv', index=False)

df[['ID','SOC_2','SOC_2_NAME','SOC_3','SOC_3_NAME','SOC_4','SOC_4_NAME','SOC_5','SOC_5_NAME']].to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/soc_details.csv', index=False)

df[['ID','LOT_CAREER_AREA','LOT_CAREER_AREA_NAME','LOT_OCCUPATION','LOT_OCCUPATION_NAME','LOT_SPECIALIZED_OCCUPATION','LOT_SPECIALIZED_OCCUPATION_NAME']].to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/lot_details.csv', index=False)

df[['ID','NAICS2','NAICS2_NAME','NAICS3','NAICS3_NAME','NAICS4','NAICS4_NAME','NAICS5','NAICS5_NAME','NAICS6','NAICS6_NAME']].to_csv('/home/ubuntu/meerachaddha.github.io/lab03/_output/naics_details.csv', index=False)

print("Done!")
