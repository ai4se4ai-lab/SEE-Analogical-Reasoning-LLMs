# Analogical Reasoning Engine for Software Engineering Education

This project implements analogical reasoning with Large Language Models (LLMs) for software engineering education, based on the principles described in the paper "Towards an Analogical Reasoning with LLMs in Software Engineering Education."

## Overview

The Analogical Reasoning Engine analyzes software engineering stories from different domains, identifies common patterns and relationships between them, and derives general principles that can be applied across domains.

The reasoning process follows four main phases:
1. Initial Graph Construction Phase (IGCP)
2. Identifying Common Relations Stage (ICRS)
3. Identifying Alignable Differences Approach (IADA)
4. Re-representation and New Concept Recognition (RNCR)

## Project Structure

```
analogical_reasoning_engine/
│
├── config/
│   └── config.json       # Configuration settings
│
├── data/
│   └── stories/
│       ├── story_1.txt   # Example story about sorting algorithms
│       ├── story_2.txt   # Example story about database indexing
│       └── story_3.txt   # Example story about design patterns
│
├── core/
│   ├── __init__.py
│   ├── analogical_reasoner.py   # Core reasoning logic
│   ├── graph_representation.py  # Graph functions
│   ├── llm_interface.py         # LLM interactions
│
├── utils/
│   ├── __init__.py
│   ├── config_loader.py         # Load configuration
│   ├── story_generator.py       # Generate stories
│
├── main.py               # Entry point
│
└── README.md             # This file
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/analogical_reasoning_engine.git
   cd analogical_reasoning_engine
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure the application:
   - Edit `config/config.json` to set your API key (if integrating with a real LLM)
   - Adjust other parameters as needed

## Usage

Run the main application:
```
python main.py
```

The application will:
1. Load initial stories from the `data/stories/` directory
2. Generate a new story about a domain specified in the config
3. Apply analogical reasoning to identify common patterns
4. Derive a general principle that captures the essence of these patterns

## Extending the Project

- **Adding New Stories**: Place new story files in the `data/stories/` directory
- **Customizing Domains**: Edit the `story_domains` list in `config/config.json`
- **Integrating Real LLM**: Modify the `generate_response` method in `core/llm_interface.py` to use an actual LLM API

## Note

This prototype simulates LLM interactions. To use an actual LLM API, you would need to modify the `LLMInterface` class to make real API calls.

## License

[MIT License](LICENSE)