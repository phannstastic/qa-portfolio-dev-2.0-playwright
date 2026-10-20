from playwright.sync_api import Page, Locator


class AdminPage:
    """
    Page Object Model untuk Halaman Admin CMS Dashboard
    (https://www.irfanlab.my.id/admin)
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.irfanlab.my.id/admin"

        # ==========================================
        # 1. SIDEBAR & NAVIGATION
        # ==========================================
        self.brand_logo = page.locator(".brand-logo")
        self.nav_overview = page.locator("#nav-overview")
        self.nav_projects = page.locator("#nav-projects")
        self.nav_experiences = page.locator("#nav-experiences")
        self.nav_tech_stacks = page.locator("#nav-tech-stacks")
        self.nav_articles = page.locator("#nav-articles")
        self.nav_contacts = page.locator("#nav-contacts")
        self.nav_error_scene = page.locator("#nav-error-scene")

        self.button_logout = page.locator("#sidebar-logout-btn")
        self.topbar_logout = page.locator("#topbar-logout-btn")
        self.page_title = page.locator("#page-title")

        # ==========================================
        # 2. TOAST NOTIFICATION & CONFIRMATION MODAL
        # ==========================================
        self.toast_container = page.locator("#toast-container")
        self.modal_confirm = page.locator("#confirm-modal")
        self.btn_confirm_delete = page.locator("#confirm-delete-btn")

        # ==========================================
        # 3. OVERVIEW / DASHBOARD STATS
        # ==========================================
        self.view_overview = page.locator("#view-overview")
        self.stat_projects_count = page.locator("#stat-projects-count")
        self.stat_experiences_count = page.locator("#stat-experiences-count")
        self.stat_tech_stacks_count = page.locator("#stat-tech-stacks-count")
        self.stat_contacts_count = page.locator("#stat-contacts-count")
        self.stat_articles_count = page.locator("#stat-articles-count")
        self.stat_unread_count = page.locator("#stat-unread-count")

        # ==========================================
        # 4. WORK EXPERIENCES
        # ==========================================
        self.view_experiences = page.locator("#view-experiences")
        self.btn_create_experience = page.locator("#btn-create-experience")
        self.modal_experience = page.locator("#experience-modal")
        self.form_experience = page.locator("#experience-form")
        self.input_exp_company = page.locator("#exp-company")
        self.input_exp_role = page.locator("#exp-role")
        self.input_exp_location = page.locator("#exp-location")
        self.input_exp_sort_order = page.locator("#exp-sort-order")
        self.input_exp_start_date = page.locator("#exp-start-date")
        self.input_exp_end_date = page.locator("#exp-end-date")
        self.checkbox_exp_is_current = page.locator("#exp-is-current")
        self.textarea_exp_description = page.locator("#exp-description")
        self.btn_save_experience = page.locator("#experience-save-btn")
        self.experiences_tbody = page.locator("#experiences-tbody")

        # ==========================================
        # 5. TECH STACKS
        # ==========================================
        self.view_tech_stacks = page.locator("#view-tech-stacks")
        self.btn_create_tech_stack = page.locator("#btn-create-tech-stack")
        self.modal_tech_stack = page.locator("#tech-stack-modal")
        self.form_tech_stack = page.locator("#tech-stack-form")
        self.input_tech_name = page.locator("#tech-stack-name")
        self.input_tech_category = page.locator("#tech-stack-category")
        self.select_tech_proficiency = page.locator("#tech-stack-proficiency")
        self.input_tech_sort_order = page.locator("#tech-stack-sort-order")
        self.checkbox_tech_is_learning = page.locator("#tech-stack-is-learning")
        self.btn_save_tech_stack = page.locator("#tech-stack-save-btn")
        self.tech_stacks_tbody = page.locator("#tech-stacks-tbody")

        # Category in Tech Stack
        self.btn_create_category = page.locator("#btn-create-category")
        self.modal_category = page.locator("#category-modal")
        self.input_new_cat_name = page.locator("#new-category-name")
        self.textarea_new_cat_skills = page.locator("#new-category-skills")
        self.btn_save_category = page.locator("#category-save-btn")

        # ==========================================
        # 6. PROJECTS
        # ==========================================
        self.view_projects = page.locator("#view-projects")
        self.btn_create_project = page.locator("#btn-create-project")
        self.modal_project = page.locator("#project-modal")
        self.form_project = page.locator("#project-form")
        self.input_project_title = page.locator("#project-title")
        self.input_project_slug = page.locator("#project-slug")
        self.input_project_category = page.locator("#project-category")
        self.textarea_project_description = page.locator("#project-description")
        self.btn_save_project = page.locator("#project-save-btn")
        self.projects_tbody = page.locator("#projects-tbody")

        # ==========================================
        # 7. ARTICLES
        # ==========================================
        self.view_articles = page.locator("#view-articles")
        self.btn_add_article = page.locator("#btn-add-article")
        self.modal_article = page.locator("#article-modal")
        self.form_article = page.locator("#article-form")
        self.input_article_title = page.locator("#article-title-input")
        self.input_article_slug = page.locator("#article-slug-input")
        self.input_article_category = page.locator("#article-category-input")
        self.textarea_article_content = page.locator("#article-content-input")
        self.btn_save_article = page.locator("#article-save-btn")
        self.articles_tbody = page.locator("#articles-tbody")

        # ==========================================
        # 8. CONTACTS / MESSAGES
        # ==========================================
        self.view_contacts = page.locator("#view-contacts")
        self.contacts_tbody = page.locator("#contacts-tbody")
        self.modal_contact_detail = page.locator("#contact-detail-modal")

        # ==========================================
        # 9. ERROR SCENE (404)
        # ==========================================
        self.view_error_scene = page.locator("#view-error-scene")
        self.form_error_scene = page.locator("#error-scene-form")
        self.input_error_headline = page.locator("#error-scene-headline")
        self.btn_save_error_scene = page.locator("#btn-save-error-scene")

    # ==========================================
    # NAVIGATION METHODS
    # ==========================================
    def navigate(self):
        """Buka langsung URL Dashboard Admin."""
        self.page.goto(self.url)

    def logout(self):
        """Melakukan logout dari Dashboard ke halaman Login."""
        self.button_logout.click()

    def go_to_overview(self):
        self.nav_overview.click()

    def go_to_projects(self):
        self.nav_projects.click()

    def go_to_experiences(self):
        self.nav_experiences.click()

    def go_to_tech_stacks(self):
        self.nav_tech_stacks.click()

    def go_to_articles(self):
        self.nav_articles.click()

    def go_to_contacts(self):
        self.nav_contacts.click()

    def go_to_error_scene(self):
        self.nav_error_scene.click()

    # ==========================================
    # ACTION METHODS: WORK EXPERIENCE
    # ==========================================
    def open_create_experience_modal(self):
        """Membuka modal tambah experience."""
        self.go_to_experiences()
        self.btn_create_experience.click()

    def fill_and_save_experience(
        self,
        company: str,
        role: str,
        location: str,
        start_date: str,
        end_date: str = "",
        is_current: bool = False,
        description: str = "",
    ):
        """Mengisi form experience dan menekan tombol simpan."""
        self.input_exp_company.fill(company)
        self.input_exp_role.fill(role)
        self.input_exp_location.fill(location)
        self.input_exp_start_date.fill(start_date)

        if is_current:
            self.checkbox_exp_is_current.check()
        elif end_date:
            self.input_exp_end_date.fill(end_date)

        if description:
            self.textarea_exp_description.fill(description)

        self.btn_save_experience.click()

    # ==========================================
    # ACTION METHODS: TECH STACK
    # ==========================================
    def open_create_tech_stack_modal(self):
        """Membuka modal tambah tech stack."""
        self.go_to_tech_stacks()
        self.btn_create_tech_stack.click()

    def fill_and_save_tech_stack(
        self,
        name: str,
        category: str,
        proficiency: str = "Advanced",
        is_learning: bool = False,
    ):
        """Mengisi form tech stack dan menekan tombol simpan."""
        self.input_tech_name.fill(name)
        self.input_tech_category.fill(category)
        self.select_tech_proficiency.select_option(proficiency)

        if is_learning:
            self.checkbox_tech_is_learning.check()
        else:
            self.checkbox_tech_is_learning.uncheck()

        self.btn_save_tech_stack.click()

    # ==========================================
    # ACTION METHODS: PROJECT
    # ==========================================
    def open_create_project_modal(self):
        """Membuka modal tambah project."""
        self.go_to_projects()
        self.btn_create_project.click()

    def fill_and_save_project(
        self,
        title: str,
        slug: str,
        category: str,
        description: str = "",
        tech_tag: str = "Playwright",
    ):
        """Mengisi form project dan menekan tombol simpan."""
        self.input_project_title.fill(title)
        self.input_project_slug.fill(slug)
        self.input_project_category.fill(category)

        # Tech stack selection wajib diisi minimal 1 tag
        if tech_tag:
            self.page.locator("#project-custom-tech-input").fill(tech_tag)
            self.page.locator("#btn-add-custom-tech").click()

        if description:
            self.textarea_project_description.fill(description)
        self.btn_save_project.click()

    # ==========================================
    # ACTION METHODS: ARTICLES
    # ==========================================
    def open_create_article_modal(self):
        """Membuka modal tambah artikel/cerita."""
        self.go_to_articles()
        self.btn_add_article.click()

    def fill_and_save_article(
        self,
        title: str,
        slug: str,
        category: str,
        content: str,
    ):
        """Mengisi form artikel dan menekan tombol simpan."""
        self.input_article_title.fill(title)
        self.input_article_slug.fill(slug)
        self.input_article_category.fill(category)
        self.textarea_article_content.fill(content)
        self.btn_save_article.click()

    # ==========================================
    # ACTION METHODS: DELETE OPERATIONS
    # ==========================================
    def delete_experience(self, company: str):
        """Mencari data experience berdasarkan company dan mengonfirmasi hapus."""
        self.go_to_experiences()
        row = self.experiences_tbody.locator("tr").filter(has_text=company).first
        row.locator("button.delete, button[title*='Delete']").click()
        self.modal_confirm.wait_for(state="visible")
        self.btn_confirm_delete.click()
        self.modal_confirm.wait_for(state="hidden")

    def delete_tech_stack(self, name: str):
        """Mencari data tech stack berdasarkan nama dan mengonfirmasi hapus."""
        self.go_to_tech_stacks()
        filter_all = self.view_tech_stacks.locator(".filter-btn").filter(has_text="All")
        if filter_all.count() > 0:
            filter_all.first.click()
        row = self.tech_stacks_tbody.locator("tr").filter(has_text=name).first
        row.locator("button.delete, button[title*='Delete']").click()
        self.modal_confirm.wait_for(state="visible")
        self.btn_confirm_delete.click()
        self.modal_confirm.wait_for(state="hidden")

    def delete_project(self, title: str):
        """Mencari data project berdasarkan title dan mengonfirmasi hapus."""
        self.go_to_projects()
        row = self.projects_tbody.locator("tr").filter(has_text=title).first
        row.locator("button.delete, button[title*='Delete']").click()
        self.modal_confirm.wait_for(state="visible")
        self.btn_confirm_delete.click()
        self.modal_confirm.wait_for(state="hidden")

    def delete_article(self, title: str):
        """Mencari data article berdasarkan title dan mengonfirmasi hapus."""
        self.go_to_articles()
        row = self.articles_tbody.locator("tr").filter(has_text=title).first
        row.locator("button.btn-danger, button:has-text('Delete'), button[title*='Delete']").click()
        self.modal_confirm.wait_for(state="visible")
        self.btn_confirm_delete.click()
        self.modal_confirm.wait_for(state="hidden")

