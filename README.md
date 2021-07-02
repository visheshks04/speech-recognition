	
# **28 June 2021**
Data: https://commonvoice.mozilla.org/ (we used the corpus 3 version so as to respect the google colab memory limits)  

### How to download the data into the notebook directly from the source:  
```!wget "source_url"```  
The file gets downloaded in a tar.gz format so to extract it run the following in another cell-  
```!tar -xzvf file_name.tar.gz```  

As the file gets extracted, you may see it has a lot of tsv files. train.tsv and test.tsv are subsets of validated.tsv+invalidated.tsv so to aim at a good accuracy we can drop invalidated.tsv and only use validated.tsv   

Directory structure: Each tsv file has the following fields:  
 0   client_id   644119 non-null  object  
 1   path        644119 non-null  object  
 2   sentence    644113 non-null  object  
 3   up_votes    644119 non-null  int64   
 4   down_votes  644119 non-null  int64   
 5   age         369018 non-null  object  
 6   gender      371045 non-null  object  
 7   accent      304119 non-null  object  
 
 The `client_id` is of no special significance to us.  <br>
 The `path` is the name of the .mp3 which is a reference to later fetch a particular audio file  <br/>
 The `sentence` column has all of the corresponding sentences to the audio file  <br>
 `upvotes` and `downvotes` tell us how many people validated it as a correct speech for the sentence. We may or may not us it later as a feature  <br>
 As `age`, `gender` and `accent` already have a huge amount of null values, they are no use to us. They were no use in our project anyway so we may drop them.  <br>
