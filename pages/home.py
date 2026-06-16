import flet as ft

# ── Palette: deep navy + warm amber (distinct from the green/dark-grey original) ──
BG       = "#0A0F1E"
SURFACE  = "#111827"
SURFACE2 = "#1A2233"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"   # warm amber
ACCENT_B = "#C07800"
BLUE     = "#4A9EFF"


class HomePage:
    def build(self):
        return ft.Column(
            controls=[
                ft.Container(height=32),
                # ── Hero greeting ────────────────────────────────────────────
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(controls=[
                                ft.Container(
                                    content=ft.Text("JH", size=22, weight=ft.FontWeight.W_800,
                                                    color=BG),
                                    width=56, height=56, border_radius=28,
                                    bgcolor=ACCENT,
                                    alignment=ft.Alignment(0, 0),
                                ),
                                ft.Column(controls=[
                                    ft.Text("Hi, I'm Jonas 👋", size=36,
                                            weight=ft.FontWeight.W_800, color=TEXT_PRI),
                                    ft.Text("Civil Engineering Student  ·  UI/UX Lead  ·  Developer",
                                            size=16, color=ACCENT),
                                ], spacing=2),
                            ], spacing=16, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Container(height=8),
                            ft.Text(
                                "University of Namibia (UNAM)  ·  School of Engineering and the Built Environment",
                                size=13, color=TEXT_SEC,
                            ),
                            ft.Container(height=16),
                            ft.Row(controls=[
                                ft.ElevatedButton(
                                    "View Projects",
                                    bgcolor=ACCENT, color=BG,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                                ),
                                ft.OutlinedButton(
                                    "Download CV",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                        side=ft.BorderSide(1, ACCENT),
                                        color=ACCENT,
                                    ),
                                ),
                            ], spacing=12),
                        ],
                        spacing=4,
                    ),
                    bgcolor=SURFACE,
                    border_radius=16,
                    padding=ft.Padding(left=28, right=28, top=28, bottom=28),
                    border=ft.Border.all(1, BORDER),
                    margin=ft.Margin(left=0, right=0, top=0, bottom=20),
                ),

                # ── About Me ────────────────────────────────────────────────
                ft.Text("About Me", size=20, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Container(height=6),
                ft.Container(
                    content=ft.Text(
                        "I'm Jonas Haikela, a Civil Engineering student at UNAM with a strong "
                        "interest in software development and UI/UX design. This semester I served "
                        "as UI/UX Lead for the Safe Sphere project — a Safety Hazard Awareness and "
                        "Prevention App built for mine and industrial workers. I enjoy bridging the "
                        "gap between engineering problems and user-friendly digital solutions.",
                        size=14, color=TEXT_SEC,
                    ),
                    bgcolor=SURFACE,
                    border_radius=12,
                    padding=ft.Padding(left=20, right=20, top=16, bottom=16),
                    border=ft.Border.all(1, BORDER),
                    margin=ft.Margin(left=0, right=0, top=0, bottom=20),
                ),

                # ── Semester Project highlight ───────────────────────────────
                ft.Text("Semester Project", size=20, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Container(height=6),
                ft.Container(
                    content=ft.Column(controls=[
                        ft.Row(controls=[
                            ft.Icon(ft.Icons.SHIELD, color=ACCENT, size=22),
                            ft.Text("Safe Sphere", size=16, weight=ft.FontWeight.W_700,
                                    color=TEXT_PRI),
                            ft.Container(
                                content=ft.Text("UI/UX Lead", size=11, color=ACCENT,
                                                weight=ft.FontWeight.W_600),
                                bgcolor=ACCENT_B + "33",
                                padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                                border_radius=20,
                                border=ft.Border.all(1, ACCENT_B),
                            ),
                        ], spacing=10),
                        ft.Text(
                            "Safety Hazard Awareness and Prevention App — a mobile platform "
                            "(Expo + React Native + Firebase) designed to educate mining and "
                            "industrial workers about hazards before they enter high-risk zones.",
                            size=13, color=TEXT_SEC,
                        ),
                        ft.Row(controls=[
                            _chip("React Native", BLUE),
                            _chip("Firebase", "#FF6D00"),
                            _chip("UI/UX", ACCENT),
                            _chip("UNAM", TEXT_SEC),
                        ], spacing=8, wrap=True),
                    ], spacing=10),
                    bgcolor=SURFACE,
                    border_radius=12,
                    padding=ft.Padding(left=20, right=20, top=16, bottom=16),
                    border=ft.Border.all(1, BORDER),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )


def _chip(label, color):
    return ft.Container(
        content=ft.Text(label, size=11, color=color),
        bgcolor=color + "22",
        padding=ft.Padding(left=10, right=10, top=4, bottom=4),
        border_radius=20,
        border=ft.Border.all(1, color + "55"),
    )
