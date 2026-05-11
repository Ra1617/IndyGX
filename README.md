# IndyGX — Company Intelligence Platform

IndyGX is a tool built for people who spend too much time hunting for company data across a dozen different tabs. It pulls together everything worth knowing about a business — financials, leadership, competitive position, digital footprint, partnerships — and puts it in one place.

---

## What it does

You give it a company. It gives you the full picture.

Each company profile is broken into seven distinct modules. Instead of one giant wall of text, you get focused sections you can jump between: core identity, competitive landscape, funding history, contact details, online presence, ecosystem partnerships, and an internal assessment score.

The backend is a FastAPI application that talks to a PostgreSQL database hosted on Supabase. The frontend is a Django app that calls those API endpoints and renders the data through a custom-built dark interface — black background, orange accents, nothing that looks like a default Bootstrap page.

---

## Project Structure

```
IndyGX/
├── backend/                   # FastAPI application
│   ├── api/                   # Route definitions per module
│   ├── repository/            # Database query logic
│   ├── schemas/               # Pydantic models for validation
│   ├── models.py              # SQLModel table definitions
│   ├── database.py            # Engine and session setup
│   └── app.py                 # FastAPI app with all routers
│
├── frontend_django/           # Django frontend
│   ├── companies/             # App: views, urls, api_client
│   ├── core/                  # Django settings, main urls
│   ├── templates/             # HTML templates per section
│   └── static/css/main.css    # Full design system
│
└── services/                  # Microservice stubs (per intelligence domain)
```

---

## The Data Model

Every company tracked in the system has a primary record and six related tables. Here's what each one holds:

| Module | What's inside |
|---|---|
| **Company Primary** | Name, type, CEO, employee size, sectors, website, LinkedIn |
| **Company Secondary** | Social handles, key leaders, licenses, compliance history |
| **Competitive Intelligence** | Competitors, differentiators, advantages, weaknesses, challenges |
| **Contact Information** | General email/phone, primary contact person details |
| **Digital Presence & Brand** | Website quality, traffic rank, social followers, ratings (Glassdoor, Google, Indeed) |
| **Financials & Funding** | Revenue, profit, valuation, growth rate, investors, funding rounds |
| **IndyGX Assessment** | Internal scoring: partnership potential, collaboration score, complementary services match |

---

## Tech Stack

**Backend**
- Python 3.12
- FastAPI — handles routing and request validation
- SQLModel — ORM layer on top of SQLAlchemy
- PostgreSQL (Supabase) — primary database
- Pydantic — schema validation and serialization

**Frontend**
- Django 6 — templating, routing, session management
- Vanilla CSS — no frameworks; custom design tokens throughout
- `requests` — the Django views call the FastAPI backend directly
- Google Fonts: Space Grotesk (headings) + Inter (body)

---

## Running It Locally

You need two things running at the same time: the FastAPI backend on port 8000, and the Django frontend on port 8080.

**Step 1 — Set up your environment**

```bash
# From the project root
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

**Step 2 — Configure the database**

Create a `.env` file at the project root (or inside the `Indygx/` subfolder):

```
DATABASE_URL=postgresql://user:password@host:5432/postgres
```

**Step 3 — Start the FastAPI backend**

```bash
uvicorn backend.app:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs`

**Step 4 — Start the Django frontend**

```bash
cd frontend_django
python manage.py migrate
python manage.py runserver 8080
```

Open `http://localhost:8080` in your browser.

---

## API Endpoints

The FastAPI backend exposes these route groups:

| Prefix | Description |
|---|---|
| `GET /companies/` | Paginated company list with optional filters |
| `GET /companies/{id}` | Basic company record |
| `GET /companies/{id}/full-profile` | All related data joined in one response |
| `POST /companies/bulk-upsert` | Batch insert or update company records |
| `GET /competitive-intelligence/{id}` | Competitive data for a company |
| `GET /financials-funding/{id}` | Funding and financial metrics |
| `GET /contact-information/{id}` | Contact details |
| `GET /digital-presence-brand/{id}` | Digital and brand metrics |
| `GET /partnerships-ecosystem/{id}` | Partnership and R&D data |
| `GET /indygx-assessment/{id}` | Internal assessment scores |

Each sub-module also has `PUT` (upsert) and `DELETE` endpoints.

---

## Frontend Pages

| URL | What you see |
|---|---|
| `/` | Dashboard with total company count and recent entries |
| `/companies/` | Searchable, filterable company directory |
| `/companies/<id>/` | Overview tab — core info and leadership |
| `/companies/<id>/competitive-intelligence/` | Competitors, gaps, advantages |
| `/companies/<id>/financials/` | Revenue, funding rounds, investors |
| `/companies/<id>/contact/` | Email, phone, primary contact person |
| `/companies/<id>/digital-presence/` | Ratings, traffic, social following |
| `/companies/<id>/partnerships/` | Corporate programs, tech partners, R&D % |
| `/companies/<id>/assessment/` | IndyGX scoring breakdown |

---

## Design Choices

The interface was built from scratch using only CSS custom properties — no Tailwind, no Bootstrap. The color system is anchored on `#080808` (near-black) and `#f97316` (orange). Headings use Space Grotesk for geometric weight. Body text uses Inter for readability at small sizes.

Sidebar navigation collapses to icon-only mode on smaller viewports. Cards animate in on scroll using a lightweight IntersectionObserver. Stat cards have a top-border gradient that lights up orange on hover.

No third-party component libraries were used. Every element — pagination, tab bars, info rows, search inputs — is hand-written.

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DATABASE_URL` | Yes | Full PostgreSQL connection string |
| `SECRET_KEY` | No (dev only) | Django secret key — change before any deployment |

---

## What's missing / known gaps

- No authentication on the frontend. Anyone who can reach port 8080 can browse all data.
- The search filter on the company list only supports exact `company_name` and `industry_segment` matches — no fuzzy search.
- The `services/` directory contains per-domain microservice stubs that are not yet wired up.
- Docker Compose file is present but empty — container setup is not done yet.

---

## Contributing

Open a pull request against `main`. Keep commits atomic — one change per commit. No force-pushes to main.
