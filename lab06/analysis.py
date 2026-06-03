import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

# Create output folder
os.makedirs('lab06/_output', exist_ok=True)

# Load dataset
data = pd.read_csv('lab06/lightcast_data.csv')

# 1.1 Data Cleaning and Typecasting
data['POSTED'] = pd.to_datetime(data['POSTED'], errors='coerce')
data['EXPIRED'] = pd.to_datetime(data['EXPIRED'], errors='coerce')
data['LAST_UPDATED_DATE'] = pd.to_datetime(data['LAST_UPDATED_DATE'], errors='coerce')
data['SALARY_FROM'] = pd.to_numeric(data['SALARY_FROM'], errors='coerce')
data['SALARY_TO'] = pd.to_numeric(data['SALARY_TO'], errors='coerce')
data['MIN_YEARS_EXPERIENCE'] = pd.to_numeric(data['MIN_YEARS_EXPERIENCE'], errors='coerce')
data['SALARY_FROM'].fillna(0, inplace=True)
data['SALARY_TO'].fillna(0, inplace=True)
data['MIN_YEARS_EXPERIENCE'].fillna(0, inplace=True)

# Save cleaned data
data.to_csv('lab06/_output/lightcast_cleaned.csv', index=False)
print("Cleaned data saved.")

# Q1: Job Count by State
job_counts = data.groupby('STATE_NAME').size().reset_index(name='Job Count')
plt.figure(figsize=(14, 6))
sns.barplot(x='STATE_NAME', y='Job Count', data=job_counts)
plt.xticks(rotation=45, ha='right')
plt.title('Number of Jobs by State')
plt.xlabel('State')
plt.ylabel('Job Count')
plt.tight_layout()
plt.savefig('lab06/_output/q1_job_count_by_state.png')
plt.close()
print("Q1 done.")

# Q2: Jobs in Information Technology Industry
industry_data = data[data['NAICS2_NAME'] == 'Professional, Scientific, and Technical Services']
industry_counts = industry_data.groupby('STATE_NAME').size().reset_index(name='Job Count')
plt.figure(figsize=(14, 6))
sns.barplot(x='STATE_NAME', y='Job Count', data=industry_counts)
plt.xticks(rotation=45, ha='right')
plt.title('Number of Jobs in Professional & Technical Services by State')
plt.xlabel('State')
plt.ylabel('Job Count')
plt.tight_layout()
plt.savefig('lab06/_output/q2_jobs_by_industry.png')
plt.close()
print("Q2 done.")

# Q3: Percentage Change in Jobs for Specific Companies
companies = ['Cognizant Technology Solutions', 'Deloitte', 'IBM']
company_data = data[data['COMPANY_NAME'].isin(companies)].copy()
company_data['MONTH'] = company_data['POSTED'].dt.to_period('M')
may = company_data[company_data['MONTH'] == '2024-05'].groupby('COMPANY_NAME').size()
sept = company_data[company_data['MONTH'] == '2024-09'].groupby('COMPANY_NAME').size()
pct_change = ((sept - may) / may * 100).reset_index()
pct_change.columns = ['Company', 'Percent Change']
plt.figure(figsize=(10, 6))
sns.barplot(x='Company', y='Percent Change', data=pct_change)
plt.title('Percentage Change in Job Postings (May to September 2024)')
plt.xlabel('Company')
plt.ylabel('Percent Change (%)')
plt.tight_layout()
plt.savefig('lab06/_output/q3_pct_change_companies.png')
plt.close()
print("Q3 done.")

# Q4: Average Salary by Industry
avg_salary = data.groupby('NAICS2_NAME')[['SALARY_FROM', 'SALARY_TO']].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='SALARY_FROM', y='NAICS2_NAME', data=avg_salary, color='steelblue')
plt.title('Average Salary by Industry')
plt.xlabel('Average Salary')
plt.ylabel('Industry')
plt.tight_layout()
plt.savefig('lab06/_output/q4_avg_salary_by_industry.png')
plt.close()
print("Q4 done.")

# Q5: Top 10 Skills
skills_data = data['SKILLS_NAME'].dropna().str.split(',')
skills_flat = [skill.strip() for sublist in skills_data for skill in sublist]
skill_counts = Counter(skills_flat).most_common(10)
skill_df = pd.DataFrame(skill_counts, columns=['Skill', 'Count'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Skill', data=skill_df)
plt.title('Top 10 Most Frequently Mentioned Skills')
plt.xlabel('Frequency')
plt.ylabel('Skill')
plt.tight_layout()
plt.savefig('lab06/_output/q5_skills_distribution.png')
plt.close()
print("Q5 done.")

print("All done!")