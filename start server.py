import uvicorn
from SkyBlue.asgi import application


uvicorn.run(application, host="localhost", port=8000, debug=True)
