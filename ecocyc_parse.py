import numpy as np
import pandas as pd
import os

def parse_dat(file):
    """
    Description:
        Parsing EcoCyc .dat file into a pandas dataframe.
    Input:
        file - (‘string’) .dat file path.
    Output:
        dat_df - (pandas.DataFrame) a dataframe where each row is an instance, and each column is an attibute.
    """
    dat_dict = {}
    f = open(file, "r", errors='ignore')
    
    ecodata = f.read()
    ecodata = ecodata.replace('\n^', '-XX-')
    tmp = open("tmp.txt", "w+")
    tmp.write(ecodata)
    
    f.close()
    tmp.close()
    
    tmp = open("tmp.txt", "r", errors='ignore')
    
    i = 0    # dictionary index
    dat_dict[i]={}
    for line in tmp:
        
        if line[0]=="#":    # escape annotations that start with a "#"
            continue
            
        else:
            #print(line)
            if line[0]!="/":
                line = line.split(" - ", maxsplit=1)

                attr = line[0]
                # if the attribute already exist, append
                # if not, create
                if line[0] in dat_dict[i].keys():
                    dat_dict[i][attr]=dat_dict[i][attr]+ " -- " + line[1]
                else:
                    dat_dict[i][attr]=line[1]

            elif line=='//\n':
                i = i+1
                dat_dict[i]={}

            elif line[0]=="/":
                dat_dict[i][attr]=dat_dict[i][attr]+ " -- " + line
                
    #print(dat_dict)
    dat_df = pd.DataFrame(dat_dict).transpose()
    dat_df.replace(to_replace=r'\n/\n/',value= ' -- ', regex = True, inplace=True)
    dat_df.replace(to_replace=r'\n',value= '', regex = True, inplace=True)
    
    tmp.close()
    os.remove("tmp.txt")
    return dat_df

def parse_col(file):
    dat_df = pd.read_csv(file, sep="\t", comment="#")
    return dat_df

def parse_linkdat(file):
    dat_df = []
    a = open(file, "r")
    for line in a:
        if line[0] =="#":
            pass
        else:
            line = line.replace("\n", "").split("\t")
            line = list(filter(None, line))
            dat_df.append(line)
    return dat_df