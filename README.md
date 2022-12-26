<h1>Overview:</h1> <br>
This app consists of: <br>
• embedded mySQL database <br>
• python scripts which: <br>
    - connect to the local db <br>
    - upload data to the db <br>
    - execute sql queries and return data in json or xml <br>
• pre-commit <br>
• unit tests <br>
Everything is executed by running the **docker-compose.yaml** file in docker directory, <br>
which upon execution creates images of mysql and python using the corresponding Dockerfiles. <br>
<h2>Running the app:</h2> <br>
First off you've got to activate the venv. <br>
To do that you have to run the following command from the root directory **\venv\scripts\activate**. <br>
After that you'll have the virtual environment activated. <br>
If you want to run the unit tests, go to the **tests** directory and run the **pytest** command. <br>
To start the app you have to navigate to the **docker** folder and run **docker-compose up** in the terminal. <br>
Next up you're gonna wait for the images and the container to build. <br>
And when the log in the terminal stops and you'll see following message: <br>
![Screenshot](github_tutorial.png)
Cancel the process and run **docker-compose up** once again. <br>
This is necessary due to the fact that the first time you run it, <br>
the database doesn't have enough time to be created <br>
before the python script execution (at least that's how I think it is). <br>
Alright, now that you've run **docker-compose up** the second time, <br>
you can see the logs and the queries printed in the terminal.
