# Book Management System (Client-Server CLI App)

A domain-specific REST API built with **FastAPI** paired with a custom **Command Line Interface (CLI)** tool to control it seamlessly over HTTP.

## 🚀 Features & Core Requirements
- **FastAPI Backend**: Fully structured endpoints for managing books.
- **Strict Data Validation**: Implemented using Pydantic models (ensures no empty titles or authors are submitted).
- **Data Contract Pattern**: Fully aligned with the course book architecture (Services return structured dictionaries containing `title` and `items`).

## 🌟 Implemented Bonus Features (+10% Extra Credit)
1. **Polished Rich UI**: Used the `rich` library to render beautiful, colored data tables directly inside the terminal.
2. **Advanced Querying**: Implemented optional query filtering by `author` in the backend and frontend CLI tool.

---

## 🛠️ Installation & Setup

First, clone the repository and install all necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt