# Student-Management
## Project Title
## Student Management System

## Overview
A simple Python-based command-line application for managing student records. This system allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student data, including adding new students, viewing all records, searching by roll number, updating information, and deleting records.

## Features
Add New Students: Create new student records with name, roll number, and marks for two subjects

View All Records: Display all student records in a formatted manner

Search Functionality: Find specific students by their roll number

Delete Records: Remove student records from the system

Update Information: Modify existing student details including name and marks

Duplicate Prevention: System prevents adding students with duplicate roll numbers

Input Validation: Basic validation for user inputs

## Technologies/Tools Used
Programming Language: Python 3.x

Core Libraries: Standard Python libraries (no external dependencies)

Data Structure: Lists and custom classes

Paradigm: Object-Oriented Programming (OOP)

## Steps to Install & Run the Project
Prerequisites
Python 3.x installed on your system

Basic command-line interface knowledge

## Installation Steps
Download the Code

Save the provided Python code as student_management.py

Verify Python Installation

bash
python --version
or

bash
python3 --version
Run the Application

bash
python student_management.py
or

bash
python3 student_management.py
## Instructions for Testing
Testing the Application
Start the Application

Run the program using the commands above

You should see the welcome message and menu

Add New Students (Option 1)

Test with valid inputs

Try adding duplicate roll numbers to test validation

Test with various mark values

View All Records (Option 2)

Use this after adding students to verify they were saved correctly

Test with empty database to see the "No record" message

Search Function (Option 3)

Search for existing roll numbers

Search for non-existent roll numbers to test error handling

Delete Records (Option 4)

Delete existing students and verify removal

Try deleting non-existent records

Update Information (Option 5)

Modify existing student records

Test partial updates (changing only some fields)

Try updating non-existent records

Exit Program (Option 6)

Test clean exit functionality

