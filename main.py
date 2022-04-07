from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, PandasUDFType

spark = SparkSession.builder.master(
    "local[1]").appName("Reddit Place").config("spark.driver.cores", "4").config("spark.driver.memory", "8g").getOrCreate()

df = spark.read.option("header", True).csv(
    "2022_place_canvas_history.csv")


@pandas_udf('string', PandasUDFType.GROUPED_AGG)
def mode(v):
    return v.mode()[0]


df.groupBy("coordinate").agg(
    mode(df["pixel_color"])).withColumnRenamed("mode(pixel_color)", "pixel_color").coalesce(1).write.option("header", True).csv("output")
