# Ecommerce Platform

## Project Setup

This section provides instructions for setting up your development environment and the main Django project.

1. **Installation**: To work with Django, you need to install it using `pip`, Python's package manager.

2. **Create Django Project**

3. **Install pgAdmin**: If your project requires a PostgreSQL database and you prefer to use a graphical interface to manage it, you can install pgAdmin. Visit the official [pgAdmin website](https://www.pgadmin.org/download/) to download and install the appropriate version for your operating system.

4. **Activate Virtual Environment**: It's a good practice to work within a virtual environment to isolate project dependencies. You can create and activate a virtual environment using Python's built-in `venv` module:
   - On Windows:
     ```
     bash
     venv\Scripts\activate
     ```
5. **Install Django Rest Framework**: pip install djangorestframework


## Features

## This section outlines the key features and functionalities of the ecommerce platform.

### Website

#### Home Page

- **Header**
- **Latest Projects**
- **Popular Categories** (based on product download counts)
- **Popular Projects** (based on product download counts)
- **Popular Sellers** (based on product download counts)
- **Customer Ratings and Reviews**
- **Footer**

#### All Category List

- List of all product categories

#### All Product List

- List of all products according to category (sorted based on price, date added, alphabet, and views)

#### Product Details

- Detailed information about a specific product

#### Checkout Page

- Payment options: PayPal, Razorpay, Stripe

#### Order Success Page

- Confirmation page after a successful order

#### Order Failure Page

- Page displayed in case of order failure

#### Multilingual Feature

- Support for multiple languages

