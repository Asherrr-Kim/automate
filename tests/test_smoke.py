import re
from playwright.sync_api import Page, expect


def test_restful_booker_api_is_alive(page: Page):
    response = page.request.get("https://restful-booker.herokuapp.com/ping")
    assert response.status == 201


def test_playwright_homepage_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))