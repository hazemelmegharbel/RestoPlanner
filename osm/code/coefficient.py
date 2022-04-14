import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.double is np.float64

def main(in_d):
    df = pd.read_json(in_d, lines=True)
    
    #am2=input("Input:")
    #aml2=am2.lower()
    
    #sns.scatterplot('lat', 'lon', data=df, hue='amenity')
    #plt.scatter(df['lat'], df['lon'])
    #plt.show()
    df1=df.amenity[(df.lat<49.1) & (df.lon>-122.2)].value_counts().rename_axis('amenity').to_frame('counts')
    df2=df.amenity[(df.lat<49.2) & (df.lat>49.1) & (df.lon>-122.2)].value_counts().rename_axis('amenity').to_frame('counts')
    df3=df.amenity[(df.lat<49.3) & (df.lat>49.2) & (df.lon>-122.2)].value_counts().rename_axis('amenity').to_frame('counts')
    df4=df.amenity[(df.lat<49.4) & (df.lat>49.3) & (df.lon>-122.2)].value_counts().rename_axis('amenity').to_frame('counts')
    df5=df.amenity[(df.lat>49.4) & (df.lon>-122.2)].value_counts().rename_axis('amenity').to_frame('counts')
    df6=df.amenity[(df.lat<49.1) & (df.lon<-122.2) & (df.lon>-122.6)].value_counts().rename_axis('amenity').to_frame('counts')
    df7=df.amenity[(df.lat<49.2) & (df.lat>49.1) & (df.lon<-122.2) & (df.lon>-122.6)].value_counts().rename_axis('amenity').to_frame('counts')
    df8=df.amenity[(df.lat<49.3) & (df.lat>49.2) & (df.lon<-122.2) & (df.lon>-122.6)].value_counts().rename_axis('amenity').to_frame('counts')
    df9=df.amenity[(df.lat<49.4) & (df.lat>49.3) & (df.lon<-122.2) & (df.lon>-122.6)].value_counts().rename_axis('amenity').to_frame('counts')
    df10=df.amenity[(df.lat>49.4) & (df.lon<-122.2) & (df.lon>-122.6)].value_counts().rename_axis('amenity').to_frame('counts')
    df11=df.amenity[(df.lat<49.1) & (df.lon<-122.6) & (df.lon>-123)].value_counts().rename_axis('amenity').to_frame('counts')
    df12=df.amenity[(df.lat<49.2) & (df.lat>49.1) & (df.lon<-122.6) & (df.lon>-123)].value_counts().rename_axis('amenity').to_frame('counts')
    df13=df.amenity[(df.lat<49.3) & (df.lat>49.2) & (df.lon<-122.6) & (df.lon>-123)].value_counts().rename_axis('amenity').to_frame('counts')
    df14=df.amenity[(df.lat<49.4) & (df.lat>49.3) & (df.lon<-122.6) & (df.lon>-123)].value_counts().rename_axis('amenity').to_frame('counts')
    df15=df.amenity[(df.lat>49.4) & (df.lon<-122.6) & (df.lon>-123)].value_counts().rename_axis('amenity').to_frame('counts')
    df16=df.amenity[(df.lat<49.1) & (df.lon<-123) & (df.lon>-123.4)].value_counts().rename_axis('amenity').to_frame('counts')
    df17=df.amenity[(df.lat<49.2) & (df.lat>49.1) & (df.lon<-123) & (df.lon>-123.4)].value_counts().rename_axis('amenity').to_frame('counts')
    df18=df.amenity[(df.lat<49.3) & (df.lat>49.2) & (df.lon<-123) & (df.lon>-123.4)].value_counts().rename_axis('amenity').to_frame('counts')
    df19=df.amenity[(df.lat<49.4) & (df.lat>49.3) & (df.lon<-123) & (df.lon>-123.4)].value_counts().rename_axis('amenity').to_frame('counts')
    df20=df.amenity[(df.lat>49.4) & (df.lon<-123) & (df.lon>-123.4)].value_counts().rename_axis('amenity').to_frame('counts')

    df1 = df1[df1.counts >= 4]
    df2 = df2[df2.counts >= 4]
    df3 = df3[df3.counts >= 4]
    df4 = df4[df4.counts >= 4]
    df5 = df5[df5.counts >= 4]
    df6 = df6[df6.counts >= 4]
    df7 = df7[df7.counts >= 4]
    df8 = df8[df8.counts >= 4]
    df9 = df9[df9.counts >= 4]
    df10 = df10[df10.counts >= 4]
    df11 = df11[df11.counts >= 4]
    df12 = df12[df12.counts >= 4]
    df13 = df13[df13.counts >= 4]
    df14 = df14[df14.counts >= 4]
    df15 = df15[df15.counts >= 4]
    df16 = df16[df16.counts >= 4]
    df17 = df17[df17.counts >= 4]
    df18 = df18[df18.counts >= 4]
    df19 = df19[df19.counts >= 4]
    df20 = df20[df20.counts >= 4]

    df1 = pd.merge(df1, df2, on="amenity",how="outer", suffixes=("1", "2"))
    df3 = pd.merge(df3, df4, on="amenity",how="outer", suffixes=("3","4"))
    df5 = pd.merge(df5, df6, on="amenity",how="outer", suffixes=("5", "6"))
    df7 = pd.merge(df7, df8, on="amenity",how="outer", suffixes=("7", "8"))
    df9 = pd.merge(df9, df10, on="amenity",how="outer", suffixes=("9", "10"))
    df11 = pd.merge(df11, df12, on="amenity",how="outer", suffixes=("11", "12"))
    df13 = pd.merge(df13, df14, on="amenity",how="outer", suffixes=("13", "14"))
    df15 = pd.merge(df15, df16, on="amenity",how="outer", suffixes=("15", "16"))
    df17 = pd.merge(df17, df18, on="amenity",how="outer", suffixes=("17", "18"))
    df19 = pd.merge(df19, df20, on="amenity",how="outer", suffixes=("19", "20"))
    df1 = pd.merge(df1, df3, on="amenity",how="outer")
    df1 = pd.merge(df1, df5, on="amenity",how="outer")
    df1 = pd.merge(df1, df7, on="amenity",how="outer")
    df1 = pd.merge(df1, df9, on="amenity",how="outer")
    df1 = pd.merge(df1, df11, on="amenity",how="outer")
    df1 = pd.merge(df1, df13, on="amenity",how="outer")
    df1 = pd.merge(df1, df15, on="amenity",how="outer")
    df1 = pd.merge(df1, df17, on="amenity",how="outer")
    df1 = pd.merge(df1, df19, on="amenity",how="outer")
    df1=df1
    dft=df1.T

    am=input("input:")
    aml=am.lower()
    amlist=df1.index.values.tolist()
    if aml not in amlist:
       print("Sorry I do not understand or this amenity does not have enough quantity to have correlation coefficient. Please try again.")
       return 0
    
    dfts=dft[dft[aml].isnull()==False]
    dflist=dfts.index.values.tolist()
    ndft=dft[~dft[aml].isnull()==False]
    ndflist=ndft.index.values.tolist()
    dff=dfts.T
    dff=dff.dropna()
    ndff=ndft.T
    ndff=ndff[ndff.isnull().all(1)==True]
    ffdff=pd.merge(dff, ndff, on="amenity",how="inner")
    flist=ffdff.index.values.tolist()
    print("Here is the list of correlation coefficient of",am,":",flist)
    
    
if __name__ == '__main__':
    in_d = sys.argv[1]
    main(in_d)


