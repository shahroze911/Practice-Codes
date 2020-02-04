employee_data = ['Ali', 125000, 'Google', 5]
name=employee_data[0];
salary=employee_data[1];
company=employee_data[2];
years=employee_data[3];
message="""{_name} is working in {_company} for {_years} years and his salary is {_salary}""".format(_company=company,_name=name,_years=years,_salary=salary)
print(message)

studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,'28 Januray 2020', '05 February 2020']
fname=studentData[0];
lname=studentData[1];
institute=studentData[2];
department=studentData[3];
program=studentData[4];
fees=studentData[5]; feeSubmissionDate=studentData[6]; startingDate=studentData[7];

message="""Hello {_fname} {_lname},
Your application is accepted for admission in "{_program} {_department}" in {_institute}.
You have to submit fee {_fees} before {_feeSubmissionDate}.
Your classes will start from {_startingDate}.
Thanks.
""".format(_fname=fname,_lname=lname,_program=program,_department=department,_institute=institute,_fees=fees,_feeSubmissionDate=feeSubmissionDate,_startingDate=startingDate)
print(message)
