{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Oblique;}
{\colortbl;\red255\green255\blue255;\red193\green152\blue86;\red16\green16\blue16;\red255\green255\blue255;
\red76\green72\blue77;\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;}
{\*\expandedcolortbl;;\cssrgb\c80392\c65882\c41176;\cssrgb\c7843\c7843\c7843;\cssrgb\c100000\c100000\c100000;
\cssrgb\c37255\c35294\c37647;\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.repo_manager \cf2 \strokec2 import\cf4 \strokec4  get_repo_path\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  mage_ai.io.bigquery \cf2 \strokec2 import\cf4 \strokec4  BigQuery\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  mage_ai.io.config \cf2 \strokec2 import\cf4 \strokec4  ConfigFileLoader\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  pandas \cf2 \strokec2 import\cf4 \strokec4  DataFrame\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0

\f1\i \cf5 \cb3 \strokec5 # import pandas as pd
\f0\i0 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 from\cf4 \strokec4  os \cf2 \strokec2 import\cf4 \strokec4  path\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf6 \strokec6 'data_exporter'\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 globals\cf7 \strokec7 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.decorators \cf2 \strokec2 import\cf4 \strokec4  data_exporter\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @data_exporter\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  export_data_to_big_query\cf7 \strokec7 (\cf4 \strokec4 df1\cf7 \strokec7 :\cf4 \strokec4  DataFrame\cf7 \strokec7 ,\cf4 \strokec4  **kwargs\cf7 \strokec7 )\cf4 \strokec4  -> \cf2 \strokec2 None\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf6 \strokec6 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6     Template for exporting data to a BigQuery warehouse.\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     Specify your configuration settings in 'io_config.yaml'.\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6     Docs: https://docs.mage.ai/design/data-loading#bigquery\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     config_path = path.join\cf7 \strokec7 (\cf4 \strokec4 get_repo_path\cf7 \strokec7 (),\cf4 \strokec4  \cf6 \strokec6 'io_config.yaml'\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     config_profile = \cf6 \strokec6 'default'\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  key\cf7 \strokec7 ,\cf4 \strokec4  value \cf2 \strokec2 in\cf4 \strokec4  df1.items\cf7 \strokec7 ():\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         table_id = \cf6 \strokec6 'taxidatapipeline.taxi_data_engineering.\{\}'\cf4 \strokec4 .\cf2 \strokec2 format\cf7 \strokec7 (\cf4 \strokec4 key\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         BigQuery.with_config\cf7 \strokec7 (\cf4 \strokec4 ConfigFileLoader\cf7 \strokec7 (\cf4 \strokec4 config_path\cf7 \strokec7 ,\cf4 \strokec4  config_profile\cf7 \strokec7 ))\cf4 \strokec4 .export\cf7 \strokec7 (\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             DataFrame\cf7 \strokec7 (\cf4 \strokec4 value\cf7 \strokec7 ),\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             table_id\cf7 \strokec7 ,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             if_exists=\cf6 \strokec6 'replace'\cf7 \strokec7 ,\cf4 \strokec4   
\f1\i \cf5 \strokec5 # Specify resolution policy if table name already exists
\f0\i0 \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\
}