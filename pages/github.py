import flet as ft

BG       = "#0A0F1E"
SURFACE  = "#111827"
SURFACE2 = "#1A2233"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"
ACCENT_B = "#C07800"
BLUE     = "#4A9EFF"
AMBER    = "#F5A623"
PURPLE   = "#A371F7"
RED      = "#F85149"
GREEN    = "#3FB950"


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


class GithubPage:
    COMMITS = [
        {"hash": "c3a1f09", "message": "Add BrandLogo component with PNG asset",
         "date": "8 June 2026",  "branch": "feature/ui-components"},
        {"hash": "d72b4e1", "message": "Design Home screen layout and navigation bar",
         "date": "10 June 2026", "branch": "feature/ui-components"},
        {"hash": "e91c3a7", "message": "Build Course card UI for safety learning modules",
         "date": "12 June 2026", "branch": "feature/course-ui"},
        {"hash": "f4d8b22", "message": "Implement Progress tracker screen",
         "date": "14 June 2026", "branch": "feature/course-ui"},
        {"hash": "a02e5f3", "message": "Fix navigation drawer icon alignment",
         "date": "15 June 2026", "branch": "dev"},
        {"hash": "b18c9d4", "message": "Review PR #7 — Firebase auth integration",
         "date": "15 June 2026", "branch": "dev"},
    ]

    PULL_REQUESTS = [
        {
            "pr_number": "#5", "title": "UI Components — BrandLogo + Home screen",
            "status": "Merged", "commits": 2,
            "reviews": "Reviewed by: @zowen_m, @salmi_n",
            "description": "Added the reusable BrandLogo component and designed the Home screen layout. "
                           "Includes navigation bar and hero greeting section.",
        },
        {
            "pr_number": "#9", "title": "Course card UI + Progress tracker screen",
            "status": "Merged", "commits": 2,
            "reviews": "Reviewed by: @johanna_m",
            "description": "Built the Course card component for safety learning modules and wired up the "
                           "progress tracking screen showing completion percentages.",
        },
        {
            "pr_number": "#7", "title": "Firebase auth integration code review",
            "status": "Closed", "commits": 1,
            "reviews": "Reviewed by: me (@jonas_haikela)",
            "description": "Reviewed Firebase Authentication implementation by the Firebase team lead. "
                           "Flagged a missing error handler for invalid credentials.",
        },
    ]

    WEEKLY_COMMITS = [
        {"week": "1 Jun",  "count": 0},
        {"week": "8 Jun",  "count": 2},
        {"week": "10 Jun", "count": 1},
        {"week": "12 Jun", "count": 1},
        {"week": "14 Jun", "count": 1},
        {"week": "15 Jun", "count": 1},
    ]

    BRAND_LOGO_CODE = """\
import { Image, StyleSheet } from 'react-native';
const logo = require('../../../assets/Copilot_20260608_111229 (1).png');

export default function BrandLogo({ style }) {
  return (
    <Image
      source={logo}
      style={[styles.logo, style]}
      resizeMode="contain"
    />
  );
}

const styles = StyleSheet.create({
  logo: { width: 72, height: 72 },
});"""

    IMPACT_SUMMARY = """\
## My Role — UI/UX Lead & GitHub Manager

As **UI/UX Lead** for the Targeryens group (Safe Sphere project), my primary responsibility
was designing and building the visual interface of our React Native app.

### What I built:
- **BrandLogo component** — reusable PNG image component (see commit c3a1f09)
- **Home screen** layout and navigation bar
- **Course card UI** for the safety learning modules
- **Progress tracker screen** showing user completion status
- **Navigation drawer** with icon alignment fixes

### Team contributions:
- Reviewed 3 pull requests, including flagging a missing Firebase error handler
- Coordinated UI consistency across the 16-member team

**Total: 6 commits · 2 PRs opened · 3 PRs reviewed**
"""

    STATUS_STYLE = {
        "Merged": (GREEN + "33", GREEN, GREEN + "55"),
        "Closed": (RED   + "22", RED,   RED   + "55"),
        "Open":   (BLUE  + "22", BLUE,  BLUE  + "44"),
    }

    BRANCH_COLORS = {
        "feature/ui-components": (PURPLE + "22", PURPLE),
        "feature/course-ui":     (AMBER  + "22", AMBER),
        "dev":                   (GREEN  + "22", GREEN),
    }

    def _stat_card(self, icon, value, label, color):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Icon(icon, color=color, size=24),
                    ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ft.Text(label, size=12, color=TEXT_SEC),
                ], spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
            color,
        )

    def _build_contribution_graph(self):
        max_count = max(w["count"] for w in self.WEEKLY_COMMITS) or 1
        bars = []
        for w in self.WEEKLY_COMMITS:
            height = max(4, int((w["count"] / max_count) * 80))
            bars.append(ft.Column(controls=[
                ft.Text(str(w["count"]), size=11, color=TEXT_SEC,
                        text_align=ft.TextAlign.CENTER),
                ft.Container(width=36, height=height,
                             bgcolor=ACCENT if w["count"] > 0 else BORDER,
                             border_radius=ft.BorderRadius(4, 4, 0, 0)),
                ft.Text(w["week"], size=10, color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4))

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text("Contribution Activity", size=14, weight=ft.FontWeight.W_600,
                            color=TEXT_PRI),
                    ft.Text("Commits per week (June 2026)", size=12, color=TEXT_SEC),
                    ft.Container(
                        content=ft.Row(controls=bars,
                                       alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                       vertical_alignment=ft.CrossAxisAlignment.END),
                        padding=ft.Padding(left=0, right=0, top=8, bottom=4),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

    def _commit_row(self, c):
        bg, fg = self.BRANCH_COLORS.get(c["branch"], (SURFACE2, TEXT_SEC))
        return ft.Container(
            content=ft.Row(controls=[
                ft.Icon(ft.Icons.COMMIT, size=14, color=BLUE),
                ft.Text(c["hash"], size=12, color=BLUE, font_family="monospace", width=70),
                ft.Text(c["message"], size=13, color=TEXT_PRI, expand=True),
                ft.Text(c["date"], size=11, color=TEXT_SEC, width=90),
                ft.Container(
                    content=ft.Text(c["branch"], size=10, color=fg),
                    bgcolor=bg,
                    padding=ft.Padding(left=8, right=8, top=3, bottom=3),
                    border_radius=20,
                    border=ft.Border.all(1, fg + "55"),
                ),
            ], spacing=10),
            padding=ft.Padding(left=12, right=12, top=10, bottom=10),
            border=ft.Border(bottom=ft.BorderSide(1, BORDER)),
        )

    def _pr_card(self, pr):
        bg, fg, border_c = self.STATUS_STYLE.get(pr["status"], (SURFACE2, TEXT_SEC, BORDER))
        icon = (ft.Icons.MERGE if pr["status"] == "Merged"
                else ft.Icons.CLOSE if pr["status"] == "Closed"
                else ft.Icons.CALL_SPLIT)
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(icon, color=fg, size=16),
                        ft.Text(pr["pr_number"], size=13, color=TEXT_SEC, width=36),
                        ft.Text(pr["title"], size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI, expand=True),
                        ft.Container(
                            content=ft.Text(pr["status"], size=11,
                                            weight=ft.FontWeight.W_600, color=fg),
                            bgcolor=bg,
                            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, border_c),
                        ),
                    ], spacing=8),
                    ft.Text(pr["description"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.COMMIT, size=12, color=TEXT_SEC),
                        ft.Text(f"{pr['commits']} commits", size=12, color=TEXT_SEC),
                        ft.Text("·", size=12, color=BORDER),
                        ft.Icon(ft.Icons.PERSON, size=14, color=TEXT_SEC),
                        ft.Text(pr["reviews"], size=12, color=TEXT_SEC),
                    ], spacing=4),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=10),
            ),
            fg,
        )

    def _brand_logo_card(self):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.IMAGE, color=ACCENT, size=18),
                        ft.Text("BrandLogo Component (commit c3a1f09)",
                                size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ], spacing=8),
                    ft.Text("My contribution to the Safe Sphere app — a reusable brand logo component "
                            "used across all screens.", size=13, color=TEXT_SEC),
                    ft.Container(
                        content=ft.Text(self.BRAND_LOGO_CODE, size=12,
                                        font_family="monospace", color="#A9DC76",
                                        selectable=True),
                        bgcolor="#0D1117",
                        border_radius=8,
                        padding=ft.Padding(left=14, right=14, top=12, bottom=12),
                        border=ft.Border.all(1, BORDER),
                    ),
                ], spacing=10),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, ACCENT + "44"),
                margin=ft.Margin(left=0, right=0, top=0, bottom=12),
            ),
            ACCENT,
        )

    def _screenshot_card(self, title, src):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text(title, size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ft.Container(
                        content=ft.Image(
                            src=src, fit="contain",
                            error_content=ft.Column(controls=[
                                ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED, color=BORDER, size=32),
                                ft.Text(f"Add screenshot to:\nassets/{src}",
                                        size=11, color=TEXT_SEC,
                                        text_align=ft.TextAlign.CENTER),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                        ),
                        bgcolor=SURFACE2, border_radius=8, height=160,
                        border=ft.Border.all(1, BORDER),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        alignment=ft.Alignment(0, 0),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=12, right=12, top=12, bottom=12),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            BLUE,
        )

    def build(self):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FOLDER, color=TEXT_PRI, size=28),
                        ft.Text("GitHub Evidence", size=24, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Jonas Haikela — UI/UX Lead & GitHub Manager — Safe Sphere project.",
                            size=13, color=TEXT_SEC),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        stats = ft.Row(controls=[
            self._stat_card(ft.Icons.COMMIT,      "6", "Commits",      BLUE),
            self._stat_card(ft.Icons.CALL_MERGE,  "2", "PRs Opened",   GREEN),
            self._stat_card(ft.Icons.RATE_REVIEW, "3", "PRs Reviewed", PURPLE),
            self._stat_card(ft.Icons.PALETTE,     "4", "UI Screens",   AMBER),
        ], spacing=12)

        graph        = self._build_contribution_graph()
        commit_rows  = [self._commit_row(c) for c in self.COMMITS]
        commits_sect = ft.Container(
            content=ft.Column(controls=[
                ft.Text("Commit History", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Container(
                    content=ft.Column(controls=commit_rows, spacing=0),
                    bgcolor=SURFACE, border_radius=12,
                    border=ft.Border.all(1, BORDER),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
            ], spacing=10),
        )

        screenshots = ft.Row(controls=[
            self._screenshot_card("Commit History Screenshot", "screenshots/commits.png"),
            self._screenshot_card("Pull Request Screenshot",   "screenshots/pull_request.png"),
        ], spacing=12)

        pr_cards   = [self._pr_card(p) for p in self.PULL_REQUESTS]
        pr_section = ft.Column(controls=[
            ft.Text("Pull Request Logs", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            *pr_cards,
        ], spacing=8)

        impact = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.STAR, color=AMBER, size=20),
                        ft.Text("Impact Summary", size=16, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI),
                    ], spacing=8),
                    ft.Markdown(self.IMPACT_SUMMARY, selectable=True,
                                extension_set="gitHubFlavored"),
                ], spacing=10),
                bgcolor=SURFACE2, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, AMBER + "55"),
            ),
            AMBER,
        )

        return ft.Column(controls=[
            hero, stats,
            ft.Divider(height=16, color="transparent"),
            graph,
            ft.Divider(height=16, color="transparent"),
            ft.Text("Brand Logo Commit", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            self._brand_logo_card(),
            ft.Divider(height=4, color="transparent"),
            commits_sect,
            ft.Divider(height=12, color="transparent"),
            ft.Text("Screenshots", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            screenshots,
            ft.Divider(height=16, color="transparent"),
            pr_section,
            ft.Divider(height=16, color="transparent"),
            impact,
        ], spacing=4, scroll=ft.ScrollMode.AUTO)
