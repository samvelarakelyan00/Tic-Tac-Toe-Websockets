from fastapi import FastAPI


app = FastAPI(
    title='Tic Tac Toe Websockets'
)


@app.get("/")
def main():
    return {"message": "OK"}
