{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red204\green0\blue78;\red255\green255\blue255;\red44\green55\blue61;
\red39\green78\blue204;\red42\green55\blue62;\red0\green0\blue0;\red238\green57\blue24;\red107\green0\blue1;
\red21\green129\blue62;}
{\*\expandedcolortbl;;\cssrgb\c84706\c10588\c37647;\cssrgb\c100000\c100000\c100000;\cssrgb\c22745\c27843\c30588;
\cssrgb\c20000\c40392\c83922;\cssrgb\c21569\c27843\c30980;\cssrgb\c0\c0\c0;\cssrgb\c95686\c31765\c11765;\cssrgb\c50196\c0\c0;
\cssrgb\c5098\c56471\c30980;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 -- Checking if the query is working or not\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 SELECT\cf4 \strokec4  \cf6 \strokec6 *\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\strokec4  \cf5 \strokec5 limit\cf4 \strokec4  \cf8 \strokec8 10\cf4 \strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find the sum of the fare amount based on vender\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 select\cf4 \strokec4  \strokec7 VendorID\strokec4 , \cf5 \strokec5 SUM\cf6 \strokec6 (\cf4 \strokec7 fare_amount\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 AS\cf4 \strokec4  \strokec7 sum_of_fare_amount\strokec4   \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\cb1 \strokec4 \
\cf5 \cb3 \strokec5 GROUP\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \strokec7 VendorID\strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find the sum of total tip amount based on payment type and tip amount is more than $5\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 select\cf4 \strokec4  \strokec7 payment_type_name\strokec4 , \cf5 \strokec5 sum\cf6 \strokec6 (\cf4 \strokec7 a\strokec4 .\strokec7 tip_amount\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 a\cb1 \strokec4 \
\cf5 \cb3 \strokec5 join\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 payment_type_dim\strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 b\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ON\cf4 \strokec4  \strokec7 a\strokec4 .\cf9 \strokec9 payment_type_id\cf4 \strokec4  = \strokec7 b\strokec4 .\strokec7 payment_type_id\strokec4  \cf5 \strokec5 and\cf4 \strokec4  \strokec7 a\strokec4 .\strokec7 tip_amount\strokec4  \cf6 \strokec6 >\cf4 \strokec4  \cf8 \strokec8 5\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 GROUP\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \strokec7 payment_type_name\strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find top 10 pickup locations(lat, log and ID) based on number of trips\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 select\cf4 \strokec4  \strokec7 a\strokec4 .\strokec7 pickup_location_id\strokec4 , \strokec7 b\strokec4 .\strokec7 pickup_latitude\strokec4 , \strokec7 b\strokec4 .\strokec7 pickup_longitude\strokec4 , \cf5 \strokec5 count\cf6 \strokec6 (\cf4 \strokec7 a\strokec4 .\strokec7 pickup_location_id\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf5 \strokec5 Count\cf4 \strokec4  \cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  \cf6 \strokec6 (\cf5 \strokec5 select\cf4 \strokec4  \cf6 \strokec6 *\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\strokec4  \cf5 \strokec5 where\cf4 \strokec4  \cf9 \strokec9 pickup_location_id\cf4 \strokec4  \cf6 \strokec6 !=\cf4 \strokec4  \strokec7 dropoff_location_id\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 a\cb1 \strokec4 \
\cf5 \cb3 \strokec5 join\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 pickup_location_dim\strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 b\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ON\cf4 \strokec4  \strokec7 a\strokec4 .\cf9 \strokec9 pickup_location_id\cf4 \strokec4  = \strokec7 b\strokec4 .\strokec7 pickup_location_id\cb1 \strokec4 \
\cf5 \cb3 \strokec5 GROUP\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \strokec7 a\strokec4 .\strokec7 pickup_location_id\strokec4 , \strokec7 b\strokec4 .\strokec7 pickup_latitude\strokec4 , \strokec7 b\strokec4 .\strokec7 pickup_longitude\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ORDER\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \cf5 \strokec5 count\cf4 \strokec4  \cf5 \strokec5 DESC\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 limit\cf4 \strokec4  \cf8 \strokec8 10\cf4 \strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find total number of trips by passenger count\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 select\cf4 \strokec4  \strokec7 b\strokec4 .\strokec7 passenger_count\strokec4 , \cf5 \strokec5 count\cf6 \strokec6 (\cf4 \strokec7 b\strokec4 .\strokec7 passenger_count\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf5 \strokec5 count\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  \cf6 \strokec6 (\cf5 \strokec5 select\cf4 \strokec4  \cf6 \strokec6 *\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 a\cb1 \strokec4 \
\cf5 \cb3 \strokec5 join\cf4 \strokec4  \strokec7 taxi_data_engineering\strokec4 .\strokec7 passenger_count_dim\strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 b\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ON\cf4 \strokec4  \strokec7 b\strokec4 .\cf9 \strokec9 passenger_count_id\cf4 \strokec4  = \strokec7 a\strokec4 .\strokec7 passenger_count_id\cb1 \strokec4 \
\cf5 \cb3 \strokec5 GROUP\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \strokec7 b\strokec4 .\strokec7 passenger_count\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ORDER\cf4 \strokec4  \cf5 \strokec5 BY\cf4 \strokec4  \cf5 \strokec5 count\cf4 \strokec4  \cf5 \strokec5 DESC\cf4 \strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find the maximum nuber of passengers travelled in a trip.\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 SELECT\cf4 \strokec4  \cf5 \strokec5 max\cf6 \strokec6 (\cf4 \strokec7 passenger_count\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxi_data_engineering\strokec4 .\strokec7 passenger_count_dim\strokec4 ;\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 -- Find the average fare amount by hour of the day\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 select\cf4 \strokec4  \cf5 \strokec5 CONCAT\cf6 \strokec6 (\cf4 \strokec7 b\strokec4 .\strokec7 pick_year\strokec4 , \cf10 \strokec10 "-"\cf4 \strokec4 , \strokec7 b\strokec4 .\strokec7 pick_month\strokec4 , \cf10 \strokec10 "-"\cf4 \strokec4 , \strokec7 b\strokec4 .\strokec7 pick_day\strokec4 , \cf10 \strokec10 " "\cf4 \strokec4 , \strokec7 b\strokec4 .\strokec7 pick_hour\strokec4 , \cf10 \strokec10 "hrs"\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf5 \strokec5 datetime\cf4 \strokec4 , \cf5 \strokec5 avg\cf6 \strokec6 (\cf4 \strokec7 a\strokec4 .\strokec7 fare_amount\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 avgr\cb1 \strokec4 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  \cf6 \strokec6 (\cf5 \strokec5 select\cf4 \strokec4  \cf6 \strokec6 *\cf4 \strokec4  \cf5 \strokec5 from\cf4 \strokec4  \strokec7 taxidatapipeline\strokec4 .\strokec7 taxi_data_engineering\strokec4 .\strokec7 fact_table\cf6 \strokec6 )\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 a\cb1 \strokec4 \
\cf5 \cb3 \strokec5 join\cf4 \strokec4  \cf10 \strokec10 `taxi_data_engineering.datetime_dim`\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \strokec7 b\cb1 \strokec4 \
\cf5 \cb3 \strokec5 ON\cf4 \strokec4  \strokec7 a\strokec4 .\cf9 \strokec9 datetime_id\cf4 \strokec4  = \strokec7 b\strokec4 .\strokec7 datetime_id\cb1 \strokec4 \
\cf5 \cb3 \strokec5 group\cf4 \strokec4  \cf5 \strokec5 by\cf4 \strokec4  \strokec7 b\strokec4 .\strokec7 pick_hour\strokec4 , \strokec7 b\strokec4 .\strokec7 pick_day\strokec4 , \strokec7 b\strokec4 .\strokec7 pick_month\strokec4 , \strokec7 b\strokec4 .\strokec7 pick_year\cb1 \strokec4 \
\cf5 \cb3 \strokec5 order\cf4 \strokec4  \cf5 \strokec5 by\cf4 \strokec4  \strokec7 b\strokec4 .\strokec7 pick_hour\strokec4  \cf5 \strokec5 DESC\cf4 \strokec4 ;\cb1 \
\
\
\
\
}