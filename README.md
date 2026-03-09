# positivity_project

A Django project with a `gratitude` app for tracking sources of gratitude.

## Project Structure

```
positivity_project/
├── positivity_project/   # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── gratitude/            # Gratitude app
│   ├── migrations/
│   ├── models.py         # SourceOfGratitude model
│   ├── admin.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── Procfile              # Heroku process config
├── runtime.txt           # Heroku Python version
└── .env.example
```

---

## Local Development Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your environment

```bash
cp .env.example .env
```

Edit `.env` and fill in:

```
DEBUG=True
SECRET_KEY=some-long-random-string
DATABASE_URL=postgres://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
```

Your Supabase connection string is found at:
**Supabase Dashboard → Project → Settings → Database → Connection string (URI mode)**

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## Deploying to Heroku

### 1. Create the Heroku app

```bash
heroku create your-app-name
```

### 2. Add Heroku Postgres addon

```bash
heroku addons:create heroku-postgresql:essential-0
```

This automatically sets `DATABASE_URL` in your Heroku config vars.

### 3. Set remaining config vars

```bash
heroku config:set SECRET_KEY="your-production-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
```

### 4. Deploy

```bash
git push heroku main
```

The `Procfile` runs `python manage.py migrate` automatically on each deploy via the `release` process.

---

## Model

### `SourceOfGratitude`

| Field | Type        | Notes             |
|-------|-------------|-------------------|
| `id`  | BigAutoField | Primary key, auto |
| `text`| TextField   | The gratitude text |
