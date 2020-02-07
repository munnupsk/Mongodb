



import pymongo


#create a mongodb client
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
                           #protocol ip address  port no
                        
# create database

mydb=client['Employee']

#create collection

information=mydb.employeeinformation 


#create a json formate in the form of key value pair

record={
        'first name': 'prasanna kumar',
        'last name':'sathunuri',
        'department':'analytics'}

information.insert_one(record)  

record=[{
        'first name': 'vinay kumar',
        'last name':'malhotra',
        'department':'Drawing'},
        {
        'first name': 'naveen kumar',
        'last name':'mal',
        'department':'software developer'}]


information.insert_many(record)                       
