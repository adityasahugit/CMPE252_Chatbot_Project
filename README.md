# CMPE252
Chatbot Project




# Canvas-Chatbot

Canvas chatbot is here to help you with all the information regarding your subject. It provides the information grading each subject, the name of the professor, grades, and other information.

Currently supported API calls to retrieve race information are:
  1. Self built API to fetch the information from Canvas to Fetch Grades
  2. Weather API
 

## *Rasa Version Used*

pc:/PROJECT$ rasa --version
Rasa Version      :         3.3.1
Minimum Compatible Version: 3.3.0
Rasa X Version    :         None
Python Version    :         3.8.15


## Instructions to run

The following process works on linux, mac or windows as a local project. (For windows, WSL used)

1. First create a virtual environment in your choice of directory using the following command and activate it: 

python -m venv venv         # Create virtual env.
source venv/bin/activate    # Activate virtual env.


2. Make sure you have all the python dependencies installed as mentioned in the provided [requirements.txt](requirements.txt) file. (Created using pip freeze in the venv itself)

3. If rasa is not installed, then install rasa using:

python -m pip install rasa  # This will install latest version of rasa


4. If you don't have a rasa project already, then you can create an initial one using the below command.

python -m rasa init         # Will create an initial rasa project

5. You can then replace the files from this repo (in [source](Source) folder) to your local project. Make sure you are using rasa 3.1.0 or above. Ensure that all files are properly placed in the respective folders in the local project. You can simply cut-paste the files from source to your project's root folder.

6. Next step is to train the rasa model using the new files. Make sure you are in the virtual environment. This can be done using the following command:

rasa train                  # This will train the model


7. To make API calls which are defined in actions.py file in the [actions](Source/actions) folder, you need to run a parallel terminal with the same virtual environment running. Use the same process as defined in step 1 above. Then to run the action file, use the following command:

rasa run actions            # This will run the actions server


8. We are now close to run the chatbot. Since the action server is up and the model has been trained, we can simply use the following command to run the chatbot.

rasa shell                  # This will run an interactive terminal for you to interact with the chatbot.


9. There you have it. You can now interact with the chatbot as you please!

10. If you wish to deploy the bot on Slack, you can follow [this](https://rasa.com/docs/rasa/connectors/slack/) link. 


## Conversation Flow

1. Grades API flow:

Your input ->  Hello

                                        Bot -> Hello! I am Canvas bot! Please share your name?

Your input ->  Aditya

                                        Bot -> Hey, Aditya how can I help you!

Your input ->  show my grades

                                        Bot ->                          Name           Out of
                                              0        Project-Related Assignments    25.00 / 25.00
                                              1               Homework Assignments    40.00 / 40.00
                                              2                Reading Assignments      0.00 / 0.00
                                              3                               Labs      0.00 / 0.00
                                              4  AI-Trends Presentation Assignment      0.00 / 0.00
                                              5         Administrative Assignments      0.00 / 0.00
                                              6     Exams, Assessments and Quizzes      1.00 / 5.00
                                              7               Imported Assignments   94.00 / 105.00
                                              8                        Assignments      0.00 / 0.00
                                              9                              Total  160.00 / 175.00


2. Weather API flow:

Your input ->  Hello

                                        Bot -> Hello! I am Canvas bot! Please share your name?

Your input ->  Aditya

                                        Bot -> Hey, Aditya how can I help you!

Your input ->  Whats the waether today

                                        Bot -> new york

Your input ->  Which city you want to check for?

                                        Bot -> Today's temperature is 5 degree Celcius.


3. Multi-turn conversations:

Your input ->  Hello

                                        Bot -> Hello! I am Canvas bot! Please share your name?

Your input ->  Aditya

                                        Bot -> Hey, Aditya how can I help you!

Your input ->  Who is Teaching assistant for this class

                                        Bot -> Shubhangi & Sumit

Your input ->  Show me mail for ISA

                                        Bot -> shubhangi.manojkumar@sjsu.edu & sumit.dutta@sjsu.edu

### Workflow of This Chatbot

![Untitled (2)](https://user-images.githubusercontent.com/40825882/206553026-971d5d61-ac4d-4bf1-91cc-1bb35ae225be.jpg)


#### Visualization of Rasa Chatbot
This is a visualization of the Dialog FLow, this chatbbot

![Rasa visualise](https://user-images.githubusercontent.com/40825882/206408103-a67f311f-e601-4fe1-9575-3aba2761a4af.png)


### Open/Current Issues in Chatbot

*  Dynamic page of Canvas makes it difficult to fetch the proper information that we need to display for users.

* This project is specific to Students of CMPE 252 class, since the Grade formatting varies for each course and due to the dynamic nature of Canvas, only for this course Grades can be fetched.
