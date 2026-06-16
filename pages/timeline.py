import flet as ft

BG       = "#0A0F1E"
SURFACE  = "#111827"
SURFACE2 = "#1A2233"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"
ACCENT_B = "#C07800"
AMBER    = "#F5A623"
BLUE     = "#4A9EFF"


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


class TimelinePage:
    ENTRIES = [
        {
            "week": "Week 1", "dates": "20 Jan – 26 Jan",
            "task": "Project setup & team role assignment",
            "contribution": "Joined the Targeryens group for the Safe Sphere project. Assigned as UI/UX Lead and GitHub Manager. Reviewed the project brief and began planning screen designs.",
            "status": "Done", "icon": ft.Icons.ROCKET_LAUNCH, "tags": ["Planning", "UI/UX"],
        },
        {
            "week": "Week 2", "dates": "27 Jan – 2 Feb",
            "task": "SRS document — UI/UX section contribution",
            "contribution": "Contributed to the System Requirements Specification (SRS) document, focusing on the Usability section. Defined requirements for intuitive interface, accessibility, and clear error messages.",
            "status": "Done", "icon": ft.Icons.DESCRIPTION, "tags": ["Documentation", "UI/UX"],
        },
        {
            "week": "Week 3", "dates": "3 Feb – 9 Feb",
            "task": "Screen wireframes and navigation design",
            "contribution": "Designed the app's main screens: Login, Home dashboard, Course list, and Progress tracker. Established the visual hierarchy and navigation flow for the React Native app.",
            "status": "Done", "icon": ft.Icons.DASHBOARD, "tags": ["UI/UX", "Design"],
        },
        {
            "week": "Week 4", "dates": "10 Feb – 16 Feb",
            "task": "BrandLogo component & Home screen implementation",
            "contribution": "Implemented the reusable BrandLogo React Native component using the project PNG asset. Built the Home screen layout with navigation bar and greeting section.",
            "status": "Done", "icon": ft.Icons.CODE, "tags": ["React Native", "UI/UX"],
        },
        {
            "week": "Week 5", "dates": "17 Feb – 23 Feb",
            "task": "Course card UI + Progress tracker screen",
            "contribution": "Built the Course card component for the safety learning modules and wired up the progress tracking screen. Reviewed a teammate's Firebase authentication PR and flagged a missing error handler.",
            "status": "Done", "icon": ft.Icons.LAYERS, "tags": ["React Native", "Git"],
        },
        {
            "week": "Week 6", "dates": "24 Feb – 2 Mar",
            "task": "MATLAB self-paced courses",
            "contribution": "Completed MATLAB Onramp, Calculations with Vectors and Matrices, and Explore Data with MATLAB Plots on MathWorks Learning Center (all 100%).",
            "status": "Done", "icon": ft.Icons.SCHOOL, "tags": ["MATLAB", "Learning"],
        },
        {
            "week": "Week 7", "dates": "June 2026",
            "task": "Remaining MATLAB certificates + portfolio",
            "contribution": "Completed Make and Manipulate Matrices, Statistics Onramp, Semi-Automated Image Segmentation (all 100%), and started Simulink Onramp (10%). Built this personal Flet web portfolio.",
            "status": "In Progress", "icon": ft.Icons.WEB, "tags": ["MATLAB", "Portfolio"],
        },
    ]

    STATUS_STYLES = {
        "Done":        (ACCENT_B + "33", ACCENT, ACCENT),
        "In Progress": (BLUE + "22",     BLUE,   BLUE),
        "Pending":     ("#6E40C933",     "#A371F7", "#A371F7"),
    }

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=10, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=8, right=8, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _build_entry(self, entry, index, is_last):
        bg, fg, dot_color = self.STATUS_STYLES.get(entry["status"],
                                                    (SURFACE2, TEXT_SEC, TEXT_SEC))
        is_done     = entry["status"] == "Done"
        is_progress = entry["status"] == "In Progress"

        dot = ft.Container(
            width=44, height=44, border_radius=22,
            bgcolor=SURFACE2,
            content=ft.Icon(entry["icon"], color=dot_color, size=20),
            alignment=ft.Alignment(0, 0),
            border=ft.Border.all(2, dot_color),
        )
        week_badge = ft.Container(
            content=ft.Text(entry["week"], size=11,
                            weight=ft.FontWeight.W_700, color=dot_color),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, dot_color + "55"),
        )
        status_icon  = (ft.Icons.CHECK_CIRCLE if is_done
                        else ft.Icons.PENDING if is_progress
                        else ft.Icons.CIRCLE)
        status_badge = ft.Container(
            content=ft.Row(controls=[
                ft.Icon(status_icon, size=12, color=fg),
                ft.Text(entry["status"], size=11, weight=ft.FontWeight.W_600, color=fg),
            ], spacing=4),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
        )
        card = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        week_badge,
                        ft.Text(entry["dates"], size=11, color=TEXT_SEC),
                        ft.Container(expand=True),
                        status_badge,
                    ], spacing=8),
                    ft.Text(entry["task"], size=14, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ft.Text(entry["contribution"], size=13, color=TEXT_SEC, no_wrap=False),
                    ft.Row(controls=[self._tag_chip(t) for t in entry.get("tags", [])],
                           spacing=6, wrap=True),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            dot_color,
        )
        connector = ft.Container(
            width=2, height=20,
            bgcolor=dot_color if is_done else BORDER,
            margin=ft.Margin(left=21, right=21, top=0, bottom=0),
        )
        left_col = ft.Column(
            controls=[dot] + ([] if is_last else [connector]),
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=44,
        )
        return ft.Container(
            content=ft.Row(controls=[left_col, card], spacing=16,
                           vertical_alignment=ft.CrossAxisAlignment.START),
            margin=ft.Margin(left=0, right=0, top=0, bottom=12),
        )

    def build(self):
        done_count = sum(1 for e in self.ENTRIES if e["status"] == "Done")
        total      = len(self.ENTRIES)
        progress   = done_count / total

        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.TODAY, color=TEXT_PRI, size=28),
                        ft.Text("Project Timeline", size=24, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Jonas Haikela — weekly log of contributions to Safe Sphere (Targeryens).",
                            size=13, color=TEXT_SEC),
                    ft.Divider(height=8, color="transparent"),
                    ft.Row(controls=[
                        ft.Text(f"{done_count} of {total} weeks completed",
                                size=12, color=TEXT_SEC),
                        ft.Container(expand=True),
                        ft.Text(f"{int(progress * 100)}%", size=12,
                                weight=ft.FontWeight.W_700, color=ACCENT),
                    ]),
                    ft.ProgressBar(value=progress, bgcolor=BORDER, color=ACCENT,
                                   height=6, border_radius=4),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=24),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        def stat_card(value, label, color):
            return _hoverable(
                ft.Container(
                    content=ft.Column(controls=[
                        ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=color),
                        ft.Text(label, size=11, color=TEXT_SEC),
                    ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=SURFACE, border_radius=12,
                    padding=ft.Padding(left=20, right=20, top=14, bottom=14),
                    border=ft.Border.all(1, BORDER),
                    expand=True, alignment=ft.Alignment(0, 0),
                ),
                color,
            )

        stats = ft.Row(controls=[
            stat_card(str(total),      "Total Weeks",  TEXT_PRI),
            stat_card(str(done_count), "Completed",    ACCENT),
            stat_card(str(sum(1 for e in self.ENTRIES if e["status"] == "In Progress")),
                      "In Progress", BLUE),
        ], spacing=12)

        entries = [self._build_entry(e, i, i == len(self.ENTRIES) - 1)
                   for i, e in enumerate(self.ENTRIES)]

        return ft.Column(controls=[
            hero, stats,
            ft.Divider(height=24, color="transparent"),
            ft.Text("Weekly Contributions", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            ft.Divider(height=8, color="transparent"),
            *entries,
        ], spacing=4, scroll=ft.ScrollMode.AUTO)
