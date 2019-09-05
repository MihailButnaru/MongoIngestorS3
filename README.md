<div align="center">
<h1> Data Ingestor Mongo -> S3 </h1>
<p1>Library that allows you to ingest data from mongo database into an s3 bucket.</p1>
</div>
<hr/>

<div align="center">

[![codebeat badge](https://codebeat.co/badges/40bccd35-c639-496a-88d2-f1e5290f46f9)](https://codebeat.co/projects/github-com-mihailbutnaru-mongoingestors3-master)

</div>


## The problem
You want to send all the collections from mongo database into S3 without touching your own implementation. As
part of this goal, MongoIngestorS3 allows you to ingest data from mongo to s3 by specifying the format of file.

## This solution
MongoIngestorS3 is a very lightweight solution allowing you to send data to s3 from mongo, and stored in either csv
or json files.

## Installation
Start by building a development environment

1. Install the dependencies of project
```
$ pip install -r requirements.txt
```
2. An example of the credentials is provided, run the credentials
```
$ source credentials.sh
```

## Samples
A short sample how to use the library
```
from src.ingestor import Ingestor

data_ingesting = Ingestor()
data_ingesting.start_ingesting('csv')
```
