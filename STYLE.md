# Coding Style and Folder Structure Protocal
All developers are required to follow the protocoal

## Comments
- Include clear comments throughout the code to explain its logic and intent

## Imports
- Organize the imports so that longer lines are at the top and shorter ones at the bottom

## API in app.py
- Functions in app.py that call an API should follow the naming pattern function_name_api

## API Folder
- All API-related code should be placed in the api folder 
- Each module should contain only one function
- Each module name should match its function

## Function Folder
- During development you’ll naturally encounter reusable logic
- Create these shared functions in the functions folder as they are used across multiple APIs
- Each module should contain only one function
- Each module name should match its function

## API and Function Call
- API should not call another API
- function should not cal API
- API can call function
- function can call function
