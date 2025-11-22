# 🎬 Netflix Data Analysis — Complete EDA Project

A full exploratory data analysis (EDA) project on the **Netflix Titles Dataset**, including data cleaning, preprocessing, visualization, and insights about genres, countries, directors, and content trends.

This repository is designed to showcase **data analysis skills**, **Python coding**, and **project structuring** for recruiters and portfolio visibility.

---

## 📊 Project Summary

The Netflix dataset contains information such as:

- Title  
- Director  
- Cast  
- Country  
- Release year  
- Date added  
- Rating  
- Duration  
- Genres  

This project answers key analytical questions:

✔ How many **Movies vs TV Shows**?  
✔ Which countries produce the most content?  
✔ What are the top trending genres?  
✔ How has Netflix content grown yearly?  
✔ Who are the top directors?

---
Netflix-Data-Analysis/
├─ data/
│ └─ netflix_titles.csv
├─ images/
│ ├─ Image_1.png
│ ├─ image_2.png
│ ├─ image_3.png
│ ├─ image_4.png
│ └─ image_5.png
├─ notebooks/
│ └─ netflix_project.py
├─ src/
│ └─ utils.py
├─ requirements.txt
├─ LICENSE
└─ .gitignore



### 📁 **Folder Explanation**

- **data/** → Contains the Netflix dataset (`netflix_titles.csv`)  
- **images/** → Stores all visualizations used in this project  
- **notebooks/** → Main analysis script (`netflix_project.py`)  
- **src/** → Helper utility functions (`utils.py`)  
- **requirements.txt** → Python dependencies  
- **LICENSE** → MIT license  
- **.gitignore** → Ignored files like venv, pycache, checkpoints  

---

## 🧹 Data Cleaning Workflow

1. Handled missing values (country, cast, director, rating)  
2. Dropped rows with invalid `date_added`  
3. Extracted year from `date_added`  
4. Split genres from `listed_in`  
5. Exported cleaned dataset as:  
   ✔ `cleaned_netflix_data.csv`

---

## 📈 Analysis & Visuals

The following visuals were generated and stored in **images/**:

1. **Movies vs TV Shows**
2. **Top 10 Countries with Most Netflix Titles**
3. **Most Popular Genres**
4. **Content Growth Over the Years**
5. **Top 10 Directors**

> All graphs can be found inside the `images/` folder.

---

## 🧪 Running the Project

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/Netflix-Data-Analysis.git
cd Netflix-Data-Analysis
```

2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

3. Install required libraries
pip install -r requirements.txt

4. Run the notebook/script
python notebooks/netflix_project.py

Or open it in VS Code / Jupyter.

🧠 Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook / VS Code

📄 License

This project is licensed under the MIT License.

⭐ Support

If you find this project helpful, please ⭐ star the repository!

## 🗂️ Repository Structure



git push
