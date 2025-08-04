from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scripts.query_engine import run_agent, run_transcript_query

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": []})

@app.post("/", response_class=HTMLResponse)
async def post_chat(request: Request, user_input: str = Form(...)):
    is_transcript = any(k in user_input.lower() for k in ["transcript", "call", "bagic", "rationale", "allianz", "organic traffic"])
    try:
        if is_transcript:
            response = run_transcript_query(user_input)
        else:
            response = run_agent(user_input)
    except Exception as e:
        response = f"❌ Error: {str(e)}"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "chat_history": [("You", user_input), ("Chatbot", response)],
    })
