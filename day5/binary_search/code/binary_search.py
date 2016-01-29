class BinarySearch(list):

    """BinarySearch class that has search method implemented in binary search."""

    def __init__(self, a, b, *args):
        """Initialise the list."""
        list.__init__(self, *args)
        self.items_length = a
        self.step = b

        end = self.items_length * self.step
        for i in range(self.step, end + 1, self.step):
            self.append(i)

    @property
    def length(self):
        """Return the length of this list."""
        return len(self)

    def search(self, element, low=0, high=None, count=0):
        """Perform an element search using recursive binary search."""
        if not high:
            high = self.length - 1

        # If the element is either the first or the last, don't bother recursing.
        if element == self[low]:
            return {'index': low, 'count': count}
        elif element == self[high]:
            return {'index': high, 'count': count}

        mid = (low + high) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            low = mid + 1
        elif element < self[mid]:
            high = mid - 1

        # Didn't find anything.
        if low >= high:
            return {'index': -1, 'count': count}

        count += 1  # Increment count right before descending into a recursive call.
        return self.search(element, low, high, count)
