-- Checking if the query is working or not
SELECT * from taxidatapipeline.taxi_data_engineering.fact_table limit 10;

-- Find the sum of the fare amount based on vender
select VendorID, SUM(fare_amount) AS sum_of_fare_amount  from taxidatapipeline.taxi_data_engineering.fact_table
GROUP BY VendorID;

-- Find the sum of total tip amount based on payment type and tip amount is more than $5
select payment_type_name, sum(a.tip_amount) from taxidatapipeline.taxi_data_engineering.fact_table as a
join taxidatapipeline.taxi_data_engineering.payment_type_dim as b
ON a.payment_type_id = b.payment_type_id and a.tip_amount > 5
GROUP BY payment_type_name;

-- Find top 10 pickup locations(lat, log and ID) based on number of trips
select a.pickup_location_id, b.pickup_latitude, b.pickup_longitude, count(a.pickup_location_id) as Count 
from (select * from taxidatapipeline.taxi_data_engineering.fact_table where pickup_location_id != dropoff_location_id) as a
join taxidatapipeline.taxi_data_engineering.pickup_location_dim as b
ON a.pickup_location_id = b.pickup_location_id
GROUP BY a.pickup_location_id, b.pickup_latitude, b.pickup_longitude
ORDER BY count DESC
limit 10;

-- Find total number of trips by passenger count
select b.passenger_count, count(b.passenger_count) as count
from (select * from taxidatapipeline.taxi_data_engineering.fact_table) as a
join taxi_data_engineering.passenger_count_dim as b
ON b.passenger_count_id = a.passenger_count_id
GROUP BY b.passenger_count
ORDER BY count DESC;

-- Find the maximum nuber of passengers travelled in a trip.
SELECT max(passenger_count) from taxi_data_engineering.passenger_count_dim;

-- Find the average fare amount by hour of the day
select CONCAT(b.pick_year, "-", b.pick_month, "-", b.pick_day, " ", b.pick_hour, "hrs") as datetime, avg(a.fare_amount) as avgr
from (select * from taxidatapipeline.taxi_data_engineering.fact_table) as a
join `taxi_data_engineering.datetime_dim` as b
ON a.datetime_id = b.datetime_id
group by b.pick_hour, b.pick_day, b.pick_month, b.pick_year
order by b.pick_hour DESC;



