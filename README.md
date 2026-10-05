# Frontend Performance Optimization Challenge

A small portfolio page built in two versions to demonstrate front-end performance optimization.

- `before/` – deliberately unoptimized (large PNGs, render-blocking scripts, unminified CSS/JS, unused CSS)
- `after/` – optimized (resized WebP + srcset, lazy loading, width/height, defer/async, minified assets, preload, cache headers)
- `gen_images.py` – script that generated the demo images
- `Performance_Report.docx` – before/after analysis report

## How to measure
1. Host each folder (GitHub Pages, Netlify, or `python -m http.server`).
2. Run PageSpeed Insights or Chrome DevTools > Lighthouse (mobile + desktop).
3. Record Performance score, FCP, LCP, TBT, CLS and total page weight.

## Optimizations applied
| Issue | Fix |
|---|---|
| ~8 MB PNG images | Resized, converted to WebP, `srcset`/`sizes` |
| Below-the-fold images load immediately | `loading="lazy"`, `decoding="async"` |
| Layout shift from images | Explicit `width`/`height` |
| Blocking scripts in `<head>` | `defer` / `async`; removed 350 ms main-thread block |
| Unminified CSS/JS | Minified; unused CSS removed |
| Slow LCP | Preloaded hero image, `fetchpriority="high"` |
| No caching | Long-lived `Cache-Control` via `_headers` (Netlify) |
