#LOG ANALYSIS

###Overview
> In this project we will work with the data that came from the fields representing information from a real-world web server. The basic aim of the project is to print a report based on data in the database by using Python and Postgresql.

###Pre-Requisites
  * [Python3]
    (https://www.python.org/)
  * [Vagrant]
    (https://www.vagrant.com/)
  * [Virtual Box]
    (https://www.virtualbox.org)

###Installation Process
  1. Install Vagrant and VirtuaBox
  2. Fork and clone the Udacity Github Repository - [fullstack-nanodegree-vm]
  3. Extract the files from the zipped file and now we see we have a newsdata.sql file. If yes then we are good to go!

###Launching the Virtual Machine
  1. Launch the VM in the sub-folder under the name vagrant in the cloned directory -  
      ```
      vagrant up
      ```

  2. To login into Vagrant -
      ```
      vagrant ssh
      ```

###Setting up the Database
  1. Load the database name news by using the commmand -
  ```
    psql -d news -f newsdata.sql
  ```
  2. Connect to the database using -  
  ```
    psql -d news
  ```

### Creating the required views
  1. article_view
      ```
      select title, author, count(title) as views from articles, log where log.path like concat('%',articles.slug) group by articles.title, articles.author order by views desc;
       ```

  2. authors_view
     ```
     select name,sum(article_view.views) as total from article_view,
     authors where authors.id=article_view.author group by authors.name order by total desc;
     ```

  3. percenterror_view
    ```
    create view percenterror_view as select date(time), round(100.00*sum(case when status = 'NOT FOUND'
    then 1 else 0 end) / count(log.status),2)
    as PercentError from log group by date(time) order by PercentError DESC;
    ```

  4. To run the program, run ```python logAnalysis.py```
