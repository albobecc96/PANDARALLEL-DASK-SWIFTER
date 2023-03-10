from numpy import dtype
import pandas as pd

#Read Salaries.csv as a dataframe called sal.
sal = pd.read_csv('Salaries.csv', low_memory = False)
#Check the head of the DataFrame
print(sal.head())
#Use the .info() method to find out how many entries there are.
print(sal.info())
#What is the average BasePay ?
sal['BasePay'].mean()
# What is the highest amount of OvertimePay in the dataset ?
sal['OvertimePay'].max()
#What is the job title of JOSEPH DRISCOLL ? Note: Use all caps
#, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"])
#How much does JOSEPH DRISCOLL make(including benefits)?
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])
#What is the name of highest paid person(including benefits)?
print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]['EmployeeName'])
#What is the name of lowest paid person (including benefits)?
#Do you notice something strange about how much he or she is paid?
print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()]['EmployeeName'])
# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print(sal.groupby('Year').mean()['BasePay'])
# How many unique job titles are there?
print(sal['JobTitle'].nunique())
# What are the top 5 most common jobs?
print(sal['JobTitle'].value_counts().head(5))
#How many Job Titles were represented by only one person 
# in 2013? (e.g. Job Titles with only one occurence in 2013?)
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)) #pretty tricky way to do this...
#  How many people have the word Chief in their job title? (This is pretty tricky)
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))
#Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len','TotalPayBenefits']].corr()) # No correlation
