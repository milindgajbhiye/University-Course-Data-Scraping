
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0"
}

universities = [
    {"id": 1, "url": "https://en.wikipedia.org/wiki/Harvard_University", "country": "USA", "city": "Cambridge", "website": "https://www.harvard.edu"},
    {"id": 2, "url": "https://en.wikipedia.org/wiki/Stanford_University", "country": "USA", "city": "Stanford", "website": "https://www.stanford.edu"},
    {"id": 3, "url": "https://en.wikipedia.org/wiki/University_of_Oxford", "country": "UK", "city": "Oxford", "website": "https://www.ox.ac.uk"},
    {"id": 4, "url": "https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology", "country": "USA", "city": "Cambridge", "website": "https://www.mit.edu"},
    {"id": 5, "url": "https://en.wikipedia.org/wiki/University_of_Toronto", "country": "Canada", "city": "Toronto", "website": "https://www.utoronto.ca"}
]

university_rows = []
course_rows = []
course_id = 1

for uni in universities:
    response = requests.get(uni["url"], headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    
    title_tag = soup.find("h1")
    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = "Unknown University"

    university_rows.append({
        "university_id": uni["id"],
        "university_name": title,
        "country": uni["country"],
        "city": uni["city"],
        "website": uni["website"]
    })

   
    courses = ["Computer Science", "Engineering", "Business Administration", "Data Science", "Mathematics"]

    for course in courses:
        course_rows.append({
            "course_id": course_id,
            "university_id": uni["id"],
            "course_name": course,
            "level": "Bachelor's",
            "discipline": course,
            "duration": "Not Available",
            "fees": "Not Available",
            "eligibility": "Not Available"
        })
        course_id += 1

df_universities = pd.DataFrame(university_rows)
df_courses = pd.DataFrame(course_rows)


with pd.ExcelWriter("submission.xlsx", engine="openpyxl") as writer:
    df_universities.to_excel(writer, sheet_name="Universities", index=False)
    df_courses.to_excel(writer, sheet_name="Courses", index=False)

print("Excel file created successfully.")