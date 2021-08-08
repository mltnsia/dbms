# Database Management System
## Library Application using MongoDB & MySQL
### BT2102 (Data Management and Visualisation)
### AY2020/2021 Semester 2

#### Configuration

For usage of this project script,
1. Enter your password under mypass for every single file for the SQL connection
2. Enter your db name and collection name for the required files for MongoDB connection

(books.json file is used in this testing)

#### Admin User

Admin UserID = Admin1
Admin password = pass

#### Borrow/Reserve/Extend

For any borrow/reserve/extend actions, double-click on the specific book row to make the respective buttons appear.
A success message will be prompted upon successful operation.
Click on the refresh button to see the changes.

#### Search

Upon searching a book, double-click on the specific book row to view more details(image & description) about the book.

#### Fines

Update for fines is triggered through an event in mySQL that occurs on schedule every 1 day. Meaning that a fine will increase by $1 each day as long as the book is not returned and overdue.
Update for deleting reserved books if there are unpaid fines for a member user is triggered through an event in mySQL that occurs on schedule every 10 seconds.
