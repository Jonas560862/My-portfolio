"""
Flet Portfolio Web App - Render Deployment
Runs the Flet app in web mode on Render with WSGI support
"""
import os
from main import main
import flet as ft

# Create Flet app with Flask WSGI export for Gunicorn
app = ft.app(
    target=main,
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER,
    export_flask_app=True,  # Export Flask app for WSGI servers
)
