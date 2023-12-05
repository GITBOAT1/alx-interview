#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of a prime number removal game.

    Parameters:
    - x (int): The number of rounds to be played.
    - nums (list): An array of integers representing the upper limits
    for each round (n).

    Returns:
    - str or None: The name of the player with the most wins
    (Maria or Ben).
    If the winner cannot be determined, returns None.

    Note:
    - The game involves selecting prime numbers and
    removing them and their multiples from the set.
    - Players take turns, and the player unable to make
    a move loses the round.
    - The function assumes optimal play from both players.

    Example:
    >>> isWinner(3, [4, 5, 1])
    'Ben'

    """
    def is_prime(num):
        """
        Check if a given number is prime.

        Parameters:
        - num (int): The number to be checked.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(nums):
        """
        Get the next prime number from a list of integers.

        Parameters:
        - nums (list): List of integers.

        Returns:
        - int or None: The next prime number in the list,
        or None if no primes are found.
        """
        for num in nums:
            if is_prime(num):
                return num
        return None

    def remove_multiples(nums, prime):
        """
        Remove multiples of a given prime number from a list.

        Parameters:
        - nums (list): List of integers.
        - prime (int): The prime number whose multiples should be removed.

        Returns:
        - list: The updated list with multiples of the prime removed.
        """
        return [num for num in nums if num % prime != 0]

    def play_round(nums, is_maria_turn):
        """
        Simulate a single round of the prime number removal game.

        Parameters:
        - nums (list): List of consecutive integers.
        - is_maria_turn (bool): Indicates whether it's Maria's turn.

        Returns:
        - bool: True if Maria wins the round, False if Ben wins.
        """
        while True:
            prime = get_next_prime(nums)
            if prime is None:
                break
            nums = remove_multiples(nums, prime)
            is_maria_turn = not is_maria_turn

        return is_maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        is_maria_turn = True
        winner = play_round(list(range(1, n + 1)), is_maria_turn)

        if winner:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
