from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import col, when
from pydeequ.analyzers import Completeness, Size, ApproxCountDistinct, Correlation, AnalysisRunner, Mean, AnalyzerContext
import pydeequ

spark = (SparkSession
    .builder
    .config("spark.jars.packages", pydeequ.deequ_maven_coord)
    .config("spark.jars.excludes", pydeequ.f2j_maven_coord)
    .getOrCreate())

spark.conf.set('spark.sql.repl.eagerEval.enabled', True)  

df1 = (spark
    .read
    .format("csv")
    .option("header", "true")
    .option("encoding", "ISO-8859-1")
    .load("../Backup/some_file.csv"))

analysisResult = (AnalysisRunner(spark)
                .onData(df1)
                .addAnalyzer(Size())
                .run())

analysisResult_df = AnalyzerContext.successMetricsAsDataFrame(spark, analysisResult)
analysisResult_df.show()                    