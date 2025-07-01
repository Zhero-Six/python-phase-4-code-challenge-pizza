# Pizza Restaurant API

This project is a Flask-based RESTful API for managing a Pizza Restaurant domain, including restaurants, pizzas, and their associations through restaurant-pizza mappings. The API supports CRUD operations for restaurants and restaurant-pizzas, as well as read operations for pizzas, with a fully functional React frontend for interaction (not assessed).

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Seeding the Database](#seeding-the-database)
- [API Routes](#api-routes)
  - [GET /restaurants](#get-restaurants)
  - [GET /restaurants/<int:id>](#get-restaurantsintid)
  - [DELETE /restaurants/<int:id>](#delete-restaurantsintid)
  - [GET /pizzas](#get-pizzas)
  - [POST /restaurant_pizzas](#post-restaurant_pizzas)
- [Testing the API](#testing-the-api)
  - [Using Postman](#using-postman)
  - [Using Pytest](#using-pytest)
  - [Using the React Frontend](#using-the-react-frontend)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Rubric Compliance](#rubric-compliance)

## Project Overview
The Pizza Restaurant API allows users to manage restaurants, pizzas, and their associations (`RestaurantPizza`). It includes:
- Models for `Restaurant`, `Pizza`, and `RestaurantPizza` with relationships and validations.
- RESTful routes for retrieving, creating, and deleting data.
- A SQLite database for persistence.
- A React frontend (provided, not modified) for testing API functionality.

The API meets the requirements of the Phase 4 Code Challenge, including proper JSON responses, HTTP status codes, and cascading deletes.

## Technologies Used
- **Backend**: Python 3.11, Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-Migrate, SQLAlchemy-Serializer
- **Database**: SQLite
- **Frontend**: React (provided, runs on `localhost:4000`)
- **Testing**: Pytest, Postman
- **Dependency Management**: Pipenv

## Setup Instructions

### Prerequisites
- **Python 3.11+**: Ensure Python 3.11 is installed (e.g., via `pyenv`).
- **Node.js**: Required for the React frontend.
- **Pipenv**: For managing Python dependencies.
- **Git**: For cloning the repository (if applicable).

Verify Python version:
```bash
python --version

If Python 3.11 is not installed, use pyenv:bash

pyenv install 3.11.9
pyenv local 3.11.9

InstallationClone the Repository (if not already done):bash

git clone <repository-url>
cd python-phase-4-code-challenge-pizza

Set Up the Virtual Environment:bash

pipenv --python 3.11
pipenv install flask flask-sqlalchemy flask-migrate sqlalchemy-serializer flask-restful
pipenv shell

Install Frontend Dependencies:bash

npm install --prefix client

