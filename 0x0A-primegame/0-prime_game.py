#!/usr/bin/python3

def isWinner(x, nums):
    """
        aria and Ben are playing a game. Given a set of 
        consecutive integers starting from 
    """
    def is_prime(num):
        """
         up to and including n, they take turns 
         choosing a prime
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """
        number from the set and removing that number 
        and its multiples from the set. The player 
        that cannot make a move loses the game.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        """
        They play x rounds of the game, where n may
          be different for each round. Assuming Maria 
        always goes first and both players play optimally,
        """
        primes = get_primes(n)
        total_numbers = set(range(1, n + 1))
        player = "Maria"

        while total_numbers:
            valid_moves = [p for p in primes if p in total_numbers]
            if not valid_moves:
                break

            move = max(valid_moves)
            total_numbers -= set(range(move, n + 1, move))
            player = "Ben" if player == "Maria" else "Maria"

        return player

    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)  # Output: Maria
