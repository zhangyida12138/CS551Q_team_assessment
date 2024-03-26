# CS551Q_team_assessment
This is the team assessment for the course CSS551Q at the University of Aberdeen. Our goal is to build a website for the Global Rural Population Survey System using the Django framework with Python.

## Installation
1) Clone the repository to your local machine.
2) Set up and activate the virtual environment. Navigate to the project folder and execute the following commands in the terminal:
``` bash
cd CS551Q_team_assessment/
pyenv local 3.10.7 # This sets the local version of Python to 3.10.7 (Optional)
python3 -m venv .venv # This creates the virtual environment
source .venv/bin/activate # This activates the virtual environment
```
## Running the Project
1)Navigate to the 'mysite' folder and start the server.
```bash
cd mysite/
python3 manage.py runserver 0.0.0.0:8000 # Use Ctrl+C to stop the server.
```

## Program  Overview
This program was collaboratively developed by a team consisting of:

Lu Chen (Design & Frontend)
Samuel Amao (Frontend)
Roope Eemeli Paivaniemi (Frontend)
Qiancheng Luo (Backend & Test)
Wei Zhang (Backend & Test)
Jia Cao (Deploy)

### Program Structure
The program is composed of two Django applications: mysite for site basic settings and RuralPopulationAPP for the website's detailed content, alongside static files (CSS) in the static folder, templates, manage.py, and db.sqlite3.

**mysite APP**: Contains basic site settings.

**static Folder**: Houses base styles, which are referenced in other HTML files.

**templates Folder**: Includes three pages where index.html serves as the template page. about.html and another about.html inherit the index.html interface, presenting the main and about pages.

**RuralPopulationAPP Folder**: Details the website's content.

* data Folder: Stores initial data.
* models.py: Defines multiple database tables including Country, DataEntry, Region, IncomeGroup, RegionCountries, and IncomeCountries, each with an auto-incremented primary key id. Region and IncomeGroup are queried by id, and DataEntry stores data for each country from 2000 to 2023. IncomeGroup and Region have content restrictions set in the database to ensure data integrity.
* views: Handles site requests with routes for listing all countries, comparing two countries, listing all countries in a region or income group, and displaying country details. Includes error handling to prevent display errors.

* management/commands Folder: Contains parse_data.py for importing initial data into the database according to the models' structure, with error handling and data formatting.

* migrations Folder: Synchronizes the model classes with the database schema.

* The templates folder within RuralPopulationAPP differs from the root templates folder by containing HTML files for different functionalities, all inheriting from the index.html interface.

* The manage.py file is utilized for starting the server and includes error handling features.