{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Oblique;}
{\colortbl;\red255\green255\blue255;\red193\green152\blue86;\red16\green16\blue16;\red255\green255\blue255;
\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;\red76\green72\blue77;\red167\green197\blue152;
}
{\*\expandedcolortbl;;\cssrgb\c80392\c65882\c41176;\cssrgb\c7843\c7843\c7843;\cssrgb\c100000\c100000\c100000;
\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;\cssrgb\c37255\c35294\c37647;\cssrgb\c70980\c80784\c65882;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  pandas \cf2 \strokec2 as\cf4 \strokec4  pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  geopandas \cf2 \strokec2 as\cf4 \strokec4  gpd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 'transformer'\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 globals\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.decorators \cf2 \strokec2 import\cf4 \strokec4  transformer\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 'test'\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 globals\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.decorators \cf2 \strokec2 import\cf4 \strokec4  test\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 @transformer\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  transform\cf6 \strokec6 (\cf4 \strokec4 df\cf6 \strokec6 ,\cf4 \strokec4  *args\cf6 \strokec6 ,\cf4 \strokec4  **kwargs\cf6 \strokec6 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf5 \strokec5 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Template code for a transformer block.\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5     Add more parameters to this function if this block has multiple parent blocks.\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     There should be one parameter for each output variable from each parent block.\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5     Args:\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5         data: The output from the upstream parent block\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5         args: The output from any additional upstream blocks (if applicable)\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5     Returns:\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5         Anything (e.g. data frame, dictionary, array, int, str, etc.)\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     
\f1\i \cf8 \strokec8 # Specify your transformation logic here
\f0\i0 \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     df\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4  = pd.to_datetime\cf6 \strokec6 (\cf4 \strokec4 df\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ])\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     df\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4  = pd.to_datetime\cf6 \strokec6 (\cf4 \strokec4 df\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ])\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     datetime_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ,\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'pick_hour'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.hour\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'pick_day'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.day\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'pick_month'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.month\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'pick_year'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.year\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'pick_weekday'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.weekday\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'drop_hour'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.hour\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'drop_day'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.day\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'drop_month'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.month\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'drop_year'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.year\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'drop_weekday'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ]\cf4 \strokec4 .dt.weekday\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     datetime_dim\cf6 \strokec6 [\cf5 \strokec5 'datetime_id'\cf6 \strokec6 ]\cf4 \strokec4  = datetime_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     datetime_dim = datetime_dim\cf6 \strokec6 [[\cf5 \strokec5 'datetime_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pick_hour'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pick_day'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pick_month'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pick_year'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pick_weekday'\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                              \cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'drop_hour'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'drop_day'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'drop_month'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'drop_year'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'drop_weekday'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     passenger_count_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'passenger_count'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     passenger_count_dim\cf6 \strokec6 [\cf5 \strokec5 'passenger_count_id'\cf6 \strokec6 ]\cf4 \strokec4  = passenger_count_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     passenger_count_dim = passenger_count_dim\cf6 \strokec6 [[\cf5 \strokec5 'passenger_count_id'\cf6 \strokec6 ,\cf5 \strokec5 'passenger_count'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     trip_distance_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'trip_distance'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     trip_distance_dim\cf6 \strokec6 [\cf5 \strokec5 'trip_distance_id'\cf6 \strokec6 ]\cf4 \strokec4  = trip_distance_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     trip_distance_dim = trip_distance_dim\cf6 \strokec6 [[\cf5 \strokec5 'trip_distance_id'\cf6 \strokec6 ,\cf5 \strokec5 'trip_distance'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     rate_code_type = \cf6 \strokec6 \{\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 1\cf6 \strokec6 :\cf5 \strokec5 "Standard rate"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 2\cf6 \strokec6 :\cf5 \strokec5 "JFK"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 3\cf6 \strokec6 :\cf5 \strokec5 "Newark"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 4\cf6 \strokec6 :\cf5 \strokec5 "Nassau or Westchester"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 5\cf6 \strokec6 :\cf5 \strokec5 "Negotiated fare"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 6\cf6 \strokec6 :\cf5 \strokec5 "Group ride"\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf6 \strokec6 \}\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     rate_code_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'RatecodeID'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     rate_code_dim\cf6 \strokec6 [\cf5 \strokec5 'rate_code_id'\cf6 \strokec6 ]\cf4 \strokec4  = rate_code_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     rate_code_dim\cf6 \strokec6 [\cf5 \strokec5 'rate_code_name'\cf6 \strokec6 ]\cf4 \strokec4  = rate_code_dim\cf6 \strokec6 [\cf5 \strokec5 'RatecodeID'\cf6 \strokec6 ]\cf4 \strokec4 .\cf2 \strokec2 map\cf6 \strokec6 (\cf4 \strokec4 rate_code_type\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     rate_code_dim = rate_code_dim\cf6 \strokec6 [[\cf5 \strokec5 'rate_code_id'\cf6 \strokec6 ,\cf5 \strokec5 'RatecodeID'\cf6 \strokec6 ,\cf5 \strokec5 'rate_code_name'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\
\cf4 \cb3 \strokec4     pickup_location_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'pickup_longitude'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pickup_latitude'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     pickup_location_dim\cf6 \strokec6 [\cf5 \strokec5 'pickup_location_id'\cf6 \strokec6 ]\cf4 \strokec4  = pickup_location_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     pickup_location_dim = pickup_location_dim\cf6 \strokec6 [[\cf5 \strokec5 'pickup_location_id'\cf6 \strokec6 ,\cf5 \strokec5 'pickup_latitude'\cf6 \strokec6 ,\cf5 \strokec5 'pickup_longitude'\cf6 \strokec6 ]]\cf4 \strokec4  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     
\f1\i \cf8 \strokec8 # geo_pickup = gpd.points_from_xy(pickup_location_dim["pickup_longitude"], pickup_location_dim["pickup_latitude"], crs = "EPSG:4326")
\f0\i0 \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     
\f1\i \cf8 \strokec8 # pickup_location_dim = gpd.GeoDataFrame(pickup_location_dim, geometry=geo_pickup)
\f0\i0 \cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     dropoff_location_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'dropoff_longitude'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'dropoff_latitude'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     dropoff_location_dim\cf6 \strokec6 [\cf5 \strokec5 'dropoff_location_id'\cf6 \strokec6 ]\cf4 \strokec4  = dropoff_location_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     dropoff_location_dim = dropoff_location_dim\cf6 \strokec6 [[\cf5 \strokec5 'dropoff_location_id'\cf6 \strokec6 ,\cf5 \strokec5 'dropoff_latitude'\cf6 \strokec6 ,\cf5 \strokec5 'dropoff_longitude'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     
\f1\i \cf8 \strokec8 # geo_dropoff = gpd.points_from_xy(dropoff_location_dim["dropoff_longitude"], dropoff_location_dim["dropoff_latitude"], crs = "EPSG:4326")
\f0\i0 \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     
\f1\i \cf8 \strokec8 # dropoff_location_dim = gpd.GeoDataFrame(dropoff_location_dim, geometry=geo_dropoff)
\f0\i0 \cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     payment_type_name = \cf6 \strokec6 \{\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 1\cf6 \strokec6 :\cf5 \strokec5 "Credit card"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 2\cf6 \strokec6 :\cf5 \strokec5 "Cash"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 3\cf6 \strokec6 :\cf5 \strokec5 "No charge"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 4\cf6 \strokec6 :\cf5 \strokec5 "Dispute"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 5\cf6 \strokec6 :\cf5 \strokec5 "Unknown"\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf9 \strokec9 6\cf6 \strokec6 :\cf5 \strokec5 "Voided trip"\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf6 \strokec6 \}\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     payment_type_dim = df\cf6 \strokec6 [[\cf5 \strokec5 'payment_type'\cf6 \strokec6 ]]\cf4 \strokec4 .drop_duplicates\cf6 \strokec6 ()\cf4 \strokec4 .reset_index\cf6 \strokec6 (\cf4 \strokec4 drop=\cf2 \strokec2 True\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     payment_type_dim\cf6 \strokec6 [\cf5 \strokec5 'payment_type_id'\cf6 \strokec6 ]\cf4 \strokec4  = payment_type_dim.index\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     payment_type_dim\cf6 \strokec6 [\cf5 \strokec5 'payment_type_name'\cf6 \strokec6 ]\cf4 \strokec4  = payment_type_dim\cf6 \strokec6 [\cf5 \strokec5 'payment_type'\cf6 \strokec6 ]\cf4 \strokec4 .\cf2 \strokec2 map\cf6 \strokec6 (\cf4 \strokec4 payment_type_name\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     payment_type_dim = payment_type_dim\cf6 \strokec6 [[\cf5 \strokec5 'payment_type_id'\cf6 \strokec6 ,\cf5 \strokec5 'payment_type'\cf6 \strokec6 ,\cf5 \strokec5 'payment_type_name'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     fact_table = df.merge\cf6 \strokec6 (\cf4 \strokec4 passenger_count_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf5 \strokec5 'passenger_count'\cf6 \strokec6 )\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 trip_distance_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf5 \strokec5 'trip_distance'\cf6 \strokec6 )\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 rate_code_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf5 \strokec5 'RatecodeID'\cf6 \strokec6 )\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 pickup_location_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf6 \strokec6 [\cf5 \strokec5 'pickup_longitude'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pickup_latitude'\cf6 \strokec6 ])\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 dropoff_location_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf6 \strokec6 [\cf5 \strokec5 'dropoff_longitude'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'dropoff_latitude'\cf6 \strokec6 ])\cf4 \strokec4 \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 datetime_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf6 \strokec6 [\cf5 \strokec5 'tpep_pickup_datetime'\cf6 \strokec6 ,\cf5 \strokec5 'tpep_dropoff_datetime'\cf6 \strokec6 ])\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              .merge\cf6 \strokec6 (\cf4 \strokec4 payment_type_dim\cf6 \strokec6 ,\cf4 \strokec4  on=\cf5 \strokec5 'payment_type'\cf6 \strokec6 )\cf4 \strokec4  \\\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4              \cf6 \strokec6 [[\cf5 \strokec5 'VendorID'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'datetime_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'passenger_count_id'\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                \cf5 \strokec5 'trip_distance_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'rate_code_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'store_and_fwd_flag'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'pickup_location_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'dropoff_location_id'\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                \cf5 \strokec5 'payment_type_id'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'fare_amount'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'extra'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'mta_tax'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'tip_amount'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'tolls_amount'\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                \cf5 \strokec5 'improvement_surcharge'\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'total_amount'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 \{\cf5 \strokec5 "datetime_dim"\cf6 \strokec6 :\cf4 \strokec4 datetime_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "passenger_count_dim"\cf6 \strokec6 :\cf4 \strokec4 passenger_count_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "trip_distance_dim"\cf6 \strokec6 :\cf4 \strokec4 trip_distance_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "rate_code_dim"\cf6 \strokec6 :\cf4 \strokec4 rate_code_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "pickup_location_dim"\cf6 \strokec6 :\cf4 \strokec4 pickup_location_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "dropoff_location_dim"\cf6 \strokec6 :\cf4 \strokec4 dropoff_location_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "payment_type_dim"\cf6 \strokec6 :\cf4 \strokec4 payment_type_dim.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf5 \strokec5 "fact_table"\cf6 \strokec6 :\cf4 \strokec4 fact_table.to_dict\cf6 \strokec6 (\cf4 \strokec4 orient=\cf5 \strokec5 "dict"\cf6 \strokec6 )\}\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 @test\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  test_output\cf6 \strokec6 (\cf4 \strokec4 output\cf6 \strokec6 ,\cf4 \strokec4  *args\cf6 \strokec6 )\cf4 \strokec4  -> \cf2 \strokec2 None\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf5 \strokec5 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Template code for testing the output of the block.\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 assert\cf4 \strokec4  output \cf2 \strokec2 is\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 None\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'The output is undefined'\cf4 \cb1 \strokec4 \
}