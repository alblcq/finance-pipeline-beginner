# Personal Finance (Dummy data) Pipeline

An ETL pipeline for credit car transactions: downloads the dataset from Kaggle, transforms the data, loads to PostgreSQL, and visualize spendings.

## Setup
1. Install Docker and Python 3.9+
2. Set up 'config/.env' with DB credentails and Kaggle_dataset
3. Run PostgreSQL using the next command: `docker run -d --name postgres-db -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=transactiondb -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:latest`.
4. Install deps: `pip install -r requirements.txt`.
5. Run: `python src/main.py` or `docker build -t finance-pipeline . && docker run ...`

## Structure
src/: ETL and Visualization scripts
tests/: Unit Tests (run pytest)
docs/: Outputs like a png image from the data visualization

## Challenges Overcome
This used to be a single file code
Added Logging, testing and Docker for robustness

Demo: https://github.com/alblcq/finance-pipeline-beginner/tree/main