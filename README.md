# Taxi Data Engineering

## Introduction

The main objective of this project is to understand and implement ETL Extract-Transform-Load process using modren data pipeline tools such as Mage AI, Looker, Google BigQuery to name a few. Learn different Data models and how to make them easily accessible for Analysis and for machine learning.

## Architecture

![architecture](https://github.com/BhanuKedhar09/Taxi-Analysis-Data-Engineering/assets/112876951/f9e8cf12-7b5b-482c-9958-c6bd7a14e06a)

## Data

The data used here is from NYC Taxi and Limousine Commission. Took only part of the data and worked on ETL process. 

Data used in the project :- https://github.com/BhanuKedhar09/Taxi-Analysis-Data-Engineering/blob/main/Taxi%20Analysis/uber_data.csv

Data Link :- https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Link for Data Dictonary :- https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


## Data Model

I have used star schema to divide the data.

[Taxi Data Model.pdf](https://github.com/BhanuKedhar09/Taxi-Analysis-Data-Engineering/files/11583064/Taxi.Data.Model.pdf)

## Tech Stack

**Programming languages**

- Python version 3.9
- SQL

**Technologies**

- MAGE AI (Open source Data Pipeline Tool)
- Google Cloud Platform
- Compute Engine
- Cloud Storage Buckets
- BigQuery
- Looker Studio (Visualing Dashboards)

## Looker Dashboard

Here's how the final dashboard looks like this

![Taxi_Dashboard1024_1](https://github.com/BhanuKedhar09/Taxi-Analysis-Data-Engineering/assets/112876951/7842fe67-d776-457d-ac96-79268855a727)


You can have interactive Dashboard with filters [here](https://lookerstudio.google.com/reporting/5fc4ebdf-a7ec-4d6a-a54a-df5e16e98935)


**Procedure**

1. Download the Dataset from either of these links
- https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- https://github.com/BhanuKedhar09/Taxi-Analysis-Data-Engineering/blob/main/Taxi%20Analysis/uber_data.csv
2. Convert the columns to appropiate types in this case convert the *tpep_pickup_datetime* and *tpep_dropoff_datetime* to date and time formats.
3. Analysze the dataset columns and decide which goes columns go to fact table and which column forms dimension table. based on the star schema data modeling steps shown [here](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema#star-schema-overview)
4. Create data model use [Lucid](https://lucid.app/) app to create one.
5. Upload the dataset to Google Colud Storeage (create google cloud account if you don't have one it is free and gives $300 free credit)
6. Spin up a new instance in Compute Engine and with machine type *e2-standard-4* and use startupscript.sh in the metadata.
7. Run mage it would automatically choose port *6789* and access it from from your web browser(make sure you have allowed your IP address in the network firewall).










