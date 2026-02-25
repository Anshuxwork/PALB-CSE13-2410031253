"""Problem 9: Best Time to Buy and Sell Stock

Given an array where the ith element is the price on day i, find the maximum
profit. You may complete at most one transaction.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    """Finds the maximum profit from buying and selling stock once.
    
    Args:
        prices: List of integers representing stock prices
    
    Returns:
        Maximum profit possible. 0 if no profit can be made
    """
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    
    return max_profit


if __name__ == "__main__":
    # Test Case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = maxProfit(prices1)
    print(f"Test 1 - Prices: {prices1}")
    print(f"Result: Maximum profit = {result1}")
    print()
    
    # Test Case 2
    prices2 = [7, 6, 4, 3, 1]
    result2 = maxProfit(prices2)
    print(f"Test 2 - Prices: {prices2}")
    print(f"Result: Maximum profit = {result2}")
    print()
    
    # Test Case 3
    prices3 = [2, 4, 1, 7, 5, 11]
    result3 = maxProfit(prices3)
    print(f"Test 3 - Prices: {prices3}")
    print(f"Result: Maximum profit = {result3}")
