from fastapi import FastAPI, Form, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <h2>🔥 HotCoachApp</h2>
    <form action="/result" method="post">
        Coffees today: <input name="coffees" type="number"><br><br>
        Multitasking (0–10): <input name="multi" type="number"><br><br>
        <button type="submit">Evaluate</button>
    </form>
    """

@app.post("/result", response_class=HTMLResponse)
def result(coffees: int = Form(...), multi: int = Form(...)):
    score = coffees + multi
    return f"""
    <h2>🔥 HotCoach Results</h2>
    <p><b>Hot Mess Meter:</b> {score}/10</p>
    <a href="/">Back</a>
    """

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

# Run locally:
#uv run uvicorn STEP0_app_html:app --reload --host 0.0.0.0 --port 8000

# make sure to kill your port
# pkill -f uvicorn || true