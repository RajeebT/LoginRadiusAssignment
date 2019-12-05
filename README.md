# LoginRadiusAssignment
Voting App. User Can Register, login and vote for available candidates.Admin can access manage User  access Candidates vote count.

Ensure python 3.8 and python django module is installed in the system.

Default useful URL:
Home : http://127.0.0.1:8000/polls/

Login and Register buttons for users to vote.

Known issue: After registering a new user. URL is not redirected correcty. Though the user is created.

After Registering. 

Use http://127.0.0.1:8000/polls/login/ to login

Admin URL: http://127.0.0.1:8000/admin/
Admin can manage User. Create new Candidates for Voting List.

How to set up in Windows System?

Step1: Open CMD. Change to desired directory where the folder mysite is in the system using cd command.

#to ensure data tables are created. datables will be created in sql lite.

Step2: Type python manage.py migrate 

#create admin using below command line.

Step3: python manage.py createsuperuser

#run server using below line

Step4: python manage.py runserver.

#Create Candidates list by login in as admin 

Step5: Open browser and type http://127.0.0.1:8000/admin/ in the url.Login and Create Candidates List using add button. Also You can create New User.

#How to vote.

Step6:Type http://127.0.0.1:8000/polls/ in the browser.

Step7: Click Register and create new user if not done in Step5. After filling the form and clicking register is not redirecting. Though user is created successfully. 

To overcome this simply go to step 8 below.

Step8: Type http://127.0.0.1:8000/polls/ in the browser.Login Click on the candidate to vote in.

Step9: Goto http://127.0.0.1:8000/admin/ and check if the particular user Vote count is incremented. Repeat Step8 and Step 9 to check if the user vote is incremented.

Thanks !!!



