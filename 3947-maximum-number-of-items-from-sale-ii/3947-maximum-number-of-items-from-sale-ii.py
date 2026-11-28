
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Find maximum factor and cheapest price
        max_factor = max(factor for factor, price in items)
        cheapest = min(price for factor, price in items)

        # Step 2: Count frequency of each factor
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 3: Count items whose factors are multiples
        for i in range(1, max_factor + 1):
            for j in range(2 * i, max_factor + 1, i):
                freq[i] += freq[j]

        # Step 4: Sort items by price
        items.sort(key=lambda x: x[1])

        ans = 0

        # Step 5: Buy double-value items first
        for factor, price in items:

            # No benefit compared with buying cheapest items
            if price > 2 * cheapest:
                break

            # Exclude the current item itself
            free_count = freq[factor] - 1

            if free_count == 0:
                continue

            # Number of double-value purchases possible
            count = min(free_count, budget // price)

            # Each purchase gives 2 items
            ans += count * 2

            # Reduce remaining budget
            budget -= count * price

        # Step 6: Buy cheapest items with remaining budget
        ans += budget // cheapest

        return ans
