# %% 
import pandas as pd
df = pd.read_csv('URD_Dropseq_Meta.txt', sep='\t', squeeze=True)
df.columns
# %%
stages = df.drop_duplicates('Stage').reset_index()
print(stages.iloc[:,:4])
# from this we see that the 12.0-6Somite stage starts at column 34328
# next step can be done with bash
# this command extracts a single column and prints the first row
## zcat URD_Dropseq_Expression_Log2TPM.txt.gz | cut -f 34329 | head -n 1
# this command extracts all the 12-6somite columns (and the first column)
# zcat URD_Dropseq_Expression_Log2TPM.txt.gz | cut -f 1, 34329- > 6somite.txt
