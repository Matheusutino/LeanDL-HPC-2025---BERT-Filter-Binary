# Efficient Filtering with BERT Embeddings for Researcher–Topic Affinity Prediction in HPC Pipelines

This repository contains the source code, and experimental configurationsfor the paper *"Efficient Filtering with BERT Embeddings for Researcher–Topic Affinity Prediction in HPC Pipelines"*, **submitted to LeanDL-HPC 2025 (co-located with SBAC-PAD 2025)**.

---

## 🧠 Overview

We address the challenge of reducing computational and environmental costs in **High-Performance Computing (HPC) pipelines** that rely on Large Language Models (LLMs).  
Our work introduces **lightweight filtering mechanisms** to decide which researcher–topic pairs should be forwarded to more expensive models.

The task is framed as a **binary classification problem** (high affinity vs. not-high affinity), and we evaluate three families of approaches:

- ✅ **Lexical baselines**: exact string and fuzzy matching  
- ✅ **BERT with similarity thresholds**: cosine similarity between profile and topic embeddings  
- ✅ **BERT with lightweight classifiers**: supervised models (e.g., KNN, Logistic Regression, Decision Trees) over pooled embeddings  

Our approach ensures a balance between **predictive performance** and **sustainability**, crucial for scalable and eco-conscious NLP in HPC environments.

---

## 🔍 Key Findings

- 🥇 The best trade-off was achieved by **Granite embeddings + KNN with max pooling**, reaching **F1 = 0.779**, the highest among all tested methods.  
- ⚡ Lexical baselines are carbon-efficient but underperform in predictive quality.  
- 📉 Threshold-based embedding methods gave modest gains but with disproportionate emissions.  
- 🔬 Statistical analysis revealed **no significant differences among pooling strategies**, showing that classifier and embedding choice matter more than pooling.  
- 🌱 Including emissions (kgCO₂) as a metric provides a principled way to balance accuracy and environmental impact.  

---

## 📊 Dataset

We rely on the **LeanDL-HPC 2025 dataset**, which includes:  

- 42,046 theses and dissertations defended in Brazil (2023)  
- Researcher profile texts (title + abstract)  
- 438 predefined strategic topics selected by Brazilian federal units  
- Affinity annotations (low, medium, high → reduced to binary: not-high vs. high)  
- Stratified split: **70% train / 10% validation / 20% test**  

Available: https://colab.research.google.com/drive/1bJUCxDJ4Cmd2VLQp1-Wx2r_vSkYQUezT?usp=sharing

---

## 📁 Repository Structure

- `analysis.ipynb` — Contains the analysis of experimental results  
- `dataset.ipynb` — Basic exploratory analysis of the dataset  
- `main.ipynb` — Main pipeline for running the experiments (lexical, threshold, and classifier approaches)  
- `utils.py` — Auxiliary functions used for preprocessing, metrics, and notebook support  
- `.env.example` — Example file with environment variable definitions (e.g., dataset paths or optional credentials)  
- `requirements.txt` — Python dependencies required to reproduce the experiments  
- `results/` — Directory containing generated outputs (metrics, reports, and analysis)  

---

## 🔬 Citation

Paper submitted. Citation information will be updated after peer review.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

For questions or collaboration inquiries, please contact:  
📧 matheusutino@usp.br
