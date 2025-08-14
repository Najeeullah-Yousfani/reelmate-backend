# 🎬 ReelMate Backend

**ReelMate** is a social streaming platform inspired by Netflix, with chat, AI recommendations, and user-to-user interaction.

This is the backend built with:
- 🐍 Django (Python)
- 🐳 Docker
- 🐘 PostgreSQL
- 🚀 Render.com for hosting
- 🔁 GitHub Actions for CI/CD

---

## 🔧 Features
- User authentication (JWT)
- Video models with metadata
- Watch history & watchlist
- Follow/unfollow system
- REST API for frontend consumption
- Ready for real-time (chat, "watching now")

---

## 🗂️ Tech Stack
| Layer     | Tech         |
|-----------|--------------|
| Backend   | Django       |
| DB        | PostgreSQL   |
| DevOps    | Docker, GitHub Actions |
| Hosting   | Render.com   |

---

## 🐳 Run Locally with Docker

```bash
git clone https://github.com/YOUR_USERNAME/reelmate-backend.git
cd reelmate-backend
docker compose up --build
```
