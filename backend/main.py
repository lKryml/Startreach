import uvicorn
from utils.logger import logger
from init import initializeApp

app = initializeApp
logger.info("Starting the server")

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000,factory=True)