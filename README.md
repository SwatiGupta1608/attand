#ATTANDENCE MANGAMENT SYSTEM
#SCOPE
Manually taking attendance and registering it in files & musters makes the daily attendance a mundane task for the faculty and unnecessarily consumes classroom time.

To overcome such inefficient work processes, there are various school software systems available to speed up the attendance process and reduce manual work. 
An online attendance management system or digital attendance platform is one of them, which is developed to automate the daily attendance in schools. 
Additionally, it helps to maintain accurate records and generate summarized student attendance reports.

Attendance management system keeps track of daily attendance, working hours, breaks, login, and logout time. It prevents staff's time theft.
An attendance management system integrates all attendance devices such as smart cards, biometric, and facial recognition devices in real-time.


#FRONTENED: PYTHON
#BACKEND: MYQL

#LIBERARIES:Open CV2, tkinter

#InitiaL phase runnning: the main two filesresponsible to the project are student.py amd main.py

#the project is run on local host for running the project u need to install all the files attached andsetup the environmentaccordingto requirements
here requirements are according to windows 

Project Structure
After run you need to give your face data to system so enter your ID and name in box than click on Take Images button.
It will collect 100 images of your faces, it save a images in TrainingImage folder
After that we need to train a model(for train a model click on Train Image button.
It will take 5-10 minutes for training(for 10 person data).
After training click on Automatic Attendance ,it can fill attendace by your face using our trained model (model will save in TrainingImageLabel )
it will create .csv file of attendance according to time & subject.
You can store data in database (install wampserver),change the DB name according to your in AMS_Run.py.
Manually Fill Attendace Button in UI is for fill a manually attendance (without facce recognition),it's also create a .csv and store in a database.

Screenshots

![image](https://user-images.githubusercontent.com/87253646/170864053-73abbadd-ec11-42d7-a131-8a1e97180e8f.png)

![image](https://user-images.githubusercontent.com/87253646/170864111-ec0af8a9-491e-417e-86e9-33e69fab40b6.png)

![image](https://user-images.githubusercontent.com/87253646/170864131-a01b9140-b0f5-4304-9f36-5795a4570212.png)

![image](https://user-images.githubusercontent.com/87253646/170864142-39861a58-4cab-4548-bbcd-87a0531b1f51.png)





