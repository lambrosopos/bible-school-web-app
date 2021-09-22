from django.urls import resolve
from app.views import main_page

def test_root_url_returns_main_page_func():
    found = resolve('/')
    assert found.func == main_page
