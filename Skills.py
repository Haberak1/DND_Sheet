# This file is used to calculate the skills of the 
import Library.py

def calc(Str, Dex, Con, Int, Wis, Cha, Prof_mod, Prof_list, Expert_list):


    Skill_List = {"Acrobatics" : None, 
                "Animal Handling" : None, 
                "Arcana" : None, 
                "Athletics" : None, 
                "Deception" : None, 
                "History" : None, 
                "Insight" : None, 
                "Intimidation" : None, 
                "Investigation" : None, 
                "Medicine" : None, 
                "Nature" : None, 
                "Perception" : None, 
                "Persuasion" : None, 
                "Religion" : None, 
                "Sleight of Hand" : None, 
                "Stealth" : None, 
                "Survival" : None}

    for key in Skill_List:
        #calculate Strength based skills
        if key in Str_skills:
            if key in Prof_list: 
               Skill_List[key] = Str + Prof_mod
            else if key in Expert_list: 
                Skill_List[key] = Str + 2 * Prof_mod
            else
                Skill_List[key] = Str

        if key in Dex_skills:
            if key in Prof_list: 
               Skill_List[key] = Dex + Prof_mod
            else if key in Expert_list: 
                Skill_List[key] = Dex + 2 * Prof_mod
            else
                Skill_List[key] = Dex
        
        if key == Int_skills:
            if key in Prof_list: 
               Skill_List[key] = Int + Prof_mod
            else if key in Expert_list: 
                Skill_List[key] = Int + 2 * Prof_mod
            else
                Skill_List[key] = Int
        
        if key == Wis_skills:
            if key in Prof_list: 
               Skill_List[key] = Wis + Prof_mod
            else if key in Expert_list: 
                Skill_List[key] = Wis + 2 * Prof_mod
            else
                Skill_List[key] = Wis

        if key == Cha_skills:
            if key in Prof_list: 
               Skill_List[key] = Cha + Prof_mod
            else if key in Expert_list: 
                Skill_List[key] = Cha + 2 * Prof_mod
            else
                Skill_List[key] = Cha

        
    return skill_list