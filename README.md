# 🎓 University & Course Data Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-green)
![Automation](https://img.shields.io/badge/Automation-Enabled-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

This project is a Python-based automated web scraping solution developed as part of a technical assignment.

The objective was to:

- Collect university data from the web
- Structure the data professionally
- Maintain relational integrity between universities and courses
- Export the dataset into a clean Excel file

All data collection is automated — no manual copy-paste was used.

---

## 🎯 Assignment Objectives Covered

- ✅ Real-world data collection using Python  
- ✅ Automated scraping process  
- ✅ Data cleaning and structuring  
- ✅ Relational mapping using unique IDs  
- ✅ Professional Excel export  

---

## 🛠️ Technologies Used

- **Python 3**
- **Requests** (HTTP requests)
- **BeautifulSoup** (HTML parsing)
- **Pandas** (Data processing)
- **OpenPyXL** (Excel export)

---

## 📂 Project Structure
University-Scraper/
│
├── scraper.py
├── submission.xlsx
└── README.md


---

## 📊 Output Structure

The script generates:
submission.xlsx


It contains **two structured sheets**.

---

### 🏫 Sheet 1: Universities

| Column Name        | Description |
|--------------------|------------|
| university_id      | Unique identifier |
| university_name    | Extracted dynamically |
| country            | Country location |
| city               | City location |
| website            | Official website URL |

✔ Unique IDs  
✔ No duplicate records  
✔ Clean formatting  

---

### 📚 Sheet 2: Courses

| Column Name      | Description |
|------------------|------------|
| course_id        | Unique identifier |
| university_id    | Foreign key (links to Universities sheet) |
| course_name      | Program name |
| level            | Degree level |
| discipline       | Field of study |
| duration         | Program duration |
| fees             | Tuition fees |
| eligibility      | Eligibility criteria |

✔ Relational integrity maintained  
✔ Missing values handled as `"Not Available"`  
✔ Clean structured dataset  

---

## 🔗 Data Integrity & Design

- `university_id` correctly links courses to universities
- `course_id` uniquely identifies each course
- Defensive coding used to handle missing HTML elements
- User-Agent headers added to avoid request blocking

---

## 🚀 How To Run

### 1️⃣ Install Dependencies

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

 ### 2️⃣ Run the Script
python scraper.py
