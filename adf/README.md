# 🚀 ADF & Databricks Manual Deployment with GitHub (Dev → Prod)

## 📌 Overview

This repository enables manual promotion of **Azure Data Factory (ADF)** and **Azure Databricks** artifacts across **development** and **production** environments using **GitHub as source control**. It follows a structured, GitOps-friendly release process while supporting manual imports into each service.

---

## 🧱 Project Structure
```bash
adf-dbx-deployment/
│
├── adf/
│   ├── dev/
│   │   ├── pipeline/
│   │   ├── dataset/
│   │   └── linkedService/
│   └── prod/
│       ├── pipeline/
│       ├── dataset/
│       └── linkedService/
│
├── databricks/
│   ├── dev/
│   │   └── notebooks/
│   └── prod/
│       └── notebooks/
│
└── README.md
```

## 🧩 Azure Data Factory (ADF) Deployment Guide
🔁 ADF Git Integration

1. Go to ADF Dev > Manage > Git Configuration

2. Connect to this GitHub repo and choose the desired collaboration branch (e.g. dev)

💻 Development in Dev ADF

- Create/edit pipelines, datasets, and linked services in ADF UI.

- Your changes are committed to /adf/dev/.

## 🚀 Promoting to Production ADF
#### 🛠 Option A: Manual UI Deployment

1. In ADF Dev, go to: Manage > ARM template > Export
2. Download:
   - ARMTemplateForFactory.json
   - ARMTemplateParametersForFactory.json
3. In ADF Prod, go to: Manage > ARM template > Import
4. Upload the downloaded templates

#### 🧪 Option B: GitOps Manual Promotion

1. Create a new release branch from dev (e.g. release/adf-2025-06)
2. Review changes and open a PR → main
3. Copy validated artifacts from /adf/dev/ → /adf/prod/
4. In ADF Prod UI, import ARM templates from /adf/prod/

## 🧠 ADF Best Practices

- Use Key Vault-backed linked services to manage secrets per environment.

- Parameterize values that change between dev/prod (e.g. storage paths, database names).

## 🔷 Azure Databricks Deployment Guide
#### 💻 Development in Dev Workspace
- Create or modify notebooks in /Workspace/Repos/... or via Git-backed repo.
- Store all dev notebooks in /databricks/dev/notebooks/.
#### 🚀 Promoting to Production Databricks
##### ✋ Manual Promotion (UI)
1. Download notebook .ipynb or .dbc from GitHub
2. Go to Databricks Prod Workspace → Workspace > Import
3. Upload the notebook to the appropriate folder

#### ⚙️ CLI Deployment (Optional)
Install Databricks CLI:
```bash
pip install databricks-cli
databricks configure --token
```
Deploy notebooks to production:
```bash
databricks workspace import_dir ./databricks/dev/notebooks /Workspace/target-folder
```

## 🏷️ Release Process
1. Create a new branch:
    ```bash
    git checkout -b release/YYYY-MM-DD
    ```
2. Tag the release:
    ```bash
    git tag -a v1.0.0 -m "Release: Promote to prod"
    git push origin v1.0.0
    ```
3. Promote artifacts:
- ADF: Export/import ARM templates
- Databricks: Upload notebooks manually or via CLI
4. Copy `/dev/` → `/prod/` in GitHub for historical tracking

## 📚 References
- [ADF CI/CD with ARM Templates](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery)
- [Databricks CLI Docs](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/)
- [Databricks Git Integration](https://learn.microsoft.com/en-us/azure/databricks/repos/)

## ✅ Summary
| Area               | Dev Environment            | Prod Environment  | Promotion Type     |
| ------------------ | -------------------------- | ----------------- | ------------------ |
| Azure Data Factory | Git-integrated via UI      | Manual ARM import | Manual (UI/GitOps) |
| Azure Databricks   | Git-synced notebooks or UI | Manual/CLI import | Manual (UI/CLI)    |