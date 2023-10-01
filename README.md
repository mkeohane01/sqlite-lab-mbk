## SQLite MiniProject 5 - CRUD operations
[![Continous Integration](https://github.com/mkeohane01/sqlite-lab-mbk/actions/workflows/cicd.yml/badge.svg)](https://github.com/mkeohane01/sqlite-lab-mbk/actions/workflows/cicd.yml)

#### Info
* Origionally Forked from https://github.com/nogibjj/sqlite-lab
* Fulfils IDS 706 Mini Project 5 using SQLite and command-line tools to perfrom CRUD operations
* Set up to use any data sets yet default uses a fithub baseball set:
    * https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv

#### USES

* Run '''python main.py''' to run Extract, Load, Query functions 
* Use crud.py to run Create, Read, Update, or Delete commands on the specified db or data
* Command Line CRUD uses:
    * Create db: '''python crud.py create --url=raw_data_url --file_path=data_file_path --db_name=DB'''
    * Read db:  '''python crud.py read --db=DB.db --query_str="SELECT..." --n_prints=n'''
    * Update db: '''python crud.py update --db=DB.db --update_query="UPDATE..."
    * Delete db"  '''python crud.py delete --db=DB.db --del_query="DELETE..."



