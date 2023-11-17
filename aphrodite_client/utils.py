import logging
import re
from colorama import Fore, Back, Style

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import re

def ansi_escape_length(text):
    # This regex matches ANSI escape sequences
    ansi_escape = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)
    return len(ansi_escape.sub('', text))

def draw_ascii_box(text, width=80):
    lines = text.split('\n')
    max_line_length = max(ansi_escape_length(line) for line in lines)
    box_width = max(max_line_length + 2, width)

    print("+" + "-" * (box_width - 2) + "+")
    for line in lines:
        line_padding = box_width - 2 - ansi_escape_length(line)
        print("|" + line + " " * line_padding + "|")
    print("+" + "-" * (box_width - 2) + "+")

def print_example(title, prompt, variables):
  # Regex pattern to match select structures like {{#select "key" ...}}...{{/select}}
  select_pattern_with_content = r'\{\{#select\s+(?:"(.*?)"|\'(.*?)\'|\b(\w+)\b).*?\}\}(.*?)\{\{\/select\}\}'
  select_pattern_without_content = r'\{\{select\s+(?:"(.*?)"|\'(.*?)\'|\b(\w+)\b).*?\}\}'
  # Regex pattern to find {{key}} in the prompt
  simple_pattern = r'\{\{(.*?)\}\}'
  # Regex pattern to find {{key}} or {{gen "key" ...}} in the prompt
  gen_pattern = r'\{\{\s*(?:gen\s+)?(?:"(.*?)"|\'(.*?)\')\s*.*?\}\}'

  # Replace select structures first
  def replace_match(match):
    key = match.group(1) or match.group(2) or match.group(3)
    return f"{Back.GREEN}{variables.get(key, '')}{Back.BLACK}"

  formatted_completion = re.sub(select_pattern_without_content, replace_match, prompt)
  formatted_completion = re.sub(select_pattern_with_content, replace_match, formatted_completion)
  formatted_completion = re.sub(gen_pattern, replace_match, formatted_completion)
  formatted_completion = re.sub(simple_pattern, replace_match, formatted_completion)

  # Function to add color to matched patterns
  def add_color_simple(match):
    return f"{Back.CYAN}{match.group(0)}{Back.BLACK}"

  # Apply color formatting to each match in the prompt
  formatted_prompt = re.sub(select_pattern_without_content, add_color_simple, f'{Back.BLACK}{prompt}')
  formatted_prompt = re.sub(select_pattern_with_content, add_color_simple, formatted_prompt)
  formatted_prompt = re.sub(gen_pattern, add_color_simple, formatted_prompt)
  formatted_prompt = re.sub(simple_pattern, add_color_simple, formatted_prompt)

  draw_ascii_box(title)
  print(f"{Fore.CYAN}Prompt:{Style.RESET_ALL}")
  draw_ascii_box(formatted_prompt)
  print(f"{Fore.GREEN}Completion:{Style.RESET_ALL}")
  draw_ascii_box(formatted_completion)
  print('\n')

