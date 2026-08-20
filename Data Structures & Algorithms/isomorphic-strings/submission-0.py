class Solution:
    def helper(self, s: str, t: str) -> bool:
        # Dictionary to store the mapping from characters in s to characters in t.
        mp = {}

        # Go through each character in both strings.
        for i in range(len(s)):

            # If the current character in s has already been mapped,
            # make sure it maps to the same character in t.
            if (s[i] in mp) and (mp[s[i]] != t[i]):
                return False

            # Store/update the mapping between the two characters.
            mp[s[i]] = t[i]

        # If no conflicting mappings were found, the strings are compatible.
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check that every character in s maps consistently to t.
        # Then check the reverse mapping to make sure two characters
        # in s cannot map to the same character in t.
        return self.helper(s, t) and self.helper(t, s)