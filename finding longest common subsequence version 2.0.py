def lcs_recursive(seq1, seq2,idx=0,idx2=0):
    if idx==len(seq1) or idx2==len(seq2):
        return 0
    elif seq1[idx]==seq2[idx2]:
        return 1+lcs_recursive(seq1,seq2,idx+1,idx2+1)
    else:
        option1=lcs_recursive(seq1,seq2,idx+1,idx2)
        option2=lcs_recursive(seq1,seq2,idx,idx2+1)
        return max(option1,option2)
seq1="shamique"
seq2="sam"
print(lcs_recursive(seq1,seq2))
