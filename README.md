# Parse GridDynamics Blog with Scrapy and visualize it
_ _ _

## Description

Imagine you are an angry and insidious HR and you want to hunt most active and public people of Grid Dynamics.<br />
You will be able to use Web Crawler to parse https://blog.griddynamics.com/, obtain articles and author information from it.<br />
And generate a report with this information.

_ _ _

## Visuals
Here is output for unit tests:

![run with correct csv](/uploads/6cdfe9c3196d41555089136575ae3ddd/Screen_Shot_2020-02-26_at_3.51.48_PM.png)

![misput articles with authors csv](/uploads/07d10c49c1a570dcfa18faf2e325dfcf/Screen_Shot_2020-02-26_at_3.55.04_PM.png)

![run with none existing file](/uploads/1264dac50adaaaf128b3b6914c4e3f5d/Screen_Shot_2020-02-26_at_4.04.24_PM.png)

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














