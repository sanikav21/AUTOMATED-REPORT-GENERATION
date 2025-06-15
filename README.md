# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS 

NAME: SANIKA VYAS 

INTERN ID:CT04DN249 

DOMAIN: PYTHON 

DURATION: 4 WEEKS 

MENTOR: NEELA SANTOSH

DESCRIPTION OF CODE:
This Python script automates the generation of a professional PDF report summarizing employee performance based on data from a CSV file. It integrates data analysis, data visualization, and document generation in a single workflow, demonstrating how Python can streamline reporting processes in organizations. The script begins by importing necessary libraries: pandas for data manipulation, fpdf for creating PDFs, matplotlib.pyplot for plotting charts, and os to check for the existence of files. These libraries are standard tools in the Python ecosystem for handling data and producing visual and textual outputs in professional formats.

The first step involves loading data from a CSV file named employee_performance.csv using the pandas.read_csv() function. This file is expected to contain at least two columns: "Employee" and "Score". Once the data is loaded into a DataFrame, the script calculates the average performance score of all employees using the .mean() function on the "Score" column. It then identifies the top-performing employee by using .idxmax() to locate the index of the highest score and retrieves the corresponding row. These basic analyses provide useful summary statistics that will be highlighted in the final report.

Next, the script creates a visual representation of the performance scores using matplotlib. It generates a horizontal bar chart that plots employee names along the X-axis and their corresponding scores along the Y-axis. This chart helps in quickly identifying performance distribution and spotting outliers visually. The figure is sized for optimal clarity and rotated slightly to make sure that the employee names are readable. The final chart is saved as a PNG file (performance_chart.png), which is later embedded into the PDF document.

The core of the PDF generation is handled through a custom class PDF that inherits from the FPDF class. Within this class, a header() method is defined to add a title ("Employee Performance Report") at the top of each page, and a footer() method is added to include page numbers at the bottom of each page. This adds a layer of professionalism and consistency to the document. After initializing and adding a page to the PDF, the script inserts summary information at the top, including the average performance score (formatted to two decimal places) and the name and score of the top performer.

To provide a comprehensive view, the script checks whether the chart image exists using os.path.exists() before embedding it into the PDF. The image is inserted with specific width positioning to ensure it fits well on the page. Following the chart, the script constructs a simple table that lists each employee’s name and score. This is done using a loop that iterates over each row in the DataFrame and creates bordered cells for names and scores, one row at a time. The table is a crucial part of the report as it offers raw data visibility alongside the summarized insights.

Once all content is added, the report is saved with the filename employee_performance_report.pdf, and a confirmation message is printed to notify the user that the report has been successfully created. This script is especially useful in HR departments, performance review systems, internal presentations, and educational settings where automated reporting of metrics is required. It can easily be adapted to other use cases by modifying column names or adding additional data points. Overall, this code is a powerful example of how Python can be used to transform raw data into structured, readable, and visually appealing business reports with minimal manual effort.

OOUTPUT OF CODE:


