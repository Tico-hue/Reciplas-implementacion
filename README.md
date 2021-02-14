# Reciplas-implementacion

This is an implementation of 'Update suppliers' use case. 

## Use Case

#### Name: Update supplier.  
#### Actor: Purcharses employee.  
#### Pre-condition: Purcharses employee logued in and with permission to modify a supplier.  
##### Description: Purcharses employee update supplier data. 
#### Post-conditions: Supplier data modified.  
#### Steps:
 
1. Purcharses employee select modify a supplier.
2. System requests new data to update. 
4. Purcharses employee types new data.
5. System verifies data.
6. System saves the changes and shows a succes message. 
7. End of use case. 


## Classes Diagram 
![](screenshots/classesDiagramUpdateSupplier.jpg? "classes diagram update supplier")

## Sequence Diagram

![](screenshots/sequenceDiagramupdateSupplier.jpg? "sequence diagram update supplier")


## Features

##### Update suppliers 

## Technologies used
#### Django 
#### Ajax
#### SqlServer
#### Bootstrap
#### JQuery 



## Screenshots
#### Suppliers Page
![](screenshots/supplierPage.jpg? "suppliers")
#### Update supplier Form
![](screenshots/updateSupplierForm.jpg? "suppliers update form")


## Installation

Place yourself in 
```console
projectReciplas\requiremnts
``` 
and run in your console (You can use virtualenv) 
```console
pip intall -r requirements.txt
```

After that, you have to create a DB called 'Reciplas' in SQLServer
or if you want to use another DBM you must change it in 
```console
\projectReciplas\reciplas\settings\local.py
```
```json 
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Reciplas',
        'Trusted_Connection':'yes',
        'HOST':'localhost\SQLEXPRESS',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0'
        },
    },
 ```
Then, place yourself in \projectReciplas\reciplas\ and run 
```console
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
Now you can just open it in your browser
```console
localhost:8000 
```
