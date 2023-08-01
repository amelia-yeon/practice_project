from typing import List
from loguru import logger
from common.utils import *

import random

def define_item(req_id:str, pw:str):
    data = {'req_id' : req_id, 'pw': pw}
    return data


def get_main(sample):
    for i in sample:
        if (i['mendatory'] == True) and i['role'] != 'mix':
            return i

class BasicFrame:
    
    def __init__(self, num, style, role, tools, grams, flavor):
        self.num = num
        self.style = style
        self.role = role
        self.tools = tools
        self.grams = grams
        self.flavor = flavor

        

# 클래스 적용 
def get_test(style: str, flavor: list, grams: list, tables:dict):
    try:
        count = len(tables)
        table = []
        init_data = {}
        
        data = get_main(tables)
        a = BasicFrame(0,
                       style,
                       data['role'],
                       list_to_str(data['tools']),
                       grams if len(grams) == 1 else random.randrange(min(grams),max(grams),10),
                       random.choice(flavor)
                       )

        main_data = {
            'count': count,
            'dishes': a.__dict__
            }
        
        # 경우의 수 3가지 filter         
        for i in range(count):
            # table 가 비어있을 때 - 초기화 
            if len(table) < 1 :
                if tables[i]['mendatory'] == True:
                    B = BasicFrame(i+1,
                                    main_data['dishes']['style'],
                                    main_data['dishes']['role'], 
                                    main_data['dishes']['tools'],
                                    main_data['dishes']['grams'],
                                    main_data['dishes']['flavor'])
                    
                    init_data['count'] = count
                    init_data['dishes'] = [B.__dict__]
                    table.append(init_data)
                    
                # role == main 일 경우 
                elif tables[i]['mendatory'] == False and tables[i]['role'] == 'main':
                    C = BasicFrame(i+1,
                                    style,
                                    tables[i]['role'],
                                    main_data['dishes']['tools'],
                                    main_data['dishes']['grams'],
                                    main_data['dishes']['flavor'])
                                   
                    
                    init_data['count'] = count
                    init_data['dishes'] = [C.__dict__]
                    table.append(init_data)
                
                # false 이면서, 그 외 role 
                elif tables[i]['mendatory'] == False:
                    D = BasicFrame(i+1,
                                    style,
                                    tables[i]['role'],
                                    list_to_str(tables[i]['tools']),
                                    main_data['dishes']['grams'],
                                    main_data['dishes']['flavor'])
                    
                    init_data['count'] = count
                    init_data['dishes'] = [D.__dict__]
                    table.append(init_data)
            
            else: 
                if len(table) > 0 :
                    if tables[i]['mendatory'] == True:
                        E = BasicFrame(i+1,
                                        main_data['dishes']['style'],
                                        main_data['dishes']['role'], 
                                        main_data['dishes']['tools'],
                                        main_data['dishes']['grams'],
                                        main_data['dishes']['flavor'])
                                        
                        
                        table[0]['dishes'].append(E.__dict__)
                        
                    elif tables[i]['mendatory'] == False and tables[i]['role'] == 'main':
                        F = BasicFrame(i+1,
                                        style,
                                        tables[i]['role'],
                                        list_to_str(tables[i]['tools']),
                                        main_data['table']['grams'],
                                        main_data['table']['flavor'])

                        
                        table[0]['dishes'].append(F.__dict__)
                        
                    elif tables[i]['mendatory'] == False:
                        G = BasicFrame(i+1,
                                        style,
                                        tables[i]['role'],
                                        list_to_str(tables[i]['tools']),
                                        main_data['dishes']['grams'],
                                        main_data['dishes']['flavor'])
                                        
                        
                        table[0]['dishes'].append(G.__dict__)

        if len(table) > 0:
            data = table[0]

        return data
   
        
    except Exception as e:
        logger.error(e)
        
        return None 


