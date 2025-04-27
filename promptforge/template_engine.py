# promptforge/template_engine.py

import json
import os

TEMPLATE_FILE = os.path.join(os.path.dirname(__file__), 'data', 'templates.json')


def load_templates():
    """Loads prompt templates from the templates.json file."""
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    return templates

def select_template(parsed_task):
    """
    Selects the best prompt template based on parsed task components.
    parsed_task = { "task_type": "summarization", "tone": "friendly", "audience": "child" }
    """

    templates = load_templates()

    # First try exact matches
    for template in templates:
        if (template['task_type'] == parsed_task['task_type'] and
            template['tone'] == parsed_task['tone'] and
            template['audience'] == parsed_task['audience']):
            return template['template']

    # If no exact match, fallback to task_type only
    for template in templates:
        if template['task_type'] == parsed_task['task_type']:
            return template['template']

    # If still no match, fallback to a general template
    return "You are an assistant. Help complete the following task clearly and correctly: {input}"
