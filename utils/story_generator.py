# utils/story_generator.py
"""
This module generates stories based on domains using the LLM.
"""

from typing import Any
from core.llm_interface import LLMInterface

def generate_story(domain: str, llm: LLMInterface) -> str:
    """
    Generate a story based on the given domain using the LLM.
    
    Args:
        domain: The domain or topic for the story.
        llm: An instance of LLMInterface for interacting with the LLM.
        
    Returns:
        A string containing the generated story.
    """
    prompt = f"""
Generate an educational story about {domain} in the context of software engineering.
The story should:
1. Include some named characters facing a software engineering challenge
2. Show a progression from a basic approach to a more sophisticated solution
3. Highlight trade-offs and decision-making processes
4. Convey a key lesson or principle about {domain}
5. Be concise (about 250-350 words)
"""
    
    # Get response from LLM
    story = llm.generate_response(prompt)
    
    return story