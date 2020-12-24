import uvicorn
from SkyBlue.asgi import application


uvicorn.run(application, host="192.168.0.187", port=80, debug=True)
