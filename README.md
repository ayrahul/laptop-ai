# AI-Based Laptop Problem Diagnosis System Using AO* Search and Knowledge Representation

An academic-grade, full-stack expert system that diagnoses computer and laptop failures by traversing a structured **AND-OR Knowledge Representation Graph** using the **AO\* Heuristic Search Algorithm**.

![Status](https://img.shields.io/badge/System-Operational-emerald)
![AI Engine](https://img.shields.io/badge/Algorithm-AO*_Search-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-teal)
![Frontend](https://img.shields.io/badge/Frontend-React_18_+_TypeScript-indigo)
![Design](https://img.shields.io/badge/Design-White_Glass_Luxury-slate)

---

## 1. Primary Project Objective

Unlike conventional chatbots or hardcoded if-else trees, this system models hardware and software troubleshooting as a formal **AND-OR search graph**:
- **OR Nodes**: Competing diagnostic hypotheses (e.g., A failure could be Power Supply Issue OR Battery Issue OR Motherboard Short).
- **AND Nodes**: Conjoint requirements where multiple symptoms and hardware tests must **all** be confirmed simultaneously (e.g., Battery Failure requires fast drain AND sudden shutoff AND worn cells).
- **AO\* Algorithm**: Explores the state space, calculates admissible heuristic costs, applies bottom-up cost propagation through parent links, and extracts the optimal Best Partial Solution Tree (BPST).
- **Explainable AI**: Produces transparent, itemized justifications answering *"Why did you diagnose this problem?"* accompanied by an interactive graph visualization.

---

## 2. Key System Capabilities

- **Genuine AO\* Search Implementation**: Explicit node expansion, hyperarcs, bottom-up cost propagation, solved marking, and execution tracing (`backend/ai/ao_star.py`).
- **Comprehensive Knowledge Base**: 16 Problem Domains, 60+ Unique Symptoms, 54 Production Rules, and 31 Hardware Diagnostic Procedures.
- **Dynamic Information-Gain Questions**: AI selects follow-up questions dynamically to partition active competing hypotheses with minimum queries.
- **Interactive AO\* Explorer**: Zoomable/pannable SVG graph visualizer highlighting the marked solution path in emerald green, with node inspection and step-by-step trace playback.
- **White Glass Design Aesthetics**: Apple-inspired minimalist luxury UI built with translucent glass cards, smooth micro-interactions, and refined typography.
- **Persistent Audit Trail**: SQLite / PostgreSQL storage of past diagnosis sessions, execution steps, and analytics.
- **Admin Management Portal**: Web interface to add, modify, or recalibrate heuristic costs and rule definitions.

---

## 3. Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, TypeScript, Tailwind CSS, Lucide Icons, Vite |
| **Backend** | Python 3.11+, FastAPI, Pydantic v2, Uvicorn |
| **AI Core** | AO\* Algorithm Engine, AND-OR Hypergraphs, Admissible Heuristics |
| **Database** | SQLAlchemy 2.0 ORM, SQLite (Default) / PostgreSQL (Supported) |
| **Testing** | Pytest, FastAPI TestClient, Automated Integration Suite |

---

## 4. Knowledge Base Metrics

- **Problem Categories (16)**: Power, Battery, Thermal, Performance, Display, Storage, RAM, Wi-Fi, Audio, Keyboard, Touchpad, USB/Ports, Operating System, Motherboard, BIOS, GPU/Graphics.
- **Symptoms (60)**: Granular technical symptoms including `laptop_not_powering_on`, `thermal_throttling`, `blue_screen`, `display_flickering`, `ssd_not_detected`, `speaker_crackling`, etc.
- **Diagnostic Rules (54)**: Structured AND/OR rules complete with heuristic cost, diagnostic cost, base confidence, and step-by-step repair checklists.
- **Diagnostic Actions (31)**: Multimeter voltage checks, thermal gradient tests, MemTest86, DDU clean installations, SMART drive diagnostics, etc.

---

## 5. How AO\* Works in This System

1. **Graph Construction**: On user input, an explicit AND-OR graph is built rooted at `root_{category}`.
2. **Evidence Initialization**: Reported symptoms set leaf node costs to `0.0` (confirmed) or `999.0` (contradicted).
3. **BPST Leaf Selection**: Identifies non-terminal leaves along the currently marked best partial solution tree.
4. **Hyperarc Expansion**: Expands candidate diagnosis AND-nodes and leaf conditions.
5. **Cost Calculation**:
   - For an OR node: $cost(n) = \min_{A_k} [ \text{cost}(A_k) + \sum_{c \in A_k} cost(c) ]$
   - For an AND node: $cost(n) = \text{cost}(\text{AND\_Arc}) + \sum_{c \in C} cost(c)$
6. **Bottom-Up Propagation**: Traverses ancestor pointers, updates parent costs, and marks the best hyperarc.
7. **Termination**: Stabilizes when the root node is marked solved or no unexpanded leaves remain.

---

## 6. Project Structure

```
laptop-diagnosis-ai/
│
├── backend/
│   ├── ai/
│   │   ├── ao_star.py              # AO* Algorithm Engine & Hypergraph structures
│   │   ├── knowledge_base.py       # 16 Categories, 60 Symptoms, 54 Rules, 31 Tests
│   │   ├── diagnostic_engine.py    # Session orchestrator & dynamic questioner
│   │   ├── heuristic.py            # Admissible heuristics & confidence formulas
│   │   └── inference.py            # Transparent reasoning & explanation generator
│   ├── api/
│   │   ├── diagnosis.py            # Diagnostic workflow & graph API endpoints
│   │   ├── symptoms.py             # Symptoms and categories catalog
│   │   ├── knowledge.py            # Knowledge base CRUD & statistics
│   │   └── dashboard.py            # Analytics & metrics endpoints
│   ├── models/
│   │   ├── database.py             # SQLAlchemy engine & sessionmaker
│   │   ├── diagnosis.py            # DiagnosisSessionModel & DiagnosticStepModel
│   │   └── knowledge.py            # KnowledgeRuleModel
│   ├── schemas/
│   │   └── diagnosis.py            # Pydantic validation schemas
│   ├── services/
│   │   └── db_service.py           # Persistence & DB operations
│   ├── tests/
│   │   ├── test_ao_star.py          # Unit tests for AO* search & cost propagation
│   │   ├── test_knowledge_base.py   # Validation tests for KB counts & integrity
│   │   ├── test_diagnostic_engine.py# Scenario-based diagnosis tests
│   │   ├── test_api.py              # FastAPI integration tests
│   │   └── verify_e2e.py            # Live end-to-end integration script
│   ├── config.py                   # Application settings
│   └── main.py                     # FastAPI application entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx          # Glassmorphism header with status badge
│   │   │   └── Footer.tsx          # System information & credits
│   │   ├── pages/
│   │   │   ├── LandingPage.tsx     # Hero, process diagram, categories, FAQ
│   │   │   ├── StartDiagnosisPage.tsx # 5-step diagnostic wizard & results
│   │   │   ├── AOStarExplorerPage.tsx # Interactive SVG AND-OR graph visualizer
│   │   │   ├── KnowledgeBasePage.tsx  # Searchable knowledge catalog
│   │   │   ├── DashboardPage.tsx   # Metrics, distribution bars, top diagnoses
│   │   │   ├── HistoryPage.tsx     # Past sessions log & replay
│   │   │   └── AdminPage.tsx       # Rule management & cost adjustment
│   │   ├── services/
│   │   │   └── api.ts              # HTTP client service
│   │   ├── types/
│   │   │   └── index.ts            # TypeScript interfaces
│   │   ├── App.tsx                 # Root application router
│   │   ├── main.tsx                # React DOM root
│   │   └── index.css               # Tailwind CSS & white glass design tokens
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── docs/
│   ├── architecture.md             # Detailed full-stack architecture
│   ├── ao-star.md                  # AO* mathematical formulation & pseudocode
│   ├── knowledge-base.md           # Knowledge schema & dynamic questioning
│   ├── api.md                      # REST API endpoints documentation
│   └── database.md                 # Database schema & entity relationships
│
├── .env.example
├── docker-compose.yml
├── Dockerfile.backend
└── README.md
```

---

## 7. Installation & Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### 1. Backend Setup
```bash
# From workspace root
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt # (or: pip install fastapi uvicorn pydantic pydantic-settings sqlalchemy pytest)

# Start backend server
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8001 --reload
```
API Documentation will be live at: `http://localhost:8001/docs`

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Web Application will be live at: `http://localhost:5173`

---

## 8. Automated Test Suite

Run all unit, algorithmic, and integration tests:

```bash
# Run backend pytest suite
python -m pytest backend/tests/ -v

# Run live end-to-end integration verification
python backend/tests/verify_e2e.py
```

### Test Coverage Results:
- `test_ao_star.py`: Validates OR node selection, AND node summation, and bottom-up cost propagation.
- `test_knowledge_base.py`: Validates that categories >= 15, symptoms >= 50, rules >= 40, and tests >= 30.
- `test_diagnostic_engine.py`: Validates power and thermal diagnostic scenarios and dynamic discriminator questions.
- `test_api.py`: Validates all REST endpoints (`/health`, `/diagnosis/start`, `/solve`, `/graph`, `/history`, `/dashboard/stats`).
- `verify_e2e.py`: Executes end-to-end HTTP pipeline against live servers.

---

## 9. Academic Presentation Guide

When demonstrating this project to a professor or examiner:
1. **Show the Knowledge Representation (`Knowledge Base` page)**:
   Point out how domain troubleshooting is expressed declaratively with symptoms, tests, heuristic costs, and confidence factors rather than hardcoded logic.
2. **Demonstrate Dynamic Questioning (`Start Diagnosis` page)**:
   Select a category (e.g. *Thermal*) and symptoms. Notice how the AI asks targeted discriminator questions specifically chosen to differentiate between competing candidate hypotheses.
3. **Inspect the AO\* Search Graph (`AO* Explorer` page)**:
   - Highlight the **AND nodes** (requiring all conjoined conditions) vs **OR branches** (competing hypotheses).
   - Point out the **green illuminated hyperarcs** indicating the globally optimal solution subgraph.
   - Click on any node to view the mathematical formula evaluation and $f(n)$ / $h(n)$ values in the sidebar.
   - Use the **Step-by-Step Playback Scrubber** to replay each expansion and cost propagation step.
4. **Explainable Reasoning (`Results` page)**:
   Review the itemized *"Why did the AI diagnose this?"* section and the step-by-step reasoning chain connecting user evidence to the prescribed hardware repair action.
