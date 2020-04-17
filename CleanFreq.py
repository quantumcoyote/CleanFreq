import sys

element={'1':'H','2':'He','3':'Li','4':'Be','5':'B','6':'C','7':'N','8':'O','9':'F',
'10':'Ne','11':'Na','12':'Mg','13':'Al','14':'Si','15':'P','16':'S','17':'Cl','18':'Ar','19':'K',
'20':'Ca','21':'Sc','22':'Ti','23':'V','24':'Cr','25':'Mn','26':'Fe','27':'Co','28':'Ni','29':'Cu',
'30':'Zn','31':'Ga','32':'Ge','33':'As','34':'Se','35':'Br','36':'Kr','37':'Rb','38':'Sr','39':'Y',
'40':'Zr','41':'Nb','42':'Mo','43':'Tc','44':'Ru','45':'Rh','46':'Pd','47':'Ag','48':'Cd','49':'In',
'50':'Sn','51':'Sb','52':'Te','53':'I','54':'Xe','55':'Cs','56':'Ba','57':'La','58':'Ce','59':'Pr',
'60':'Nd','61':'Pm','62':'Sm','63':'Eu','64':'Gd','65':'Tb','66':'Dy','67':'Ho','68':'Er','69':'Tm',
'70':'Yb','71':'Lu','72':'Hf','73':'Ta','74':'W','75':'Re','76':'Os','77':'Ir','78':'Pt','79':'Au',
'80':'Hg','81':'Tl','82':'Pb','83':'Bi','84':'Po','85':'At','86':'Rn','87':'Fr','88':'Ra','89':'Ac',
'90':'Th','91':'Pa','92':'U','93':'Np','94':'Pu','95':'Am','96':'Cm','97':'Bk','98':'Cf','99':'Es',
'100':'Fm','101':'Md','102':'No','103':'Lr','104':'Rf','105':'Db','106':'Sg','107':'Bh','108':'Hs','109':'Mt',
'110':'Ds','111':'Rg','112':'Cn','113':'Nh','114':'Fl','115':'Mc','116':'Lv','117':'Ts','118':'Og'}

def Gaussian():
    global negative
    global col_neg
    global position_neg
    global select

    #
    # Initialize Function Variables
    #

    nline=0

    with open(sys.argv[1], 'r') as searchfile:
        for line in searchfile:
            #
            # Find the line number before the final geometry is printed
            #
            if 'Center     Atomic      Atomic             Coordinates (Angstroms)' in line:
                geo = int(nline)
            #
            # Find the number of atoms
            #
            if 'NAtoms=' in line:
                tmp = line.split()
                natoms = tmp[1]
            #
            # Find the frequencies
            #
            if 'Frequencies --' in line:
                tmp = line.split()
                frequencies.append(tmp[2])
                if(float(frequencies[len(frequencies)-1])) < 0.0:
                    if negative <= select-1:
                        negative=negative+1
                        position_neg=nline
                        col_neg='1'
                frequencies.append(tmp[3])
                if(float(frequencies[len(frequencies)-1])) < 0.0:
                    if negative <= select-1:
                        negative = negative + 1
                        position_neg=nline
                        col_neg='2'
                frequencies.append(tmp[4])
                if(float(frequencies[len(frequencies)-1])) < 0.0:
                    if negative <= select-1:
                        negative = negative + 1
                        position_neg=nline
                        col_neg='3'

            nline = nline + 1

    nline = 1
    with open(sys.argv[1], 'r') as searchfile:
        for line in searchfile:
            if int(geo) + 3 < int(nline) < int(geo) + int(natoms) + 4:
                tmp = line.split()
                name.append(element[tmp[1]])
                x.append(tmp[3])
                y.append(tmp[4])
                z.append(tmp[5])
            if int(position_neg)+5 < int(nline) < int(position_neg) + int(natoms) + 6:
                if col_neg == '1':
                    dx.append(line.split()[2])
                    dy.append(line.split()[3])
                    dz.append(line.split()[4])
                if col_neg == '2':
                    dx.append(line.split()[5])
                    dy.append(line.split()[6])
                    dz.append(line.split()[7])
                if col_neg == '3':
                    dx.append(line.split()[8])
                    dy.append(line.split()[9])
                    dz.append(line.split()[10])

            nline = nline + 1

#
# Initialization of Variables
#

select=1
frequencies=[]
negative=0
nline=1
name=[]
x=[]
y=[]
z=[]
dx=[]
dy=[]
dz=[]
position_neg=[]
col_neg=[]
Gaussian()
disp=float(sys.argv[2])
for i in range(0,len(name),1):
    print(str(name[i])+' '+str(float(x[i])+(disp*float(dx[i])))+' '+str(float(y[i])+(disp*float(dy[i])))+' '+str(float(z[i])+(disp*float(dz[i]))))
