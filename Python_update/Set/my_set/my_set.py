class MySet:
    def __init__(self, capacity = 16, load_factor = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _get_bucket_index(self, element):
        return hash(element) % self.capacity

    def add(self, element):
        if self.size >= self.load_factor * self.capacity:
            self._resize()
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        if element in bucket:
            return False
        bucket.append(element)
        self.size += 1
        return True

    def _resize(self):
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.capacity)]
        for bucket in self.buckets:
            for element in bucket:
                index = self._get_bucket_index(element)
                new_buckets[index].append(element)
        self.buckets = new_buckets
        # No need to update self.size as it remains the same

    def remove(self, element):
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        if element not in bucket:
            return False
        bucket.remove(element)
        self.size -= 1
        return True

    def __contains__(self, element):
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        return element in bucket

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def __iter__(self):
        for bucket in self.buckets:
            for element in bucket:
                yield element

    