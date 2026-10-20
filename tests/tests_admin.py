import time
import pytest
from playwright.sync_api import Page, expect
from pages.admin_pages import AdminPage


# Generate unique test data for this run to keep test data isolated and clean
RUN_ID = int(time.time())
TEST_EXP_COMPANY = f"[TEST] QA Experience {RUN_ID}"
TEST_TECH_NAME = f"[TEST] Skill_{RUN_ID}"
TEST_PROJECT_TITLE = f"[TEST] Project {RUN_ID}"
TEST_PROJECT_SLUG = f"test-project-{RUN_ID}"
TEST_ARTICLE_TITLE = f"[TEST] Article {RUN_ID}"
TEST_ARTICLE_SLUG = f"test-article-{RUN_ID}"


# ==============================================================================
# SECTION 1: OVERVIEW & DASHBOARD STATS
# ==============================================================================

def test_overview_statistics_cards(admin_page: AdminPage):
    """
    Test 1: Memverifikasi halaman Dashboard Overview dan kartu statistik utama.
    """
    admin_page.go_to_overview()

    # Assert overview aktif dan kartu statistik tampil
    expect(admin_page.view_overview).to_be_visible()
    expect(admin_page.stat_projects_count).to_be_visible()
    expect(admin_page.stat_experiences_count).to_be_visible()
    expect(admin_page.stat_tech_stacks_count).to_be_visible()


# ==============================================================================
# SECTION 2: WORK EXPERIENCES
# ==============================================================================

def test_navigate_to_experiences(admin_page: AdminPage):
    """
    Test 2: Memverifikasi navigasi ke menu Work Experience berhasil.
    """
    admin_page.go_to_experiences()

    expect(admin_page.view_experiences).to_be_visible()
    expect(admin_page.btn_create_experience).to_be_visible()
    expect(admin_page.experiences_tbody).to_be_visible()


def test_open_and_close_experience_modal(admin_page: AdminPage):
    """
    Test 3: Memverifikasi modal Add Experience dapat dibuka dan ditutup.
    """
    admin_page.open_create_experience_modal()

    expect(admin_page.modal_experience).to_be_visible()
    expect(admin_page.input_exp_company).to_be_visible()
    expect(admin_page.input_exp_role).to_be_visible()

    # Batalkan / tutup modal
    admin_page.modal_experience.locator("button[data-close-modal]").filter(has_text="Cancel").click()
    expect(admin_page.modal_experience).not_to_be_visible()


def test_create_new_experience(admin_page: AdminPage):
    """
    Test 4: Menambahkan data Work Experience baru.
    """
    admin_page.open_create_experience_modal()

    admin_page.fill_and_save_experience(
        company=TEST_EXP_COMPANY,
        role="Senior QA Automation Engineer",
        location="Jakarta, Indonesia",
        start_date="2024-01-01",
        is_current=True,
        description="End-to-End Automation Testing menggunakan Playwright & Pytest."
    )

    expect(admin_page.modal_experience).not_to_be_visible()
    expect(admin_page.experiences_tbody.locator("tr").filter(has_text=TEST_EXP_COMPANY).first).to_be_visible()


def test_delete_experience(admin_page: AdminPage):
    """
    Test 5: Menghapus data Work Experience yang dibuat dan memastikan terhapus.
    """
    admin_page.delete_experience(TEST_EXP_COMPANY)
    expect(admin_page.experiences_tbody.locator("tr").filter(has_text=TEST_EXP_COMPANY)).to_have_count(0)


# ==============================================================================
# SECTION 3: TECH STACKS
# ==============================================================================

def test_navigate_to_tech_stacks(admin_page: AdminPage):
    """
    Test 6: Memverifikasi navigasi ke menu Tech Stacks berhasil.
    """
    admin_page.go_to_tech_stacks()

    expect(admin_page.view_tech_stacks).to_be_visible()
    expect(admin_page.btn_create_tech_stack).to_be_visible()
    expect(admin_page.tech_stacks_tbody).to_be_visible()


def test_open_and_close_tech_stack_modal(admin_page: AdminPage):
    """
    Test 7: Memverifikasi modal Add Tech Stack dapat dibuka dan ditutup.
    """
    admin_page.open_create_tech_stack_modal()

    expect(admin_page.modal_tech_stack).to_be_visible()
    expect(admin_page.input_tech_name).to_be_visible()

    # Batalkan / tutup modal
    admin_page.modal_tech_stack.locator("button[data-close-modal]").filter(has_text="Cancel").click()
    expect(admin_page.modal_tech_stack).not_to_be_visible()


def test_create_new_tech_stack(admin_page: AdminPage):
    """
    Test 8: Menambahkan data Tech Stack baru.
    """
    admin_page.open_create_tech_stack_modal()

    admin_page.fill_and_save_tech_stack(
        name=TEST_TECH_NAME,
        category="Automation Testing",
        proficiency="Advanced",
        is_learning=False
    )

    expect(admin_page.modal_tech_stack).not_to_be_visible()
    expect(admin_page.tech_stacks_tbody.locator("tr").filter(has_text=TEST_TECH_NAME).first).to_be_visible()


def test_delete_tech_stack(admin_page: AdminPage):
    """
    Test 9: Menghapus data Tech Stack yang dibuat dan memastikan terhapus.
    """
    admin_page.delete_tech_stack(TEST_TECH_NAME)
    expect(admin_page.tech_stacks_tbody.locator("tr").filter(has_text=TEST_TECH_NAME)).to_have_count(0)


# ==============================================================================
# SECTION 4: PROJECTS
# ==============================================================================

def test_navigate_to_projects(admin_page: AdminPage):
    """
    Test 10: Memverifikasi navigasi ke menu Projects berhasil.
    """
    admin_page.go_to_projects()

    expect(admin_page.view_projects).to_be_visible()
    expect(admin_page.btn_create_project).to_be_visible()
    expect(admin_page.projects_tbody).to_be_visible()


def test_open_and_close_project_modal(admin_page: AdminPage):
    """
    Test 11: Memverifikasi modal Add Project dapat dibuka dan ditutup.
    """
    admin_page.open_create_project_modal()

    expect(admin_page.modal_project).to_be_visible()
    expect(admin_page.input_project_title).to_be_visible()
    expect(admin_page.input_project_slug).to_be_visible()

    # Batalkan / tutup modal
    admin_page.modal_project.locator("button[data-close-modal]").filter(has_text="Cancel").click()
    expect(admin_page.modal_project).not_to_be_visible()


def test_create_new_project(admin_page: AdminPage):
    """
    Test 12: Menambahkan data Project baru.
    """
    admin_page.open_create_project_modal()

    admin_page.fill_and_save_project(
        title=TEST_PROJECT_TITLE,
        slug=TEST_PROJECT_SLUG,
        category="QA Engineering",
        description="Full E2E Testing Framework with Page Object Model"
    )

    expect(admin_page.modal_project).not_to_be_visible()
    expect(admin_page.projects_tbody.locator("tr").filter(has_text=TEST_PROJECT_TITLE).first).to_be_visible()


def test_delete_project(admin_page: AdminPage):
    """
    Test 13: Menghapus data Project yang dibuat dan memastikan terhapus.
    """
    admin_page.delete_project(TEST_PROJECT_TITLE)
    expect(admin_page.projects_tbody.locator("tr").filter(has_text=TEST_PROJECT_TITLE)).to_have_count(0)


# ==============================================================================
# SECTION 5: ARTICLES / STORIES
# ==============================================================================

def test_navigate_to_articles(admin_page: AdminPage):
    """
    Test 14: Memverifikasi navigasi ke menu Articles berhasil.
    """
    admin_page.go_to_articles()

    expect(admin_page.view_articles).to_be_visible()
    expect(admin_page.btn_add_article).to_be_visible()
    expect(admin_page.articles_tbody).to_be_visible()


def test_open_and_close_article_modal(admin_page: AdminPage):
    """
    Test 15: Memverifikasi modal Add Article dapat dibuka dan ditutup.
    """
    admin_page.open_create_article_modal()

    expect(admin_page.modal_article).to_be_visible()
    expect(admin_page.input_article_title).to_be_visible()
    expect(admin_page.input_article_category).to_be_visible()

    # Batalkan / tutup modal
    admin_page.modal_article.locator("button[data-close-modal]").filter(has_text="Cancel").click()
    expect(admin_page.modal_article).not_to_be_visible()


def test_create_new_article(admin_page: AdminPage):
    """
    Test 16: Menambahkan artikel/cerita baru.
    """
    admin_page.open_create_article_modal()

    admin_page.fill_and_save_article(
        title=TEST_ARTICLE_TITLE,
        slug=TEST_ARTICLE_SLUG,
        category="Testing",
        content="Panduan lengkap setup dan implementasi Page Object Model Playwright Python."
    )

    expect(admin_page.modal_article).not_to_be_visible()
    expect(admin_page.articles_tbody.locator("tr").filter(has_text=TEST_ARTICLE_TITLE).first).to_be_visible()


def test_delete_article(admin_page: AdminPage):
    """
    Test 17: Menghapus data Article yang dibuat dan memastikan terhapus.
    """
    admin_page.delete_article(TEST_ARTICLE_TITLE)
    expect(admin_page.articles_tbody.locator("tr").filter(has_text=TEST_ARTICLE_TITLE)).to_have_count(0)



# ==============================================================================
# SECTION 6: CONTACTS / MESSAGES
# ==============================================================================

def test_navigate_to_contacts(admin_page: AdminPage):
    """
    Test 18: Memverifikasi navigasi ke menu Contacts / Messages berhasil.
    """
    admin_page.go_to_contacts()

    expect(admin_page.view_contacts).to_be_visible()
    expect(admin_page.contacts_tbody).to_be_visible()


# ==============================================================================
# SECTION 7: ERROR SCENE (404 Page Customizer)
# ==============================================================================

def test_navigate_to_error_scene(admin_page: AdminPage):
    """
    Test 19: Memverifikasi halaman konfigurasi 404 Error Scene berhasil dibuka.
    """
    admin_page.go_to_error_scene()

    expect(admin_page.view_error_scene).to_be_visible()
    expect(admin_page.form_error_scene).to_be_visible()
    expect(admin_page.input_error_headline).to_be_visible()
    expect(admin_page.btn_save_error_scene).to_be_visible()
