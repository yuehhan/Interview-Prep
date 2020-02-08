# Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        items = list(counts.items())
        items.sort(key=lambda item:(-item[1],item[0]))
        
        return [item[0] for item in items[0:k]]
        