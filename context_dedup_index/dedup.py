"""N-gram Jaccard similarity deduplication for RAG contexts."""
from typing import List, Set


class ContextDedupIndex:
    def __init__(self, similarity_threshold: float = 0.75, shingle_size: int = 3):
        self.threshold = similarity_threshold
        self.shingle_size = shingle_size
        self._seen_shingles: List[Set[str]] = []
        self._unique_docs: List[str] = []

    def _get_shingles(self, text: str) -> Set[str]:
        words = text.lower().split()
        if len(words) < self.shingle_size:
            return {" ".join(words)}
        return {" ".join(words[i:i + self.shingle_size]) for i in range(len(words) - self.shingle_size + 1)}

    @staticmethod
    def _jaccard(s1: Set[str], s2: Set[str]) -> float:
        if not s1 or not s2:
            return 0.0
        return len(s1.intersection(s2)) / len(s1.union(s2))

    def filter_unique(self, documents: List[str]) -> List[str]:
        unique = []
        for doc in documents:
            shingles = self._get_shingles(doc)
            is_dup = False
            for seen in self._seen_shingles:
                if self._jaccard(shingles, seen) >= self.threshold:
                    is_dup = True
                    break
            if not is_dup:
                self._seen_shingles.append(shingles)
                self._unique_docs.append(doc)
                unique.append(doc)
        return unique
