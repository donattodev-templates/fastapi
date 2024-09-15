# Score API Documentation

## Base URL

All endpoints are prefixed with `/scores`.

## Endpoints

### 1. Get All Scores

Retrieves all scores from the database.

* **URL:** `/`
* **Method:** GET
* **Success Response:**
    * **Code:** 200
    * **Content:** Array of Score objects
* **Error Response:**
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

### 2. Get Score by ID

Retrieves a specific score by its ID.

* **URL:** `/{score_id}`
* **Method:** GET
* **URL Params:** 
    * `score_id`: UUID of the score
* **Success Response:**
    * **Code:** 200
    * **Content:** Score object
* **Error Response:**
    * **Code:** 404
    * **Content:** `{ "detail": "Score not found" }`
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

### 3. Submit New Score

Adds a new score to the database.

* **URL:** `/submit-score`
* **Method:** POST
* **Data Params:** Score object
* **Success Response:**
    * **Code:** 200
    * **Content:** Newly created Score object
* **Error Response:**
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

### 4. Replace Score

Replaces an existing score with new data.

* **URL:** `/replace-score/{score_id}`
* **Method:** PUT
* **URL Params:**
    * `score_id`: UUID of the score to replace
* **Data Params:** Score object
* **Success Response:**
    * **Code:** 200
    * **Content:** Updated Score object
* **Error Response:**
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

### 5. Update Score

Updates specific fields of an existing score.

* **URL:** `/update-score/{score_id}`
* **Method:** PATCH
* **URL Params:**
    * `score_id`: UUID of the score to update
* **Data Params:** Score object (only include fields to be updated)
* **Success Response:**
    * **Code:** 200
    * **Content:** Updated Score object
* **Error Response:**
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

### 6. Delete Score

Deletes a score from the database.

* **URL:** `/delete-score/{score_id}`
* **Method:** DELETE
* **URL Params:**
    * `score_id`: UUID of the score to delete
* **Success Response:**
    * **Code:** 200
    * **Content:** Confirmation message
* **Error Response:**
    * **Code:** 500
    * **Content:** `{ "detail": "Error: <error_message>" }`

## Data Model

The Score object has the following structure:

```python
class Score:
    id: UUID
    name: str
    math_score: int
    english_score: int
```

## Notes

* All endpoints use database session dependency injection.
* Proper error handling is implemented for all endpoints.
* The API uses FastAPI for routing and SQLAlchemy for database operations.