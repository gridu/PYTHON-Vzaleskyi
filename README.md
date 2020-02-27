# Parse GridDynamics Blog with Scrapy and visualize it
_ _ _

## Description

Imagine you are an angry and insidious HR and you want to hunt most active and public people of Grid Dynamics.<br />
You will be able to use Web Crawler to parse https://blog.griddynamics.com/, obtain articles and author information from it.<br />
And generate a report with this information.

_ _ _

## Visuals
Here is output for unit tests:

![run with correct csv](images/ok.png)

![misput articles with authors csv](images/keyerror.png)

![run with none existing file](images/notexist.png)

_ _ _

## Installation
1. Install python if you don`t have on your Mac:<br />
$ brew install python3.6
1. Clone repo https/ssh from gitlab:<br />
$ git clone https://gitlab.com/vzaleskyi/scrapy_pet_project.git<br />
$ git clone git@gitlab.com:vzaleskyi/scrapy_pet_project.git
1. Create and start venv:<br />
$ python3 -m venv venv<br />
$ source venv/bin/activate
1. Install dependencies<br />
$ pi3 install -r requirements.txt
_ _ _

## Usage
To start crawler and get report use command:
$ python report.py
_ _ _

## License & Copyright
© Valentyn Zaleskyi














