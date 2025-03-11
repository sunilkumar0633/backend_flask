# DataBase_Testing

## Overview

This repository provides a set of Python scripts designed to facilitate various database operations, including:

- **Creating a Database**: Scripts to set up a new MySQL database.
- **Importing Data from CSV**: Tools to import data from CSV files into the database.
- **Exporting Data to CSV**: Utilities to export data from the database back into CSV format.
- **API for Route Retrieval**: A Flask-based API (`app.py`) to fetch route data from the database.

These scripts are particularly useful for tasks such as data migration, backup, analysis, and real-time data retrieval.

## Contents

- **`create_db.py`**: Script to create a new MySQL database.  
- **`csv_to_db.py`**: Script to import data from a CSV file into the database.  
- **`db_to_csv.py`**: Script to export data from the database to a CSV file.  
- **`logistics_facilities_updated.csv`**: Dataset containing historical logistics and route data for machine learning-based route prediction and optimization.
- **`app.py`**: Flask-based API to retrieve route information from the database. 
