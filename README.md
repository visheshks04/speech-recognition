This is a journal to the project, a documentation of did’s and did not’s


22-23 June 2021

Idea Selection: After a good amount of brainstorming, we figured out a few ideas:

1) Handwriting reviewer: This came to our mind while thinking about how can we apply Machine Learning in a classroom. A student in his early age has to practice handwriting so as to get fluent at it. As the young hands are naive they are obviously not as perfect. The project aims to help them find out their weak points for them to focus on more. 
The data that can be used in this project: https://archive.ics.uci.edu/ml/datasets/Devanagari+Handwritten+Character+Dataset

2) Graphology analyzer: Graphology is the study of predicting human behaviour and personality traits using the handwriting of the individuals. The idea was to build a model that does the job of predicting.
No suitable dataset could be found for this idea. This idea was also dropped later on because most scientific researches claim there is no backing for if graphology really works and also call it pseudoscience.

3) Dropout Predictor: Students dropout of their education due to all kinds of reasons from financial issues to mental stress from the studies. The idea was to predict for a given student and its details, if the student is likely to drop or not.
The data that can be used here:
 https://data.mendeley.com/datasets/pn8k5xp37c/1
 https://github.com/nehabharambe/Student-Dropout-Prediction

4) Student grade predictor: This is about predicting a students grade based on details like age, sex, family size, family occupation etc.
Data: https://www.kaggle.com/dipam7/student-grade-prediction



With due discussion, Handwriting reviewer was finalised.


24 June 2021

Flaw in the Handwriting reviewer idea: Turns out the handwriting reviewer concept isn’t perfect. If a kid writes ‘c’ in a way that the model thinks its an ‘e’ the score will be calculated for e only and the child will be notified that he needs to work on e’s where in reality he needs to work on c’s

Few more Ideas:

5) Speech to text/images/summary: This aims at making a students life easy during the lectures. The model should recognise speech and be able to transcribe it down for later use. Another version of this idea can be to modify the model to summarise what has been transcribed (Text Summarisation). In another more advanced version of this idea this concept can be modified to display pictures alongside as the lecturer speaks, or to attach pictures in the summary/notes (GAN).
Data: https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data
	
6) Handwritten equation solver: Most students struggle solving basic algebra or equations. This can help the student by recognizing the equation from the image and helping them solve.
https://www.geeksforgeeks.org/handwritten-equation-solver-in-python/
https://www.kaggle.com/xainano/handwrittenmathsymbols

7) Self-paced Time Table: To help the staff prepare the time table. Given the data like the number of ours you are free the number of classes you can attend in a day etc, the model generates a time table.
https://nevonprojects.com/automated-college-timetable-generator/
https://irjmets.com/rootaccess/forms/uploads/AUTOMATED%20TIMETABLE%20GENERATOR%20USING%20MACHINE%20LEARNING.pdf
https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.735.9805&rep=rep1&type=pdf
http://www.ijmlc.org/papers/174-L031.pdf	
