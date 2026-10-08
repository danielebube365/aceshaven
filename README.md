# Aces Haven website

A fast, static website for Aces Haven: six self-contained short-stay homes near Heathrow and west London.
There's no WordPress and no database. The site is plain HTML, CSS and a little JavaScript, so it can be hosted anywhere.

## Pages

| Page | File |
| --- | --- |
| Home | `index.html` |
| All Havens | `stays.html` |
| Each Haven | `stays/<name>.html` |
| Local guide | `explore.html` |
| About | `about.html` |
| Contact | `contact.html` |

## Editing content

Phone numbers, email, properties (text, photos, Airbnb and Booking.com links), reviews and the local guide
all live in **`tools/build.py`**. Edit that file, then rebuild:

```bash
python tools/build.py
```

Styles are in `assets/css/site.css`, interactions in `assets/js/site.js`, photos in `assets/img/`
(each photo has a full-size `name.webp` and a small `name-sm.webp`).

## Preview locally

```bash
python -m http.server 8080
```

Then open http://localhost:8080.

## Hosting on GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repository go to **Settings → Pages**, set the source to **Deploy from a branch**, choose `main` and `/ (root)`.
3. The site goes live at `https://<username>.github.io/<repo>/`.

## Moving to aceshaven.co later

1. In **Settings → Pages → Custom domain**, enter `aceshaven.co` (this creates a `CNAME` file).
2. At the domain registrar, point the domain at GitHub Pages:
   - `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record for `www`: `<username>.github.io`
3. Once the DNS check passes, tick **Enforce HTTPS**.

Alternatively, upload the whole folder (minus `tools/`) to any web host; there is nothing to install.
