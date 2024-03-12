# DB_HW_2
This is the 2nd homework assignment for topics in databases.


## Exercise 1: Data Crawling
Crawl WikiCFP for "Big Data", "Machine Learning", and "Artificial Intelligence" conferences and their
location every year.
Crawl all 20 pages for big data, machine learning and artificial intelligence.
The output of the crawling should be in the tab separated format:
```
conference_acronym  conference_name conference_location
```
* The policy states at most 1 query per 5 seconds, so please set the limiter to 9 or 10 seconds (it might take a bit longer to run so you might want to let your crawler run and go
to dinner and/or watch a movie in the meanwhile).

### Setup

* venv
* python requirements
    * python version
    * requests
    * bs4
    * pandas
    * selenium
        * selenium==4.18.1 (for requirement.txt)

### Errors 
Big data doesn't have 20 pages.
* [Link for proof](http://www.wikicfp.com/cfp/servlet/tool.search?q=big+data&year=a)
* ![Image proving that big data only returns 1 page](./images/big_data_not_20_pages.png)

## Exercise 2
TODO write about consider cases such as empty locations/online, repeatedly posted conferences, etc.

## Exercise 3
hdfs dfs -rm -r -f /user/shanemay/exercise_3/output/num_conference_per_city    
`hadoop namenode -format`
Run: `start-all.sh`
Go to: http://localhost:9870
`hdfs dfs -mkdir -p /user/shanemay/exercise_3/input`
```
hadoop jar /opt/homebrew/Cellar/hadoop/3.3.6/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-file "num_conference_per_city_mapper.py"     -mapper "num_conference_per_city_mapper.py"  \
-file "num_conference_per_city_reducer.py"   -reducer "num_conference_per_city_reducer.py" \
-input /user/shanemay/exercise_3/input/MAY_EXERCISE_2_OUTPUT.csv -output /user/shanemay/exercise_3/output/num_conference_per_city
```
`hadoop fs -get /user/shanemay/exercise_3/output/num_conference_per_city num_conference_per_city`
### number of conferences per city
    * create plot
    * 1 mapper and 1 reducer
`hdfs dfs -put MAY_EXERCISE_2_OUTPUT.csv /user/shanemay/exercise_3/input`
* list of conferences per city
    * 1 mapper and 1 reducer
* list of cities per conference (regardless of year)
    * 1 mapper and 1 reducer
* number of conferences per city per year (time series plot)
    * create plot
    * not limited to 1 mapper and 1 reducer