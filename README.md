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


# 安装MySQL或MariaDB的开发库:

这些库包含了mysqlclient安装过程中需要的头文件和静态库。具体的安装命令取决于你使用的操作系统。
对于Debian或Ubuntu系统，你可以使用以下命令安装MySQL的开发库：

sql
```
sudo apt-get update
sudo apt-get install libmysqlclient-dev
```

如果你使用的是MariaDB，相应的命令可能会有所不同，例如：

sql
```
sudo apt-get update
sudo apt-get install libmariadb-dev
```

对于Red Hat、Fedora或CentOS系统，命令可能如下：
```
sudo yum install mysql-devel
```
或者，对于MariaDB：
```
sudo yum install MariaDB-devel
```
设置环境变量（如果上一步没有解决问题）:
如果即便安装了开发库之后，pkg-config仍然找不到它们，你可能需要手动设置MYSQLCLIENT_CFLAGS和MYSQLCLIENT_LDFLAGS环境变量。这两个变量应该指向你的MySQL或MariaDB开发库的头文件和库文件位置。具体如何设置取决于你的安装路径，但一般来说，命令会类似于：

```
export MYSQLCLIENT_CFLAGS=`mysql_config --cflags`
export MYSQLCLIENT_LDFLAGS=`mysql_config --libs`
```
注意：在一些系统中，mysql_config工具可能随着客户端库或开发库一起安装。

安装mysqlclient:
设置好环境变量后，尝试安装mysqlclient：
```
pip install mysqlclient
```

