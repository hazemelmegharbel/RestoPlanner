# Helper functions for amenity selection and feedback

import pandas as pd

def get_input(choice, df):
   #First method: enter one or more amenities
    if choice=="1":
       am=input("Input the name(s) separated by a space: ")
       aml=am.lower()
       am_l=aml.split(" ")
       result = (df[df.amenity.isin(am_l)])
    #Second method: enter the start of the amenity
    elif choice=="2":
       am2=input("Input your search phrase: ")
       aml2=am2.lower()
       result = (df[df.amenity.str.startswith(aml2)])
    #Third method: enter some value contained in the amenity
    elif choice=="3":
       am3=input("Input your search phrase: ")
       aml3=am3.lower()
       result = (df[df.amenity.str.contains(aml3)])
    elif choice=="4":
       result = df
    else: 
       choice=input("Please enter a number from the given choices {1, 2, 3}: ")
       result = get_input(choice, df)
    return result.amenity.drop_duplicates().tolist()


def search_amenities(df):
      # User input the way how they want to filter the data
      choice=input(
         ''' To see a list of possible amenities, choose your method of filtering by search:
         (1) enter one or more complete amenity names
         (2) enter the start of the amenity name
         (3) enter the middle of the amenity name
         (4) see all amenities
         Please enter the number of your choice:
         ''')
      
      result = get_input(choice, df)
      print("Matches:")
      print(result)

def select_amenity(df):
    am=input("\nPlease enter one amenity/business that you would like to open: ").lower()
    amlist=df.amenity.tolist()
    if am not in amlist:
       print("Sorry, you have entered an invalid name.")
       return 0
    return am

def find_similar(amenity):
    print("\nGenerating list of similar amenities...")

    df = pd.read_csv('generate_datasets/amenity_densities.csv')
    dft=df.T
    amlist=dft.index.values.tolist()
    if amenity not in amlist:
       print("This amenity does not have enough quantity to have correlate with others.")
       return

    #Find out the coresponding zones of the chosen amenity
    dfts=df[df[amenity].isnull()==False]
  
    #Find out the zones not coresponding to the chosen amenity
    ndft=df[~df[amenity].isnull()==False]

    #Filter the all the amenities which also coresponding to the zones
    dff=dfts.T
    dff=dff.dropna()
    #Filter the all the amenities which also not coresponding to the zones
    ndff=ndft.T
    ndff=ndff[ndff.isnull().all(1)==True]
    #Find out other amenities also coresponding to the same zones and not coresponding to the same zones
    ffdff=pd.merge(dff, ndff, on="amenity",how="inner")
    flist=ffdff.index.values.tolist()
    #Output
    print("Consider opening one of these businesses similar to ",amenity,": ",flist)
      

