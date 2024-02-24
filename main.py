from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/reservations}")
async def get_reservations():
    return {"reservations": ["1", "2"]}


@app.post("/reservations/{spot}")
async def get_reservations(user: str):
    return {"reservations": ["1", "2"]}
