from fastapi import FastAPI, Form, Response
from fastapi.responses import HTMLResponse
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <h2>🔥 HotCoachApp</h2>
    <form action="/result" method="post">
        ☕ Coffees today: <input name="coffees" type="number"><br><br>
        Multitasking (0–10): <input name="multi" type="number"><br><br>
        Sleep start: <input name="sleep_start" type="time"><br><br>
        Sleep end: <input name="sleep_end" type="time"><br><br>
        <button type="submit">Evaluate</button>
    </form>
    """

@app.post("/result", response_class=HTMLResponse)
def result(
    coffees: int = Form(...),
    multi: int = Form(...),
    sleep_start: str | None = Form(None),
    sleep_end: str | None = Form(None),
):
    score = coffees + multi

    sleep_info_html = ""
    if sleep_start and sleep_end:
        try:
            fmt = "%H:%M"
            start_dt = datetime.strptime(sleep_start, fmt)
            end_dt = datetime.strptime(sleep_end, fmt)
            duration = end_dt - start_dt
            if duration.total_seconds() < 0:
                duration += timedelta(days=1)
            hours = round(duration.total_seconds() / 3600.0, 2)
            sleep_info_html = f'\n    <p><b>Sleep Today:</b> {hours} hours</p>'
        except Exception:
            sleep_info_html = "\n    <p><b>Sleep Today:</b> invalid time inputs</p>"

    return f"""
    <h2>🔥 HotCoach Results</h2>
    <p><b>Hot Mess Meter:</b> {score}/10</p>{sleep_info_html}
    <a href="/">Back</a>
    """

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

# Run locally:
#uv run uvicorn STEP0_app_html:app --reload --host 0.0.0.0 --port 8000

# make sure to kill your port
# pkill -f uvicorn || true