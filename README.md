# Sleep Quality Analyzer

Sleep Quality Analyzer is a web-based application built with Streamlit that enables users to log their sleep patterns, visualize trends, and receive personalized insights to help improve sleep habits. The tool provides an intuitive interface for daily entries and generates both visual summaries and exportable reports.

---

## Features

- Log daily sleep data:
  - Date
  - Sleep hours
  - Sleep quality (1–10 scale)
  - Bed time and wake time
- Analyze trends through interactive line and bar charts
- Receive personalized sleep tips based on recent data
- Export sleep logs to CSV or PDF format
- Simple and responsive UI for desktop use

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- PDFKit (for PDF export)
- HTML/CSS (via Streamlit components)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sleep-quality-analyzer.git
   cd sleep-quality-analyzer
Set up a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Install wkhtmltopdf (for PDF export):

Download and install from: https://wkhtmltopdf.org/downloads.html

Ensure it's added to your system PATH

Run the application:

bash
Copy
Edit
streamlit run app.py
File Structure
perl
Copy
Edit
sleep-quality-analyzer/
│
├── app.py                  # Main application script
├── sleep_data.csv          # Auto-generated log file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
Screenshots
Add screenshots here to show the UI and charts
Example:

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Pavan Srinivaas R
Sri Krishna Arts and Science College
