import flet as ft
from pages.home import HomePage
from pages.timeline import TimelinePage
from pages.matlab import MatlabPage
from pages.blog import BlogPage
from pages.github import GithubPage

# ── Jonas's palette — deep navy + warm amber ──────────────────────────────────
BG       = "#0A0F1E"
SURFACE  = "#111827"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"
NAV_BG   = "#0D1526"


def main(page: ft.Page):
    page.title      = "Jonas Haikela — Portfolio 2026"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding    = 0
    page.bgcolor    = BG
    page.scroll     = ft.ScrollMode.AUTO

    home_page     = HomePage()
    timeline_page = TimelinePage()
    matlab_page   = MatlabPage()
    blog_page     = BlogPage()
    github_page   = GithubPage()

    fade_wrapper = ft.Container(
        expand=True,
        opacity=1,
        animate_opacity=250,
        padding=ft.Padding(left=32, right=32, top=24, bottom=24),
        content=home_page.build(),
    )

    current_index = {"v": 0}
    nav_buttons: list[ft.Container] = []

    nav_labels = ["Home", "Timeline", "MATLAB", "Blog", "GitHub"]
    nav_icons  = [ft.Icons.HOME, ft.Icons.TODAY, ft.Icons.GRADE,
                  ft.Icons.ARTICLE, ft.Icons.FOLDER]

    def rebuild_nav():
        for i, btn in enumerate(nav_buttons):
            active             = i == current_index["v"]
            row: ft.Row        = btn.content
            icon_ctrl: ft.Icon = row.controls[0]
            text_ctrl: ft.Text = row.controls[1]
            icon_ctrl.color    = ACCENT    if active else TEXT_SEC
            text_ctrl.color    = ACCENT    if active else TEXT_SEC
            text_ctrl.weight   = ft.FontWeight.W_600 if active else ft.FontWeight.W_400
            btn.bgcolor        = ACCENT + "22" if active else "transparent"
            btn.border         = ft.Border.all(1, ACCENT + "55") if active else ft.Border.all(1, "transparent")

    def switch_page(idx: int):
        if idx == current_index["v"]:
            return
        fade_wrapper.opacity = 0
        page.update()

        import time, threading

        def do_switch():
            time.sleep(0.25)
            current_index["v"] = idx
            rebuild_nav()
            if idx == 0:
                fade_wrapper.content = home_page.build()
            elif idx == 1:
                fade_wrapper.content = timeline_page.build()
            elif idx == 2:
                fade_wrapper.content = matlab_page.build()
                threading.Thread(target=matlab_page._run_animations, daemon=True).start()
            elif idx == 3:
                fade_wrapper.content = blog_page.build(page)
            elif idx == 4:
                fade_wrapper.content = github_page.build()
            fade_wrapper.opacity = 1
            page.update()

        threading.Thread(target=do_switch, daemon=True).start()

    for i, (lbl, ico) in enumerate(zip(nav_labels, nav_icons)):
        active = i == 0
        btn = ft.Container(
            content=ft.Row(controls=[
                ft.Icon(ico, size=15, color=ACCENT if active else TEXT_SEC),
                ft.Text(lbl, size=13,
                        weight=ft.FontWeight.W_600 if active else ft.FontWeight.W_400,
                        color=ACCENT if active else TEXT_SEC),
            ], spacing=6, tight=True),
            padding=ft.Padding(left=14, right=14, top=8, bottom=8),
            border_radius=8,
            bgcolor=ACCENT + "22" if active else "transparent",
            border=ft.Border.all(1, ACCENT + "55" if active else "transparent"),
            on_click=lambda e, i=i: switch_page(i),
            ink=True,
            animate=200,
        )
        nav_buttons.append(btn)

    # ── Top navbar with Jonas's identity ─────────────────────────────────────
    topbar = ft.Container(
        content=ft.Row(controls=[
            ft.Row(controls=[
                ft.Container(
                    content=ft.Text("JH", size=14, weight=ft.FontWeight.W_800, color=BG),
                    width=36, height=36, border_radius=18,
                    bgcolor=ACCENT,
                    alignment=ft.Alignment(0, 0),
                ),
                ft.Column(controls=[
                    ft.Text("Jonas Haikela", size=14, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ft.Text("Civil Engineering · UI/UX Lead", size=11, color=ACCENT),
                ], spacing=0),
            ], spacing=10),
            ft.Container(expand=True),
            ft.Row(controls=nav_buttons, spacing=4),
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=NAV_BG,
        padding=ft.Padding(left=32, right=32, top=12, bottom=12),
        border=ft.Border(bottom=ft.BorderSide(1, BORDER)),
    )

    page.appbar = None
    page.add(
        ft.Column(controls=[topbar, fade_wrapper], spacing=0, expand=True)
    )
    page.update()


ft.run(main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
