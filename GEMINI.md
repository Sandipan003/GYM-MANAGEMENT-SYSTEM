# Gemini Multi-Agent Architecture for KINETIC PULSE

This document outlines the multi-agent workflow configured for KINETIC PULSE, an Elite Performance Gym Management System. By utilizing the Gemini CLI's Agent-to-Agent (A2A) protocol, we delegate specific development, database, and UI tasks to specialized remote subagents optimized for our tech stack.

## 🤖 Agent Directory

The local Gemini CLI orchestrator routes tasks based on the descriptions provided in the `.gemini/agents/` directory.

### 1. Backend Django Agent (`backend-agent.md`)
* **Role:** Manages the Django 4.2 framework and PyMySQL backend integrations.
* **Responsibilities:** Updates the core business logic for the member CRM, automated billing status, tier plans, and smart filtering.
* **Trigger Keywords:** "Update Django views," "modify Python models," "check membership auto-billing logic."
* **Location:** `https://agents.internal.kineticpulse.com/django-backend`

### 2. Database & Analytics Agent (`database-agent.md`)
* **Role:** Interacts directly with the MySQL 8.0 database (`kinetic_pulse_db`).
* **Responsibilities:** Executes complex queries to feed the Elite Dashboard, such as aggregating data for the Revenue Velocity Chart, Peak Hours Heatmap, and transaction ledger.
* **Trigger Keywords:** "Query MySQL," "generate attendance heatmap," "fetch revenue data."
* **Location:** `https://agents.internal.kineticpulse.com/mysql-analytics`

### 3. Frontend UI Agent (`frontend-agent.md`)
* **Role:** Maintains and updates the Vanilla HTML/JS and Tailwind CSS (3.0) interface.
* **Responsibilities:** Ensures the modern glassmorphism aesthetic is consistent, manages Google Material Symbols, and handles Lexend & Inter typography updates.
* **Trigger Keywords:** "Update Tailwind styling," "modify dashboard UI," "add glassmorphism effect."
* **Location:** `https://agents.internal.kineticpulse.com/tailwind-ui`

---

## ⚙️ Setup and Configuration

To use these agents locally while developing KINETIC PULSE:

1. **Verify Environment:** Ensure your `.env` file is properly configured with your `kinetic_pulse_db` credentials, including the default MAMP port (`8889`).
2. **Clone the Agent Cards:** Place the corresponding agent markdown files into the `.gemini/agents/` folder of your project repository.
3. **Start the Orchestrator:** Run `gemini chat` from the root directory where your `manage.py` file is located.

---

## 🚀 Usage Examples

**Example 1: Dashboard Analytics**
> **User:** "Calculate the live active member counts and monthly revenue for the Elite Dashboard."
> **Action:** The orchestrator delegates this task to the **Database & Analytics Agent** to run the necessary queries against `kinetic_pulse_db`.

**Example 2: UI Enhancements**
> **User:** "Add a new section to the live activity feed using Tailwind CSS to match the existing glassmorphism style."
> **Action:** The orchestrator assigns the styling and component layout updates to the **Frontend UI Agent** to implement the required Vanilla JS and Tailwind classes.

**Example 3: Backend Logic**
> **User:** "Write a new Python function to auto-generate professional member IDs starting with #KP-0001."
> **Action:** The orchestrator routes this to the **Backend Django Agent** to implement the logic within the appropriate Django model.