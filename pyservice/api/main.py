from fastapi import FastAPI

app = FastAPI(title="PyService Template", description="This is a internal template for fastapi")

@app.get("/hello")
def hello():
    return "Hello, World"

@app.post("/again")
def hello_again():
    return "Hello, again"
