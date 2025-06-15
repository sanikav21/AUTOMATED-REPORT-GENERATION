#import the necessary libraries
import pandas as pd
from fpdf import FPDF 
import matplotlib.pyplot as plt
import os
 
 # Load data from CSV
df = pd.read_csv("employee_performance.csv") #Load the csv file into a DataFrame. File must be in same folder

#Analyze Data
average_score = df["Score"].mean()  #Calculate average score of all employee
top_employee = df.loc[df["Score"].idxmax()]    #Find the row of the employee with highest score

#Create Bar Chart of Employee Scores
plt.figure(figsize=(8,4))  #Create a figure for the chart with size 8x4 inches
plt.bar(df["Employee"], df["Score"], color='green')  #Create a bar chart (names on X axis,scores on Y axis)
plt.title("Employee Performance Scores")  #Set chart title
plt.xlabel("Employee")  #Label for X axis
plt.ylabel("Score")  #Label for Y axis
plt.xticks(rotation=45)   #Rotate X axis labels for better readability
plt.tight_layout()   #Adjust layout so labels don't overlap
chart_filename = "performance_chart.png"  #Define image file name 
plt.savefig(chart_filename)   #Save chart as an image file(PNG)
plt.close()

#Define Custom PDF Class

class PDF(FPDF):
    def header(self):
        self.set_font("Arial","B",16)
        self.cell(200,10,"Employee Performance Report", ln=True, align="C")  #Centered tile
        self.ln(10)  #line break

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial","I",8) #Set font to Arial ITalics size 8
        self.cell(0,10,f"Page{self.page_no()}",align="C")

#Create PDF
pdf = PDF()
pdf.add_page()

#Add Summary
pdf.set_font("Arial",size=12)
pdf.cell(200,10,f"Average Performance Score:{average_score:.2f}",ln=True)
pdf.cell(200,10, f"Top Performer: {top_employee['Employee']} with score {top_employee['Score']} ",ln=True)
pdf.ln(10)

#Insert Chart
if os.path.exists(chart_filename):
    pdf.image(chart_filename, x=30,w=150)
    pdf.ln(10)

 #create Table Header 
pdf.set_font("Arial","B",12)
for i,row in df.iterrows():
    pdf.cell(100,10,row["Employee"], 1)
    pdf.cell(50,10,str(row["Score"]),1)
    pdf.ln()

    #Save pdf
output_filename = "employee_performance_report.pdf"
pdf.output(output_filename)

print(f"PDF generated successfully: {output_filename}")
