#!/usr/bin/python3
"""Module for prime game"""


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def simulate_game(n):
    """
    Simulate a game for the given n and return the winner ('Maria' or 'Ben').
    """
    primes = sieve_of_eratosthenes(n)
    nums = [True] * (n + 1)  # True means the number is still in the game

    # Remove multiples of primes
    for prime in primes:
        for multiple in range(prime, n + 1, prime):
            nums[multiple] = False  # Mark as removed

    # Game simulation, alternating turns between Maria and Ben
    turn = 0  # 0 for Maria, 1 for Ben
    while any(nums[prime] for prime in primes):
        for prime in primes:
            if nums[prime]:  # If this prime is still available
                # Remove the prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    nums[multiple] = False
                break  # Exit loop once a move is made

        turn = 1 - turn  # Switch turns

    # If turn == 0, Maria has won (because Ben couldn't play)
    return 'Ben' if turn == 0 else 'Maria'


def isWinner(x, nums):
    """
    Decide the winner
    """
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 1:  # Handle case where there are no primes
            ben_wins += 1
        else:
            winner = simulate_game(n)
            if winner == 'Maria':
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
