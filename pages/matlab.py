import flet as ft
import random, threading, time

# ── Palette ───────────────────────────────────────────────────────────────────
BG       = "#0A0F1E"
SURFACE  = "#111827"
SURFACE2 = "#1A2233"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"
ACCENT_B = "#C07800"
BLUE     = "#4A9EFF"

CONFETTI_COLORS = ["#F5A623","#4A9EFF","#6BCB77","#FF6B6B","#CC5DE8","#FF922B","#FFD93D"]


def _hoverable(c: ft.Container, col: str) -> ft.Container:
    c.animate = 200
    def on_hover(e, _c=c, _col=col):
        if e.data == "true":
            _c.bgcolor = SURFACE2
            _c.border  = ft.Border.all(1, _col)
            _c.shadow  = ft.BoxShadow(spread_radius=0, blur_radius=18,
                                      color=_col + "33", offset=ft.Offset(0, 4))
        else:
            _c.bgcolor = SURFACE
            _c.border  = ft.Border.all(1, BORDER)
            _c.shadow  = None
        _c.update()
    c.on_hover = on_hover
    return c


class MatlabPage:
    # ── Jonas's actual 7 MathWorks certificates ───────────────────────────────
    COURSES = [
        {
            "title": "MATLAB Onramp",
            "description": "Introduction to MATLAB syntax, variables, and basic operations. Completed 100%.",
            "date": "29 April 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Calculations with Vectors and Matrices",
            "description": "Matrix arithmetic, dot products, and linear algebra fundamentals. Completed 100%.",
            "date": "29 April 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Explore Data with MATLAB Plots",
            "description": "Data visualisation techniques: scatter, line, bar, and customisation. Completed 100%.",
            "date": "30 April 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Make and Manipulate Matrices",
            "description": "Advanced matrix creation, indexing, reshaping, and concatenation. Completed 100%.",
            "date": "14 June 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Statistics Onramp",
            "description": "Descriptive stats, distributions, and hypothesis testing in MATLAB. Completed 100%.",
            "date": "15 June 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Semi-Automated Image Segmentation",
            "description": "Interactive segmentation workflows using MATLAB image processing tools. Completed 100%.",
            "date": "15 June 2026", "hours": "~2 hrs", "pct": 100,
        },
        {
            "title": "Simulink Onramp",
            "description": "Block diagram modelling and simulation of dynamic systems. Completed 10%.",
            "date": "14 June 2026", "hours": "~2 hrs", "pct": 10,
        },
    ]

    def __init__(self):
        self._overlay_ref  = ft.Ref[ft.Container]()
        self._confetti_ref = ft.Ref[ft.Stack]()
        self._card_refs    = []
        self._badge_refs   = []

    def _close_preview(self, e):
        self._overlay_ref.current.visible = False
        self._overlay_ref.current.update()

    def _build_badge(self, ref, pct):
        label = "Completed" if pct == 100 else f"{pct}% done"
        color = ACCENT if pct == 100 else BLUE
        dark  = ACCENT_B if pct == 100 else "#1A4080"
        return ft.Container(
            ref=ref,
            content=ft.Text(label, size=11, weight=ft.FontWeight.W_600, color=color),
            bgcolor=dark + "33",
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
            border=ft.Border.all(1, dark),
            animate=800,
        )

    def _build_card(self, course, index, card_ref, badge_ref):
        pct = course["pct"]
        return _hoverable(
            ft.Container(
                ref=card_ref,
                opacity=0,
                animate_opacity=600,
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Text(str(index), size=13,
                                            weight=ft.FontWeight.W_700, color=ACCENT),
                            width=32, height=32, border_radius=16,
                            bgcolor=ACCENT_B + "33",
                            border=ft.Border.all(1, ACCENT_B),
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Text(course["title"], size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI, expand=True),
                        ft.Icon(ft.Icons.CHECK_CIRCLE if pct == 100 else ft.Icons.PENDING,
                                color=ACCENT if pct == 100 else BLUE, size=20),
                    ], spacing=10),
                    ft.Text(course["description"], size=13, color=TEXT_SEC),
                    ft.ProgressBar(value=pct / 100, bgcolor=BORDER,
                                   color=ACCENT if pct == 100 else BLUE,
                                   height=6, border_radius=4),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.CALENDAR_TODAY, size=12, color=TEXT_SEC),
                        ft.Text(course["date"], size=11, color=TEXT_SEC),
                        ft.Text("·", size=11, color=BORDER),
                        ft.Icon(ft.Icons.TIMER, size=12, color=TEXT_SEC),
                        ft.Text(course["hours"], size=11, color=TEXT_SEC, italic=True),
                        ft.Container(expand=True),
                        self._build_badge(badge_ref, pct),
                    ], spacing=4),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

    def _make_confetti_piece(self):
        return ft.Container(
            width=random.randint(10, 18), height=random.randint(10, 18),
            bgcolor=random.choice(CONFETTI_COLORS),
            border_radius=random.choice([0, 10]),
            left=random.randint(0, 1200), top=random.randint(-50, 0),
            opacity=1, animate_opacity=1500, animate_position=1500,
        )

    def _run_animations(self, page=None):
        for ref in self._card_refs:
            time.sleep(0.12)
            try:
                ref.current.opacity = 1
                ref.current.update()
            except Exception:
                pass
        try:
            pieces = self._confetti_ref.current.controls
            for p in pieces:
                p.top = random.randint(400, 800)
                p.opacity = 0
                p.left = random.randint(0, 1200)
            self._confetti_ref.current.update()
            time.sleep(2.5)
            self._confetti_ref.current.visible = False
            self._confetti_ref.current.update()
        except Exception:
            pass

    def build(self):
        self._card_refs  = [ft.Ref[ft.Container]() for _ in self.COURSES]
        self._badge_refs = [ft.Ref[ft.Container]() for _ in self.COURSES]

        completed = sum(1 for c in self.COURSES if c["pct"] == 100)
        total     = len(self.COURSES)
        progress  = completed / total

        cards     = [self._build_card(c, i + 1, self._card_refs[i], self._badge_refs[i])
                     for i, c in enumerate(self.COURSES)]

        progress_section = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Text("Overall Progress", size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI),
                        ft.Container(expand=True),
                        ft.Text(f"{completed} / {total} courses complete", size=14,
                                weight=ft.FontWeight.W_700, color=ACCENT),
                    ]),
                    ft.ProgressBar(value=progress, bgcolor=BORDER, color=ACCENT,
                                   height=10, border_radius=5),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.CHECK_BOX, color=ACCENT, size=14),
                        ft.Text(f"{completed} of {total} courses 100% complete — requirement met!",
                                size=12, color=ACCENT, weight=ft.FontWeight.W_600),
                    ], spacing=6),
                ], spacing=10),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=20, right=20, top=20, bottom=20),
                border=ft.Border.all(1, ACCENT_B),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
            ),
            ACCENT,
        )

        left_col  = ft.Column(controls=cards[::2],  spacing=14, expand=True)
        right_col = ft.Column(controls=cards[1::2], spacing=14, expand=True)

        confetti_layer = ft.Stack(ref=self._confetti_ref,
                                  controls=[self._make_confetti_piece() for _ in range(40)],
                                  expand=True)
        overlay = ft.Container(ref=self._overlay_ref, visible=False,
                               expand=True, bgcolor="transparent")

        def on_mount(e=None):
            threading.Thread(target=self._run_animations, args=(None,), daemon=True).start()

        main_column = ft.Column(controls=[
            ft.Text("MATLAB Achievement Hub", size=22, weight=ft.FontWeight.W_700,
                    color=TEXT_PRI),
            ft.Text("Jonas Haikela — MathWorks Learning Center self-paced certificates.",
                    size=14, color=TEXT_SEC),
            ft.Divider(height=12, color="transparent"),
            progress_section,
            ft.Row(controls=[left_col, right_col], spacing=14,
                   vertical_alignment=ft.CrossAxisAlignment.START),
        ], spacing=4, scroll=ft.ScrollMode.AUTO, expand=True)

        wrapper = ft.Stack(controls=[main_column, confetti_layer, overlay], expand=True)
        outer   = ft.Container(content=wrapper, expand=True)
        outer.did_mount = on_mount
        return outer
