Testing code found at:

- [FastAPI Tutorial EP1 - Setup with Poetry, Uvicorn & Ruff James Clare](https://www.youtube.com/watch?v=cUVUnv9gA8c&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=5)

# The entrypoint for the app.
### Running the app
uvicorn main:app --port 5050
### Sending a Get Request
curl http://127.0.0.1:5050/hello-world
### Sending a Post Request
curl -X 'POST' 'http://127.0.0.1:5050/submit-score' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "name": "John",
  "math_score": 66,
  "english_score": 85
}'
- [FastAPI Tutorial EP2 - Posting Data to an API (with Pydantic)](https://www.youtube.com/watch?v=w_dp6EzMST0&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=5)
## Agenda
### Accepting Post Requests - Pydantic
### Using Curl to send a payload&
### Using a router - separating routes into their own modules
### Worked example - Posting some data and writing to CSV

- [FastAPI Tutorial EP3 - Sending Files to an API (With Aiofiles)](https://www.youtube.com/watch?v=VHlqNDg9cPM&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=3)
- [FastAPI Tutorial EP4 - Intercept Requests With Middleware](https://www.youtube.com/watch?v=P4j4mxvjtTo&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=2)
- [FastAPI Tutorial E5 - Query Parameters](https://www.youtube.com/watch?v=CiUu-PNxtOo&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=1)