# promptforge/task_parser.py

import re

def parse_task_description(task_text):
    """
    Parses the input task description and extracts:
    - task_type (summarization, classification, generation, etc.)
    - tone (formal, friendly, technical)
    - audience (kids, professionals, general public)
    """

    task_text = task_text.lower()

    # Default values
    task_type = "general"
    tone = "neutral"
    audience = "general"

    # Very basic keyword-based parsing
    if "summarize" in task_text:
        task_type = "summarization"
    elif "classify" in task_text or "categorize" in task_text:
        task_type = "classification"
    elif "generate" in task_text or "write" in task_text:
        task_type = "generation"

    if "simple" in task_text or "easy" in task_text:
        tone = "friendly"
    elif "professional" in task_text or "formal" in task_text:
        tone = "formal"
    elif "technical" in task_text:
        tone = "technical"

    if "child" in task_text or "kid" in task_text:
        audience = "child"
    elif "expert" in task_text or "specialist" in task_text:
        audience = "expert"
    elif "general public" in task_text or "everyone" in task_text:
        audience = "general"

    return {
        "task_type": task_type,
        "tone": tone,
        "audience": audience
    }
