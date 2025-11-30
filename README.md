# Healthcare Appointment Analytics System 🏥

## 📌 Project Overview
[cite_start]This project is an end-to-end **Healthcare Appointment Analytics Application** developed during my internship at **MedTourEasy**[cite: 3, 16]. [cite_start]The system is designed to modernize healthcare operational monitoring by transforming raw appointment data into actionable insights[cite: 61].

[cite_start]It features a robust data pipeline that performs data cleaning, preprocessing, and exploratory data analysis (EDA), culminating in an interactive **Streamlit Dashboard**[cite: 24]. [cite_start]This dashboard allows healthcare administrators to monitor key performance indicators (KPIs) like patient footfall, revenue, cancellation rates, and operational efficiency in real-time[cite: 99, 108].

## 🚀 Features
* [cite_start]**Data Generation:** A script to generate synthetic healthcare datasets that mimic real-world scenarios, including "dirty data" (outliers, missing values) for cleaning practice[cite: 18].
* **Data Cleaning & Preprocessing:**
    * [cite_start]Handling missing values and duplicate records[cite: 20].
    * [cite_start]Standardizing date-time formats[cite: 131].
    * [cite_start]Feature Engineering: Extracting `Hour`, `Day_of_Week`, and `Time_Slot` (Morning/Afternoon/Evening)[cite: 21].
* **Key Performance Indicators (KPIs):**
    * [cite_start]Total Appointments & Revenue[cite: 452, 453].
    * [cite_start]Appointment Completion Rates[cite: 148].
    * [cite_start]Cancellation & No-Show Rates[cite: 149, 150].
    * [cite_start]Average Consultation Duration[cite: 454].
* **Interactive Dashboard:**
    * [cite_start]Built with **Streamlit**[cite: 24].
    * [cite_start]Dynamic filters for **Branch** and **Department**.
    * [cite_start]Visualizations using Matplotlib & Seaborn (Bar Charts, Pie Charts, Heatmaps)[cite: 23].

## 🛠️ Tech Stack
* [cite_start]**Language:** Python [cite: 254]
* [cite_start]**Data Manipulation:** Pandas, NumPy [cite: 276, 279]
* [cite_start]**Visualization:** Matplotlib, Seaborn [cite: 283, 286]
* [cite_start]**Dashboard Framework:** Streamlit [cite: 290]

## 📂 Project Structure
```bash
Healthcare-Appointment-Analytics/
├── app.py                 # Main Streamlit dashboard application
├── generate_dataset.py    # Script to create the synthetic dataset
├── appointments.csv       # The generated dataset (created after running script)
├── requirements.txt       # List of python dependencies
└── README.md              # Project documentation
⚙️ Installation & Setup
Clone the Repository

Bash

git clone [https://github.com/Nitin9310/Healthcare-Appointment-Analytics.git](https://github.com/Nitin9310/Healthcare-Appointment-Analytics.git)
cd Healthcare-Appointment-Analytics
Install Dependencies

Bash

pip install -r requirements.txt
Generate the Dataset Run the generation script to create the appointments.csv file (includes synthetic cleaning challenges):

Bash

python generate_dataset.py
Run the Dashboard Launch the Streamlit app:

Bash

streamlit run app.py
📊 Dashboard Usage
Once the app is running (usually at http://localhost:8501), you can:


Filter Data: Use the sidebar to select specific Branches (Delhi, Mumbai, etc.) or Departments (Surgery, Diagnostics, etc.).


View KPIs: Top-level metrics show Total Revenue, No-Show Rates, and Appointment counts instantly.

Analyze Trends:


Pie Chart: See which departments are busiest.


Bar Chart: Compare appointment volume across branches.


Heatmap: Identify peak hours for patient visits.

👨‍💻 Author
Nitin

Role: Data Analytics Trainee


Organization: MedTourEasy 


Supervisor: Dr. Sachin Singh (NIT Delhi) 

📜 Acknowledgements
Special thanks to the MedTourEasy Data Analytics Training Team for their mentorship in data cleaning, KPI development, and dashboard creation.



### How to add this to your project:
1.  Create a new file in your folder named `README.md`.
2.  Paste the text above into it.
3.  Run these commands to push it to GitHub:
    ```powershell
    git add README.md
    git commit -m "Add project documentation"
    git push
    ```
