"""
Flet Portfolio Web App - Render Deployment
Runs the Flet app in web mode on Render
"""
import os
from main import main
import flet as ft

if __name__ == "__main__":
    # Get the port from environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    
    # Run Flet in web mode
    ft.app(
        target=main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=port,
    )
