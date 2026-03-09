# books-analysis-form-web-scrapping

Project Overview  
This project builds a small data pipeline that collects book data from the web, cleans the dataset, stores it in a database, and generates insights through dashboards.  
  
  
Architecture  
Scraping → Raw Data → Data Cleaning → MySQL Database → Analysis → Dashboard  
  
  
Project Structure  
books-analysis-from-web-scraping/  
│  
├── data/   
│ ├── raw/   
│ │ └── dataset.csv   
│ │   
│ └── processed/   
│ └── cleaned_data.csv  
│  
├── scripts/   
│ ├── scraping_books.py   
│ ├── data_cleaning.py   
│ └── load_to_mysql.py   
│  
├── analysis/   
│ └── eda.py   
│  
├── dashboards/   
│ └── dashboards.pbix   
│  
├── requirements.txt   
├── .gitignore   
├── .env.example   
└── README.md  
  
  
ETL Pipeline  
1. Data Extraction  
Book data is collected using web scraping with Python and BeautifulSoup.  
2. Data Cleaning  
Data is cleaned using Pandas  
3. Data Loading  
4. The cleaned dataset is loaded into a MySQL database using SQLAlchemy.  
  
  
Dashboard  
The cleaned data is visualized using Power BI  
  
  
Installation  
Clone the repository using this command in terminal : git clone https://github.com/anastktr/books-analysis-form-web-scrapping.git  
Install dependencies: pip install -r requirements.txt or py -m pip install -r requirements.txt  
  
  
Environment Variables    
Create a .env file in the root directory like .env.example and put your credentials  
for example:  
DB_USER=your_user   
DB_PASSWORD=your_password   
DB_HOST=localhost   
DB_NAME=your_db  
  
  
Change the paths in order to tun it!  
