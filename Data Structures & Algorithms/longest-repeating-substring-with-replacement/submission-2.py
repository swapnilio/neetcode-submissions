class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        seen={}
        maxf=0
        for r in range(len(s)):
            c=s[r]
            seen[c]= seen.get(c,0)+1
            maxf=max(maxf, seen[c])
            while (r-l+1)-maxf>k:
                seen[s[l]]-=1
                l+=1
            res= max(res, r-l+1)
        
        return res

        