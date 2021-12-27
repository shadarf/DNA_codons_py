# DNA_codons_py
A simple code to split DNA into codon list using two methods: 1) with a for loop, 2) with list comprehension. 

a DNA sample can be split using an index to feed the for loop and a method on how to append the split codons into an empty list. 
in python assign your DNA sample as follows: 

```
DNA_sample = str("ATGGGGCCCGTGCAGCCGCGTGGCACGATGCTGTAA")
```

Then, create a step size to walk on the DNA, here the step size is 3: 
```
n = 3  
```
after that, assing an empty list to contain the split DNA at the final step: 
```
split_DNA = []
```

The for loop below can be explained as: 
start from index 0 to the final nucleotide of the DNA, then split by 3 nucleotides and then append each of them into the list per loop: 

```
for i in range(0,        len(DNA_sample)  ,             n):                      
               # Final Output( steps of 3 nucleotides in substrings to be appended)
               split_DNA.append(DNA_sample[i : i +n])
print("Your Codon list is: \n  \n %s" %split_DNA)   # here you print out the   
```


This method can be further simplified using a list comprehension (which implements the sampe logic, but in one line of code): 
```
# 2: using list comprehension:
print([[DNA_sample[i: i +3]] for i in range(0, len(DNA_sample),3)])
```







