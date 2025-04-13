# Analogical Reasoning System for Software Engineering Education (SEE-Analogical-Reasoning-LLMs)

## Description

This project implements a multi-agent system designed to facilitate analogical reasoning, particularly in the context of software engineering education. The system leverages Large Language Models (LLMs) to analyze and relate software engineering concepts through analogies, as described in "Towards an Analogical Reasoning with LLMs in Software Engineering Education" (FSE25.pdf).

## Architecture

The system follows a three-component architecture:

1.  **Control and Data Management:** This component handles system configuration, input data processing, and workflow orchestration.
2.  **Analogical Reasoning Engine:** This component implements the core analogical reasoning logic, including graph construction, relational structure identification, alignable differences identification, and conceptual relation abstraction.
3.  **Output and Presentation:** This component formats and presents the results to the user and manages user interaction.

## Components and Agents

### 1. Control and Data Management

   * **Purpose:** Manages system operation, configuration, data input, and workflow.
   * **Agents:**
        * **Orchestrator Agent:** Reads configuration, controls execution flow.
        * **Data Manager Agent:** Reads, preprocesses, and formats input data.

### 2. Analogical Reasoning Engine

   * **Purpose:** Performs the core analogical reasoning tasks.
   * **Agents (Tool Agents):**
        * **Graph Constructor Agent:** Constructs graph representations of stories.
        * **Relational Structure Identifier Agent:** Identifies common relational structures.
        * **Alignable Differences Identifier Agent:** Re-represents non-identical relations.
        * **Conceptual Relation Abstraction Agent:** Abstracts general principles.

### 3. Output and Presentation

   * **Purpose:** Formats and presents results, handles user interaction.
   * **Agents:**
        * **Output Formatter Agent:** Formats output for display.
        * **User Interface Agent:** Manages user interaction and displays results.

## Implementation Details

   * Each component is implemented as a Python package/module.
   * Agents are implemented as Python classes with methods for their tasks.
   * LLMs are used with prompt engineering to assist agents.
   * Coding guidelines from "General Instructions for All Agents.docx" are followed.

## Getting Started

   1.  Ensure you have Python installed.
   2.  Install the required dependencies (specified in `requirements.txt`, if available).
   3.  Configure the system using `system_config.yaml` or `.json`.
   4.  Run the main script to start the application.
