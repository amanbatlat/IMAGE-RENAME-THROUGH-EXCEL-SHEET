import pandas as pd
import os
os.getcwd() # Points to Current Directory
df = pd.read_excel ('Book1.xlsx') #Reading Data From Excel 
enrollment = df['Enrollment'].tolist() #Reading Enrollment Colument and Converting to List
names = df['Name'].tolist() #Reading Names Column and Converting to List
collection = "E:/Aman/Python/ChangeNameOfFileFromExcelSheet/Image" #Saving The Path in Collection
for i, filename in enumerate(os.listdir(collection)): #iterating one by one element from File
	if str(filename.split('.')[0]) == str(enrollment[i]):
		os.rename(collection+"/"+filename,collection+"/"+names[i]+".jpg")
print("Your Files Are Being Renamed")