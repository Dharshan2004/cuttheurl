## [1.0.1] - 20/6/2024

### Added

* **API Interface:**
  * **RESTful API Endpoints:** Introduced new endpoints to interact with the URL shortening service programmatically.
    * `POST /api/shorten`: Accepts a long URL and returns a shortened URL.
    * `GET /api/get/<short_code>`: Returns the original url.

## [1.0.0] - 13/06/2024

* **URL Shortening:**

  * Allows users to input a long URL and receive a shortened URL.
  * Shortened URLs redirect to the original long URLs.
* **Web Interface:**

  * Simple and user-friendly web interface for entering and receiving shortened URLs.
  * Basic form validation to ensure valid URLs are provided.
* **Database Integration:**

  * Stores original and shortened URLs in a database.
  * Automatically generates unique short codes for each URL.
* **Redirect Functionality:**

  * Handles URL redirection from short URLs to the original long URLs.
* **Basic Error Handling:**

  * Provides basic error pages for common issues like 404 (Not Found) and 500 (Internal Server Error).
