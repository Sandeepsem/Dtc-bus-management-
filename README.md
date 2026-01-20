DTC Bus Service Project

This project simulates a bus service management system for the Delhi Transport Corporation (DTC) with two main components: an SQL database for managing the bus data and a Python application for interacting with it.

Database Structure (SQL File)
The SQL file defines the following tables:
1.**staff**: Stores staff details including the bus number, driver, conductor, marshal, number of rounds per day, and timing.
    * Relationships: Linked to the bus table via bus_no (foreign key).

2.earnings_summary: Contains the daily earnings summary for each bus, including bus number, fare, rounds per day, average passengers, and daily earnings.
3.customer_feedback: Allows customers to submit feedback and ratings for buses.
  * Relationships: Linked to the bus table via bus_no (foreign key).
4.bus: Stores details about each bus, such as its number, source, destination, route, stops, timing, and fare.
5.admin: Holds admin login credentials (username and password).

Key Relationships:
  Foreign Keys:
  * staff and customer_feedback tables reference the bus table via bus_no.
  * staff table also references the bus table with bus_no for mapping staff to         specific buses.

Python Application Overview
The Python code facilitates interactions between users, admins, and the database:

Libraries Used:
* mysql.connector: For connecting to the MySQL database.
* pandas: For handling and displaying data in tabular format.
* matplotlib: For generating visual charts (e.g., bus fare comparison).
* tabulate: For formatting and displaying data in a readable table format.

Core Features:
1.User Functions:
  * View all buses.
  * Search for buses by number, between two stops, or passing through a specific           stop.
  * Add feedback with ratings for buses.

2.Admin Functions:
* Login and authentication.
* View all buses and staff.
* Add, delete buses and staff.
* View earnings summary and customer feedback.
* Generate analytics charts (e.g., bus fare comparison).

Functionality Flow:
* User Panel:

    *Provides functionality for searching buses, viewing all buses, and submitting     feedback.

* Admin Panel:

     * Allows admins to manage buses, staff, view earnings summaries, and                 customer feedback, as well as generate charts for bus fares.

* Menu System:

    *The system is interactive with a main menu that branches into user and admin       panels. The admin has more control, including the ability to add/delete buses       and view earnings/feedback data.

* How It Works:

  * The Python code connects to a MySQL database (dtc_bus_service1).

  * User and admin operations are executed via SQL queries (CRUD operations).

  * The admin has full access to manage buses, staff, earnings, and customer         feedback.

  * The user can interact with the system by searching for buses, getting details,   and submitting feedback.

  * This project is a simple example of how to manage a bus service using SQL and     Python, integrating data management, user interaction, and data visualization.

Setup Instructions:

1.Import the SQL schema to your MySQL database.

2.Install the required Python libraries:

        pip install mysql-connector-python pandas matplotlib tabulate


3.Run the Python script to start the application.
