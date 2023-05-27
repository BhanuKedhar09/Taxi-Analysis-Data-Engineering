{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red193\green152\blue86;\red16\green16\blue16;\red255\green255\blue255;
\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;}
{\*\expandedcolortbl;;\cssrgb\c80392\c65882\c41176;\cssrgb\c7843\c7843\c7843;\cssrgb\c100000\c100000\c100000;
\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  io\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  pandas \cf2 \strokec2 as\cf4 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  requests\cb1 \
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 'data_loader'\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 globals\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.decorators \cf2 \strokec2 import\cf4 \strokec4  data_loader\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 'test'\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 globals\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 from\cf4 \strokec4  mage_ai.data_preparation.decorators \cf2 \strokec2 import\cf4 \strokec4  test\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 @data_loader\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  load_data_from_api\cf6 \strokec6 (\cf4 \strokec4 *args\cf6 \strokec6 ,\cf4 \strokec4  **kwargs\cf6 \strokec6 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Template for loading data from API\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     url = \cf5 \strokec5 'https://storage.googleapis.com/taxi-data-engineering/uber_data.csv'\cf4 \cb1 \strokec4 \
\cb3     response = requests.get\cf6 \strokec6 (\cf4 \strokec4 url\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 return\cf4 \strokec4  pd.read_csv\cf6 \strokec6 (\cf4 \strokec4 io.StringIO\cf6 \strokec6 (\cf4 \strokec4 response.text\cf6 \strokec6 ),\cf4 \strokec4  sep=\cf5 \strokec5 ','\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 @test\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  test_output\cf6 \strokec6 (\cf4 \strokec4 output\cf6 \strokec6 ,\cf4 \strokec4  *args\cf6 \strokec6 )\cf4 \strokec4  -> \cf2 \strokec2 None\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Template code for testing the output of the block.\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 assert\cf4 \strokec4  output \cf2 \strokec2 is\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 None\cf6 \strokec6 ,\cf4 \strokec4  \cf5 \strokec5 'The output is undefined'\cf4 \cb1 \strokec4 \
\
}