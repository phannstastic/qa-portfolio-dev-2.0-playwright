# QA Portfolio 2.0 - Playwright Test Automation Suite

Automated end-to-end regression testing framework for [irfanLab](https://www.irfanlab.my.id) built with **Playwright Python** and **pytest**, utilizing the Page Object Model (POM) pattern and GitHub Actions CI/CD.

## Features

- **Page Object Model (POM)** architecture for maintainable and reusable locators and actions (pages/login_pages.py, pages/admin_pages.py).
- **Authentication & Dashboard Testing**: Automated tests for admin authentication flows and CMS management.
- **GitHub Actions CI/CD Integration**: Automatically executes tests on every push, pull_request, or manual workflow_dispatch.

## Tech Stack

- **Language**: Python 3.11+
- **Test Runner**: Pytest (pytest-playwright)
- **Browser Automation**: Playwright (Chromium)
- **CI/CD**: GitHub Actions

## Local Setup

1. **Clone the repository:**
   `ash
   git clone https://github.com/phannstastic/qa-portfolio-dev-2.0-playwright.git
   cd qa-portfolio-dev-2.0-playwright
   `

2. **Set up virtual environment & install dependencies:**
   `ash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install pytest-playwright python-dotenv
   playwright install chromium
   `

3. **Configure Environment Variables:**
   Copy .env.example to .env and fill in your admin credentials:
   `nv
   ADMIN_EMAIL=your_admin_email@example.com
   ADMIN_PASSWORD=your_admin_password
   `

4. **Run the Tests:**
   `ash
   # Run all tests
   pytest

   # Run with headed browser
   pytest --headed

   # Run specific test file
   pytest tests/tests_login.py
   pytest tests/tests_admin.py
   `

## CI/CD Pipeline

The GitHub Actions workflow (.github/workflows/playwright.yml) runs on:
- Every push to main / master
- Every pull_request to main / master
- Manual trigger via **Actions** tab (workflow_dispatch)

Ensure ADMIN_EMAIL and ADMIN_PASSWORD are configured under **Settings > Secrets and variables > Actions** in the GitHub repository.