import os
#os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "D:/Spark/"

# tornar o pyspark "importável"
import findspark
findspark.init('D:/Spark/')

# iniciar uma sessão local e importar dados do Airbnb
from pyspark.sql import SparkSession
sc = SparkSession.builder.master('local[*]').getOrCreate()

# download do http para arquivo local
#wget --quiet --show-progress http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2019-07-15/visualisations/listings.csv

# carregar dados do Airbnb
df_spark = sc.read.csv("../Backup/some_file.csv", inferSchema=True, header=True)

# ver algumas informações sobre os tipos de dados de cada coluna
df_spark.orderBy('papel')