# CleanFreq

Version 1.1

python CleanFreq.py file1 disp nfreq soft

file1 = Gaussian or ADF output
disp = Displacement to apply. Usually 0.1 to 0.2 is enough. 
nfreq = Position of the negative frequency to correct. Usually you want to correct
        the first negative frequency so 1. Exceptionally might want to clean a negative
        frequency in a transitions state, then you want to avoid displacing the 
        transition state frequency and you select the second negative frequency. 
soft = Software used. The options are G19 and ADF        
