# CPU & Memory Monitoring API

This repository provides a Python-based API built using Flask, which allows you to monitor CPU and memory usage on a server. The API has the following endpoints:

## Endpoints

### 1. `POST /configure`

- **Description**: Configures the server name and region for monitoring.
- **Request Body**:
    ```json
    {
      "server_name": "your_server_name",
      "region": "your_region"
    }
    ```
    - `server_name`: The name of the server (required).
    - `region`: The region of the server (required).

- **Response**:
    - **200 OK**: Server configured successfully.

### 2. `GET /system_usage`

- **Description**: Retrieves the current CPU and memory usage for the configured server.
- **Response**:
    - **200 OK**: Returns the current CPU and memory usage.
    - Example response:
    ```json
    {
      "cpu_usage_percent": 2.7,
      "memory_usage": {
        "percentage": 58.1,
        "total": 17092161536,
        "used": 9930407936
      },
      "server_name": "ghymah server",
      "timestamp": "2024-12-01 21:40:52"
    }
    ```
    - `cpu_usage_percent`: The percentage of CPU usage.
    - `memory_usage`: An object containing:
        - `percentage`: Memory usage percentage.
        - `total`: Total available memory (in bytes).
        - `used`: Used memory (in bytes).
    - `server_name`: The name of the configured server.
    - `timestamp`: The timestamp when the usage was recorded.

    - **400 Bad Request**: If the server is not configured or `server_name` is missing.
    - Example response:
    ```json
    {
      "error": "Please configure server"
    }
    ```

### 3. `POST /update`

- **Description**: Updates the server name.
- **Request Body**:
    ```json
    {
      "server_name": "new_server_name"
    }
    ```
    - `server_name`: New name for the server.

- **Response**:
    - **200 OK**: Server name updated successfully.
    - Example response:
    ```json
    {
      "message": "Server name updated successfully"
    }
    ```

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/momenmotaz/ghaymah_CPU_memory_api.git
    cd ghaymah_CPU_memory_api
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.x installed. Then install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the API**:
    To start the server, run the following command:
    ```bash
    python Cpu_memory_api_code.py
    ```
    The API will be available at `http://127.0.0.1:5000/`.

## Example Usage with `Insomnia` or `Postman`

1. **Configure the Server** (POST `/configure`):
    - URL: `http://127.0.0.1:5000/configure`
    - Method: `POST`
    - Body (JSON):
    ```json
    {
      "server_name": "ghymah server",
      "region": "us-east-1"
    }
    ```

2. **Get System Usage** (GET `/system_usage`):
    - URL: `http://127.0.0.1:5000/system_usage`
    - Method: `GET`

3. **Update Server Name** (POST `/update`):
    - URL: `http://127.0.0.1:5000/update`
    - Method: `POST`
    - Body (JSON):
    ```json
    {
      "server_name": "new_server_name"
    }
    ```

## Error Handling

- If the server is not configured, the `GET /system_usage` request will return a `400` response:
    ```json
    {
      "error": "Please configure server"
    }
    ```

## Notes

- This API is designed for local use and does not require authentication.
- The `total` and `used` memory values are in bytes. You can convert them to a more readable format (e.g., MB, GB) depending on your needs.

---

### License

This project is licensed under the momenmotaz License 
