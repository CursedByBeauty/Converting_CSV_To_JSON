import csv, json

# READ THE CSV AND ADD THE DATA TO A DICTIONARY
csv_file_path = "sample-part-data.csv"
json_file_path = "sample-part-data.json"
data ={}
with open (csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    out = [{
            "Sku": row["sku"],
            "Display_Pn": row["display_pn"],
            "Be_Product_Cat_Name": row["be_product_cat_name"],
            "Short_Description": row["short_description"],
            "Lead_Time": row["lead_time"],
            "Meta_Description": row["meta_description"],
            "Meta_Title": row["meta_title"],
            "Part_Status": row["part_status"],
            "Images": 
            [
                row["image"],
                row["prod_drawing"],
                row["datasheet"],
                row["3d_model_iges"]
            ],
            "Attributes":
            [
                row["eu_rohs_y"],
                row["china_rohs"],
                row["reach"],
                row["halogen_free"],
                row["country_of_manufacture"],
                row["package_qty"],
                row["primary_pack_type"],
                row["primary_pack_qty"],
                row["contact_location_filter"],
                row["current_rating"],
                row["dielectric_withstanding_volt"],
                row["material_insulator"],
                row["material_shield"],
                row["material_slider"],
                row["number_of_contacts_filter"],
                row["operating_temperature_range"],
                row["orientation_filter"],
                row["packaging"],
                row["termination_style_filter"],
                row["voltage_rating"]
            ]

        }for row in csv_reader]

        
# WRITE THE DATA TO A JSON FILE
with open (json_file_path, "w") as json_file:
    json_file.write(json.dumps(out, indent=4))

