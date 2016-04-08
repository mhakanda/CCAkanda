Insight Data Engineering - Coding Challenge
===========================================================

## Summary

The coding challenge is to clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API and calculate the average degree of a vertex (adv) in a Twitter hashtag graph over a moving 60-second window, and update this each time a new tweet appears. The coding is done in Python 3.4. For simplification (also to mimic real world problems), tweets are read from an input file sequentially, selecting eligible tweets for a sliding 60-second exclusive window, forming Hashtag graph and finally computing and writing average degree of the graph in an output file. The code was tested for the given tweets in tweets.txt and 9295 adv's (704 tweets are about rate information out of 9999 total tweets) were written in the output file. 

## Implementation details

Two main components of coding: MyGraph() Class and main() method.

###The MyGraph() Class

1. The MyGraph class is the main workhorse of my coding. It has three methods: add(nodes), remove (nodes) and avg() (also initialization to empty defaultdict(list)). add(nodes) is for adding nodes to the existing graph, remove(nodes) for removing nodes from the existing graph. Here nodes are provided as lists, sush as ['Apache','Hadoop','Spark']

2. Graph is represented as python 'dictionary' (more specifically defaultdict type) such as graph of ['Apache','Hadoop'] would be {'Apache':['Hadoop'],'Hadoop':['Apache']}

3. For any list as input to add(nodes) or remove(nodes), first all possible tuples are generated (by permutations) and then append or remove from the existing graph. For remove(nodes) method, there might be some empty keys (keys with empty values). Those empty keys do not contribute anything to adv calculation (and also mislead computation), so they are removed again.

4. In avg() method, the average degree in a vertex of a Hashtag graph is computed. The updated graph may contain same values for some keys, so for uniqueness, set function is used. Finally try-except block used, as empty graph or all disconnected graph may cause ZeroDivisionError but their advs are zero. All output is formatted in right way (truncated after two decimal places i.e. X.XX).   

###The main() method

1. Input (tweets.txt) and output file (output.txt) are opened from the command line argument. Input file  is read tweet by tweet i.e. one tweet with readline(). Escape from the while loop is done by identifying EOF.

2. Strings from the readline() are converted to dictionary by json.loads(). Good tweet is separated from bad tweet (tweet about the connection and the API rate limits) for further analysis. Datetime (also converted to datetime object) and hashtags are extracted to form a dictionary where key is datetime object and values are hashtags. This dictionary will eventually form the hashtag graphs. 

3. 60-second exclusive window (such as from 01:01:31 to 01:02:30 i.e. 60 second-th is excluded) is implemented by genrating two lists, one list to be added to the graph and one list to be removed from the graph. 

4. The two lists are used to update time:hashtag dictionary and the current graph. Finally adv is computed and written in the output file.  


## Dependency

1. The program will run with Python 3.4, so as to change the run.sh as "python3 ./src/average_degree.py ./tweet_input/tweets.txt ./tweet_output/output.txt". The program will not run with Python 2.

2. The modules json, itertools, math, sys, datetime, collections and itertools are needed to run the program.

## Conclusion

1. Python 3 is usded to solve the coding challenge.

2. 60-second exclusive sliding window is used in this coding.

3. The code has been tested successfully in Windows 8 and Ubuntu 14.04 environment.

4. Testing directory structure and output format are performed with two differrent test inputs and found okay.  