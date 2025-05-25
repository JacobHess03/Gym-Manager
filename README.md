GymManager

This repository hosts a gym client management system written in Python, built with an object-oriented approach. The program handles client registration and login, manages annual memberships, course enrollment, seasonal discounts, and differentiates between standard and premium (plus) clients.
Key Features

    Client Registration (Standard/Plus) with input validation.
    Client Login with membership verification.
    Course Management (Yoga, Gym, Pilates, Karate).
    Monthly Discounts based on course type.
    Annual Membership System with expiration dates and active/inactive status.
    View and Modify Client Data.
    Separate Admin Interface from the client interface.

Project Structure
    Plaintext
    
    ├── main.py               # Application entry point with Admin/User menu
    └── README.md             # This file

For simplicity, the project is contained within a single Python file, but it's structured to allow for easy modularization.
Main Classes

    Cliente (abstract)
    ClienteStandard
    ClientePlus (30% annual discount)
    Tessera (Membership Card)
    Admin

How to Use the Program
Requirements

    Python 3.10 or higher

Execution
Bash

    python main.py

Available Modes

    Admin: Can register/modify clients, view all client data, and see monthly discounts.
    User: Can register, log in, check their membership status, and view the month's discounts.

Security

    The tax code (Codice Fiscale) must be 16 characters long.
    Passwords must be at least 9 characters long.

Membership System

Each client receives an annual membership upon registration. The membership expires 365 days from the activation date. The system automatically verifies membership validity upon login.
Seasonal Discounts

Discounts vary based on the course and the current month. Here's an example:

    Course  | Months with Discount | Discounted Price
    Yoga    | Apr, May, Jun        | €35
    Pilates | Jan, Feb, Mar        | €35
    Gym     | Jul, Aug, Sep        | €35
    Karate  | Oct, Nov, Dec        | €40

Usage Example

Select your option:
    
    1. ADMIN
    2. USER
    0. Exit
    > 1

    --- Admin Menu ---
    1. Add Client
    2. Modify Client
    3. Verify Client Membership
    4. View All Clients
    5. View monthly discounts for clients
    0. Exit

Authors: Giacomo Visciotti, Giuseppe Del Vecchio
