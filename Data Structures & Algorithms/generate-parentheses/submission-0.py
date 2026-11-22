class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sequences = []

        def generate(seq, lefts, rights):
            print(seq, lefts, rights)

            if lefts + rights == n * 2:
                sequences.append("".join(seq))
                return
            
            if lefts < n:
                seq.append("(")
                generate(seq, lefts + 1, rights)
                seq.pop()
                print("l:", seq, lefts, rights)
            if lefts - rights > 0:
                seq.append(")")
                generate(seq, lefts, rights + 1)
                seq.pop()
                print("r:", seq, lefts, rights)
            

        generate([], 0, 0)
        return sequences
        