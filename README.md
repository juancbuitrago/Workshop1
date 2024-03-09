# ETL Workshop 1 #
## Overview ##
_This workshop demonstrates how to create and manage candidate data using PostgreSQL and Python. It covers connecting to a PostgreSQL database, creating tables, importing data from CSV files, and performing basic SQL operations._

_Also, *[Detailed Documentation](https://github.com/juancbuitrago/Workshop1/blob/main/docs/documentation.pdf)* is available that covers everything from data selection to the final visualizations_

## Table of Contents ##
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Transformation](#data-transformation)
- [Data Analysis](#exploratory-data-analysis)
- [Analysis & Visualizations](#analysis-visualizations)

## Requirements <a name="requirements"></a> ##
- Python 3.x
- SQLAlchemy
- psycopg2
- Matplotlib & Seaborn
- Pandas
- PostgreSQL
- Jupyter Notebook
- JSON credentials file ("config.json") with this format:
 
```
{
  "no_db":{
    "user": "your_user",
    "password": "your_password",
    "host": "your_host",
    "port": "your_port"
  },
  "with_db":{
    "user": "your_user",
    "password": "your_password",
    "db": "candidates"
    "host": "your_host",
    "port": "your_port"
  }
}

``` 

## Setup <a name="setup"></a> ##
_First of all, 
ensure you have the following programs installed with which the entire project procedure is carried out:_

   - **[Python](https://www.python.org)**
   - **[PostgreSQL](https://www.postgresql.org/download/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**

_Using the **[requirements.txt](https://github.com/RJuanJo/etl-project/blob/main/config/requirements.txt)**
run the following command in the Terminal_

```python
pip install -r src/requirements.txt
```
_Previous command will install the following necessary libraries for the workshop_

```python
- psycopg2
- matplotlib
- pandas
- pip
- sqlalchemy
- seaborn
- sys

```
## Data Transformation <a name="data-treatment"></a> ##

 _This process was carried out in **[First Notebook](https://github.com/juancbuitrago/Workshop1/blob/main/notebooks/Transformation.ipynb)** where the following procedures are being carried out:_

- Identification of all the technologies
- Categorize the technologies in a dictionary
- Create a new column called: category_of_technologies
- Update the table of candidates_hired
 
 ## Explorate Data Analysis <a name="exploratory-data-analysis"></a> ##

 _This process was carried out in **[Second Notebook](https://github.com/juancbuitrago/Workshop1/blob/main/notebooks/EDA.ipynb)** where the following procedures are being carried out:_

- Identification of the data frame structure
- Identification of columns names
- Identification of data types
- Identification of null data
- Exploratory Data Analysis
- Graphics

## Analysis & Visualization <a name="analysis-visualizations"></a> ###

### These visualizations can be seen in the **[Dashboard Summary](https://github.com/juancbuitrago/Workshop1/blob/main/docs/dashboard.pdf)**.

### Also, threre is the **[Published Dashboard](https://app.powerbi.com/links/TVzsQN2Hxq?ctid=693cbea0-4ef9-4254-8977-76e05cb5f556&pbi_source=linkShare)** for a better interactive experience with the dashboard and the data.


