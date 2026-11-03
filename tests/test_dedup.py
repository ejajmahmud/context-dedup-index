"""Unit tests for ContextDedupIndex."""
import unittest
from context_dedup_index.dedup import ContextDedupIndex

class TestContextDedupIndex(unittest.TestCase):
    def test_filter_exact_duplicates(self):
        index = ContextDedupIndex(similarity_threshold=0.8)
        docs = ["Hello world from python", "Hello world from python", "Something else entirely"]
        filtered = index.filter_unique(docs)
        self.assertEqual(len(filtered), 2)

if __name__ == "__main__":
    unittest.main()
