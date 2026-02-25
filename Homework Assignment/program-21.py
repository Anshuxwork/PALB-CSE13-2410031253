"""Problem 21: LRU Cache

Implement an LRU (Least Recently Used) Cache with get and put operations.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

from collections import OrderedDict


class LRUCache:
    """LRU Cache implementation using OrderedDict."""
    
    def __init__(self, capacity):
        """Initialize cache with given capacity.
        
        Args:
            capacity: Maximum number of items to store
        """
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """Get value for key, mark as recently used.
        
        Args:
            key: The key to retrieve
        
        Returns:
            Value if key exists, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """Put key-value pair in cache.
        
        Args:
            key: Key to insert
            value: Value to store
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Remove least recently used if exceeds capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    # Test Case 1
    print("Test 1 - LRU Cache with capacity 2")
    lru1 = LRUCache(2)
    lru1.put(1, 1)
    lru1.put(2, 2)
    print(f"get(1): {lru1.get(1)}")  # Returns 1
    lru1.put(3, 3)  # Evict key 2
    print(f"get(2): {lru1.get(2)}")  # Returns -1
    print()
    
    # Test Case 2
    print("Test 2 - LRU Cache with capacity 1")
    lru2 = LRUCache(1)
    lru2.put(2, 1)
    print(f"get(2): {lru2.get(2)}")  # Returns 1
    lru2.put(3, 2)
    print(f"get(2): {lru2.get(2)}")  # Returns -1
    print()
    
    # Test Case 3
    print("Test 3 - LRU Cache operations")
    lru3 = LRUCache(3)
    lru3.put(1, 1)
    lru3.put(2, 2)
    lru3.put(3, 3)
    print(f"get(2): {lru3.get(2)}")  # Returns 2
    lru3.put(4, 4)  # Evict key 1
    print(f"get(1): {lru3.get(1)}")  # Returns -1
