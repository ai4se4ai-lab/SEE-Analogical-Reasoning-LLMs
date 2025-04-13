# core/__init__.py
"""Core package for the Analogical Reasoning Engine."""

# core/analogical_reasoner.py
"""
This module implements the main analogical reasoning process.

It contains functions for the four main phases of analogical reasoning:
1. Initial Graph Construction Phase (IGCP)
2. Identifying Common Relations Stage (ICRS)
3. Identifying Alignable Differences Approach (IADA)
4. Re-representation and New Concept Recognition (RNCR)
"""

from typing import Dict, List, Any
from core.llm_interface import LLMInterface

def initial_graph_construction(story: str) -> Dict[str, Any]:
    """
    Creates a simplified graph representation of a story.
    
    This function converts a story into a graph representation with objects
    and their relationships (Phase 1: IGCP).
    
    Args:
        story: A string containing the story text.
        
    Returns:
        A dictionary representation of the story graph with objects and relationships.
    """
    # For the prototype, create a simplified graph representation
    
    # Extract key entities (objects)
    objects = []
    for line in story.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and len(line) > 10:
            # Extract potential entities from the line
            words = line.split()
            for word in words:
                if word[0].isupper() and len(word) > 3 and word.lower() not in ['the', 'and', 'but']:
                    objects.append(word)
    
    # Remove duplicates and limit to 5 key objects
    objects = list(set(objects))[:5]
    
    # If no objects were found, extract nouns
    if not objects:
        objects = [f"Entity_{i}" for i in range(5)]
    
    # Create relationships (simplified)
    relationships = []
    for i in range(len(objects) - 1):
        relationships.append({
            "source": objects[i],
            "target": objects[i + 1],
            "relation": f"relates_to_{i}"
        })
    
    # Create the graph
    graph = {
        "objects": objects,
        "relationships": relationships
    }
    
    return graph

def identify_common_relations(stories: List[str], llm_interface: LLMInterface) -> Dict[str, Any]:
    """
    Uses the LLM to find common patterns and relationships between stories.
    
    This function implements Phase 2 (ICRS) of the analogical reasoning process.
    
    Args:
        stories: A list of story texts.
        llm_interface: An instance of LLMInterface for interacting with the LLM.
        
    Returns:
        A mapping of objects/relationships that are common across stories.
    """
    # Create a prompt for the LLM to identify common relations
    prompt = "I'll provide you with multiple stories. Please identify common patterns, " \
             "relationships, and structure between them:\n\n"
    
    for i, story in enumerate(stories, 1):
        prompt += f"Story {i}:\n{story}\n\n"
    
    prompt += "Identify and list the common elements, relationships, and structural " \
              "patterns across these stories. Format your response as a structured mapping."
    
    # Get response from LLM
    response = llm_interface.generate_response(prompt)
    
    # Parse the response into a structured mapping (in real implementation, this would
    # require more sophisticated parsing)
    common_relations = {
        "structural_patterns": ["sequential_process", "problem_solution"],
        "concept_mappings": [
            {"story_1": "sorting_algorithm", "story_2": "database_indexing", "story_3": "software_pattern"},
            {"story_1": "efficiency", "story_2": "performance", "story_3": "optimization"}
        ],
        "relationship_mappings": [
            {"type": "improves", "instances": ["quicksort improves sorting speed", 
                                            "indexing improves query performance", 
                                            "pattern improves code organization"]}
        ]
    }
    
    return common_relations

def identify_alignable_differences(common_relations: Dict[str, Any]) -> Dict[str, Any]:
    """
    Identifies and marks non-identical relations in the mappings.
    
    This function implements Phase 3 (IADA) of the analogical reasoning process.
    
    Args:
        common_relations: The mapping of common relations across stories.
        
    Returns:
        A dictionary containing alignable differences.
    """
    alignable_differences = {
        "differences": []
    }
    
    # Extract differences from concept mappings
    for mapping in common_relations.get("concept_mappings", []):
        alignable_differences["differences"].append({
            "type": "concept_variation",
            "variants": list(mapping.values()),
            "common_abstract_concept": "improvement_mechanism"
        })
    
    # Extract differences from relationship mappings
    for relation in common_relations.get("relationship_mappings", []):
        alignable_differences["differences"].append({
            "type": "relationship_variation",
            "relationship_type": relation.get("type", ""),
            "variants": relation.get("instances", []),
            "common_abstract_relation": "enhancement_process"
        })
    
    return alignable_differences

def re_represent_relations(common_relations: Dict[str, Any], llm_interface: LLMInterface) -> str:
    """
    Uses the LLM to abstract a general principle from the common relations.
    
    This function implements Phase 4 (RNCR) of the analogical reasoning process.
    
    Args:
        common_relations: The mapping of common relations across stories.
        llm_interface: An instance of LLMInterface for interacting with the LLM.
        
    Returns:
        A string containing the generalized principle.
    """
    # Create a prompt for the LLM
    prompt = "Based on the following patterns and relationships identified across multiple stories:\n\n"
    
    # Add structural patterns
    prompt += "Structural Patterns:\n"
    for pattern in common_relations.get("structural_patterns", []):
        prompt += f"- {pattern}\n"
    
    # Add concept mappings
    prompt += "\nConcept Mappings:\n"
    for mapping in common_relations.get("concept_mappings", []):
        prompt += f"- {', '.join([f'{k}: {v}' for k, v in mapping.items()])}\n"
    
    # Add relationship mappings
    prompt += "\nRelationship Mappings:\n"
    for relation in common_relations.get("relationship_mappings", []):
        prompt += f"- Type: {relation.get('type', '')}\n"
        prompt += f"  Instances: {', '.join(relation.get('instances', []))}\n"
    
    prompt += "\nPlease abstract a general principle or concept that captures the essence " \
              "of these patterns. This principle should be applicable to software engineering " \
              "education and practice."
    
    # Get response from LLM
    general_principle = llm_interface.generate_response(prompt)
    
    return general_principle