# Pinecone Quickstart

This repository contains a script to create an index in Pinecone.

## Usage

0. Install the dependencies using uv

```bash
uv pip install
```

1. Copy the .env.sample file to .env and add your Pinecone API key

```bash
cp .env.sample .env
```

2. Run the script

```bash
uv run main.py
```

3. Check the index in [Pinecone](https://app.pinecone.io/)

4. Copy the host information from the index settings page and use in your AWS Bedrock Knowledge Base configuration.