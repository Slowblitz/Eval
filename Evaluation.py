#!/usr/bin/python3
# -*- coding: utf-8 -*



import  numpy as np
import sys
import os
import  glob


n=[]
def baseline(dir):
	    """
    create a list of all the file in the folder .

 

    Parameters
    ----------
    arg1 : folder
        
		folder with all the GoldenStandar
  
    Returns
    -------
    list
       
       list of list with all the segment by file

    """
    
    big_one=list()
    for currentFile in glob.glob( os.path.join(dir, '*') ):
        if os.path.isdir(currentFile):
            baseline(currentFile)
        print(currentFile)
        n.append(currentFile)
        if currentFile.endswith(".txt"):
                with open(currentFile) as f:
                  for line in f:
                    lineList = [int(line) for line in open(currentFile)]
                big_one.append(lineList)
                lineListAr=np.array(big_one)

    return big_one

#recursif
def evalline(dir):
	    """
    create a list of all the file in the folder .

 

    Parameters
    ----------
    arg1 : folder
        
		folder with all the other output's system
  
    Returns
    -------
    list
       
       list of list with all the segment by file

    """
    big_two=list()
    lineList2 = list()
    for currentFile in glob.glob( os.path.join(dir, '*') ):
        if os.path.isdir(currentFile):
            evalline(currentFile)
        print(currentFile)
        with open(currentFile) as f:
            for line in f:
                lineList2 = [int(line) for line in open(currentFile)]
            big_two.append(lineList2)
            lineList2Ar=np.array(big_two)

    return (big_two)


def intersection(lst1, lst2):    
	"""
	Make the intersection between two list at +1 or -1.


    Parameters
    ----------
    arg1 :list
        
		first list

	arg2 :list
        
		second lsit
  
  
    Returns
    -------
    int
       
       Number of Match

    """
    lst3 = len([value for value in lst1 if value+1 in lst2])
    lst4 = len( [value for value in lst1 if value-1 in lst2])
    lst5 = len([value for value in lst1 if value in lst2])
    number_of_match=lst3 +lst4+lst5

    return number_of_match


def precision(list_ref,list_system):

        list=intersection(list_ref,list_system)

        return list/len(list_system)

def rapel(list_ref,list_system):
        list=intersection(list_ref,list_system)

        return list/len(list_ref)

def glob_P(lglob,N_sys):
    pg=sum(lglob)/sum(N_sys)
    return pg


def glob_R(lglob,N_ref):
    pg=sum(lglob)/sum(N_ref)
    return pg



def factor(p,r):
    f=2*(p*r)/(p+r)
    return f





total= list()
tmp_base=baseline(sys.argv[1])
tmp_val=evalline(sys.argv[2])

for _ in range(len(tmp_val)):
    total.append([tmp_base[_],tmp_val[_]])




pertext=list()
lgob=list()
N_ref=list()
N_sys=list()



for i in range(len(tmp_val) ):
    lgob.append(intersection(total[i][0],total[i][1]))
    pertext.append([precision(total[i][0],total[i][1]),rapel(total[i][0],total[i][1])])
    N_ref.append(len(total[i][0]))


#print all the precision and the rapel for all text

for i in range(len(tmp_val) ):
    lgob.append(intersection(total[i][0],total[i][1]))
    pertext.append([precision(total[i][0],total[i][1]),rapel(total[i][0],total[i][1])])
    N_ref.append(len(total[i][0]))
    N_sys.append(len(total[i][1]))



print("global precision : "+str(glob_P(lgob,N_sys))," global rapel: "+str(glob_R(lgob,N_ref)))
print("global factor: "+str(factor(glob_P(lgob,N_sys),glob_R(lgob,N_ref)))+"\n")


print(*pertext, sep="\n ")

