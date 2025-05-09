from collections import Counter
import typing


class Solution:
    @staticmethod
    def countBalancedPermutations(num: str) -> int:
        MOD = 10**9 + 7
        L = len(num)
        freq = Counter(int(d) for d in num)

        s_total = sum(int(d) for d in num)
        if s_total % 2 != 0:
            return 0
        s_target = s_total // 2

        # 0-indexed: even positions 0, 2, ... odd positions 1, 3, ...
        n_e = (L + 1) // 2  # Number of even positions
        n_o = L // 2      # Number of odd positions

        # Precompute factorials and inverse factorials
        max_val_fact = L
        fact = [1] * (max_val_fact + 1)
        inv_fact = [1] * (max_val_fact + 1)
        for i in range(1, max_val_fact + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        inv_fact[max_val_fact] = pow(fact[max_val_fact], MOD - 2, MOD)
        for i in range(max_val_fact - 1, -1, -1): # inv_fact[0] will also be 1
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        def nCr_mod(n, r):
            if r < 0 or r > n:
                return 0
            num = fact[n]
            den = (inv_fact[r] * inv_fact[n - r]) % MOD
            return (num * den) % MOD

        # DP state: dp[k_odd][s_odd] = sum of product of nCr values
        # k_odd: number of digits chosen for odd positions
        # s_odd: sum of digits chosen for odd positions
        dp = [[0] * (s_target + 1) for _ in range(n_o + 1)]
        dp[0][0] = 1

        for digit_val in range(10): # Digits 0 through 9
            count_d = freq[digit_val]
            if count_d == 0: # No instances of this digit, dp table doesn't change
                continue
            
            # Iterate downwards to use dp values from before considering this digit_val
            # for the "smaller subproblem"
            for k_chosen_so_far in range(n_o, -1, -1):
                for s_sum_so_far in range(s_target, -1, -1):
                    if dp[k_chosen_so_far][s_sum_so_far] == 0: # If this state was not reachable
                        continue
                    # Now, try to add 'c' instances of digit_val
                    # The base value dp[k_chosen_so_far][s_sum_so_far] corresponds to c=0 for digit_val
                    # We need to update states that *add* c > 0 instances of digit_val
                    # using the value from *before* digit_val was considered at all.
                    # This means the DP should be structured with dp_prev and dp_curr
                    
                    # Corrected DP iteration structure:
                    # dp_prev holds results from digits < digit_val
                    # dp_curr computes results including digit_val
                    pass # This will be rewritten below with dp_prev/dp_curr

        # DP state definition: dp[k_odd][s_odd]
        # dp_prev state is from considering digits < current digit_val
        # dp_curr state includes current_digit_val
        dp_prev = [[0] * (s_target + 1) for _ in range(n_o + 1)]
        dp_prev[0][0] = 1

        for digit_val in range(10):
            count_d = freq[digit_val]
            dp_curr = [[0] * (s_target + 1) for _ in range(n_o + 1)]
            for prev_k in range(n_o + 1):
                for prev_s in range(s_target + 1):
                    if dp_prev[prev_k][prev_s] == 0:
                        continue
                    for c in range(count_d + 1): # Number of `digit_val` chosen for odd positions
                        curr_k = prev_k + c
                        curr_s = prev_s + c * digit_val
                        if curr_k <= n_o and curr_s <= s_target:
                            combinations_val = nCr_mod(count_d, c)
                            term = (dp_prev[prev_k][prev_s] * combinations_val) % MOD
                            dp_curr[curr_k][curr_s] = (dp_curr[curr_k][curr_s] + term) % MOD
            dp_prev = dp_curr
        
        sum_prod_nCr = dp_prev[n_o][s_target]

        if sum_prod_nCr == 0: # No way to pick digits for odd positions
            return 0

        # Calculate ConstantPart = (N_o! * N_e!) * product(1 / freq[d]!)
        factor1 = (fact[n_o] * fact[n_e]) % MOD
        
        denom_factor_inv = 1
        for d_val_freq in freq.values(): # Use actual frequencies from input num
             denom_factor_inv = (denom_factor_inv * inv_fact[d_val_freq]) % MOD
        
        constant_part = (factor1 * denom_factor_inv) % MOD
        
        result = (constant_part * sum_prod_nCr) % MOD
        return result
    
if __name__ == '__main__':
    print(Solution.countBalancedPermutations("112"))
    print(Solution.countBalancedPermutations("123"))
    print(Solution.countBalancedPermutations("12345"))
