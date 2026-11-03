"""Command-line interface for Context Dedup Index."""
import argparse
from .dedup import ContextDedupIndex

def main():
    parser = argparse.ArgumentParser(description="Context Dedup Index CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate context deduplication")
    args = parser.parse_args()

    docs = [
        "Python is an interpreted high-level general-purpose programming language.",
        "Python is an interpreted, high-level, general-purpose programming language for developers.",
        "PostgreSQL is an advanced open-source object-relational database system."
    ]

    deduper = ContextDedupIndex(similarity_threshold=0.60)
    unique = deduper.filter_unique(docs)
    print(f"Original doc count: {len(docs)}, Unique doc count: {len(unique)}")
    for i, d in enumerate(unique, 1):
        print(f"  #{i}: {d}")

if __name__ == "__main__":
    main()
