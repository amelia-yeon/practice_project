
from loguru import logger

from common.connect import BigqueryDac
from common.utils import *




def get_sample(gender: str):
    try:
        query = f"""
        SELECT *
        FROM `sy-gcp-project.tip_table.tip_table_sample` 
        WHERE tip > (SELECT round(avg(tip),1) as avg_tip
                    FROM `sy-gcp-project.tip_table.tip_table_sample`)
        AND sex = '{gender}'
        """

        dac= BigqueryDac()
        query_job = dac.select_query_phase(query)
        data = []
        
        for row in query_job:
            row_data = {}
            row_data['total_bill'] = row.total_bill
            row_data['tip'] = row.tip
            row_data['gender'] = row.sex
            row_data['smoker'] = row.smoker
            row_data['day'] = row.day
            row_data['time'] = row.time
            row_data['size'] = row.size
            data.append(row_data)

        return data
        
    except Exception as e:
        logger.error(e)
        
        return None
    
