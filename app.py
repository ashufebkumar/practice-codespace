from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_user(request):
  pass
