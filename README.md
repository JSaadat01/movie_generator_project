# movie-generator

## Contents
* [Introduction ](#introduction )
   * [Objective](#objective)
   * [My Project Proposal ](#my-project-proposal )
* [Software Architecture ](#software-architecture )
   * [Project Tracking ](#project-tracking)
   * [Risk Assessment](#risk-assessment)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [CI Pipeline](#ci-pipeline)
* [Software Infrastructure](#software-infrastructure)
   * [Jenkins](#jenkins)
   * [Swarm Configuration](#swarm-configuration)
   * [Services Setup](#Services-Setup)
* [Testing](#testing)
* [Future Improvements](#future-improvements)
* [Author](#author)

## Introduction 
### Objective
This is an individual project in order to meet the SFIA requirements. The objective of this project is to create a web application based on the microservice architecture. Which allows us to split up the application into more manageble bits as opposed to one monolithic application.

The services are to create an “object” which will either be used or displayed by the other services. Service 1 will be the core service, i.e. the front-end that the user will see. Here will contain the relevant html files. Also, this service will communicate with the other services. Service 2 and 3 will each generate a random object that will be sent to service 1. Service 4 will generate an object based on the response from service 2 and 3. 

The constraints are as follows: 
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

### My Project Proposal 
The idea I went with is a website that produces a movie based on a location and weather. The user will first connect to service 1 which will display the webpage, but before displaying the page, a GET request is made to service 2 and service 3. Service 2 will return a random location, and service 3 a random weather. Then a POST request is made to service 4 sending the location and weather information obtained from the previous GET requests. Service 4 will then choose a film based on that information.

## Software Architecture 
### Project tracking
For project tracking, I decided to use Trello board. Trello board is a nice lightweight tool to help organise what tasks need to be done. I have set it up such that there is several lists each containing cards related to that list. Each card may contain colour coded labels which represent what that particular card is related to. I have also decided to use the MoSCow approach, which are also shown on the cards as labels. The lists I've made are as follows:
* Project Resources - Containing relevant links
* User Stories - Each card has the format "As a [User]..., I want... [Feature], so that... [Details]"
* Backlog - Tasks needed to be done
* In-Progress - Tasks currently being worked on
* Testing - Features that need to be tested
* Complete - All completed tasks
* Issues - Any issues that came up

![kanban_board](https://user-images.githubusercontent.com/73299366/105685604-2a4f4e80-5eee-11eb-9f0c-4cb49d51dca2.JPG)


### Risk Assessment
![Risk_Assessment](https://user-images.githubusercontent.com/73299366/105685674-3cc98800-5eee-11eb-8c96-ab46ec2cd399.JPG)


### Entity Relationship Diagram
For the sake of this project, only one ERD is needed. The image below shows the "Movie" ERD which contains the id, name, location and weather. This table will help us create data that persists in the database after each refresh.
![Movie_erd](https://user-images.githubusercontent.com/73299366/105685717-49e67700-5eee-11eb-8624-e74e3eb2d3b7.JPG)

### CI Pipeline
The image below shows the CI Pipeline used for this project. The first thing to be done is to grab a task from the trello board, then after completing that task, the code is pushed to GitHub which triggers a webhook. This then starts the Jenkins pipeline, first the tests are done. Then using Docker-compose, the images are built and pushed to Dockerhub. Jenkins then uses Ansible to configure external nodes, including installing docker on them. Anisble also configures an NGINX node to act as a load balancer. The user connects to the load balancer and recieves the webpage. 

![CI-Pipeline](https://user-images.githubusercontent.com/73299366/105685792-61bdfb00-5eee-11eb-8b8d-63db57953ad7.JPG)


## Software Infrastructure
### Jenkins 
Jenkins is an open source automation server that automates many parts of the project, including testing and deployment. This helps facilitate continous integration and deployment. For this project, the stages of the Jenkins pipeline is as follows: 
* Testing - Which produces coverage reports on the console
* Build and push images - Docker-compose is used to build the images and push them to Docker-Hub
* Ansible configuration - Allows us to configure several servers at once, including
* * Installing necessary dependencies
* * Initializing the swarm and connecting to worker nodes
* * Configuring the NGINX server for load-balancing
* Deploy stack - Configures the web-applcation on the manager and worker nodes

Details on the stages used in the Jenkins pipeline can be found in the jenkinsfile. 

### Swarm Configuration
The below image shows the basic set up of the swarm. After Ansible installs docker on both swarm-manager and swarm-worker nodes, it then initialises the swarm on the manager node and joins the worker nodes. 
![swarm](https://user-images.githubusercontent.com/73299366/105685854-79957f00-5eee-11eb-85bd-6ae8db0616f8.JPG)

### Services Setup
As mentioned before, the project must include atleast 4 services as part of the MVP. The below image shows the set up of the services for this project.  The front-end recieves GET requests from service 1 and 2, then posts that information to service 4, which returns an object, this is a simple set up. 
![services](https://user-images.githubusercontent.com/73299366/105685888-84501400-5eee-11eb-8d29-8e4ea46acba3.JPG)

## Testing
For this project, I have decided to implement unit testing in the application. Unit testing allows us to test whether each functions returns an expected response. The images below show information on how many tests have passed and how many lines have been covered, these have posted on coverage reports for easy viewing.

![s1r](https://user-images.githubusercontent.com/73299366/105688687-cd559780-5ef1-11eb-87e4-df9a457ced6d.JPG)
![s2r](https://user-images.githubusercontent.com/73299366/105688705-d0e91e80-5ef1-11eb-93c1-d04adf6281a5.JPG)
![s3r](https://user-images.githubusercontent.com/73299366/105688708-d34b7880-5ef1-11eb-8394-0ebcb2c3e0c0.JPG)
![s4r](https://user-images.githubusercontent.com/73299366/105688712-d47ca580-5ef1-11eb-963e-261c485018d1.JPG)


The command used to produce the report is:
```py
python3 -m pytest --cov --cov-config=code/.coveragerc --cov-report term-missing --cov-report xml --junitxml junit.xml
 ```
A junit.xml is also produced which allows us to make use of a Jenkins plugin called Junit. This gives us a graphical view of the test results, making it easier to debug if any errors arise. 

![testing](https://user-images.githubusercontent.com/73299366/105688476-8d8eb000-5ef1-11eb-9570-01248b05ad21.JPG)

The graph shows that in the latest build all tests have passed, as well as 100% coverage. 

## Future Improvements 
There are many improvements that can be made to the application. However, to name a few:

* Implement an external api call to get the users location, and the weather 
* Reduce downtime by using NEXUS as opposed to Dockerhub
* Add more testing to make it even more robust, including integration testing 

## Author
Yusuf Yasin 