from collections import Counter

def winner_of_election(arr):
    votes = Counter(arr)

    max_votes = max(votes.values())

    # Candidates with maximum votes
    winners = [name for name, count in votes.items() if count == max_votes]

    # Lexicographically smallest candidate
    winner = min(winners)

    return [winner, str(max_votes)]


# Example 1
arr = [
    "john", "johnny", "jackie", "johnny", "john",
    "jackie", "jamie", "jamie", "john", "johnny",
    "jamie", "johnny", "john"
]

print(winner_of_election(arr))
# Output: ['john', '4']


# Example 2
arr = ["andy", "blake", "clark"]

print(winner_of_election(arr))
# Output: ['andy', '1']