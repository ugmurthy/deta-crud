from fastapi import FastAPI
from routes.device import router as DeviceRouter
from fastapi.responses import HTMLResponse

import os
from markdown import markdown as md 

with open("index.html","r") as f:
	html = f.read()

with open("README.md",'r') as f:
	md_content = f.read()
	content = md(md_content)

html = html.replace("{{README}}",content)


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_root():
	return html
	
app.include_router(DeviceRouter,tags=["Device"])



