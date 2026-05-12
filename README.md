# Python in 90 Days — Productivity Tracker

**Goal:** Learn the 20% of Python that unlocks 80% of real-world data science & sports analytics output.
**Owner:** Wisdom (Matthew Wisdom Letam)
**Start date:** Tuesday, 12 May 2026
**Target end date:** Monday, 10 August 2026 (Day 90)
**End state:** Rebuild the Betting Engine's statistical core in Python with proper libraries, plus ~10 mini-projects and one portfolio-grade capstone.

---

## Ground Rules

- [ ] I write all the code. Claude only explains, reviews, and debugs.
- [ ] Daily GitHub commit (even a small one). The streak is the receipt.
- [ ] Daily dev journal entry (use the accountability template).
- [ ] One mini-project shipped per week.
- [ ] No skipping fundamentals to chase shiny libraries.
- [ ] Weekly retro every Sunday (or whichever day closes my week).

---

## Phase 1 — Core Python (Days 1–21)

**Spine:** _Tiny Python Projects_ by Ken Youens-Clark
**Supplement:** Corey Schafer's OOP playlist on YouTube (Week 3)
**Tooling setup:** Python 3.12+, VS Code, `venv`, `pip`, Git, `pytest`, `black`, `ruff`

### Week 1 — Foundations & Pythonic Idioms

- [ ] Environment setup (Python, VS Code, venv, Git)
- [ ] Syntax, types, operators, control flow
- [ ] Lists, tuples, dicts, sets — and _when each is the right choice_
- [ ] First `pytest` test passing
- [ ] **Mini-project 1:** CLI tip/odds calculator (with tests)
- [ ] 7 daily commits

### Week 2 — Functions, Comprehensions, Generators

- [ ] Functions: positional/keyword args, `*args`/`**kwargs`, `lambda`, scope
- [ ] Default-argument pitfall (mutable defaults)
- [ ] List / dict / set comprehensions
- [ ] Generators and `yield`
- [ ] Modules and virtual environments
- [ ] **Mini-project 2:** Parse a fixtures CSV and emit a league table
- [ ] 7 daily commits

### Week 3 — OOP, Errors, Stdlib Essentials

- [ ] Classes, `__init__`, inheritance, dunder methods (`__repr__`, `__eq__`, `__len__`)
- [ ] Watch Corey Schafer's OOP playlist (~2 hrs)
- [ ] Exception handling, custom exceptions
- [ ] `pathlib` for file I/O
- [ ] Type hints basics
- [ ] Stdlib tour: `datetime`, `collections`, `itertools`, `json`, `csv`, `re`, `functools`
- [ ] **Mini-project 3:** Class-based bet tracker that saves to JSON
- [ ] 7 daily commits

---

## Phase 2 — The Data Stack (Days 22–49)

**Spine:** _Python for Data Analysis_ (3rd ed.) by Wes McKinney — free online

### Week 4 — NumPy

- [ ] Arrays, dtypes, shape, reshape
- [ ] Vectorization and broadcasting
- [ ] Axis operations (`sum`, `mean`, `argmax` over axes)
- [ ] Boolean indexing and fancy indexing
- [ ] Random sampling (`np.random.default_rng`)
- [ ] **Mini-project 4:** Vectorized Monte Carlo coin-flip / dice simulator (no `for` loops)
- [ ] 7 daily commits

### Week 5 — Pandas Part 1

- [ ] Series and DataFrame fundamentals
- [ ] `.loc` vs `.iloc` indexing
- [ ] Filtering, sorting, basic transformations
- [ ] Reading/writing CSV, Excel, SQL
- [ ] **Mini-project 5:** Load a season of EPL match data, compute a basic league table
- [ ] 7 daily commits

### Week 6 — Pandas Part 2

- [ ] `groupby` (split-apply-combine)
- [ ] `merge` / `join` / `concat`
- [ ] Pivot tables and crosstabs
- [ ] Time series basics (`pd.to_datetime`, resampling)
- [ ] Missing-data handling (`isna`, `fillna`, `dropna`)
- [ ] Method chaining as a style
- [ ] **Mini-project 6:** Pandas notebook analyzing my own historical bets — ROI by market, CLV, drawdown curves
- [ ] 7 daily commits

### Week 7 — Visualization

- [ ] Matplotlib: figure/axes model, subplots, styling
- [ ] Seaborn: distributions, heatmaps, regression plots
- [ ] Plotly: one interactive chart end-to-end
- [ ] **Mini-project 7:** One-screen PNG dashboard summarizing a league's season
- [ ] 7 daily commits

---

## Phase 3 — Statistical Modeling (Days 50–70)

### Week 8 — SciPy.stats & Monte Carlo

- [ ] Distributions: Poisson, Negative Binomial, Beta, Normal
- [ ] PMFs, CDFs, sampling, fitting
- [ ] Hypothesis testing basics (`ttest`, `chi2`)
- [ ] **Mini-project 8:** Monte Carlo match simulator given team strengths
- [ ] 7 daily commits

### Week 9 — statsmodels & Dixon-Coles

- [ ] GLM with Poisson family
- [ ] GLM with Negative Binomial family (overdispersion)
- [ ] Model diagnostics (residuals, AIC)
- [ ] **Implement Dixon-Coles from scratch in Python** — JS version is the spec
- [ ] **Mini-project 9:** Fit a Poisson goals model on real data and evaluate it
- [ ] 7 daily commits

### Week 10 — scikit-learn essentials

- [ ] Train/test split, k-fold cross-validation
- [ ] Logistic regression
- [ ] Isotonic and Platt calibration
- [ ] Brier score, log loss, reliability diagrams
- [ ] **Mini-project 10:** Full calibration pipeline — raw probs → calibrated → reliability plot
- [ ] 7 daily commits

---

## Phase 4 — Capstone: Betting Engine, Python Edition (Days 71–90)

One substantial project that demonstrably uses everything above.

### Week 11 — Data Ingestion

- [ ] Scrape or API-fetch fixtures and results (Requests + BeautifulSoup)
- [ ] Clean data with Pandas
- [ ] Persist to SQLite via `sqlite3`
- [ ] Document data sources and schema in `README.md`
- [ ] 7 daily commits

### Week 12 — Modeling

- [ ] Fit Dixon-Coles + decay-weighted xG on the persisted data
- [ ] Output calibrated probabilities for 1X2, Over/Under, BTTS
- [ ] Compare to bookmaker odds and flag value bets
- [ ] Write unit tests for the math
- [ ] 7 daily commits

### Week 13 — Reporting & Backtest

- [ ] Jupyter notebook producing a weekly report (top edges, CLV, bankroll curve)
- [ ] Backtest on past seasons with proper out-of-sample discipline
- [ ] Automate weekly run (cron, Task Scheduler, or GitHub Actions)
- [ ] Write a `README.md` with usage, architecture diagram, results
- [ ] Final 7 daily commits

---

## Day 90 Deliverables Checklist

- [ ] GitHub repo with ≥ 90 daily commits
- [ ] 10 mini-projects, each with a `README` and tests
- [ ] Capstone project: Python Betting Engine repo with docs
- [ ] Dev journal: 90 daily entries + 13 weekly retros
- [ ] CV updated to reflect new Python competency
- [ ] One short blog post or LinkedIn write-up: "What I built in 90 days"

---

## What I am deliberately NOT learning (yet)

These are useful but not part of the 20%. Park them.

- Django, Flask, FastAPI (will pick up via MERN backend if needed)
- async/await deep dive
- Decorators deep dive, metaclasses
- PyTorch / deep learning
- Web scraping at scale (Scrapy, Selenium)

---

_Streak counter:_ Day **\_** of 90
_Mini-projects shipped:_ **\_** of 10
