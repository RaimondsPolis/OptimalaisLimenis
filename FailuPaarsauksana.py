import os
folder_path = r'C:\Users\rpolis4\Downloads\Bildes\Bildes' # Šeit ieliek folder path kur atrodas viss ko vajag renameot
#i = 0
for filename in os.listdir(folder_path):
    if filename.startswith('OldName'):
        #new_filename = f"NewNameXD{i}.png" šis ir ja vajag precīzu nosaukumu
        #i +=1
        new_filename = filename.replace('OldName', 'NewName')#tā daļa kuru replaceo un tas ar ko viņu replaceo. šis ir ja vajag tikai daļu nomainīt
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
    else:
        print(f"Kļūda: {new_filename} jau eksistē")

