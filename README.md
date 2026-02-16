# BFSI Call Center AI Assistant

This project implements a compliant AI assistant for handling Banking, Financial Services, and Insurance (BFSI) queries.

## Features
- Dataset-first response strategy
- Lightweight local model
- Retrieval-Augmented Generation (RAG)
- Strict guardrails

## Architecture Flow

User Query
   ↓
Dataset Similarity Check
   ↓
If Match → Return Stored Response
   ↓
Else → RAG Knowledge Retrieval
   ↓
Final Response

## Compliance Strategy

- Dataset-first response gating
- Embedding similarity threshold (0.80)
- Guardrails for sensitive queries
- RAG grounding for policy explanations
- No hallucinated financial data
