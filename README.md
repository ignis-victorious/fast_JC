Testing code found at:

#  
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


#  
- [FastAPI Tutorial EP2 - Posting Data to an API (with Pydantic)](https://www.youtube.com/watch?v=w_dp6EzMST0&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=5)
## Agenda
### Accepting Post Requests - Pydantic
### Using Curl to send a payload&
### Using a router - separating routes into their own modules
### Worked example - Posting some data and writing to CSV  (Install Pandas!)

#  
- [FastAPI Tutorial EP3 - Sending Files to an API (With Aiofiles)](https://www.youtube.com/watch?v=VHlqNDg9cPM&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=3)

## Agenda 
### Accepting files via a post endpoint (Install aiofiles)
### Save the file contents
### why async?
### Sending a Post Request
curl -X POST http://127.0.0.1:5050/post-file -F "file=@myfile.txt"

#  
- [FastAPI Tutorial EP4 - Intercept Requests With Middleware](https://www.youtube.com/watch?v=P4j4mxvjtTo&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=2)
### Running the app
uvicorn main: app -port 5050
### Post request!
curl -H "User: Emagnu" http://127.0.0.1:5050/hello-world
## App → Middleware → Endpoint
### If the header contains the correct user, let them through!

#  
- [FastAPI Tutorial E5 - Query Parameters](https://www.youtube.com/watch?v=CiUu-PNxtOo&list=PLRJ25SyJ5NMYsZJMcU9RZ2WZ2TD2yHAzS&index=1)

### Query Params, what are they?
http://127.0.0.1:8000/items/?skip=0&limit=10"
### Declaring Query Params
curl "http://127.0.0.1:5050/hello-world"
curl "http://127.0.0.1:5050/hello-world?name=Emmagnu"
curl "http://127.0.0.1:5050/hello-world?name=Emmagnu&city=london"
### Optional Query Params
### Query Param Type Conversion
### Combining Path & Query Params
curl "http://127.0.0.1:5050/hello-world/Valuetest?name=Emmagnu&city=london"
curl "http://127.0.0.1:5050/hello-world/Valuetest/Moretest?name=Emmagnu&city=london"