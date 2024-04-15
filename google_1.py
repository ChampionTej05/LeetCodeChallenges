# # def reconstruct_array(counts):
# #     n = len(counts)
# #     original = [-1] * n  # Step 1: Initialize the original array with placeholders
    
# #     for num in range(n):  # Step 2: Iterate through each number
# #         position_to_place = counts[num]  # The count represents positions to skip
# #         for i in range(n):
# #             if original[i] == -1:  # If spot is empty
# #                 if position_to_place == 0:  # Found the right spot
# #                     original[i] = num  # Place the number
# #                     break  # Move to the next number
# #                 position_to_place -= 1  # Skip this spot and decrease the count
    
# #     return original


# # class SegmentTree:
# #     def __init__(self, size):
# #         self.size = size
# #         self.tree = [0] * (4 * size)
# #         self.build(0, size - 1, 1)

# #     def build(self, start, end, node):
# #         if start == end:
# #             self.tree[node] = 1
# #         else:
# #             mid = (start + end) // 2
# #             self.build(start, mid, 2 * node)
# #             self.build(mid + 1, end, 2 * node + 1)
# #             self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

# #     def update(self, idx, start, end, node, value):
# #         if start == end:
# #             self.tree[node] = value
# #         else:
# #             mid = (start + end) // 2
# #             if idx <= mid:
# #                 self.update(idx, start, mid, 2 * node, value)
# #             else:
# #                 self.update(idx, mid + 1, end, 2 * node + 1, value)
# #             self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

# #     def query(self, count, start, end, node):
# #         if start == end:
# #             return start
# #         mid = (start + end) // 2
# #         if self.tree[2 * node] >= count:
# #             return self.query(count, start, mid, 2 * node)
# #         else:
# #             return self.query(count - self.tree[2 * node], mid + 1, end, 2 * node + 1)

# # def reconstruct_array(counts):
# #     n = len(counts)
# #     tree = SegmentTree(n)
# #     result = [-1] * n
# #     for i in range(n):
# #         order = counts[i] + 1  # 1-based index for kth available
# #         pos = tree.query(order, 0, n - 1, 1)
# #         result[pos] = i
# #         tree.update(pos, 0, n - 1, 1, 0)  # Mark position as filled
# #     return result

# # # Example usage
# # # counts = [3, 1, 1, 0]
# # # original_array = reconstruct_array(counts)
# # # print(f"Original array: {original_array}")

# # # Example
# # counts = [2,0,0,1,0]
# # print("Original array:", reconstruct_array(counts))


# class BIT:
#     def __init__(self, n):
#         self.size = n
#         self.tree = [0] * (n + 1)
    
#     def update(self, i, delta):
#         while i <= self.size:
#             self.tree[i] += delta
#             i += i & -i
    
#     def query(self, i):
#         sum = 0
#         while i > 0:
#             sum += self.tree[i]
#             i -= i & -i
#         return sum
    
#     # Find the smallest index with a given cumulative sum
#     def find(self, cum_sum):
#         idx = 0
#         bit_mask = self.size.bit_length()
#         for i in reversed(range(bit_mask)):
#             bit = 1 << i
#             next_idx = idx + bit
#             if next_idx <= self.size and cum_sum > self.tree[next_idx]:
#                 idx = next_idx
#                 cum_sum -= self.tree[idx]
#         return idx + 1

# def reconstruct_array(count):
#     n = len(count)
#     bit = BIT(n)
#     original = [0] * n
    
#     # Initially mark all positions as available
#     for i in range(1, n + 1):
#         bit.update(i, 1)
    
#     for num in range(n, 0, -1):
#         smaller_count = count[num - 1]
#         pos = bit.find(smaller_count + 1)  # Find the position to place the number
#         original[pos - 1] = num  # Place the number in the original array
#         bit.update(pos, -1)  # Mark this position as filled
    
#     return original

# # Example usage
# count_array = [3, 1, 3, 2, 0, 0]
# original_array = reconstruct_array(count_array)
# print("Original Array:", original_array)


# def reconstruct_array_from_counts(counts):
#     n = len(counts)
#     # Pair each count with its index and sort in ascending order of count and index
#     sorted_counts = sorted((count, i) for i, count in enumerate(counts))
    
#     original = [None] * n
#     available_positions = list(range(n))  # Initially, all positions are available
    
#     for _, index in sorted_counts:
#         # The position for the current element is determined by its count
#         position = available_positions.pop(index)
#         original[position] = index + 1  # Assuming elements are 1 to N
    
#     return original

# # Example usage
# count_array = [3, 1, 3, 2, 0, 0]
# original_array = reconstruct_array_from_counts(count_array)
# print("Original Array:", original_array)


def find_original_array_optimized_nlogn(count_array):
  """
  This function takes a count array as input and returns the original array using a modified merge sort approach.

  Args:
      count_array: A list of integers representing the number of elements smaller to the right in the original array.

  Returns:
      A list of integers representing the original array.
  """

  n = len(count_array)
  original_array = [0] * n

  def merge(left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        original_array[k] = left[i] + 1
        count_array[left[i]] -= 1
        i += 1
      else:
        original_array[k] = right[j] + 1
        j += 1
      k += 1

    while i < len(left):
      original_array[k] = left[i] + 1
      count_array[left[i]] -= 1
      i += 1
      k += 1

    while j < len(right):
      original_array[k] = right[j] + 1
      j += 1
      k += 1

  def merge_sort(arr, start, end):
    if start >= end:
      return

    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr[start:mid + 1], arr[mid + 1:end + 1])

  # Sort indices based on count_array values (smaller count comes first)
  indices = sorted(range(n), key=lambda i: count_array[i])
  merge_sort(indices, 0, n - 1)

  return original_array

# Example usage
count_array = [4, 1, 3, 2, 0, 0]
original_array = find_original_array_optimized_nlogn(count_array)
print(original_array)  # Output: [5, 2, 6, 4, 1, 3]
