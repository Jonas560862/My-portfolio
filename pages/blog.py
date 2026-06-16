import flet as ft
import math

BG       = "#0A0F1E"
SURFACE  = "#111827"
SURFACE2 = "#1A2233"
BORDER   = "#2A3347"
TEXT_PRI = "#F0F4FF"
TEXT_SEC = "#8FA3C0"
ACCENT   = "#F5A623"
ACCENT_B = "#C07800"
BLUE     = "#4A9EFF"


def _estimate_read_time(content: str) -> str:
    words   = len(content.split())
    minutes = max(1, math.ceil(words / 200))
    return f"{minutes} min read"


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


class BlogPage:
    POSTS = [
        {
            "title": "Semester Reflection Video — My Contributions to Safe Sphere",
            "date": "15 June 2026",
            "summary": "A personal walkthrough of my role as UI/UX Lead on the Safe Sphere safety app project.",
            "content": """## My Semester Reflection

In this video I walk through my individual contributions to the Safe Sphere group project during the Computer Programming semester at UNAM.

### What I covered:
- My role as UI/UX Lead and GitHub manager
- Designing the app screens and user flow for Safe Sphere
- Collaborating with the Firebase and development leads
- Lessons learned about working in a large team (16 members)
- How I applied React Native and Expo in practice
""",
            "video_embedded": True,
            "video_file": "reflection_video.mp4",
            "tags": ["Reflection", "Safe Sphere", "UI/UX"],
        },
        {
            "title": "Understanding the Safe Sphere App Architecture",
            "date": "10 June 2026",
            "summary": "A breakdown of how we built the Safe Sphere safety education app using React Native and Firebase.",
            "content": """## Safe Sphere Tech Stack

**Frontend:** Expo + React Native
**Backend:** Firebase Authentication + Firestore + Firebase Storage

### Key Components

```javascript
// User authentication
import { signInWithEmailAndPassword } from 'firebase/auth';

// Firestore course data structure
const course = {
  courseId: 'mining-101',
  title: 'Mining Safety Basics',
  description: '...',
  content: '...'
};
```

### Data Model
- **Users**: userID, name, email, progress level
- **Courses**: courseID, title, description, content
- **Progress**: userID, courseID, completion status, score
""",
            "video_embedded": False,
            "video_file": None,
            "tags": ["React Native", "Firebase", "Safe Sphere"],
        },
        {
            "title": "UI/UX Design Decisions for a Safety App",
            "date": "5 June 2026",
            "summary": "Why clarity and simplicity matter most when designing for mine workers and industrial visitors.",
            "content": """## Designing for Safety

When designing Safe Sphere, the primary users are:
- Mine workers (often basic smartphone users)
- Industrial visitors
- Engineering students

### Design Principles Applied
1. **Simple, intuitive interface** — no training required
2. **Clear contrast and readable fonts** — accessibility first
3. **Iconography** — icons and labels that are self-explanatory
4. **Error guidance** — messages that tell users how to fix issues

The app had to feel trustworthy. A safety app that confuses its users defeats its own purpose.
""",
            "video_embedded": False,
            "video_file": None,
            "tags": ["UI/UX", "Design", "Safe Sphere"],
        },
        {
            "title": "Brand Logo Integration in React Native",
            "date": "14 June 2026",
            "summary": "How I added the Safe Sphere brand logo as a reusable component across our React Native app.",
            "content": """## BrandLogo Component

One of my UI/UX contributions was creating a reusable brand logo component for the Safe Sphere app.

```javascript
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
  logo: {
    width: 72,
    height: 72,
  },
});
```

This component can be dropped into any screen with a custom `style` prop override, keeping the brand consistent across the entire app.
""",
            "video_embedded": False,
            "video_file": None,
            "tags": ["React Native", "UI/UX", "Components"],
        },
        {
            "title": "How Git Branching Kept Our 16-Person Team in Sync",
            "date": "1 June 2026",
            "summary": "Lessons from managing a large group repository for the Safe Sphere semester project.",
            "content": """## Git Strategy for Large Teams

With 16 members across 4 sub-teams (Dev, UI/UX, Firebase, Docs), branching discipline was critical.

### Our approach:
1. **main** — stable, deployable code only
2. **dev** — integration branch for testing
3. **feature/your-name-feature** — individual work branches

As GitHub manager, I helped enforce this structure so no one accidentally broke main.
""",
            "video_embedded": False,
            "video_file": None,
            "tags": ["Git", "Collaboration", "Safe Sphere"],
        },
    ]

    ALL_TAGS = sorted({tag for post in POSTS for tag in post["tags"]})

    def __init__(self):
        self._active_tag = None
        self._cards_ref  = ft.Ref[ft.Column]()

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=11, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _filter_chip(self, label, on_click):
        active = (label == "All" and self._active_tag is None) or (label == self._active_tag)
        return ft.Container(
            content=ft.Text(label, size=12,
                            color=BG if active else TEXT_SEC,
                            weight=ft.FontWeight.W_600 if active else ft.FontWeight.W_400),
            bgcolor=ACCENT if active else SURFACE,
            padding=ft.Padding(left=14, right=14, top=6, bottom=6),
            border_radius=20,
            border=ft.Border.all(1, ACCENT if active else BORDER),
            on_click=on_click,
            ink=True,
        )

    def _build_video_section(self, video_file):
        playlist = [ft.VideoMedia(f"assets/{video_file}")]
        player = ft.Video(
            playlist=playlist,
            width=640,
            height=360,
            fit=ft.ImageFit.CONTAIN,
            autoplay=False,
            show_controls=True,
            playlist_mode=ft.PlaylistMode.NONE,
        )
        return ft.Container(
            content=ft.Column(controls=[
                ft.Text("📹 Semester Reflection Video", size=13,
                        weight=ft.FontWeight.W_600, color=TEXT_PRI),
                ft.Container(
                    content=player,
                    bgcolor=SURFACE2,
                    border_radius=10,
                    border=ft.Border.all(1, ACCENT + "44"),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
            ], spacing=8),
            bgcolor=SURFACE2, border_radius=8,
            padding=ft.Padding(left=12, right=12, top=12, bottom=12),
            margin=ft.Margin(left=0, right=0, top=8, bottom=0),
            border=ft.Border.all(1, ACCENT + "44"),
        )

    def _build_post_card(self, post):
        read_time   = _estimate_read_time(post["content"])
        content_col = ft.Column(
            controls=[ft.Markdown(post["content"], selectable=True,
                                  extension_set="gitHubFlavored",
                                  code_theme="atom-one-dark")],
            visible=False,
        )
        if post.get("video_embedded") and post.get("video_file"):
            content_col.controls.append(self._build_video_section(post["video_file"]))

        btn_text   = ft.Text("Read more ▾", color=ACCENT, size=13)
        expand_btn = ft.TextButton(content=btn_text)

        def toggle_expand(e, cc=content_col, bt=btn_text):
            cc.visible = not cc.visible
            bt.value   = "Read less ▴" if cc.visible else "Read more ▾"
            e.page.update()

        expand_btn.on_click = toggle_expand

        # First post gets a special video badge
        is_video_post = post.get("video_embedded")
        badges = []
        if is_video_post:
            badges.append(ft.Container(
                content=ft.Row(controls=[
                    ft.Icon(ft.Icons.VIDEOCAM, size=12, color=ACCENT),
                    ft.Text("Video", size=11, color=ACCENT, weight=ft.FontWeight.W_600),
                ], spacing=4),
                bgcolor=ACCENT_B + "33",
                padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                border_radius=20,
                border=ft.Border.all(1, ACCENT_B),
            ))

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Text(post["title"], size=15, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI, expand=True),
                        ft.Text(post["date"], size=12, color=TEXT_SEC),
                    ]),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ACCESS_TIME, size=13, color=TEXT_SEC),
                        ft.Text(read_time, size=12, color=TEXT_SEC),
                        *badges,
                    ], spacing=8),
                    ft.Text(post["summary"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[self._tag_chip(t) for t in post["tags"]],
                           spacing=6, wrap=True),
                    content_col,
                    expand_btn,
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, ACCENT + "55" if is_video_post else BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=12),
            ),
            ACCENT if is_video_post else BLUE,
        )

    def _rebuild_cards(self, page):
        filtered = (self.POSTS if self._active_tag is None
                    else [p for p in self.POSTS if self._active_tag in p["tags"]])
        self._cards_ref.current.controls = [self._build_post_card(p) for p in filtered]
        page.update()

    def _make_filter_row(self, page):
        all_labels = ["All"] + self.ALL_TAGS

        def make_handler(label):
            def handler(e):
                self._active_tag = None if label == "All" else label
                filter_row.controls = [self._filter_chip(l, make_handler(l)) for l in all_labels]
                self._rebuild_cards(page)
            return handler

        filter_row = ft.Row(
            controls=[self._filter_chip(l, make_handler(l)) for l in all_labels],
            spacing=8, wrap=True,
        )
        return filter_row

    def build(self, page=None):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ARTICLE, color=TEXT_PRI, size=28),
                        ft.Text("Technical Blog", size=24, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Jonas Haikela — programming concepts, design decisions, and semester reflections.",
                            size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Text(f"{len(self.POSTS)} Posts", size=12, color=ACCENT),
                            bgcolor=ACCENT_B + "33",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, ACCENT_B),
                        ),
                        ft.Container(
                            content=ft.Row(controls=[
                                ft.Icon(ft.Icons.VIDEOCAM, size=12, color=ACCENT),
                                ft.Text("Reflection video embedded below", size=12, color=ACCENT),
                            ], spacing=4),
                            bgcolor=ACCENT_B + "22",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, ACCENT_B + "88"),
                        ),
                    ], spacing=8),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        cards_col  = ft.Column(ref=self._cards_ref,
                               controls=[self._build_post_card(p) for p in self.POSTS],
                               spacing=0)
        filter_row = self._make_filter_row(page) if page else ft.Row(spacing=8)

        return ft.Column(controls=[
            hero,
            ft.Text("Filter by Topic", size=13, weight=ft.FontWeight.W_600, color=TEXT_SEC),
            filter_row,
            ft.Divider(height=16, color="transparent"),
            cards_col,
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
