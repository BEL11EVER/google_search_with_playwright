import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.google.com')
        await page.wait_for_selector('#APjFqb', timeout=10000)  # Wait for the search box to appear
        await page.fill('#APjFqb', 'islam')  # Fill in the search box with the query
        await page.press('#APjFqb', 'Enter')  # Press Enter key
        await page.wait_for_selector('h3')  # Wait for search results to load
        results = await page.query_selector_all('h3')  # Find all search result titles
        for result in results:
            print(await result.inner_text())  # Print each search result title
        await browser.close()  # Close the browser when done

asyncio.run(run())
