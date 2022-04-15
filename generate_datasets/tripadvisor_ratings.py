import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, types, functions
spark = SparkSession.builder.appName('Tripadvisor restaurant ratings').getOrCreate()
assert spark.version >= '2.4' # make sure we have Spark 2.4+
spark.sparkContext.setLogLevel('WARN')

# Clean Tripadvisor data
ratings_schema = types.StructType([
    types.StructField('id', types.IntegerType()),
    types.StructField('awards', types.MapType(types.StringType(), types.StringType())),
    types.StructField('priceLevel', types.StringType()),
    types.StructField('latitude', types.DoubleType()),
    types.StructField('longitude', types.DoubleType()),
    types.StructField('rankingDenominator', types.LongType()),
    types.StructField('rankingPosition', types.LongType()),
    types.StructField('rating', types.DoubleType()),
    types.StructField('numberOfReviews', types.LongType())
])
    
tripadvisor_df = spark.read.option("multiline","true").json('dataset_tripadvisor.json')
tripadvisor_df = tripadvisor_df.withColumn('awards_num', functions.size(tripadvisor_df['awards']))
tripadvisor_df = tripadvisor_df.select('id', 'latitude', 'longitude', 'awards_num', 'priceLevel',
    'rankingDenominator', 'rankingPosition', 'rating', 'numberofReviews')
tripadvisor_df = tripadvisor_df.dropna(subset=['rating', 'latitude', 'longitude', 'rankingPosition', 'rankingDenominator', 'priceLevel', 'awards_num'])
tripadvisor_df = tripadvisor_df.withColumnRenamed("latitude", "lat")
tripadvisor_df = tripadvisor_df.withColumnRenamed("longitude", "lon")

tripadvisor_df.toPandas().to_csv('dataset_tripadvisor_clean.csv')
