"""Assemble The AI Growth Stack book."""
from book_part1 import FRONT, PART1, PART2A
from book_part2 import PART2B
from book_part3 import PART3, PART4, APPENDIX

BOOK = {
    "file": "the-ai-growth-stack-book.pdf",
    "kind": "Book",
    "book": True,
    "title": "The AI Growth Stack",
    "subtitle": "How DTC, eCommerce and SaaS teams use AI to grow faster on the same budget",
    "sections": FRONT + PART1 + PART2A + PART2B + PART3 + PART4 + APPENDIX,
}
