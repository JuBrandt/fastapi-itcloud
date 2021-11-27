from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers.votes import vote
from . import models
from .database import engine
from .routers import post, user, auth, votes
from .config import settings
from app import database
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()


origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):

    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/about_us", response_class=HTMLResponse)
def get_about(request: Request):

    return templates.TemplateResponse('about-us.html', {'request': request})


@app.get("/blog", response_class=HTMLResponse)
def get_blog(request: Request):

    return templates.TemplateResponse('blog.html', {'request': request})


@app.get("/post", response_class=HTMLResponse)
def get_postblog(request: Request):

    return templates.TemplateResponse('post.html', {'request': request})


@app.get("/contact", response_class=HTMLResponse)
def get_contact(request: Request):

    return templates.TemplateResponse('contact.html', {'request': request})


@app.get("/base_header", response_class=HTMLResponse)
def get_header(request: Request):

    return templates.TemplateResponse('base_header.html', {'request': request})


@app.get("/base_footer", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('base_footer.html', {'request': request})


@app.get("/1c-otchetnost", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('1c-otchetnost.html', {'request': request})


@app.get("/typography", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('typography.html', {'request': request})


@app.get("/1c-itc", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('1c-itc.html', {'request': request})


@app.get("/1s-fresh-upravlenie-nashey-firmoy", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('1s-fresh-upravlenie-nashey-firmoy.html', {'request': request})


@app.get("/theme-post", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('theme-post.html', {'request': request})
