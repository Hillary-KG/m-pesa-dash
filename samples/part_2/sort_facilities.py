import random
import sys

import pandas as pd

class SortFacilies():
    """a class that represents the implementation of sorting the facilities list
    into four different lists and writing them into 4 different excel sheets """
    # print(os.getcwd())
    facilities_file = 'res/Facilities.xlsx'

    def read_excel(self):
        """a function to open and read the  Facilities excel file"""
        excel_file = self.facilities_file
        with open(excel_file) as xlsx_file:
            facilities = pd.read_excel(xlsx_file)

        return facilities

    def sort_facilities(self):
        """a function that sorts the faacilities read from the excel file into
        List1, List2, List3, List4"""
        Kiambu_list = []
        others = []
        mama1xx_count = 0
        mimba1xx_count = 0
        others_count = 0
        try:
            facilities = self.read_excel()
        except Exception as e:
            sys.exit(e)
            
        for facility in facilities.itertuples():
            if "mimba1" in str(facility.FacilityCode).lower():
                Kiambu_list.append(str(facility.Contact_UUID))
                mimba1xx_count += 1

            elif "mama1" in str(facility.FacilityCode).lower():
                Kiambu_list.append(str(facility.Contact_UUID))
                mama1xx_count += 1
            else:
                others.append(str(facility.Contact_UUID))
                others_count += 1


        random.shuffle(Kiambu_list)
        random.shuffle(others)
        list1 = [Kiambu_list[i::2] for i in range(2)][0]
        list2 = [Kiambu_list[i::2] for i in range(2)][1]

        list3 = [others[i::2] for i in range(2)][0]
        list4 = [others[i::2] for i in range(2)][1]

        #writing kiambu contact UUIDs to a csv file 
        kiambuList_df = pd.DataFrame(Kiambu_list, columns=["Contact_UUID"])
        kiambuList_df.to_csv('outputs/Kiambu.csv')

        #write other contact UUIDs to a csv file
        others_df = pd.DataFrame(others, columns=["Contact_UUID"])
        others_df.to_csv('outputs/Others.csv')

        #write statistics to an excel file
        stats = [[' MAMA1XX', mama1xx_count],['MIMBA1XX', mimba1xx_count], ['OTHERS', others_count]]
        stats_df = pd.DataFrame(stats, columns=["FacilityCode", "Count"])
        stats_df.to_excel('outputs/Stats_code.xlsx', index=False)

        return list1, list2, list3, list4, mama1xx_count, mimba1xx_count, others_count

#module execution 
if __name__ == '__main__':
    sortFacilitiesObj = SortFacilies()
    sortFacilitiesObj.sort_facilities()
        
    
