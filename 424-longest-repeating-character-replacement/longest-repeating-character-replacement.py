class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_freq = 0
        result = 0
        count = {}

        for right in range(len(s)):

            # Count the current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency character in the window
            max_freq = max(max_freq, count[s[right]])

            # Characters that need to be replaced
            window_length = right - left + 1
            replacements = window_length - max_freq

            # If replacements are more than k, shrink window
            if replacements > k:
                count[s[left]] -= 1
                left += 1

            # Update maximum length
            result = max(result, right - left + 1)

        return result