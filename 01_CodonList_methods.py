# 27.12.2021    
# Creating a codon list:

# Sample DNA sequence: 
DNA_sample = str("ATGGGGCCCGTGCAGCCGCGTGGCACGATGCTGTAA")

# Method 1 : Using a simple for loop 
n = 3                 # a step size to walk along the DNA sequence. 
split_DNA = []  # this is an empty container to contain the codons later on.

## below is a for loop that splits the DNA sequence into a single codon list:


#                   0,         DNA_length           , split_by 3 nucleotides 
for i in range(0,        len(DNA_sample)  ,             n):                      
               # Final Output( steps of 3 nucleotides in substrings to be appended)
               split_DNA.append(DNA_sample[i : i +n])
# print("Your Codon list is: \n  \n %s" %split_DNA)   # here you print out the   

# 2: using list comprehension:
print([[DNA_sample[i: i +3]] for i in range(0, len(DNA_sample),3)])






