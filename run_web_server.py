#!/usr/bin/env python3
"""
🌟 Smart Face Recognition Web Server Startup Script
"""

import sys
import os
from smart_face_recognition import run_web_server

def main():
    print("🌟 Smart Face Recognition Web Server")
    print("=" * 50)
    
    # Check if required files exist
    required_files = [
        "visit-cluster.json",
        "templates/index.html",
        "static/no-image.png"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all required files are present before starting the server.")
        return
    
    print("✅ All required files found!")
    print("\n🚀 Starting web server...")
    print("📱 Web Interface: http://localhost:8000")
    print("📊 API Documentation: http://localhost:8000/docs")
    print("🔄 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Start the web server
        run_web_server(host="0.0.0.0", port=8007)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
