# core/llm_interface.py
"""
This module handles interactions with the LLM.

For the prototype, LLM calls are simulated.
"""

from typing import Dict, Any

class LLMInterface:
    """
    Interface for interacting with Large Language Models.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the LLM interface.
        
        Args:
            config: Configuration dictionary containing LLM settings.
        """
        self.api_key = config.get("api_key", "mock_api_key")
        self.model = config.get("model", "gpt-3.5-turbo")
        self.temperature = config.get("temperature", 0.7)
        self.max_tokens = config.get("max_tokens", 1000)
    
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the LLM based on the given prompt.
        
        For the prototype, this returns a simulated response.
        
        Args:
            prompt: The prompt to send to the LLM.
            
        Returns:
            The LLM's response as a string.
        """
        # Simulate LLM response based on the prompt
        if "identify common patterns" in prompt.lower():
            return self._simulate_pattern_identification()
        elif "abstract a general principle" in prompt.lower():
            return self._simulate_principle_abstraction()
        elif "generate a story" in prompt.lower():
            return self._simulate_story_generation(prompt)
        else:
            return "This is a simulated response from the LLM."
    
    def _simulate_pattern_identification(self) -> str:
        """Simulate LLM identifying patterns between stories."""
        return """
I've identified the following common patterns across the stories:

Structural Patterns:
1. Progressive improvement: Each story describes a progression from a basic approach to an optimized solution.
2. Problem-solution structure: All stories present a problem and then detail solutions.

Concept Mappings:
- Story 1's sorting algorithms correspond to Story 2's database indexing methods and Story 3's design patterns
- The efficiency metrics in Story 1 align with performance metrics in Story 2 and quality attributes in Story 3

Relationship Mappings:
- "Enables optimization": Quicksort enables optimization of sorting processes; indexing enables optimization of database queries; patterns enable optimization of code structure
- "Trades complexity for performance": Complex sorting algorithms trade implementation complexity for runtime performance; complex indexing strategies trade storage space for query speed; complex design patterns trade learning curve for maintainability
"""
    
    def _simulate_principle_abstraction(self) -> str:
        """Simulate LLM abstracting a general principle."""
        return """
# The Optimization-Complexity Trade-off Principle

In software engineering, there exists a fundamental principle where improving a system's performance, efficiency, or quality typically involves increasing its structural or conceptual complexity. This principle manifests across different domains of software engineering:

1. **Progressive Refinement**: Solutions evolve from simple but inefficient implementations to more sophisticated and efficient ones through systematic refinement.

2. **Problem-Space Transformation**: Optimizing a solution often requires reframing the problem into a different representation that enables more efficient processing.

3. **Knowledge Encapsulation**: Advanced solutions encapsulate specialized knowledge (algorithms, patterns, techniques) that create abstraction layers, trading immediate comprehensibility for long-term maintainability.

4. **Resource Trade-offs**: Improvements in one dimension (time, space, reliability) often come at the cost of another, requiring engineers to make deliberate choices based on context-specific requirements.

This principle provides an educational framework for teaching software engineering concepts by helping students recognize common patterns across seemingly different domains, facilitating knowledge transfer and deeper understanding of the discipline's fundamental challenges and solutions.
"""
    
    def _simulate_story_generation(self, prompt: str) -> str:
        """Simulate LLM generating a story based on a domain."""
        if "sorting algorithms" in prompt.lower():
            return """
# The Tale of Sorting Algorithms

In a large tech company, a junior developer named Alex was assigned to improve the performance of a legacy application that processed customer data. The application was using bubble sort for organizing records, which worked fine when the company was small, but became painfully slow as the customer database grew.

Alex began by implementing insertion sort, which provided some improvement over bubble sort. However, the senior developer, Maya, suggested that for large datasets, they should consider more efficient algorithms like quicksort or mergesort.

After analyzing the data characteristics, Alex implemented quicksort, which dramatically reduced processing time from hours to minutes. However, they discovered that for nearly sorted data, quicksort's performance degraded. Maya then introduced Alex to adaptive sorting algorithms like Timsort, which combines mergesort and insertion sort to handle various real-world data patterns efficiently.

By selecting the right algorithm for their specific data patterns, the team achieved optimal performance. Alex learned that understanding algorithm complexity and data characteristics is crucial for effective software engineering.
"""
        elif "database indexing" in prompt.lower():
            return """
# The Database Indexing Journey

Emma, a database administrator at a growing e-commerce platform, was facing challenges with increasingly slow query performance as their product catalog expanded to millions of items.

Initially, the database used simple sequential scans for all queries. Emma first implemented basic B-tree indexes on the most frequently queried columns, which improved performance for exact matches and range queries.

As the system grew more complex with varied query patterns, Emma explored specialized indexing strategies. She implemented hash indexes for exact-match queries on certain fields, bitmap indexes for low-cardinality columns used in analytics, and full-text search indexes for product descriptions.

The team then faced a challenge with multi-condition queries that couldn't efficiently use single-column indexes. Emma implemented composite indexes and covering indexes that included all fields referenced in common queries, eliminating the need to access the actual table data.

Through careful analysis of query patterns and selective application of appropriate indexing techniques, Emma transformed the database performance while balancing the trade-offs between query speed, update overhead, and storage requirements.
"""
        elif "software design patterns" in prompt.lower() or "software pattern" in prompt.lower():
            return """
# Evolving Through Design Patterns

Carlos was leading a team developing a new financial reporting system. Initially, they built a monolithic application with tightly coupled components, which was quick to develop but became increasingly difficult to maintain as requirements evolved.

The first improvement came when Carlos introduced the Strategy pattern to encapsulate different calculation algorithms. This allowed them to switch between different calculation methods without modifying the core code, making the system more flexible.

As the application grew, they encountered issues with managing complex object creation. Carlos refactored the code to use the Factory Method pattern, which standardized the object creation process and decoupled the client code from specific implementation classes.

Later, they faced challenges with component dependencies. By implementing the Dependency Injection pattern, they improved testability and further reduced coupling between components.

Finally, to address the increasing complexity of the user interface, the team applied the Observer pattern to create a responsive UI that automatically updated when the underlying data changed.

Through this evolutionary process, Carlos's team learned that design patterns aren't just academic concepts but practical tools that solve real-world software engineering problems. Each pattern addressed specific challenges while contributing to a more maintainable, flexible, and robust architecture.
"""
        elif "software testing" in prompt.lower():
            return """
# The Testing Transformation

Priya joined as the quality assurance lead for a healthcare software company that was struggling with reliability issues. Their existing testing approach consisted mainly of manual end-to-end tests performed before each release, resulting in bugs frequently reaching production.

She began by introducing unit testing, focusing first on the critical components handling patient data calculations. This caught simple logic errors early in the development process, but integration issues between components still slipped through.

Next, Priya implemented integration tests for component interactions and API contracts. This revealed several assumptions developers were making about how their code would be used by other parts of the system.

As they grew more comfortable with automated testing, the team adopted test-driven development (TDD) for new features. Writing tests before implementation helped clarify requirements and design more testable code.

Finally, Priya established continuous integration with automated test suites that ran on every code change. This created immediate feedback loops for developers and prevented regression bugs.

The most valuable lesson came when Priya introduced mutation testing to measure test quality. The team discovered that high code coverage didn't guarantee effective tests. By systematically introducing "mutations" in the code to ensure tests would fail appropriately, they developed a deeper understanding of meaningful test design.

Through this progressive refinement of testing strategies, the team transformed not only their product quality but also their entire development approach, demonstrating how testing methodologies represent different trade-offs between development speed, detection effectiveness, and maintenance costs.
"""
        else:
            return """
# A Story About Software Engineering

In a rapidly growing startup, the development team faced increasing challenges with their codebase. What started as a simple application had evolved into a complex system with numerous interdependencies.

Initially, the team focused on rapid feature development, using a straightforward monolithic architecture. This approach worked well in the beginning stages when requirements were changing frequently.

As the user base grew, performance issues started to emerge. The team began refactoring critical components, applying optimization techniques to improve response times. They also introduced caching mechanisms for frequently accessed data.

With continued growth, the monolithic approach became a bottleneck for both development and operations. After careful analysis, the team decided to migrate toward a microservices architecture, breaking down the application into smaller, independently deployable services.

This architectural evolution taught the team valuable lessons about the trade-offs between development speed, architectural complexity, and system performance. They learned that software engineering is not just about coding solutions but about making appropriate decisions based on the current context and future growth expectations.
"""