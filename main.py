#!/usr/bin/env python3
"""
Analogical Reasoning Engine for Software Engineering Education

This script serves as the main entry point for the application,
orchestrating the workflow of the analogical reasoning process.
"""

import os
from typing import List
from core.analogical_reasoner import (
    initial_graph_construction, 
    identify_common_relations,
    identify_alignable_differences,
    re_represent_relations
)
from core.llm_interface import LLMInterface
from utils.config_loader import load_config
from utils.story_generator import generate_story

def load_stories_from_directory(directory_path: str) -> List[str]:
    """
    Load all story files from the specified directory.
    
    Args:
        directory_path: Path to the directory containing story files.
        
    Returns:
        A list of story contents as strings.
    """
    stories = []
    
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Warning: Story directory {directory_path} not found. Creating it...")
        os.makedirs(directory_path, exist_ok=True)
        return stories
    
    # Load all text files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            try:
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    story_content = file.read()
                    if story_content.strip():  # Ensure story isn't empty
                        stories.append(story_content)
                        print(f"Loaded story from {filename}")
            except Exception as e:
                print(f"Error loading story from {filename}: {e}")
    
    return stories

def main():
    """Main execution function."""
    # Load configuration
    config = load_config()
    
    # Initialize LLM interface
    llm = LLMInterface(config)
    
    print("Analogical Reasoning Engine for Software Engineering Education")
    print("=" * 70)
    
    # Load stories from directory
    print("\nLoading stories from data/stories directory...")
    stories_directory = os.path.join('data', 'stories')
    stories = load_stories_from_directory(stories_directory)
    
    # Generate stories if not enough are found
    if len(stories) < 2:
        print(f"Not enough stories found in {stories_directory}. Generating default stories...")
        domains = config.get("story_domains", ["sorting algorithms", "database indexing"])
        
        # Ensure data/stories directory exists
        os.makedirs(stories_directory, exist_ok=True)
        
        for i, domain in enumerate(domains[:2]):
            story = generate_story(domain, llm)
            stories.append(story)
            print(f"Generated story about {domain}")
            
            # Save generated story to file
            story_filename = f"story_{i+1}.txt"
            story_path = os.path.join(stories_directory, story_filename)
            try:
                with open(story_path, 'w', encoding='utf-8') as file:
                    file.write(story)
                print(f"Saved story to {story_filename}")
            except Exception as e:
                print(f"Error saving story to {story_filename}: {e}")
    
    # Generate a new story from one of the domains in config
    domains = config.get("story_domains", ["software design patterns"])
    target_domain = domains[-1] if domains else "software testing"
    print(f"\nGenerating a new story about {target_domain}...")
    new_story = generate_story(target_domain, llm)
    stories.append(new_story)
    
    # Apply analogical reasoning process
    print("\nPerforming analogical reasoning...")
    
    # 1. Create graph representations for each story
    print("Step 1: Initial Graph Construction...")
    graphs = [initial_graph_construction(story) for story in stories]
    
    # 2. Identify common relations
    print("Step 2: Identifying Common Relations...")
    common_relations = identify_common_relations(stories, llm)
    
    # 3. Identify alignable differences
    print("Step 3: Identifying Alignable Differences...")
    alignable_differences = identify_alignable_differences(common_relations)
    
    # 4. Re-represent to derive the general principle
    print("Step 4: Re-representation to Derive General Principle...")
    general_principle = re_represent_relations(common_relations, llm)
    
    # Display results
    print("\nResults:")
    print("-" * 50)
    print("General Principle Derived:")
    print(general_principle)
    print("-" * 50)
    
    print("\nAnalogical reasoning process complete.")

if __name__ == "__main__":
    main()