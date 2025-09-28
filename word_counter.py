#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word counter for Chinese-English mixed text
Counts Chinese characters, English words, and numbers separately
"""

import re
import sys
import os

def count_words_in_file(file_path):
    """
    Count words in a markdown file, handling Chinese characters, English words, and numbers
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove markdown formatting and HTML tags
        content = re.sub(r'#+\s*', '', content)  # Remove headers
        content = re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', content)  # Remove bold/italic
        content = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
        content = re.sub(r'-\s*', '', content)  # Remove bullet points
        content = re.sub(r'\|\s*[^|]+\s*\|', '', content)  # Remove table content

        # Count Chinese characters and words
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
        # Count English words
        english_words = len(re.findall(r'[a-zA-Z]+', content))
        # Count numbers as words
        numbers = len(re.findall(r'\d+', content))

        total_words = chinese_chars + english_words + numbers

        return {
            'chinese_chars': chinese_chars,
            'english_words': english_words,
            'numbers': numbers,
            'total_words': total_words
        }

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    """Main function to count words in a file"""
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    result = count_words_in_file(file_path)

    if result:
        print(f"File: {file_path}")
        print(f"Chinese characters: {result['chinese_chars']}")
        print(f"English words: {result['english_words']}")
        print(f"Numbers: {result['numbers']}")
        print(f"Total word count: {result['total_words']}")

        # Check if it meets the book requirement (3000-5000 words)
        if 3000 <= result['total_words'] <= 5000:
            print("✅ Word count meets book requirement (3000-5000 words)")
        elif result['total_words'] < 3000:
            print(f"⚠️  Chapter is too short ({result['total_words']} words, needs 3000+)")
        else:
            print(f"⚠️  Chapter is too long ({result['total_words']} words, needs <5000)")

if __name__ == "__main__":
    main()