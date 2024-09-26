# Auction Platform API

## Overview

The Auction Platform API allows administrators to add products and start auctions on them. Authorized users can place bids on these products within a time limit. After the auction concludes, the winner is determined, and the auction is deleted. Bid winners receive a notification via email.

## Features

- Admin functionality to add products and manage auctions.
- Authorized users can place bids on products.
- Time-limited auctions with automatic winner determination.
- Email notifications for winning bidders.
- Dockerized application running with Gunicorn.
- JWT authentication for secure access.

## Requirements

- Python 3.x
- Docker
- PostgreSQL
- Email server for sending notifications

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Elwa88/Auction-Platform--bitcamp.git
   cd auction-platform-api
2. Build the Docker image:
   ```bash
   docker-compose build
3. Create a .env file in the root directory using the provided template below:
   - SECRET_KEY: Your Django secret key for security.
   - DATABASE_NAME: The name of your PostgreSQL database.
   - DATABASE_USER: The PostgreSQL user with access to the database.
   - DATABASE_PASSWORD: The password for the PostgreSQL user.
   - DATABASE_HOST: The host where your PostgreSQL database is running.
   - DATABASE_PORT: The port for connecting to PostgreSQL (default is 5432).
   - DEBUG: Set to True for development; change to False in production.
   - EMAIL_HOST_USER: The email account used to send notifications.
   - EMAIL_HOST_PASSWORD: The password for the email account.
   - DEFAULT_FROM_EMAIL: The default sender email address.
4. Start the application
   ```bash
   docker-compose up

## API Endpoints

### Authentication Endpoints

- **Register a User**
  - **Endpoint:** `POST /auth/register/`
  - **Description:** Register a new user.

- **Obtain JWT Access Token**
  - **Endpoint:** `POST /auth/token/`
  - **Description:** Get a JWT access token using username and password.

- **Refresh JWT Token**
  - **Endpoint:** `POST /auth/refresh/`
  - **Description:** Refresh the JWT token to obtain a new access token.

### Product and Auction Endpoints

- **Product List and Create**
  - **Endpoint:** `POST /api/products/`
  - **Description:** Admin adds a new product.

- **Start Auction**
  - **Endpoint:** `POST /api/auction_start/`
  - **Description:** Admin starts a new auction on a product.

- **List Active Auctions**
  - **Endpoint:** `GET /api/auction_list/`
  - **Description:** Retrieve a list of all active auctions.

### Bidding Endpoints

- **Place a Bid**
  - **Endpoint:** `POST /api/bid/`
  - **Description:** Users place a bid on an active auction.

- **List All Bids**
  - **Endpoint:** `GET /api/bid_list/`
  - **Description:** Retrieve a list of all bids made on auctions.

- **Find Auction Winner**
  - **Endpoint:** `GET /api/find_winner/<int:pk>/`
  - **Description:** Get the winner of an auction (specified by primary key `pk`) if it has ended.
