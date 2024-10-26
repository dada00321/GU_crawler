import pandas as pd
import os
import shutil 

df_GU_menu = pd.read_csv("C:/Users/USER/Desktop/Cloth_App/code_process_0/apparel_big_crawler/GU_crawler/csv/GU_menu.csv")
banned_big_cat_IDs = [5, 6, 11, 12, 14, 15, 16, 17, 18]
banned_sales_cat_IDs = df_GU_menu[df_GU_menu["big_category_id"].isin(banned_big_cat_IDs)]["sales_category_id"]
#print(banned_sales_cat_IDs)

df_GU_basic_attr = pd.read_csv("C:/Users/USER/Desktop/Cloth_App/code_process_0/apparel_big_crawler/GU_crawler/csv/GU_basic_attr.csv")
banned_spu_IDs = df_GU_basic_attr[df_GU_basic_attr["sales_category_id"].isin(banned_sales_cat_IDs)]["spu_id"]
#print(banned_spu_IDs)

df_GU_specific_attr = pd.read_csv("C:/Users/USER/Desktop/Cloth_App/code_process_0/apparel_big_crawler/GU_crawler/csv/GU_specific_attr.csv")
valid_sku_IDs = df_GU_specific_attr[~df_GU_specific_attr["spu_id"].isin(banned_spu_IDs)]["sku_id"]
#print(valid_sku_IDs)
#print(len(valid_sku_IDs))

df_GU_images = pd.read_csv("C:/Users/USER/Desktop/Cloth_App/code_process_0/apparel_big_crawler/GU_crawler/csv/GU_images.csv")
valid_records = df_GU_images[df_GU_images["sku_id"].isin(valid_sku_IDs)]
base_dir = os.getcwd().replace('\\','/')

sku_img_paths = [f"{base_dir}/{e}" for e in valid_records["sku_img_path"] if e != 'X']
outfit_img_paths = [f"{base_dir}/{e}" for e in valid_records["outfit_img_path"] if e != 'X']

os.makedirs("data_selection", exist_ok=True)

'''
save_as_csv = lambda list_obj, file_name: pd.DataFrame({"path": list_obj}).to_csv(f"data_selection/{file_name}.csv", index=False, encoding="utf-8-sig")
save_as_csv(sku_img_paths, "sku_img_paths")
save_as_csv(outfit_img_paths, "outfit_img_paths")
'''

os.makedirs("data_selection/sku_img", exist_ok=True)
[shutil.copy(src, "data_selection/sku_img") for src in sku_img_paths]

os.makedirs("data_selection/outfit_img", exist_ok=True)
[shutil.copy(src, "data_selection/outfit_img") for src in outfit_img_paths]