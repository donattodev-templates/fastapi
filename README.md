# PyService

Python FastAPI template for microservices - internal use only

## Setup Development Environment

1. **Install Docker**

   * Follow the instructions for your operating system on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

2. **Create `.env` File**

   * In the project root directory, create a file named `.env`.
   * Open the `.env` file and add the following lines, replacing the placeholders with your actual database credentials:

     ```
     POSTGRES_USER=your_postgres_username
     POSTGRES_PASSWORD=your_postgres_password
     POSTGRES_DB=your_postgres_database_name
     REDIS_PASSWORD=your_redis_password
     ```
    * Replace the connection string in the adapter postgres_adapter.py
3. **Start Docker Containers**

   * Open your terminal and navigate to the root directory.
   * Run the following command to start the PostgreSQL and Redis containers:

     ```bash
     docker-compose up -d
     ```

4. **Run the Application**

   * Navigate to the `pyservice/api` directory within your project.
   * Execute the following command to start the FastAPI development server:

     ```bash
     uvicorn main:app --port 8000 --reload
     ```

   * Your application should now be accessible at `http://localhost:8000`. 

**Note(s):** 
- The `--reload` flag enables automatic server restarts whenever you make changes to your code, which is helpful during development.

- The `docker-compose.yml` file is intended for use in development, creating the external services required by the application (cache and database) and making them accessible from your host machine. However, the application itself is expected to run in debug mode within the editor or IDE of your choice.