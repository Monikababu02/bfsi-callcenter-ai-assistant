# BFSI Call Center AI Assistant

## Objective
To build a compliant AI assistant for BFSI queries using a dataset-first approach.

## Architecture

User Query → Dataset Similarity → If Match Return Response  
If No Match → RAG Knowledge Retrieval → Final Response

## System Components

1. Dataset Layer (Primary)
2. Lightweight Model Layer
3. RAG Layer
4. Guardrails for compliance

## Safety Measures

- No guessing financial numbers
- No exposing customer data
- No generating fake policies
- Reject out-of-domain queries

