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

# Installing the Development Libraries for MySQL or MariaDB::

These libraries include the header files and static libraries required during the installation process of mysqlclient. The specific installation commands depend on the operating system you're using. For Debian or Ubuntu systems, you can install the development libraries for MySQL using the following command:


```sql
sudo apt-get update
sudo apt-get install libmysqlclient-dev
```

If you're using MariaDB, the corresponding commands might differ, for example:


```sql
sudo apt-get update
sudo apt-get install libmariadb-dev
```

For Red Hat, Fedora, or CentOS systems, the commands might be as follows:
```
sudo yum install mysql-devel
```
Or, for MariaDB:
```
sudo yum install MariaDB-devel
```
Setting Environment Variables (If the previous step didn't resolve the issue):
If, after installing the development libraries, pkg-config still cannot find them, you might need to manually set the MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS environment variables. These variables should point to the header files and library files locations of your MySQL or MariaDB development libraries. How to set them depends on your installation path, but generally, the commands would look like:

```
export MYSQLCLIENT_CFLAGS=`mysql_config --cflags`
export MYSQLCLIENT_LDFLAGS=`mysql_config --libs`
```
Note: In some systems, the mysql_config tool may be installed along with the client libraries or development libraries.

Installing mysqlclient:
After setting the environment variables, try installing mysqlclient:
```
pip install mysqlclient
```

## Running the Project
1)Navigate to the 'mysite' folder and start the server.
```bash
python3 manage.py runserver 0.0.0.0:8000 # Use Ctrl+C to stop the server.
```

## Program  Overview
This program was collaboratively developed by a team consisting of:

Lu Chen (Design & Frontend)
Samuel Amao (Frontend)
Roope Eemeli Paivaniemi (Frontend)
Qiancheng Luo (Backend & Test)
Wei Zhang (Backend & Test)
Jia Cao (Deplo & Test)

### Program Structure
The program is composed of two Django applications: mysite for site basic settings and RuralPopulationAPP for the website's detailed content.

**mysite Folder**: Contains basic site settings.

**static Folder**: Contains all the css files, which are referenced in other HTML files.

**features Folder**: Contains all BDD test files and test environment configuration files. If you want to run the BDD test please execute the following commands:
* Open the file **environment.py** on the folder features, change the **context.home_page_url** into your local host.
* Then execute the following commands in the terminal
```bash
behave #make sure you are now on CS551Q_team_assessment/
```
* You will see the BDD test.

**RuralPopulationAPP Folder**: Details the website's content.

* The 'data' Folder: Stores initial data.
* The 'models.py': Defines multiple database tables including Country, DataEntry, Region, IncomeGroup, RegionCountries, and IncomeCountries, each with an auto-incremented primary key id. Region and IncomeGroup are queried by id, and DataEntry stores data for each country from 2000 to 2023. IncomeGroup and Region have content restrictions set in the database to ensure data integrity.
* The 'views': Handles site requests with routes for listing all countries, comparing two countries, listing all countries in a region or income group, and displaying country details. Includes error handling to prevent display errors.

* The 'management'/'commands' Folder: Contains 'parse_data.py' for importing initial data into the database according to the models' structure, with error handling and data formatting.

* 'migrations' Folder: Synchronizes the model classes with the database schema.

* The 'templates' folder within RuralPopulationAPP differs from the root templates folder by containing HTML files for different functionalities, all inheriting from the 'index.html' interface.

* The 'tests' folder contains all the unitest files and test functionalities of the website.

**The 'manage.py'** file is utilized for starting the server and includes error handling features.

**The db.sqlite3** file is the database file containing the data from 'parse_data.py' and the tables from 'models.py'.



